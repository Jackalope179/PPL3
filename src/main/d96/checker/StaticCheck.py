
"""
 * @author nhphung
"""
from ast import Pass
from AST import * 
from Visitor import *
from StaticError import *
import copy

from main.d96.utils.AST import Instance

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
        self.check_in_loop = False
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

    # classname: Id
    # memlist: List[MemDecl]
    # parentname: Id = None
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
        typ = self.visit(typ,c) # => Symbol

        '''Visit value'''
        if value:
            self.visit(value,c)

        '''Store attribute'''
        c[0]["array"][0][name] = Symbol(name,kind,typ.mtype,value)

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
        c[0]["array"][0][ast.name.name] = Symbol(ast.name.name,"Method", MType([p.varType for p in ast.param], temp))
        
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
        if isinstance(ast.varType, ClassType): 
            self.visit(ast.varType,c)

        '''Visit Value'''
        if ast.varInit:
            self.visit(ast.varInit,c)

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

        '''Check type if value is exist'''
        if ast.value:
            value = self.visit(ast.value,c) #=> Symbol

            both_side_same = False

            '''LHS = float, RHS = int'''
            if typ.mtype == value.mtype or (typ.mtype == 2 and value.mtype == 1):
                both_side_same = True

            '''RHS are subtype of LHS -> subclasses'''
            if typ.kind == "ClassType" and value.kind == "ClassType":
                parent_name = typ.mtype   # => lhs
                child_name = value.mtype  # => rhs
                parent_list = []
                parent_list = self.parentList(child_name, parent_list, c)
                if parent_name in parent_list:
                    both_side_same = True

            '''LHS is array type'''
            # if isinstance(constant, Symbol):
            #     if self.visit(constant.mtype, c) == 5:
            #         size = constant.mtype.size
            #         eleType = value.mtype.eleType

            #         '''Check size of LHS and RHS'''
            #         if size != value.length: raise TypeMismatchInConstant(ast)

            #         '''Check type of all element in RHS'''
            #         for i in range(size):
            #             if eleType == 2:
            #                 '''If LHS is float => RHS is int or float'''
            #                 if value[i] != 1  and value[i] != 2: raise TypeMismatchInConstant(ast)
            #             elif eleType in [1,3,4]:
            #                 if eleType != value[i]: raise TypeMismatchInConstant(ast)
            #             else:
            #                 '''If LHS is classType (className)'''
                            
            #                 both_side_same = False
            #                 for class_ in c:
            #                     if class_["name"] == value[i].mtype.classname.name and class_["parent"] == parent_name:
            #                         both_side_same = True
            #                 if not both_side_same: raise TypeMismatchInConstant(ast)

            if both_side_same == False: raise TypeMismatchInConstant(ast)

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
       

        for i in range(len(c[0]["array"])-1):
            if ast.name in c[0]["array"][i]:
                return c[0]["array"][i][ast.name]  #=>Symbol

        '''Check if id is a class name'''
        for class_ in c:
            if class_["name"] == ast.name: return  Symbol(mtype = class_["name"], kind = "ClassType")
        raise Undeclared(Identifier(),ast.name)

    #int 1, float 2, string 3, bool 4
    def visitBinaryOp(self, ast,c): 
        lhs = self.visit(ast.left,c).mtype # => Symbol
        rhs = self.visit(ast.right,c).mtype # => Symbol

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

    def visitNewExpr(self, ast,c):
        for class_ in c:
            if class_["name"] == ast.classname.name:
                return Symbol(mtype = class_["name"], kind ="ClassType")
        raise Undeclared(Class(),ast.classname.name)

    def visitArrayCell(self, ast,c): 
        arr = self.visit(ast.arr)
        '''E1[E2] => E1 must be array type'''
        if isinstance(arr, Symbol):
            if not isinstance(arr.mtype, ArrayType):
                raise TypeMismatchInExpression(ast)
        '''E1[E2] => E2 must be int'''
        for idx in ast.idx:
            if self.visit(idx, c) != 1: 
                raise TypeMismatchInExpression(ast)

    def IsStatic(self, name):
        if name[0] == "$": return True
        return False

    def checkMethodClass_Parent(self, className, methodName, c, error):
        for class_ in c:
            if class_["name"] == className:
                '''Check in current class'''
                for env_ in class_["array"]:
                    if methodName in env_: return env_[methodName] #=> Symbol
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
            undeclare = True
            for i in range(len(c[0]["array"])-1):
                if ast.obj.name in c[0]["array"][i]:
                    undeclare = False
            if undeclare: raise Undeclared(Identifier(), ast.obj.name)        
            
            obj = self.visit(ast.obj, c) #=> Symbol(name, kind, A, value)
            className = obj.mtype

            '''Check if attribute is in parent class or not'''
            return self.checkMethodClass_Parent(className, attName, c, error)


    def visitCallExpr(self, ast,c):
        name = ast.method.name
        sym = self.checkAccess(ast, name, c, Method())
        for param_ in ast.param: self.visit(param_,c)
        return sym

    def visitFieldAccess(self, ast,c):
        name = ast.fieldname.name
        '''Check is declared object, attribute'''
        sym = self.checkAccess(ast, name, c, Attribute()) #=> symbol of attribute
        return sym

    def visitAssign(self, ast,c):
        lhs = self.visit(ast.lhs,c) # =>Symbol
        if lhs.kind == "Val": raise CannotAssignToConstant(ast)

        rhs = self.visit(ast.exp,c) # =>Symbol

        lhs_type = lhs.mtype if not isinstance(lhs.mtype, MType) else lhs.mtype.rettype
        rhs_type = rhs.mtype if not isinstance(rhs.mtype, MType) else rhs.mtype.rettype
        '''LHS cant be void'''
        if lhs_type == 6: raise TypeMismatchInStatement(ast)

        if not self.checkTypeOfSide(lhs_type, rhs_type, c):
            raise TypeMismatchInStatement(ast)
            
        # if self.visit(lhs.mtype, c) == 5:
        #     size = lhs.mtype.size
        #     eleType = lhs.mtype.eleType

        #     '''Check size of LHS and RHS'''
        #     if size != rhs.length: raise TypeMismatchInStatement(ast)

        #     '''Check type of all element in RHS'''
        #     for i in range(size):
        #         if eleType == 2:
        #             '''If LHS is float => RHS is int or float'''
        #             if rhs[i] != 1  and rhs[i] != 2: raise TypeMismatchInStatement(ast)
        #         elif eleType in [1,3,4]:
        #             if eleType != rhs[i]: raise TypeMismatchInStatement(ast)
        #         else:
        #             '''If LHS is classType (className)'''
                    
        #             both_side_same = False
        #             for class_ in c:
        #                 if class_["name"] == rhs[i].mtype.classname.name and class_["parent"] == parent_name:
        #                     both_side_same = True
        #             if not both_side_same: raise TypeMismatchInStatement(ast)

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
        StaticChecker.check_in_loop = True
        self.visit(ast.loop, c)

    def visitBreak(self, ast,c):
        if not StaticChecker.check_in_loop:
            raise MustInLoop(ast)

    def visitContinue(self, ast,c):
        if not StaticChecker.check_in_loop:
            raise MustInLoop(ast)

    def visitReturn(self, ast,c):
        if ast.expr == None: return Symbol(mtype= 6)
        return self.visit(ast.expr, c)
    
    def checkTypeOfSide(self, lhs, rhs, c):
        both_side_same = False

        '''LHS = float, RHS = int'''
        if lhs == rhs or (lhs == 2 and rhs == 1):
            both_side_same = True

        '''RHS are subtype of LHS'''
        array_typ =[1,2,3,4,5,6]
        if rhs not in array_typ and lhs not in array_typ:
            child_name = rhs
            parent_name = lhs
            parent_list = []
            parent_list = self.parentList(child_name, parent_list, c)
            if parent_name in parent_list:
                both_side_same = True
        return both_side_same

    def visitCallStmt(self, ast,c):
        '''E.<method name>(<args>)'''

        '''E must be in class type'''
        obj_ = self.visit(ast.obj,c) #=>Symbol
        array_typ = [1,2,3,4,5,6]
        if obj_.mtype in array_typ:
            raise TypeMismatchInStatement(ast)

        '''Method must be void type'''
        name = ast.method.name
        sym = self.checkAccess(ast, name, c, Method())
        if sym.mtype.rettype != 6 : raise TypeMismatchInStatement(ast)

        for i in range(len(sym.mtype.partype)):
            if not self.checkTypeOfSide(sym.mtype.partype[i], self.visit(ast.param[i],c).mtype):
                raise TypeMismatchInStatement(ast)                
        return sym

    def visitInstance(self, ast,c): pass

    def visitStatic(self, ast,c): pass


    '''Visit Type'''
    def visitIntType(self, ast,c):
        return Symbol(mtype = 1, kind= "IntType")

    def visitFloatType(self, ast,c):
        return Symbol(mtype = 2, kind= "FloatType")

    def visitStringType(self, ast,c):
        return Symbol(mtype = 3, kind= "StringType")
    
    def visitBoolType(self, ast,c): 
        return Symbol(mtype = 4, kind= "BoolType")

    def visitArrayType(self, ast,c):
        typ = self.visit(ast.eleType, c).value  #=> symbol
        return Symbol(mtype = Atype(typ, ast.size), kind= "ArrayType")
    
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
        return Symbol(None, None, "Null", None)

    def visitSelfLiteral(self, ast,c): 
        return Symbol(None, None, "Self", None)

    # value: List[Expr]
    def visitArrayLiteral(self, ast,c): 
        for i in range (len(ast.value)-1):
            if self.visit(ast.value[i]).value != self.visit(ast.value[i+1]).value:
                raise IllegalArrayLiteral(ast) 
        return Symbol(mtype = [self.visit(ast.value[i]).value for i in range (len(ast.value))])
    '''Return Symbol(mtype = [1,2,3,4])'''

    def shallowCopy(self,c,env):
        for i in c:
            temp = []
            for j in i["array"]:
                temp.append(j.copy())
            env.append({"array":temp, "name": i["name"], "parent": i["parent"]})