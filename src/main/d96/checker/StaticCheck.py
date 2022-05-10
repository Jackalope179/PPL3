
"""
 * @author nhphung
"""
from ast import Pass
import copy
from AST import * 
from Visitor import *
from StaticError import *
from main.d96.utils.AST import FieldAccess



class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Atype:
    def __init__(self, size, atype):
        self.size = size
        self.atype = atype


class Symbol:
    def __init__(self,name = None ,kind = None, mtype = None, value = None):
        self.name = name
        self.kind = kind
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):
    
    def __init__(self,ast):
        self.check_const_decl = False
        self.error_const_decl = False
        self.check_in_loop = False
        self.check_inner_array = False
        self.is_in_destructor = False
        self.is_in_constructor = False
        self.is_in_main = False
        self.is_program = False
        self.previous_return = 0
        self.check_main_return = 0

        self.ast = ast
        self.global_env = []
        self.check_entry = False

    def check(self):
        return self.visit(self.ast, self.global_env)

    def visitProgram(self,ast, c): 
        # c = [{"array":[[]], "name": None, "parent":None}]
        '''Visit all class in program'''
        for decl in ast.decl:
            self.visit(decl,c)

        '''Check entry point'''
        if not self.check_entry: raise NoEntryPoint()
        return ""

    def visitClassDecl(self, ast,c):
        if ast.classname.name in ["Program"]:
            self.is_program = True
        else:
            self.is_program = False

        parent_name = ast.parentname.name if ast.parentname else None
        undeclare_parent = True
        for class_ in c:
            '''Check redeclare class name'''
            if class_["name"] == ast.classname.name:
                raise Redeclared(Class(),ast.classname.name)
            '''Check Undeclare parent'''
            if parent_name == class_["name"]:
                undeclare_parent = False
        if parent_name and undeclare_parent: 
            raise Undeclared(Class(),parent_name) 
        
        c.insert(0,{"array":[[]], "name": ast.classname.name, "parent":parent_name}) 

        '''Memlist -> Attribute Decl || Method Decl'''
        for mem in ast.memlist:
            res = self.visit(mem,c) # => return Symbol(name, kind, mtype, value)
            if ast.classname.name == "Program" and res.name == "main" and res.kind == "Method" and len(res.mtype.partype) == 0 and res.mtype.rettype == 6:
                self.check_entry = True

    def checkExistingMember(self, list_of_env, target, kind):
        for env in list_of_env:
            for sym in env:
                if sym.name == target and (sym.kind == kind == "Method" or (sym.kind  in ["Val", "Var"] and kind in ["Val", "Var"])): 
                    return True, sym
        return False, None

    def checkExistingIdFunction(self, list_of_env, target):
        for env in list_of_env:
            for sym in env:
                if sym.name == target: return True, sym
        return False, None
    
    def checkExistingClassName(self, classname , c):
        for class_ in c:
                if classname == class_["name"]: return True
        return False

    def visitAttributeDecl(self,ast,c):
        if isinstance(ast.decl, VarDecl):
            name = ast.decl.variable.name
            kind = "Var"
            typ = ast.decl.varType # =>Type()
            value = ast.decl.varInit 
        else: 
            name = ast.decl.constant.name
            kind = "Val"
            typ = ast.decl.constType # =>Type()
            value = ast.decl.value
        
        '''Check if id was declared or not'''
        check_exist, sym = self.checkExistingMember([c[0]["array"][-1]], name, kind)
        if check_exist : raise Redeclared(Attribute(), name)

        '''Check undeclare class type'''
        typ_ = self.visit(typ, c) #=> Symbol(mtype, kind)
        if typ_.kind == "ClassType":
            if not self.checkExistingClassName(typ_.mtype, c): raise Undeclared(Class,typ_.mtype)
 
        '''Check with const decl'''
        if kind == "Val":
            if value is None:
                raise Undeclared(Constant(), name)
        
            self.check_const_decl = True
            value = self.visit(value,c) #=> Symbol
            self.check_const_decl = False

            if value is None: raise IllegalConstantExpression(None)

            '''Visit value and check if operands is const'''
            if isinstance(value, Id) or isinstance(value, NullLiteral) or isinstance(value, SelfLiteral) or value.kind == "Method":
                    raise IllegalConstantExpression(ast.decl.value)

            if self.error_const_decl:
                raise IllegalConstantExpression(ast.decl.value)
            
            if value.mtype == 6: raise IllegalConstantExpression(ast.decl.value)

            if not self.checkTypeOfSide(typ_.mtype, value.mtype, c, self.visit(ast.decl.value,c).mtype): 
                raise TypeMismatchInConstant(ast)

        '''Visit value'''
        if kind == "Var":
            if value and not isinstance(value, NullLiteral):
                value = self.visit(value,c)
                if not self.checkTypeOfSide(typ_.mtype, value.mtype, c, self.visit(ast.decl.varInit,c).mtype): 
                    raise TypeMismatchInStatement(ast)


        sym = Symbol(name,kind,typ_.mtype,value)
        '''Store attribute'''
        c[0]["array"][0] = [sym] + c[0]["array"][0]

        return sym

    def visitMethodDecl(self, ast,c):
        if ast.name.name == "Destructor":
            self.is_in_destructor = True
        else:
            self.is_in_destructor = False

        if ast.name.name == "main":
            self.is_in_main = True
        else:
            self.is_in_main = False
        
        if ast.name.name == "Constructor":
            self.is_in_constructor = True
        else:
            self.is_in_constructor = False

        env = []
        '''Copy c to env'''
        env = copy.deepcopy(c)

        name = ast.name.name
        '''Check if method was declared or not'''
        check_exist, sym = self.checkExistingMember([c[0]["array"][-1]], name, "Method")
        if check_exist: raise Redeclared(Method(), name)

        env[0]["array"].insert(0,[])

        for param_ in ast.param:
            self.visitParam(param_,env)
        
        temp = self.visitBody(ast.body,name,env)

        if self.is_program and ast.name.name == "main" and not self.check_main_return:
            raise NoEntryPoint()

        result = Symbol(ast.name.name,"Method", MType([self.visit(p.varType,c).mtype for p in ast.param], temp))
        c[0]["array"][0] = [result] + c[0]["array"][0]
        
        return result

    def visitBody(self, ast,name, c):
        typ = 6
        for inst_ in ast.inst:
            typ = self.visit(inst_,c)
        self.previous_return = 0
        if isinstance(typ, Symbol): return typ.mtype
        else: return 6
    '''--------------Decl--------------'''
    def visitVarDecl(self, ast,c): 
        '''Check if id was declared or not''' 
        name = ast.variable.name
        check_exist, _ = self.checkExistingMember([c[0]["array"][0]], name, 'Val')
        if check_exist: raise Redeclared(Variable(), name)

        '''Check undeclare class in Field access '''
        typ = self.visit(ast.varType, c) #=> Symbol(mtype, kind)
        if typ.kind == "ClassType":
            if not self.checkExistingClassName(typ.mtype, c): raise Undeclared(Class(),typ.mtype)
        

        '''Visit Value'''
        if ast.varInit and not isinstance(ast.varInit, NullLiteral):
            value = self.visit(ast.varInit,c)
            if not self.checkTypeOfSide(typ.mtype, value.mtype, c, self.visit(ast.varInit,c).mtype): 
                raise TypeMismatchInStatement(ast)


        result = Symbol(ast.variable.name,"Var", self.visit(ast.varType,c).mtype, ast.varInit)
        '''Store variable value'''
        c[0]["array"][0] =  [result] + c[0]["array"][0]
    
    def visitConstDecl(self, ast,c):
        '''Check if id was declared or not'''
        name = ast.constant.name
        check_exist, _ = self.checkExistingIdFunction([c[0]["array"][0]], name)
        if check_exist: raise Redeclared(Constant(), name)

        '''Check undeclare class in Field access '''
        typ = self.visit(ast.constType, c) #=> Symbol(mtype, kind)
        if typ.kind == "ClassType":
            if not self.checkExistingClassName(typ.mtype, c): raise Undeclared(Class(),typ.mtype)
        
        self.check_const_decl = True
        value = self.visit(ast.value,c) #=> Symbol
        self.check_const_decl = False

        '''If value of const is None'''
        if ast.value is None: raise IllegalConstantExpression(None)

        '''Visit value and check if operands is const'''
        if isinstance(ast.value, Id) or isinstance(ast.value, NullLiteral) or isinstance(ast.value, SelfLiteral) or value.kind == "Method":
            raise IllegalConstantExpression(ast.value)
        
        if self.error_const_decl:
            raise IllegalConstantExpression(ast.value)
        
        
        if value.mtype == 6: raise IllegalConstantExpression(ast.value)
        """'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
 
        if not self.checkTypeOfSide(typ.mtype, value.mtype, c, self.visit(ast.value,c).mtype): 
            raise TypeMismatchInConstant(ast)


        result = Symbol(ast.constant.name,"Val",typ.mtype, ast.value)
        '''Store constant value'''
        c[0]["array"][0] = [result] +  c[0]["array"][0]

    def visitParam(self, ast, env):
        '''Check if id was declared or not'''
        name = ast.variable.name
        check_exist, _ = self.checkExistingIdFunction([env[0]["array"][0]], name)
        if check_exist: raise Redeclared(Parameter(), name)
        
        '''Check undeclare class in param'''
        self.visit(ast.varType, env)
        result = Symbol(ast.variable.name,"Var",self.visit(ast.varType, env).mtype, ast.varInit)
        env[0]["array"][0] = [result] + env[0]["array"][0] 
    
    def visitBlock(self, ast,c):
        env = copy.deepcopy(c)
        env[0]["array"].insert(0, [])

        for inst_ in ast.inst:
            self.visit(inst_,env)

    def visitId(self, ast,c):
        '''Check if id was declared or not'''
        name = ast.name
        check_exist, id = self.checkExistingIdFunction(c[0]["array"][:-1], name)
        if not check_exist:
            raise Undeclared(Identifier(),name)
        return id

    def visitBinOp(self, ast, c, original):
        if isinstance(ast.left, BinaryOp):
            lhs = self.visitBinOp(ast.left, c, original).mtype
        else:
            lhs = self.visit(ast.left, c).mtype
        if isinstance(ast.right, BinaryOp):
            rhs = self.visitBinOp(ast.right, c, original).mtype
        else:
            rhs = self.visit(ast.right, c).mtype

        '''Handle return type'''
        if isinstance(lhs, MType):
            lhs = lhs.rettype
        if isinstance(rhs, MType):
            rhs = rhs.rettype
            
        if isinstance(lhs, Atype):
            lhs = lhs.atype
        if isinstance(rhs, Atype):
            rhs = rhs.atype

        '''Check constdecl'''
        if self.check_const_decl:
            if isinstance(ast.left, CallExpr) or isinstance(ast.right, CallExpr):
                self.error_const_decl = True
            if isinstance(ast.left, Id) or isinstance(ast.right, Id):
                self.error_const_decl = True
            if isinstance(ast.left, NullLiteral) or isinstance(ast.right, NullLiteral):
                self.error_const_decl = True

        if ast.op in ['-', '+', '*', '/']:
            if lhs == 1 and rhs == 1: return Symbol(mtype=1, kind = "BinOp")
            elif (lhs in [1,2]) and (rhs in [1,2]): return Symbol(mtype=2, kind = "BinOp")
            else:
                raise TypeMismatchInExpression(original)
        if ast.op == '%':
            if lhs != 1 or rhs != 1: raise TypeMismatchInExpression(original)
            return Symbol(mtype=1, kind = "BinOp")

        if ast.op in ["==", "!="]:
            if rhs == lhs == 1 or rhs == lhs == 4: return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(original)

        if ast.op in ["<", ">", "<=", ">="]: 
            if (lhs in [1,2]) and (rhs in [1,2]) : return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(original)
        
        if ast.op in ["&&", "||"]:
            if rhs == lhs == 4: return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(original)
        
        if ast.op == "+.":
            if rhs == lhs == 3: return Symbol(mtype=3, kind = "BinOp")
            raise TypeMismatchInExpression(original)
        
        if ast.op == "==.":
            if rhs == lhs == 3: return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(original)
        
    #int 1, float 2, string 3, bool 4
    def visitBinaryOp(self, ast,c): 
        return self.visitBinOp(ast, c, ast)

    #int 1, float 2, string 3, bool 4
    def visitUnaryOp(self, ast,c):
        typ = self.visit(ast.body,c).mtype
        if isinstance(typ, MType):
            typ = typ.rettype
        if isinstance(typ, Atype):
            typ = typ.atype
            
        if ast.op == "!":
            if typ != 4: raise TypeMismatchInExpression(ast)
            return Symbol(mtype=4, kind = "UnaryOp")
        if ast.op == "-":
            if typ == 1: return Symbol(mtype=1, kind = "UnaryOp")
            if typ == 2: return Symbol(mtype=2, kind = "UnaryOp")
            raise TypeMismatchInExpression(ast)
        if self.check_const_decl:
            if not isinstance(ast.body, BinaryOp) and not isinstance(ast.body, UnaryOp) and not isinstance(ast.body, FieldAccess):
                    self.error_const_decl = True

    def visitNewExpr(self, ast,c):
        classname = ast.classname.name
        if not self.checkExistingClassName(classname, c):
            raise Undeclared(Class(), classname)
        constructor_exist = True
        for class_ in c:
            if class_["name"] == classname:
                constructor_exist, sym = self.checkExistingMember([class_["array"][-1]], "Constructor", "Method")
        if not constructor_exist: 
            if len(ast.param) > 0: raise TypeMismatchInExpression(ast)
        else:
            if len(ast.param) != len(sym.mtype.partype): raise TypeMismatchInExpression(ast)
            
            for i in range(len(ast.param)):
                if not self.checkTypeOfSide(sym.mtype.partype[i],self.visit(ast.param[i],c).mtype,c, self.visit(ast.param[i],c).mtype):
                    raise TypeMismatchInExpression(ast)

        return Symbol(mtype = classname, kind ="ClassType")

    def isPrimitiveType(self, typ):
        if typ in [1,2,3,4,6]: return True
        return False

    def visitArrayCell(self, ast,c): 
        array = self.visit(ast.arr, c)
        if not isinstance(array.mtype, Atype): raise TypeMismatchInExpression(ast)

        # Atype(Atype(Int))
        arr_typ = []
        cur_array = array.mtype
        while(True):
            if type(cur_array) is Atype:
                arr_typ  += [cur_array]
                cur_array = cur_array.atype
            else:
                arr_typ += [cur_array]
                break
        return_typ = 0

        if len(ast.idx) >= len(arr_typ):
            raise TypeMismatchInExpression(ast)
        else:
            return_typ = arr_typ[len(ast.idx)]

        '''E1[E2] => E2 must be int'''
        for idx in ast.idx:
            if self.visit(idx, c).mtype != 1: 
                raise TypeMismatchInExpression(ast)
        return Symbol(mtype=return_typ, kind = "Var")

    def IsStatic(self, name):
        if name[0] == "$" or name == "main": return True
        return False

    def checkMemberOfClass(self, className, memberName, c, error, type):
        for class_ in c:
            if class_["name"] == className:
                '''Check in current class'''
                for member in class_["array"][-1]:
                    if member.name == memberName:
                        
                        if (member.kind == type == "Method") or (type in ["Val", "Var"] and member.kind in ["Val", "Var"]): 
                            '''If LSH is val'''
                            if self.check_const_decl:
                                if member.kind == "Var":
                                    self.error_const_decl = True
                            
                            return member #=>Symbol
        raise Undeclared(error, memberName)

    def checkAccess(self, ast, memberName, c, error, type): 
        if self.IsStatic(memberName):
            '''ClassName:: $static_member'''
            if not self.checkExistingClassName(ast.obj.name, c):
                raise Undeclared(Class(), ast.obj.name)
            return self.checkMemberOfClass(ast.obj.name, memberName, c, error, type) # => Symbol
        else:
            '''Check undeclare object'''
            if isinstance(ast.obj, Id):
                if not self.checkExistingIdFunction(c[0]["array"][:-1], ast.obj.name):
                    raise Undeclared(Identifier(), ast.obj.name)
                
                obj = self.visit(ast.obj, c) #=> Symbol(name, kind, A, value)
                className = obj.mtype
            else:    
                className = self.visit(ast.obj,c).mtype
            return self.checkMemberOfClass(className, memberName, c, error, type)  

    def visitCallExpr(self, ast,c):
        '''E.<method name>(<args>)'''

        '''obj.method()'''
        '''A::$method()'''

        '''Access instance method with class error'''
        if isinstance(ast.obj, Id):
            for class_ in c:
                if ast.obj.name == class_["name"]:
                    check_same_name_att, _ = self.checkExistingIdFunction(c[0]["array"][:-1], ast.obj.name)
                    check, sym = self.checkExistingIdFunction([class_["array"][-1]], ast.method.name)
                    if not check_same_name_att and not check:
                        raise Undeclared(Attribute(), ast.method.name)
                    if check and sym.kind == "Method" and not self.IsStatic(sym.name) and not check_same_name_att:
                        raise IllegalMemberAccess(ast)
                    return sym

        '''E is not a className'''   
        '''E must be in object in class type'''
        obj_ = self.visit(ast.obj,c) #=>Symbol
        array_typ = [1,2,3,4,6]
        if obj_.mtype in array_typ:
            '''E is not in class type => int, float,...'''
            raise TypeMismatchInExpression(ast)

        '''Access static method with object error'''
        for class_ in c:
            if obj_.mtype == class_["name"]:
                check, sym = self.checkExistingIdFunction([class_["array"][-1]], ast.method.name)
                if check and sym.kind == "Method" and self.IsStatic(ast.method.name):
                    raise IllegalMemberAccess(ast)

        '''Method must be void type'''
        name = ast.method.name
        sym = self.checkAccess(ast, name, c, Method(), "Method")
        if sym.mtype.rettype == 6: 
            raise TypeMismatchInExpression(ast)

        '''Check number of argument'''
        if len(ast.param) != len(sym.mtype.partype):
            raise TypeMismatchInExpression(ast)

        for i in range(len(sym.mtype.partype)):
            if not self.checkTypeOfSide(sym.mtype.partype[i], self.visit(ast.param[i],c).mtype,c, None):
                raise TypeMismatchInExpression(ast)               
        return sym

    def visitFieldAccess(self, ast,c):
        '''Class::<$static>'''

        '''Object.<att>'''
        multability = "Val"
        '''if obj is class'''
        if isinstance(ast.obj, Id):
            for class_ in c:
                if ast.obj.name == class_["name"]:
                    check_same_name_att, _ = self.checkExistingIdFunction(c[0]["array"][:-1], ast.obj.name)

                    check, sym = self.checkExistingMember([class_["array"][-1]], ast.fieldname.name, "Val")

                    if check: multability = sym.kind
                    else:
                        if not check_same_name_att:
                            raise Undeclared(Attribute(), ast.fieldname.name)
                    if check and not self.IsStatic(sym.name) and not check_same_name_att:
                        raise IllegalMemberAccess(ast)
                    return sym

        '''E is not a className'''   
        '''E must be in object in class type'''
        obj_ = self.visit(ast.obj,c)  #=>Symbol
        array_typ = [1,2,3,4,6]
        if obj_.mtype in array_typ:
            '''E is not in class type => int, float,...'''
            raise TypeMismatchInExpression(ast)


        '''Access static field with object error'''
        for class_ in c:
            if obj_.mtype == class_["name"]:
                check, sym = self.checkExistingMember([class_["array"][-1]], ast.fieldname.name, "Val")
                if check: multability = sym.kind
                if check and self.IsStatic(ast.fieldname.name):
                    raise IllegalMemberAccess(ast)

        name = ast.fieldname.name
        sym = self.checkAccess(ast, name, c, Attribute(), multability)
        return sym

    def visitAssign(self, ast,c):
        lhs = self.visit(ast.lhs,c) # =>Symbol
        if lhs.kind == "Val": raise CannotAssignToConstant(ast)

        rhs = self.visit(ast.exp,c) # =>Symbol
        lhs_type = lhs.mtype if not isinstance(lhs.mtype, MType) else lhs.mtype.rettype
        rhs_type = rhs.mtype if not isinstance(rhs.mtype, MType) else rhs.mtype.rettype
        '''LHS cant be void'''
        if lhs_type == 6: raise TypeMismatchInStatement(ast)
        
        if not self.checkTypeOfSide(lhs_type, rhs_type, c, self.visit(ast.exp,c).mtype):
            raise TypeMismatchInStatement(ast)

        self.visit(ast.exp,c)

    def visitIf_Stmt(self, ast, c, original):
        if_expr = self.visit(ast.expr,c)
        '''If '''
        if if_expr.mtype != 4:
            raise TypeMismatchInStatement(original)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt is not None:
            if isinstance(ast.elseStmt, If):
                self.visitIf_Stmt(ast.elseStmt, c, original)
            else:
                self.visit(ast.elseStmt, c)

    def visitIf(self, ast,c):
        self.visitIf_Stmt(ast,c, ast)

    def visitFor(self, ast,c):
        '''Check type of scalar , exp1, exp2'''
        scalar_var = self.visit(ast.id,c) # => Symbol
        exp1 = self.visit(ast.expr1,c) # => Symbol
        exp2 = self.visit(ast.expr2,c) # => Symbol
        
        if (scalar_var.mtype != 1 or exp1.mtype != 1 or exp2.mtype != 1):
            raise TypeMismatchInStatement(ast)
        '''Check immutable variable'''
        if scalar_var.kind == "Val": raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        
        '''Check break and continue in For loop'''
        self.check_in_loop = True
        self.visit(ast.loop, c)
        self.check_in_loop = False

    def visitBreak(self, ast,c):
        if not self.check_in_loop:
            raise MustInLoop(ast)

    def visitContinue(self, ast,c):
        if not self.check_in_loop:
            raise MustInLoop(ast)

    def visitReturn(self, ast,c):
        if self.is_in_destructor :
            raise TypeMismatchInStatement(ast)

        if ast.expr == None: return Symbol(mtype= 6)
        typ = self.visit(ast.expr, c)
        if self.is_in_main and self.is_program and typ.mtype != 6:
            raise TypeMismatchInStatement(ast)
        if self.is_in_constructor and typ.mtype != 6:
            raise TypeMismatchInStatement(ast)
        if self.is_in_main:
            self.check_main_return = True
        if self.previous_return == 0:
            self.previous_return = typ.mtype
        elif self.previous_return != typ.mtype:
            raise TypeMismatchInStatement(ast)

        return typ
    
    def checkTypeOfSide(self, lhs, rhs, c, rhs_literal):
        if isinstance(rhs_literal, list):
            for i in range(len(rhs_literal)):
                if not self.checkTypeOfSide(lhs, rhs_literal[i], c, rhs_literal[i]):
                    return False
            return True

        ''' LHs and RHS are method'''
        if isinstance(lhs, MType):
            lhs = lhs.rettype

        if isinstance(rhs, MType):
            rhs = rhs.rettype
        '''LHS = float, RHS = int'''
        
        if lhs == rhs or (lhs == 2 and rhs == 1): return True

        if isinstance(lhs, Atype) and isinstance(rhs, Atype):    
            if lhs.size != rhs.size: return False
            if not self.checkTypeOfSide(lhs.atype, rhs.atype, c, rhs.atype):
                return False
            return True   

        return False

    def visitCallStmt(self, ast,c):
        '''E.<method name>(<args>)'''

        '''obj.method()'''
        '''A::$method()'''

        '''Access instance method with class error'''

        if isinstance(ast.obj, Id):
            for class_ in c:
                if ast.obj.name == class_["name"]:
                    check_same_name_att, _ = self.checkExistingIdFunction(c[0]["array"][:-1], ast.obj.name)
                    check, sym = self.checkExistingIdFunction([class_["array"][-1]], ast.method.name)
                    if not check_same_name_att and not check:
                        raise Undeclared(Attribute(), ast.method.name)
                    if check and sym.kind == "Method" and not self.IsStatic(sym.name) and not check_same_name_att:
                        raise IllegalMemberAccess(ast)
                    return sym

        '''E is not a className'''   
        '''E must be in object in class type'''
        obj_ = self.visit(ast.obj,c) #=>Symbol
        array_typ = [1,2,3,4,6]
        if obj_.mtype in array_typ:
            '''E is not in class type => int, float,...'''
            raise TypeMismatchInStatement(ast)

        '''Access static method with object error'''
        for class_ in c:
            if obj_.mtype == class_["name"]:
                check, sym = self.checkExistingIdFunction([class_["array"][-1]], ast.method.name)
                if check and sym.kind == "Method" and self.IsStatic(ast.method.name):
                    raise IllegalMemberAccess(ast)

        '''Method must be void type'''
        name = ast.method.name
        sym = self.checkAccess(ast, name, c, Method(), "Method")
        if sym.mtype.rettype != 6 : 
            raise TypeMismatchInStatement(ast)

        '''Check number of argument'''

        if len(ast.param) != len(sym.mtype.partype):
            raise TypeMismatchInStatement(ast)

        for i in range(len(sym.mtype.partype)):
            if not self.checkTypeOfSide(sym.mtype.partype[i], self.visit(ast.param[i],c).mtype,c, None):
                raise TypeMismatchInStatement(ast)                

    def visitInstance(self, ast,c): pass

    def visitStatic(self, ast,c): pass

    def visitIntType(self, ast,c):
        return Symbol(mtype = 1, kind= "IntType")

    def visitFloatType(self, ast,c):
        return Symbol(mtype = 2, kind= "FloatType")

    def visitStringType(self, ast,c):
        return Symbol(mtype = 3, kind= "StringType")
    
    def visitBoolType(self, ast,c): 
        return Symbol(mtype = 4, kind= "BoolType")

    def visitArrayType(self, ast,c):
        typ = self.visit(ast.eleType, c).mtype  #=> symbol
        return Symbol(mtype = Atype( ast.size, typ), kind= "ArrayType")
    
    def visitVoidType(self, ast,c):
        return Symbol(mtype = 6, kind= "VoidType")
    
    def visitClassType(self, ast,c):
        for class_ in c:
            if class_["name"] == ast.classname.name:
                return Symbol(mtype = class_["name"], kind = "ClassType")
        raise Undeclared(Class(),ast.classname.name)
    
    '''Visit Literal'''
    def visitIntLiteral(self, ast,c): 
        return Symbol(mtype = 1, kind = "IntLit")

    def visitFloatLiteral(self, ast,c): 
        return Symbol(mtype = 2, kind = "FloatLit")

    def visitStringLiteral(self, ast,c): 
        return Symbol(mtype = 3, kind = "StringLit")

    def visitBooleanLiteral(self, ast,c): 
        return Symbol(mtype = 4, kind = "BooleanLit")

    def visitNullLiteral(self, ast,c): 
        return Symbol(mtype=5, kind = "NullLit")

    def visitSelfLiteral(self, ast,c): 
        return Symbol(mtype = c[0]["name"], kind="SelfLit")
    
    def recursiveCheckArrayType(self, l,r):
        if l.size == r.size:
            if isinstance(l.atype, Atype) and isinstance(r.atype, Atype):
                return self.recursiveCheckArrayType(l.atype, r.atype)
            else:
                return l.atype == r.atype
        return False

    def innerCheckArray(self, ast,c, originals):
        for i in range (len(ast.value)-1):
            if isinstance(ast.value[i],ArrayLiteral) and isinstance(ast.value[i + 1],ArrayLiteral):
                lhs = self.visitArray(ast.value[i],c, originals).mtype
                rhs = self.visitArray(ast.value[i+1],c, originals).mtype
            else: 
                lhs = self.visit(ast.value[i],c).mtype
                rhs = self.visit(ast.value[i+1],c).mtype

            if isinstance(lhs, Atype) and isinstance(rhs, Atype):
                if not self.recursiveCheckArrayType(lhs,rhs):
                    raise IllegalArrayLiteral(originals)
            else:   
                if lhs != rhs: 
                    raise IllegalArrayLiteral(originals)

    def visitArray(self, ast, c, originals):
        self.innerCheckArray(ast, c, originals)
        return Symbol(mtype = Atype(size = len(ast.value), atype =self.visit(ast.value[0],c).mtype), kind= "ArrayLit")

    def visitArrayLiteral(self, ast,c): 
        self.innerCheckArray(ast,c, ast)
        return Symbol(mtype = Atype(size = len(ast.value), atype =self.visit(ast.value[0],c).mtype), kind= "ArrayLit")
