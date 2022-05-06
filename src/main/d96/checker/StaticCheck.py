
"""
 * @author nhphung
"""
from ast import Pass
from typing_extensions import Literal
from AST import * 
from Visitor import *
from StaticError import *

from main.d96.utils.AST import FieldAccess, NullLiteral


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

        self.ast = ast
        self.global_env = []
        self.check_entry = False

    def check(self):
        return self.visit(self.ast, self.global_env)

    def visitProgram(self,ast, c): 
        # c = [{"array":[{}], "name": None, "parent":None}]
        '''Visit all class in program'''
        for decl in ast.decl:
            self.visit(decl,c)

        '''Check entry point'''
        if not self.check_entry: raise NoEntryPoint()
        return []

    def visitClassDecl(self, ast,c):
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
        
        c.insert(0,{"array":[{}], "name": ast.classname.name, "parent":parent_name}) 

        '''Memlist -> Attribute Decl || Method Decl'''
        for mem in ast.memlist:
            res = self.visit(mem,c) # => return Symbol(name, kind, mtype, value)
            if ast.classname.name == "Program" and res.name == "main" and len(res.mtype.partype) == 0 and res.mtype.rettype == 6:
                self.check_entry = True

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

        if name in c[0]["array"][0]:
            raise Redeclared(Attribute(),name)

        '''Check undeclare class type'''
        typ_ = self.visit(typ, c) #=> Symbol(mtype, kind)
        
        undeclare_class = True

        if typ_.kind == "ClassType":
            for class_ in c:
                if typ_.mtype == class_["name"]: undeclare_class = False
            if undeclare_class: raise Undeclared(Class(),typ_.mtype)
        

        '''Check with const decl'''
        if kind == "Val":
            if value is None: raise IllegalConstantExpression(None)

            '''Visit value and check if operands is const'''
            if isinstance(value, Id) or isinstance(value, Id):
                    raise IllegalConstantExpression(ast.value)
        
            self.check_const_decl = True
            value = self.visit(value,c) #=> Symbol
            self.check_const_decl = False

            if self.error_const_decl:
                raise IllegalConstantExpression(ast.value)
            
            
            if value.mtype == 6: raise IllegalConstantExpression(ast.value)


            if not self.checkTypeOfSide(typ_.mtype, value.mtype,c, value.mtype): 
                raise TypeMismatchInConstant(ast)


        '''Visit value'''
        if kind == "Var":
            if value:
                value = self.visit(value,c)
                if not self.checkTypeOfSide(typ_.mtype, value.mtype,c,value.mtype): 
                    raise TypeMismatchInStatement(ast)

        '''Store attribute'''
        c[0]["array"][0][name] = Symbol(name,kind,typ_.mtype,value)

        return c[0]["array"][0][name]

    def visitMethodDecl(self, ast,c):
        env = []
        '''Copy c to env'''
        self.shallowCopy(c,env)

        '''Check if method was declared or not'''
        if ast.name.name in env[0]["array"][0]:
            raise Redeclared(Method(),ast.name.name)
        env[0]["array"].insert(0, {})

        for param_ in ast.param:
            self.visitParam(param_,env)
        
        temp = self.visitBody(ast.body,env)
        c[0]["array"][0][ast.name.name] = Symbol(ast.name.name,"Method", MType([self.visit(p.varType,c).mtype for p in ast.param], temp))
        
        return c[0]["array"][0][ast.name.name]

    def visitBody(self, ast, c):
        temp = 6
        for inst_ in ast.inst:
            sym = self.visit(inst_,c)
            if isinstance(inst_, Return):
                temp = sym.mtype
                break
        return temp
    '''--------------Decl--------------'''
    def visitVarDecl(self, ast,c): 
        '''Check if id was declared or not''' 
        if ast.variable.name in c[0]["array"][0]:
            raise Redeclared(Variable(),ast.variable.name)

        '''Check undeclare class => Var a:A''' 
        typ = self.visit(ast.varType, c) #=> Symbol(mtype, kind)
        undeclare_class = True

        if typ.kind == "ClassType":
            for class_ in c:
                if typ.mtype == class_["name"]: undeclare_class = False
            if undeclare_class: raise Undeclared(Class(),typ.mtype)


        '''Visit Value'''
        if ast.varInit:
            value = self.visit(ast.varInit,c)

            if not self.checkTypeOfSide(typ.mtype, value.mtype,c,self.visit(ast.varInit,c).mtype): 
                raise TypeMismatchInStatement(ast)

        '''Store variable value'''
        c[0]["array"][0][ast.variable.name] = Symbol(ast.variable.name,"Var", self.visit(ast.varType,c).mtype, ast.varInit)
    
    def visitConstDecl(self, ast,c):
        '''Check if id was declared or not''' 
        if ast.constant.name in c[0]["array"][0]:
            raise Redeclared(Constant(),ast.constant.name)

        '''Check declare class type =>  Val a: A'''
        typ = self.visit(ast.constType, c) #=> Symbol(mtype, kind)
        undeclare_class = True
        
        if typ.kind == "ClassType":
            for class_ in c:
                if typ.mtype == class_["name"]: undeclare_class = False
            if undeclare_class: raise Undeclared(Class(),typ.mtype)

        '''If value of const is None'''
        if ast.value is None: raise IllegalConstantExpression(None)

        '''Visit value and check if operands is const'''
        if isinstance(ast.value, Id) or isinstance(ast.value, Id):
                raise IllegalConstantExpression(ast.value)
    
        self.check_const_decl = True
        value = self.visit(ast.value,c) #=> Symbol
        self.check_const_decl = False

        if self.error_const_decl:
            raise IllegalConstantExpression(ast.value)
        
        
        if value.mtype == 6: raise IllegalConstantExpression(ast.value)
        """'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

        if not self.checkTypeOfSide(typ.mtype, value.mtype,c,self.visit(ast.value,c).mtype): 
            raise TypeMismatchInConstant(ast)

        '''Store constant value'''
        c[0]["array"][0][ast.constant.name] = Symbol(ast.constant.name,"Val",typ.mtype, ast.value)

    def parentList(self, childName, parentList, c):
        for class_ in c:
            if class_["name"] == childName:
                parentList.append(class_["name"])
                if class_["parent"]:
                    self.parentList(class_["parent"],parentList,c)
                return parentList

    def visitParam(self, ast, env):
        if ast.variable.name in env[0]["array"][0]:
            raise Redeclared(Parameter(),ast.variable.name)

        '''Check undeclare class in param'''
        self.visit(ast.varType, env)
        env[0]["array"][0][ast.variable.name] = Symbol(ast.variable.name,"Var",self.visit(ast.varType, env).mtype, ast.varInit)
    
    def visitBlock(self, ast,c):
        env = []
        self.shallowCopy(c,env)
        env[0]["array"].insert(0, {})

        for inst_ in ast.inst:
            self.visit(inst_,env)

    def recursiveCheckAttribute(self, target, currentClass, c):
        for env_ in currentClass["array"]:
            if target in env_:
                return env_[target]  #=> Symbol
        if currentClass["parent"] is not None:
            for class_ in c:
                if class_["name"] == currentClass["parent"]:
                    return self.recursiveCheckAttribute(target, class_, c)

    def visitId(self, ast,c):

        '''Check if id is a class name'''
        for class_ in c:
            if class_["name"] == ast.name: return  Symbol(mtype = class_["name"], kind = "ClassType")
        
        for i in range(len(c[0]["array"])-1):
            if ast.name in c[0]["array"][i]:
                return c[0]["array"][i][ast.name]  #=>Symbol
    
        raise Undeclared(Identifier(),ast.name)

    #int 1, float 2, string 3, bool 4
    def visitBinaryOp(self, ast,c): 
        lhs = self.visit(ast.left,c).mtype # => Symbol
        rhs = self.visit(ast.right,c).mtype # => Symbol
        
        '''Check constdecl'''
        if self.check_const_decl:
            if isinstance(ast.left, Id) or isinstance(ast.right, Id):
                self.error_const_decl = True
            if isinstance(ast.left, NullLiteral) or isinstance(ast.right, NullLiteral):
                self.error_const_decl = True

        if ast.op in ['-', '+', '*', '/']:
            if lhs == 1 and rhs == 1: return Symbol(mtype=1, kind = "BinOp")
            elif (lhs in [1,2]) and (rhs in [1,2]): return Symbol(mtype=2, kind = "BinOp")
            else:
                raise TypeMismatchInExpression(ast)
        if ast.op == '%':
            if lhs != 1 or rhs != 1: raise TypeMismatchInExpression(ast)
            return Symbol(mtype=1, kind = "BinOp")

        if ast.op in ["==", "!="]:
            if rhs == lhs == 1 or rhs == lhs == 4: return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(ast)

        if ast.op in ["<", ">", "<=", ">="]: 
            if (lhs in [1,2]) and (rhs in [1,2]) : return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["&&", "||"]:
            if rhs == lhs == 4: return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(ast)
        
        if ast.op == "+.":
            if rhs == lhs == 3: return Symbol(mtype=3, kind = "BinOp")
            raise TypeMismatchInExpression(ast)
        
        if ast.op == "==.":
            if rhs == lhs == 3: return Symbol(mtype=4, kind = "BinOp")
            raise TypeMismatchInExpression(ast)

    #int 1, float 2, string 3, bool 4
    def visitUnaryOp(self, ast,c):
        typ = self.visit(ast.body,c).mtype
        if ast.op == "!":
            if typ != 4: raise TypeMismatchInExpression(ast)
            return Symbol(mtype=4, kind = "UnaryOp")
        if ast.op == "-":
            if typ == 1: return Symbol(mtype=1, kind = "UnaryOp")
            if typ == 2: return Symbol(mtype=2, kind = "UnaryOp")
            raise TypeMismatchInExpression(ast)
        if self.check_const_decl:
            if not isinstance(ast.body, BinaryOp) and not isinstance(ast.body, UnaryOp):
                    self.error_const_decl = True

    def visitNewExpr(self, ast,c):
        for class_ in c:
            if class_["name"] == ast.classname.name:
                return Symbol(mtype = class_["name"], kind ="ClassType")
        raise Undeclared(Class(),ast.classname.name)

    def isPrimitiveType(self, typ):
        if typ in [1,2,3,4,6]: return True
        return False

    def visitArrayCell(self, ast,c): 
        array = self.visit(ast.arr, c)
        '''E1[E2] => E1 must be array type'''
        if not isinstance(array.mtype, Atype): raise TypeMismatchInExpression(ast)

        '''E1[E2] => E2 must be int'''
        for idx in ast.idx:
            if self.visit(idx, c).mtype != 1: 
                raise TypeMismatchInExpression(ast)

    def IsStatic(self, name):
        if name[0] == "$": return True
        return False

    def checkMethodClass_Parent(self, className, methodName, c, error):
        for class_ in c:
            if class_["name"] == className:
                '''Check in current class'''
                if methodName in class_["array"][-1]:
                    if self.check_const_decl:
                        if class_["array"][-1][methodName].kind == "Var":
                            self.error_const_decl = True
                    return class_["array"][-1][methodName]
                # for env_ in class_["array"]:
                #     if methodName in env_: return env_[methodName] #=> Symbol
                '''Check in parent class'''
                if class_["parent"] is not None:
                    return self.checkMethodClass_Parent(class_["parent"], methodName, c, error)
        raise Undeclared(error, methodName)

    def checkAccess(self, ast, attName, c, error): 
        if self.IsStatic(attName):
            declare_class = False
            for class_ in c:
                if class_["name"] == ast.obj.name: 
                    declare_class = True
                    break
            className = ast.obj.name
            if not declare_class: raise Undeclared(Class(), className)
            return self.checkMethodClass_Parent(className, attName, c, error)
        else:
            '''Check undeclare object'''
            if not isinstance(ast.obj, SelfLiteral):                        
                undeclare = True
                for i in range(len(c[0]["array"])-1):
                    
                    if ast.obj.name in c[0]["array"][i]:
                        undeclare = False
                if undeclare: raise Undeclared(Identifier(), ast.obj.name)        
                
                obj = self.visit(ast.obj, c) #=> Symbol(name, kind, A, value)
                className = obj.mtype
                '''Check if attribute is in parent class or not'''
            else:    
                className = self.visit(ast.obj,c).mtype
            return self.checkMethodClass_Parent(className, attName, c, error)

    def visitCallExpr(self, ast,c):
        '''E.<method name>(<args>)'''

        for class_ in c:
            if ast.obj.name == class_["name"]:
                if ast.method.name in class_["array"][-1]:
                    if not self.IsStatic(ast.method.name):
                        raise IllegalMemberAccess(ast)

        '''E must be in class type'''
        obj_ = self.visit(ast.obj,c) #=>Symbol
        array_typ = [1,2,3,4,6]
        if obj_.mtype in array_typ:
            raise TypeMismatchInExpression(ast)

        for class_ in c:
            if obj_.mtype == class_["name"]:
                if ast.method.name in class_["array"][-1]:
                    if self.IsStatic(ast.method.name):
                        raise IllegalMemberAccess(ast)

        '''Method must be void type'''
        name = ast.method.name
        sym = self.checkAccess(ast, name, c, Method())
        if sym.mtype.rettype == 6 : raise TypeMismatchInExpression(ast)

        '''Check number of argument'''
        if len(ast.param) != len(sym.mtype.partype):
            raise TypeMismatchInExpression(ast)

        for i in range(len(sym.mtype.partype)):
            if not self.checkTypeOfSide(sym.mtype.partype[i], self.visit(ast.param[i],c).mtype,c, [self.visit(param,c).mtype for param in ast.param]):
                raise TypeMismatchInExpression(ast)                
        return sym

    def visitFieldAccess(self, ast,c):
        '''Class::<$static>'''
        '''Object.<att>'''

        '''if obj is class'''
        if not isinstance(ast.obj, SelfLiteral):
            for class_ in c:
                if ast.obj.name == class_["name"] and ast.fieldname.name in class_["array"][-1] and not self.IsStatic(ast.fieldname.name):
                    raise IllegalMemberAccess(ast)

        obj = self.visit(ast.obj,c)
        '''obj must be in class type'''
        if obj.mtype in [1,2,3,4,6]:
            raise TypeMismatchInExpression(ast)


        #  obj::$a
        if not isinstance(ast.obj, SelfLiteral):
            for class_ in c:
                if obj.mtype == class_["name"] and ast.obj.name != class_["name"]:
                    if ast.fieldname.name in class_["array"][-1]:
                        if self.IsStatic(ast.fieldname.name):
                            raise IllegalMemberAccess(ast)
        '''Trường hợp  att trùng với class name'''
        
        name = ast.fieldname.name
        
        '''Check declared object, attribute'''
        sym = self.checkAccess(ast, name, c, Attribute()) #=> symbol of attribute
        return sym

    def visitAssign(self, ast,c):
        lhs = self.visit(ast.lhs,c) # =>Symbol
        if lhs.kind == "Val": raise CannotAssignToConstant(ast)

        rhs = self.visit(ast.exp,c) # =>Symbol
        lhs_type = lhs.mtype if not  isinstance(lhs.mtype, MType) else lhs.mtype.rettype
        rhs_type = rhs.mtype if not isinstance(rhs.mtype, MType) else rhs.mtype.rettype
        '''LHS cant be void'''
        if lhs_type == 6: raise TypeMismatchInStatement(ast)

        if not self.checkTypeOfSide(lhs_type, rhs_type, c, self.visit(ast.exp,c).mtype):
            raise TypeMismatchInStatement(ast)

        self.visit(ast.exp,c)

    def visitIf(self, ast,c):
        typ = self.visit(ast.expr, c)
        if typ.mtype != 4:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, c)

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
        if ast.expr == None: return Symbol(mtype= 6)
        return self.visit(ast.expr, c)
    
    def checkTypeOfSide(self, lhs, rhs, c, rhs_literal):

        if isinstance(rhs_literal, list):
            for i in range(len(rhs_literal)):
                if not self.checkTypeOfSide(lhs, rhs_literal[i], c, rhs_literal[i]):
                    return False
            return True

        '''LHS = float, RHS = int'''
        if lhs == rhs or (lhs == 2 and rhs == 1): return True

        '''RHS are subtype of LHS'''
        array_typ = [1,2,3,4,6]
        if not (isinstance(lhs, Atype) and isinstance(rhs, Atype)):
            if rhs not in array_typ and lhs not in array_typ:
                child_name = rhs
                parent_name = lhs
                parent_list = []
                parent_list = self.parentList(child_name, parent_list, c)
                if parent_name in parent_list: return True
        
        if isinstance(lhs, Atype) and isinstance(rhs, Atype):    
            if lhs.size != rhs_literal.size: return False
            if not self.checkTypeOfSide(lhs.atype, rhs.atype, c, rhs.atype):
                return False
            return True   

        return False

    def visitCallStmt(self, ast,c):
        '''E.<method name>(<args>)'''
        name = ast.method.name
        self.checkAccess(ast, name, c, Method())
        
        '''E must be in class type'''
        obj_ = self.visit(ast.obj,c) #=>Symbol
        array_typ = [1,2,3,4,5,6]
        if obj_.mtype in array_typ:
            raise TypeMismatchInStatement(ast)

        '''Method must be void type'''
        name = ast.method.name
        sym = self.checkAccess(ast, name, c, Method())
        if sym.mtype.rettype != 6 : raise TypeMismatchInStatement(ast)

        '''Check number of argument'''
        if len(ast.param) != len(sym.mtype.partype):
            raise TypeMismatchInStatement(ast)

        for i in range(len(sym.mtype.partype)):
            if not self.checkTypeOfSide(sym.mtype.partype[i], self.visit(ast.param[i],c).mtype,c, [self.visit(param,c).mtype for param in ast.param]):
                raise TypeMismatchInStatement(ast)                
        return sym

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
                print("ArrayLiteral")
                lhs = self.visitArray(ast.value[i],c, originals).mtype
                rhs = self.visitArray(ast.value[i+1],c, originals).mtype
            else: 
                lhs = self.visit(ast.value[i],c).mtype
                rhs = self.visit(ast.value[i],c).mtype

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

    def shallowCopy(self,c,env):
        for i in c:
            temp = []
            for j in i["array"]:
                temp.append(j.copy())
            env.append({"array":temp, "name": i["name"], "parent": i["parent"]})