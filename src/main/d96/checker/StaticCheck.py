
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

        '''Fisrt store all attribute and method in array'''
        self.firstCheck(ast,c)

        for mem in ast.memlist:
            res = self.visit(mem,c) # => return Symbol(name, kind, mtype, value)
            if ast.classname.name == "Program" and res.name == "main" and len(res.mtype.partype) == 0 and res.mtype.rettype == 6:
                self.check_entry = True

    def firstCheck(self, ast, c):
        for decl_ in ast.memlist:
            if isinstance(decl_, AttributeDecl):
                if isinstance(decl_.decl, VarDecl):
                    if decl_.decl.variable.name in c[0]["array"][0]:
                        raise Redeclared(Attribute(),decl_.decl.variable.name)
                    else:
                        c[0]["array"][0][decl_.decl.variable.name] = Symbol(decl_.decl.variable.name,"Attr",self.visit(decl_.decl.varType,c).mtype,decl_.decl.varInit)
                elif isinstance(decl_.decl, ConstDecl):
                    if decl_.decl.constant.name in c[0]["array"][0]:
                        raise Redeclared(Attribute(),decl_.decl.constant.name)
                    else:
                        c[0]["array"][0][decl_.decl.constant.name] = Symbol(decl_.decl.constant.name,"Attr",self.visit(decl_.decl.constType,c).mtype,decl_.decl.value)
            elif isinstance(decl_, MethodDecl):
                method_name = decl_.name.name
                if method_name in c[0]["array"][0]:
                    raise Redeclared(Method(),method_name)
                else:
                    c[0]["array"][0][method_name] = Symbol(method_name,"Method",None,None)
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
    
    def parentList(self, childName, parentList, c):
        for class_ in c:
            if class_["name"] == childName:
                parentList.append(class_["name"])
                if class_["parent"]:
                    self.parentList(class_["parent"],parentList,c)
                return parentList


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

            # '''LHS is array type'''
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

    # kind: SIKind  # Instance or Static
    # decl: StoreDecl  # VarDec
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


        env[0]["array"].insert(0, {})

        for param_ in ast.param:
            self.visitParam(param_,env)
        
        temp = self.visitBody(ast.body,env)
        c[0]["array"][0][ast.name.name] = Symbol(ast.name.name,"Method", MType([p.varType for p in ast.param], temp))
        return c[0]["array"][0][ast.name.name]

    def visitParam(self, ast, env):
        if ast.variable.name in env[0]["array"][0]:
            raise Redeclared(Parameter(),ast.variable.name)

        '''Check undeclare class in param'''
        self.visit(ast.varType, env)

        env[0]["array"][0][ast.variable.name] = Symbol(ast.variable.name,ast.varType, ast.varInit)
    
    def visitBody(self, ast, c):
        temp = 6
        for inst_ in ast.inst:
            sym = self.visit(inst_,c)
            if isinstance(inst_, Return):
                temp = sym.mtype
        return temp
            

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

        '''Check undeclare attribute or method'''
        check = self.recursiveCheckAttribute(ast.name, c[0], c)    
        if check is None: raise Undeclared(Identifier(),ast.name)
        return check

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

    def checkAccess(self, ast, attName, c): 
        if self.IsStatic(attName):
            declare_class = False
            obj = self.visit(ast.obj,c) #=> Symbol(A, "ClassType")
            for class_ in c:
                if class_["name"] == obj.mtype:
                    declare_class = True
            className = obj.mtype
            if not declare_class: raise Undeclared(Class(), className)
            return self.checkMethodClass_Parent(className, attName, c, Attribute())
        else:
            '''Check undeclare object'''
            obj = self.visit(ast.obj, c) #=> Symbol(name, kind, A, value)
            className = obj.mtype

            '''Check if attribute is in parent class or not'''
            return self.checkMethodClass_Parent(className, attName, c, Attribute())


    def visitCallExpr(self, ast,c):
        name = ast.method.name
        self.checkAccess(ast, name, c)
        for param_ in ast.param: self.visit(param_,c)

    def visitFieldAccess(self, ast,c):
        name = ast.fieldname.name
        '''Check is declared object, attribute'''
        sym = self.checkAccess(ast, name, c) #=> symbol of attribute

        return sym

    def visitAssign(self, ast,c):
        lhs = self.visit(ast.lhs,c) # =>Symbol
        rhs = self.visit(ast.exp,c) # =>Symbol
        '''LHS cant be void'''
        # if lhs.mtype == 6: raise TypeMismatchInStatement(ast)
        # both_side_same = False

        '''LHS = float, RHS = int'''
        # if lhs.mtype == rhs.mtype or (lhs.mtype == 2 and rhs.mtype == 1):
        #     both_side_same = True

        '''RHS are subtype of LHS'''
        # if rhs.kind == "ClassType" and lhs.kind =="ClassType":
        #     child_name = rhs.mtype.classname.name
        #     parent_name = lhs.mtype.classname.name
        #     for class_ in c:
        #         if class_["name"] == child_name and class_["parent"] == parent_name:
        #             both_side_same = True
        #             break

        '''LHS is array type'''
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

        # if both_side_same == False: raise TypeMismatchInStatement(ast)
        
        '''Check constant'''
        # if lhs.kind == "Var": raise CannotAssignToConstant(ast)
        
        self.visit(ast.exp,c)

    def visitIf(self, ast,c):
        typ = self.visit(ast.expr, c)
        if typ != 4:
            raise TypeMismatchInStatement(ast)

    def visitFor(self, ast,c):
        '''Check type of scalar , exp1, exp2'''
        scalar_var = self.visit(ast.id) # => Symbol
        exp1 = self.visit(ast.expr1) # => Symbol
        exp2 = self.visit(ast.expr2) # => Symbol
        if (scalar_var != 1 or exp1 != 1 or exp2 != 1):
            raise TypeMismatchInStatement(ast)
        
        '''Check immutable variable'''
        if scalar_var.kind == "Var": raise CannotAssignToConstant(Assign(ast.id,ast.exp))
        
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
        if ast.expr == None: return Symbol(None, None, 6, None)
        return self.visit(ast.expr, c)
        
    def visitCallStmt(self, ast,c): pass

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