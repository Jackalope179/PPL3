
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

class Symbol:
    def __init__(self,name,kind, mtype,value = None):
        self.name = name
        self.kind = kind
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):
    
    
    def __init__(self,ast):
        self.check_in_loop = False
        self.check_entry = False
        self.ast = ast
        self.global_env = []

    def check(self):
        return self.visit(self.ast, self.global_env)

    def visitProgram(self,ast, c): 
        # c = [{"array":[{}], "name": None, "parent":None}]

        '''Store all atribute and method first'''
        for i in ast.decl:
            if isinstance(i, AttributeDecl):
                c[0]["array"][0][i.name] = Symbol(i.name,"Attr",i.type,i.value)
            elif isinstance(i, MethodDecl):
                self.visit(i,c)
        '''Check entry Program'''
        if "Program" not in c[0]["array"][0]:
            raise NoEntryPoint()
        

        for decl in ast.decl:
            self.visit(decl,c)

    def firstCheck(self, ast, c):
        for decl_ in ast.decl:
            if isinstance(decl_, AttributeDecl):
                if isinstance(decl_.decl, VarDecl):
                    if decl_.decl.variable.name in c[0]["array"][0]:
                        raise Redeclared(Attribute(),decl_.decl.variable.name)
                    else:
                        c[0]["array"][0][decl_.decl.variable.name] = Symbol(decl_.decl.variable.name,"Attr",decl_.decl.varType,decl_.decl.varInit)
                elif isinstance(decl_.decl, ConstDecl):
                    if decl_.decl.constant.name in c[0]["array"][0]:
                        raise Redeclared(Attribute(),decl_.decl.constant.name)
                    else:
                        c[0]["array"][0][decl_.decl.constant.name] = Symbol(decl_.decl.constant.name,"Attr",decl_.decl.constType,decl_.decl.value)
            elif isinstance(decl_, MethodDecl):
                if ast.name.name in c[0]["array"][0]:
                    raise Redeclared(Method(),ast.name.name)
                else:
                    c[0]["array"][0][ast.name.name] = Symbol(ast.name.name,"Method",ast.type,ast.body)


    '''--------------Decl--------------'''
    def visitVarDecl(self, ast,c): 
        '''Check Redeclare Variable '''
        if ast.variable.name in c[0]["array"][0]:
            raise Redeclared(Variable(),ast.variable.name)

        '''Check undeclare class => Var a:A''' 
        if isinstance(ast.varType, ClassType): 
            self.visit(ast.varType,c)

        '''Visit Value'''
        if ast.varInit:
            self.visit(ast.varInit,c)

        '''Store variable value'''
        c[0]["array"][0][ast.variable.name] = Symbol(ast.variable.name,"Var",ast.varType, ast.varInit)
        
    def visitConstDecl(self, ast,c):
        constant = self.visit(ast.constant) #=> Symbol
        '''Check if id was declared or not''' 
        if constant.name in c[0]["array"][0]:
            raise Redeclared(Constant(),constant.name)

        '''Check declare class type =>  Val a: A'''
        if isinstance(constant.mtype, ClassType): 
            self.visit(constant.constType,c)

        if ast.value:
            value = self.visit(ast.value,c) #=> Symbol or Int
        
        both_side_same = False
        '''LHS = float, RHS = int'''
        if constant.mtype == value.mtype or (constant.mtype == 2 and value.mtype == 1):
            both_side_same = True

        '''RHS are subtype of LHS'''
        child_name = value.mtype.classname.name
        parent_name = constant.mtype.classname.name
        for class_ in c:
            if class_["name"] == child_name and class_["parent"] == parent_name:
                both_side_same = True
                break

        '''LHS is array type'''
        if isinstance(constant, Symbol):
            if self.visit(constant.mtype, c) == 5:
                size = constant.mtype.size
                eleType = value.mtype.eleType

                '''Check size of LHS and RHS'''
                if size != value.length: raise TypeMismatchInConstant(ast)

                '''Check type of all element in RHS'''
                for i in range(size):
                    if eleType == 2:
                        '''If LHS is float => RHS is int or float'''
                        if value[i] != 1  and value[i] != 2: raise TypeMismatchInConstant(ast)
                    elif eleType in [1,3,4]:
                        if eleType != value[i]: raise TypeMismatchInConstant(ast)
                    else:
                        '''If LHS is classType (className)'''
                        
                        both_side_same = False
                        for class_ in c:
                            if class_["name"] == value[i].mtype.classname.name and class_["parent"] == parent_name:
                                both_side_same = True
                        if not both_side_same: raise TypeMismatchInConstant(ast)

        if both_side_same == False: raise TypeMismatchInConstant(ast)

        '''Store constant value'''
        c[0]["array"][0][ast.constant.name] = Symbol(ast.constant.name,"Val",ast.constType, ast.value)

    def visitAttributeDecl(self,ast,c):
        if isinstance(ast.decl, VarDecl):
            name = ast.decl.variable.name
            typ = ast.decl.varType
            value = ast.decl.varInit
            
        else: 
            name = ast.decl.constant.name
            typ = ast.decl.constType
            value = ast.decl.value

        '''Check undeclare class type'''
        self.visit(typ,c)

        '''Visit value'''
        self.visit(value,c)

        '''Store attribute'''
        c[0]["array"][0][name] = Symbol(name,typ, value)

    def visitClassDecl(self, ast,c):
        parent_name = ast.parentname.name if ast.parentname else None
        undeclare_parent = True
        for class_ in c:
            if class_["name"] == ast.classname.name:
                raise Redeclared(Class(),ast.classname.name)
            if parent_name == class_["name"]:
                undeclare_parent = False
        if parent_name and undeclare_parent: 
            raise Undeclared(Class(),parent_name) 
        c.insert(0,{"array":[{}], "name": ast.classname.name, "parent":ast.parentname.name if ast.parentname != None else None}) 
        
        check_entry = False
        for mem in ast.memlist:
            res = self.visit(mem,c)
            if ast.classname.name == "Program" and res.name == "main" and res.mtype.partype.length == 0 and res.mtype.rettype.length == 6:
                check_entry = True
        if not check_entry: raise NoEntryPoint()

    def shallowCopy(self,c,env):
        for i in c:
            temp = []
            for j in i["array"]:
                temp.append(j.copy())
            env.append({"array":temp, "name": i["name"], "parent": i["parent"]})

    def visitMethodDecl(self, ast,c):
        env = []
        self.shallowCopy(c,env)
        env[0]["array"].insert(0, {})

        for param_ in ast.param:
            self.visitParam(param_,env)
        
        temp = self.visitBody(ast.body,env)
        
        c[0]["array"][0][ast.name.name] = Symbol(ast.name.name,"Val", MType([p.varType for p in ast.param], temp))
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

    def visitId(self, ast,c):
        class_env = []
        self.shallowCopy(c, class_env)

        '''Check if id is an attribute in current class'''
        for env_ in c[0]["array"]:
            if ast.name in env_:
                return env_[ast.name] # ====> Symbol    

        '''Check if id is an attribute in parrent class'''
        if c[0]["parent"]:
            for env_ in c:
                if env_["name"] == c[0]["parent"]:
                    if ast.name in env_["array"][-1]:
                        return env_["array"][-1][ast.name]

        '''Check if id is a class name'''
        for env_ in c:
            if env_["name"] == ast.name: return ast.name


        raise Undeclared(Identifier(),ast.name)
    #int 1, float 2, string 3, bool 4
    def visitBinaryOp(self, ast,c): 
        lhs = self.visit(ast.left) # => Symbol
        rhs = self.visit(ast.right) # => Symbol

        if isinstance(lhs, Symbol):
            lhs = lhs.mtype 
        if isinstance(rhs, Symbol):
            rhs = rhs.mtype
        if ast.op in ['-', '+', '*', '/']:
            if lhs == 1 and rhs == 1: return 1
            elif (lhs == 1 and rhs == 2) or (lhs == 2 and rhs == 1)  : return 2
            else: TypeMismatchInExpression(ast)
        if ast.op == '%':
            if lhs != 1 or rhs != 1: raise TypeMismatchInExpression(ast)
            return 1
        if ast.op in ["==", "!="]:
            if rhs == lhs == 1: return 1
            if rhs == lhs == 4: return 4
            raise TypeMismatchInExpression(ast)

        if ast.op in ["<", ">", "<=", ">="]: 
            if rhs == lhs == 1: return 1
            if rhs == lhs == 2: return 2
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["&&", "||"]:
            if rhs == lhs == 4: return 4
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ["==.", "+."]:
            if rhs == lhs == 3: return 3
            raise TypeMismatchInExpression(ast)

    #int 1, float 2, string 3, bool 4
    def visitUnaryOp(self, ast,c):
        sym = self.visit(ast.body)
        if isinstance(sym, Symbol):
            body = sym.body
        if ast.op == "!":
            if sym.mtype != 4: raise TypeMismatchInExpression(ast)
            return 4
        if ast.op == "-":
            if sym.mtype == 1: return 1
            if sym.mtype == 2: return 2
            raise TypeMismatchInExpression(ast)

    def checkMethodClass_Parent(self, className, methodName, c, error):
        parent  = []
        current = []
        declared = False
        for class_ in c:
            if class_["name"] == className:
                declared = True
                current = class_["array"]
                if class_["parent"] is not None:
                    for parent_ in c:
                        if parent_["parent"] == class_["name"]: 
                            parent = parent_["array"]
        if declared == False: raise Undeclared(Class(),className)
        if (methodName not in parent) or (methodName not in current):
            raise Undeclared(error,methodName)

    def visitNewExpr(self, ast,c):
        for class_ in c:
            if class_["name"] == ast.classname.name:
                return class_["name"], 
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

    
    
    def IsStatic(name):
        if name[0] == "$": return True
        return False

    def checkAccess(self, ast, name, c): 
        if StaticChecker.IsStatic(name):
            className = ast.obj.name
            check_undeclared_class = False
            for env_ in c:
                if env_["name"] == className:
                    check_undeclared_class = True
            '''Check undeclared class'''        
            if check_undeclared_class == False: raise Undeclared(Class(),className)
            
            '''Not a className'''
            if isinstance(className, Symbol): 
                raise IllegalMemberAccess(ast)
        else:
            res = self.visit(ast.obj, c)

            if(isinstance(res, Symbol)):
                '''Object name'''
                className = res.name
            else: 
                '''New expr class name'''
                if isinstance(ast.obj, NewExpr):
                    className = res
                else:
                    '''Class Name error'''
                    raise IllegalMemberAccess(ast)

        StaticChecker.checkMethodClass_Parent(className, name, c, Attribute())

    def visitCallExpr(self, ast,c):
        name = ast.method.name
        self.checkAccess(ast, name, c)
        for param_ in ast.param: self.visit(param_,c)

    def visitFieldAccess(self, ast,c):
        # wrong way to
        # A.b , a::$b
        name = ast.fieldname.name
        self.checkAccess(ast, name, c)

        '''Return Symbol of variable'''
        return c[0]["array"][-1]["name"] # => Symbol


    def visitIntLiteral(self, ast,c): 
        return 1

    def visitFloatLiteral(self, ast,c): 
        return 2

    def visitStringLiteral(self, ast,c): 
        return 3

    def visitBooleanLiteral(self, ast,c): 
        return 4

    def visitNullLiteral(self, ast,c): 
        return 5

    def visitSelfLiteral(self, ast,c): 
        return "Self"

    def visitArrayLiteral(self, ast,c): 
        for i in range (ast.value.length()-1):
            if self.visit(ast.value[i]) != self.visit(ast.value[i+1]):
                raise IllegalArrayLiteral(ast) 
        return [self.visit(ast.value[i]) for i in range (ast.value.length())]

    def visitAssign(self, ast,c):
        lhs = self.visit(ast.lhs,c)
        rhs = self.visit(ast.exp,c)

        '''LHS cant be void'''
        if lhs == 6: raise TypeMismatchInStatement(ast)
        both_side_same = False

        '''LHS = float, RHS = int'''
        if lhs == rhs or (lhs == 2 and rhs == 1):
            both_side_same = True

        '''RHS are subtype of LHS'''
        child_name = rhs.mtype.classname.name
        parent_name = lhs.mtype.classname.name
        for class_ in c:
            if class_["name"] == child_name and class_["parent"] == parent_name:
                both_side_same = True
                break

        '''LHS is array type'''
        if isinstance(lhs, Symbol):
            if self.visit(lhs.mtype, c) == 5:
                size = lhs.mtype.size
                eleType = lhs.mtype.eleType

                '''Check size of LHS and RHS'''
                if size != rhs.length: raise TypeMismatchInStatement(ast)

                '''Check type of all element in RHS'''
                for i in range(size):
                    if eleType == 2:
                        '''If LHS is float => RHS is int or float'''
                        if rhs[i] != 1  and rhs[i] != 2: raise TypeMismatchInStatement(ast)
                    elif eleType in [1,3,4]:
                        if eleType != rhs[i]: raise TypeMismatchInStatement(ast)
                    else:
                        '''If LHS is classType (className)'''
                        
                        both_side_same = False
                        for class_ in c:
                            if class_["name"] == rhs[i].mtype.classname.name and class_["parent"] == parent_name:
                                both_side_same = True
                        if not both_side_same: raise TypeMismatchInStatement(ast)

        if both_side_same == False: raise TypeMismatchInStatement(ast)
        
        '''Check constant'''
        if lhs.kind == "Var": raise CannotAssignToConstant(ast)
        
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
        return self.visit(ast.expr, c)
        

    def visitCallStmt(self, ast,c): pass

    def visitInstance(self, ast,c): pass

    def visitStatic(self, ast,c): pass

    def visitIntType(self, ast,c):
        return 1

    def visitFloatType(self, ast,c):
        return 2

    def visitStringType(self, ast,c):
        return 3
    
    def visitBoolType(self, ast,c): 
        return 4
    
    def visitArrayType(self, ast,c):
        return 5
    
    def visitVoidType(self, ast,c):
        return 6
    
    def visitClassType(self, ast,c):
        for class_ in c:
            if class_["name"] == ast.classname.name:
                return class_["name"]
        raise Undeclared(Class(),ast.classname.name)
