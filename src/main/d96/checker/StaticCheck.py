
"""
 * @author nhphung
"""
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
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):
    check_in_loop = False
    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
    
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    
    def visitProgram(self,ast, c): 
        # c = [{"array":[{}], "name": None, "parent":None}]
        c = []
        for decl in ast.decl:
            self.visit(decl,c)

    '''--------------Decl--------------'''
    def visitVarDecl(self, ast,c): 
        '''Check Redeclare Variable '''
        if ast.variable.name in c[0]["array"][0]:
            raise Redeclared(Variable(),ast.variable.name)
        typ = self.visit(ast.varType,c)
        if ast.varInit:
            self.visit(ast.varInit,c)

        c[0]["array"][0][ast.variable.name] = Symbol(ast.variable.name,typ, ast.varInit)
        '''Check Undeclare Variable '''
        
    def visitConstDecl(self, ast,c): 
        if ast.constant.name in c[0]["array"][0]:
            raise Redeclared(Constant(),ast.constant.name)
        else: self.visitClassType(ast.constType,c)
        c[0]["array"][0][ast.constant.name] = Symbol(ast.constant.name,ast.constType, ast.value)
        if ast.value:
            self.visit(ast.value,c)

    def visitAttributeDecl(self,ast,c):
        if isinstance(ast.decl, VarDecl):
            name = ast.decl.variable.name
            typ = ast.decl.varType
            value = ast.decl.varInit
        else: 
            name = ast.decl.constant.name
            typ = ast.decl.constType
            value = ast.decl.value
        if name in c[0]["array"][0]:
            raise Redeclared(Attribute(),name)
        else:
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
        c.insert(0,{"array":[{}], "name": ast.classname.name, "parent":ast.parentname.name if ast.parentname != None else None }) 
        for mem in ast.memlist:
            self.visit(mem,c)
        #Check no entry point
        
    
    def shallowCopy(self,c,env):
        for i in c:
            temp = []
            for j in i["array"]:
                temp.append(j.copy())
            env.append({"array":temp, "name": i["name"], "parent": i["parent"]})

    def visitMethodDecl(self, ast,c):
        if ast.name.name in c[0]["array"][0]:
            raise Redeclared(Method(),ast.name.name)
        c[0]["array"][0][ast.name.name] = Symbol(ast.name.name,MType([p.varType for p in ast.param], None))
        env = []
        self.shallowCopy(c,env)
        env[0]["array"].insert(0, {})
        for param_ in ast.param:
            self.visitParam(param_,env)
        self.visitBody(ast.body,env)

    def visitParam(self, ast,env):
        if ast.variable.name in env[0]["array"][0]:
            raise Redeclared(Parameter(),ast.variable.name)
        else:
            env[0]["array"][0][ast.variable.name] = Symbol(ast.variable.name,ast.varType, ast.varInit)
    
    def visitBody(self, ast, c):
        for inst_ in ast.inst:
            self.visit(inst_,c)

    def visitBlock(self, ast,c):
        env = []
        self.shallowCopy(c,env)
        env[0]["array"].insert(0, {})

        for inst_ in ast.inst:
            self.visit(inst_,env)

    def visitId(self, ast,c):
        class_env = []
        self.shallowCopy(c, class_env)
        for env_ in c[0]["array"]:
            if ast.name in env_:
                return env_[ast.name] # ====> Symbol    
        if c[0]["parent"]:
            for env_ in c:
                if env_["name"] == ast.name: return ast.name
                if env_["name"] == c[0]["parent"]:
                    if ast.name in env_["array"][-1]:
                        return env_["array"][-1][ast.name]
        raise Undeclared(Identifier(),ast.name)

    def visitBinaryOp(self, ast,c): 
        lhs = self.visit(ast.left)
        rhs = self.visit(ast.right)
        if isinstance(lhs, Symbol):
            lhs = lhs.mtype
        if isinstance(rhs, Symbol):
            rhs = rhs.mtype
        if ast.op in ['-', '+', '*', '/']:
            if lhs == "IntType" and rhs == "IntType": return "Intype"
            else: return "FloatType"
        if ast.op == '%':
            return "IntType"
        if ast.op in ["==", "!=", "<", ">", "<=", ">=", "!", "&&", "||", "==."]: 
            return "BoolType"
        if ast.op == "+.": return "StringType"

    def visitUnaryOp(self, ast,c):
        sym = self.visit(ast.body)
        if ast.op in ["!"]: return "BoolType"
        if ast.op == "-": return sym.mtype

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

    def visitArrayCell(self, ast,c): pass

    def IsStatic(self, name):
        if name[0] == "$": return True
        return False

    def checkAccess(self, ast, name, c): 
        if StaticChecker.IsStatic(name):
            className = self.visit(ast.obj,c)
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
        StaticChecker.checkAccess(ast, name, c)
        for param_ in ast.param: self.visit(param_,c)

    def visitFieldAccess(self, ast,c):
        # wrong way to
        # A.b , a::$b
        name = ast.fieldname.name
        StaticChecker.checkAccess(ast, name, c)

    def visitIntLiteral(self, ast,c): 
        return "IntType"

    def visitFloatLiteral(self, ast,c): 
        return "FloatType"

    def visitStringLiteral(self, ast,c): 
        return "StringType"

    def visitBooleanLiteral(self, ast,c): 
        return "BoolType"

    def visitNullLiteral(self, ast,c): 
        return "Null"

    def visitSelfLiteral(self, ast,c): 
        return "Self"

    def visitArrayLiteral(self, ast,c): 
        for i in range (ast.value.length()-1):
            if self.visit(ast.value[i]) != self.visit(ast.value[i+1]):
                raise IllegalArrayLiteral(ast) 
        return "Array"

    def visitAssign(self, ast,c):
        sym = self.visit(ast.lhs,c)
        if StaticChecker.IsStatic(sym.name): raise CannotAssignToConstant(ast)
        self.visit(ast.exp,c)

    def visitIf(self, ast,c):
        pass

    def visitFor(self, ast,c):
        sym = self.visit(ast.id)
        if StaticChecker.IsStatic(sym.name): raise CannotAssignToConstant(Assign(ast.id,ast.exp))
        StaticChecker.check_in_loop = True
        self.visit(ast.loop, c)

    def visitBreak(self, ast,c):
        if not StaticChecker.check_in_loop:
            raise MustInLoop(ast)

    def visitContinue(self, ast,c):
        if not StaticChecker.check_in_loop:
            raise MustInLoop(ast)

    def visitReturn(self, ast,c): pass

    def visitCallStmt(self, ast,c): pass

    def visitInstance(self, ast,c): pass

    def visitStatic(self, ast,c): pass

    def visitIntType(self, ast,c):
        return "IntType"

    def visitFloatType(self, ast,c):
        return "FloatType"

    def visitStringType(self, ast,c):
        return "StringType"
    
    def visitBoolType(self, ast,c): 
        return "BoolType"
    
    def visitArrayType(self, ast,c):
        return "ArrayType"
    
    def visitVoidType(self, ast,c):
        return "VoidType"
    
    def visitClassType(self, ast,c):
        for class_ in c:
            if class_["name"] == ast.classname.name:
                return class_["name"]
        raise Undeclared(Class(),ast.classname.name)
