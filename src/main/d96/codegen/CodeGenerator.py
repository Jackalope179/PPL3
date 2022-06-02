from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

from main.d96.utils.AST import BoolType, FloatType, IntType, MethodDecl, Return, VoidType

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
                Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("getBool", MType(list(), BoolType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType([], VoidType()), CName(self.libName)),
            ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(self, ast, o):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(self, ast, o):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None

class ClassType(self, ast, o):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class FuncDecl():
    def __init__(self, kind, name, param, body, retType):
        self.kind = kind
        self.name = name
        self.param = param
        self.body = body
        self.returnType = retType

class BodyBlock():
    def __init__(self, type, stmt) -> None:
        self.type = type
        self.stmt = stmt

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)     
        for x in ast.decl:
            e = self.visit(x, e)      
        # generate default constructor
        self.genMETHOD(FuncDecl(False, Id("<init>"), [], Block(list()), VoidType()), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        partype = []
        for param_ in consdecl.param:
            partype += [param_.varType]

        isInit = consdecl.name.name == "Constructor"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = partype if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            for param_ in consdecl.param:
                self.visit(param_ , SubBody(frame, o.sym[::-1]))


        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.inst))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitClassDecl(self, ast, o):
        for memlist in ast.memlist:
            self.visit(memlist,o)
        return o

    def visitMethodDecl(self,ctx,o):
        subctxt = o
        
        # Return type
        returnType = None
        for stmt in ctx.body.inst:
            if type(stmt) is Return:
                returnType = self.visit(stmt,o)
                break
        
        # Static or instance
        if ctx.name.name == "main" or ctx.name.name[0] == "$":
            isStatic = True
        else:
            isStatic = False
            
        frame = Frame(ctx.name, returnType)
        constdecl = FuncDecl(isStatic, ctx.name, ctx.param, ctx.body, returnType)
        self.genMETHOD(constdecl,subctxt,frame)

        return SubBody(None, [Symbol(ctx.name, MType(list(), returnType), CName(self.className))] + subctxt.sym)

    def visitReturn(self,ctx,o):
        if ctx.expr:
            ec, et = self.visit(ctx.expr, o)
            self.emit.printout(self.emit.emitRETURN(et, o.frame))
        else: 
            et = VoidType()
        return et

    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame), sym.mtype.rettype
        # self.emit.printout(in_[0])
        # self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitId(self, ctx, o):
        sym = next(filter(lambda x : x.name == ctx.name, o.sym), False) 
        if o.isLeft:
            if type(sym.value) is Index:
                code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o .frame)
            else:        
                code = self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, sym.mtype, o .frame)
        else:
            if type(sym.value) is Index:
                code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o .frame)
        typ = sym.mtype
        return code, typ

    def visitBinaryOp(self, ctx, o):
        lc, lt = self.visit(ctx.left, o)
        rc, rt = self.visit(ctx.right, o)

        
        if type(lt) != type(rt):
            if type(lt) is IntType and type(rt) is FloatType:
                lc += self.emit.emitI2F(o.frame) 
            elif type(lt) is FloatType and type(rt) is IntType:
                rc += self.emit.emitI2F(o.frame)
            rettype = FloatType()
        elif type(lt) is IntType:
            rettype = IntType()
        elif type(lt) is FloatType: 
            rettype = FloatType()
        elif type(lt) is BoolType:
            rettype = BoolType()
        else:
            rettype = StringType()

        if ctx.op in ['+','-']:
            code = lc + rc + self.emit.emitADDOP(ctx.op, rettype, o.frame)
        elif ctx.op in ["/", "*"]: code = lc + rc + self.emit.emitMULOP(ctx.op, rettype, o.frame)
        elif ctx.op in ['>','>=','<','<=']: 
            code =  lc + rc + self.emit.emitREOP(ctx.op, rettype, o.frame)
        elif ctx.op in ['==','!=']:
            code = lc + rc + self.emit.emitREOP(ctx.op, IntType() if type(lt) is IntType else BoolType(), o.frame)
        elif ctx.op == "%":
            code = lc + rc + self.emit.emitMOD(o.frame)
        elif ctx.op == "+.":
            code = lc + rc + self.emit.emitADDOP(ctx.op[0], StringType(), o.frame)
        elif ctx.op == "==.":
            code = lc + rc + self.emit.emitREOP(ctx.op[0], BoolType(), o.frame)
        return code, rettype

    def visitUnaryOp(self, ctx, o):
        ec, et = self.visit(ctx.body, o)
        if ctx.op == "!":
            return ec + self.emit.emitNOT(et, o.frame), et
        else:
            return ec + self.emit.emitNEGOP(et, o.frame), et

    def visitNewExpr(self, ctx, o):
        code = self.emit.emitNEW(ctx.classname.name) + self.emit.emitDUP(o.frame) + self.emit.emitINVOKESPECIAL(ctx.classname.name + "/<init>")
        return code, ctx.classname.type
        
    def visitArrayCell(LHS):
        pass

    def visitFieldAccess(self, ctx, o):
        ec, et = self.visit(ctx.body, o)
        cname = o.sym.value.value
        ctype = o.sym.mtype
        return self.emit.emitINVOKESTATIC(cname + "/" + ctx.fieldname.name, ctype, o.frame), et

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), IntType()
        
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), BoolType()
        
    def visitNullLiteral(Literal):
        pass

    def visitSelfLiteral(Literal):
        pass

    def visitArrayLiteral(Literal):
        pass

    def visitAssign(self, ast, o):
        rs, rt = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        ls, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True, True))
        if type(lt) is FloatType and type(rt) is IntType :
            self.emit.printout(rs + self.emit.emitI2F(None) + ls)
        else: self.emit.printout(rs + ls)

    def visitIf(self,ctx,o):
        ec, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
        self.emit.printout(ec)
        falseLabel = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, o.frame))
        self.visit(ctx.tstmt, o)
        if ctx.estmt:
            exitLabel = o.frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(exitLabel, o.frame))
            self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))
            self.visit(ctx.estmt, o)
            self.emit.printout(self.emit.emitLABEL(exitLabel, o.frame))
        else:
            self.emit.printout(self.emit.emitLABEL(falseLabel, o.frame))

    def visitFor(self, ctx, o):
        idx = o.frame.getNewIndex()
        o.frame.enterLoop()
        continueLabel = o.frame.getContinueLabel()
        breakLabel = o.frame.getBreakLabel()
        exp1, et1 = self.visit(ctx.expr1, Access(o.frame, o.sym, False))
        self.emit.printout(exp1)
        self.emit.printout(self.emit.emitWRITEVAR(ctx.expr1.name, IntType(), idx, o.frame))
        self.emit.emitLABEL(continueLabel, o.frame)
        exp2, et2 = self.visit(ctx.expr2, Access(o.frame, o.sym, False))
        self.emit.printout(exp2)
        self.emit.printout(self.emit.emitIFICMPGT(breakLabel, o.frame))
        self.visit(ctx.loop, o)
        self.emit.printout(self.emit.emitREADVAR(ctx.expr1.name, IntType(), idx, o.frame))
        if ctx.expr3:
            exp3, et3 = self.visit(ctx.expr3, Access(o.frame, o.sym, False))
            self.emit.printout(exp3)
        else:
            self.emit.printout(self.emit.emitPUSHICONST(1, o.frame))
        self.emit.printout(self.emit.emitADDOP("+", IntType(), o.frame))
        self.emit.printout(self.emit.emitWRITEVAR(ctx.epxr1.name, IntType(), idx, o.frame))
        self.emit.printout(self.emit.emitGOTO(continueLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, o.frame))
        o.frame.exitLoop()

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.breakLabel[-1], o.frame))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.continueLabel[-1], o.frame))

    def visitReturn(self, ast, o):
        if not ast.expr:
            self.emit.printout(self.emit.emitRETURN(VoidType(),o.frame))
            return
        ec, et = self.visit(ast.expr,Access(o.frame, o.sym, False, True))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitRETURN(et,o.frame))

    def visitCallStmt(self, ctx, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ctx.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ctx.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ctx.method.name, ctype, frame))

    def visitVarDecl(self, ast, o):
        if o.frame:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            return Symbol(ast.variable.name, ast.varType, Index(idx))
        else:
            code = self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, None))
            return Symbol(ast.variable.name ,ast.varType, CName(self.className))

    def visitBlock(self, ast, o):
        for inst in ast.inst:
            self.visit(inst, o)

    def visitConstDecl(self, ast, o):
        if o.frame:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            return Symbol(ast.variable.name, ast.varType, Index(idx))
        else:
            code = self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, None))
            return Symbol(ast.variable.name ,ast.varType, CName(self.className))

    def visitAttributeDecl(self, ast, o):
        if o.frame:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            return Symbol(ast.variable.name, ast.varType, Index(idx))
        else:
            code = self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, None))
            return Symbol(ast.variable.name ,ast.varType, CName(self.className))

