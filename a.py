
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from CodeGenError import *

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
                   Symbol("getInt",     MType([],IntType()), CName(self.libName)),
                   Symbol("putInt",     MType([IntType()],VoidType()), CName(self.libName)),
                   Symbol("putIntLn",   MType([IntType()],VoidType()), CName(self.libName)),
                   Symbol("getFloat",   MType([],FloatType()), CName(self.libName)),
                   Symbol("putFloat",   MType([FloatType()],VoidType()), CName(self.libName)),
                   Symbol("putFloatLn", MType([FloatType()],VoidType()), CName(self.libName)),
                   Symbol("putBool",    MType([BoolType()],VoidType()), CName(self.libName)),
                   Symbol("putBoolLn",  MType([BoolType()],VoidType()), CName(self.libName)),
                   Symbol("putString",  MType([StringType()],VoidType()), CName(self.libName)),
                   Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                   Symbol("putLn",      MType([],VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        global_env = self.init()
        gc = CodeGenVisitor(ast, global_env, dir_)
        gc.visit(ast, None)

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None

class ClassType(Type):
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

class CodeGenVisitor(BaseVisitor, Utils):
############## INIT #################
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
############# PROGRAM ###############
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for i in ast.decl:
            if type(i) is VarDecl: self.env += [self.visit(i, None)]
            else: self.env += [Symbol(i.name.name, MType([j.varType for j in i.param],i.returnType), CName(self.className))]
        e = SubBody(None, self.env)
        for x in ast.decl:
            if type(x) is FuncDecl: self.visit(x, e)
        # generate default constructor
        
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(), None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c
############## DECLs ################
    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list() if isInit else [i.varType for i in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)
        try: glenv = o[:]
        except Exception as e: glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), glenv))
        else:
            if isMain:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), glenv))
            else:
                for i in consdecl.param:
                    index = frame.getNewIndex()
                    self.emit.printout(self.emit.emitVAR(index, i.variable.name, i.varType, frame.getStartLabel(),frame.getEndLabel(), glenv))
                    glenv = [Symbol(i.variable.name, i.varType, Index(index))] + glenv
            for i in consdecl.local:
                index = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(index, i.variable.name, i.varType, frame.getStartLabel(),frame.getEndLabel(), glenv))
                glenv = [Symbol(i.variable.name, i.varType, Index(index))] + glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        a = list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType: self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return

    def visitVarDecl(self, ast, o):
        if type(ast.varType) is ArrayType: raise Exception("Array type variable found")
        self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, True, 5))
        return Symbol(ast.variable.name, ast.varType, CName(self.className))
############## STMTs ################
    def visitAssign(self, ast, o):
        rs, rt = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        ls, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True, True))
        if type(rt) is IntType and type(lt) is FloatType:
            self.emit.printout(rs + self.emit.emitI2F(None) + ls)
        else: self.emit.printout(rs + ls)
        pass
    
    def visitAssign(self, ast, o):
        rc, rt = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        self.emit.printout(rc)
        lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True))
        self.emit.printout(lc)

    def visitIf(self, ast, o):
        frame = o.frame
        nenv = o.sym
        self.emit.printout(self.visit(ast.expr, Access(frame, nenv, False, True))[0])
        if ast.elseStmt == []:
            exitLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(exitLabel,frame))
            for i in ast.thenStmt:
                self.visit(i, o)
            if ast.thenStmt == [] or (ast.thenStmt != [] and not(type(ast.thenStmt[-1]) is Return)):
                self.emit.printout(self.emit.emitGOTO(exitLabel, frame))
            self.emit.printout(self.emit.emitLABEL(exitLabel, frame))
        else:
            falseLabel = frame.getNewLabel()
            exitLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(falseLabel,frame))
            for i in ast.thenStmt: self.visit(i, o)
            if ast.thenStmt == [] or (ast.thenStmt != [] and not(type(ast.thenStmt[-1]) is Return)):
                self.emit.printout(self.emit.emitGOTO(exitLabel, frame))
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            for i in ast.elseStmt: self.visit(i, o)
            self.emit.printout(self.emit.emitLABEL(exitLabel, frame))

    def visitWhile(self, ast, o):
        frame = o.frame
        whileCondition = ""

        labelCondition = frame.getNewLabel()
        labelExit = frame.getNewLabel()
        frame.conLabel += [labelCondition]
        frame.brkLabel += [labelExit]
        exp, expT = self.visit(ast.exp, Access(frame, o.sym, False, True))
        whileCondition = self.emit.emitLABEL(labelCondition, frame) + exp + self.emit.emitIFFALSE(labelExit,frame)
        self.emit.printout(whileCondition)

        for i in ast.sl: self.visit(i, o)

        self.emit.printout(self.emit.emitGOTO(labelCondition, frame))
        self.emit.printout(self.emit.emitLABEL(labelExit, frame))
        frame.conLabel = frame.conLabel[:-1]
        frame.brkLabel = frame.brkLabel[:-1]

    def visitFor(self, ast, o):
        frame = o.frame
        forInit = forCondition = forIncrement = ""
        expr1, expr1t = self.visit(ast.expr1, Access(frame, o.sym, False, True))
        id, idt = self.visit(ast.id, Access(frame, o.sym, True, True))
        if not (type(idt) is IntType or type(expr1t) is IntType): raise TypeMismatchInStatement(ast)
        forInit = expr1 + id
        self.emit.printout(forInit)

        labelCondition = frame.getNewLabel()
        labelIncrement = frame.getNewLabel()
        labelExit = frame.getNewLabel()
        frame.conLabel += [labelIncrement]
        frame.brkLabel += [labelExit]
        expr2, expr2t = self.visit(ast.expr2, Access(frame, o.sym, False, True))
        if not(type(expr2t) is IntType): raise TypeMismatchInStatement(ast)
        forCondition = self.emit.emitLABEL(labelCondition, frame)
        forCondition = self.emit.emitLABEL(labelCondition, frame) + self.visit(ast.id, Access(frame, o.sym, False, True))[0] + expr2 + (self.emit.emitIFICMPGT(labelExit,frame) if ast.up else self.emit.emitIFICMPLT(labelExit,frame))
        self.emit.printout(forCondition)

        for i in ast.loop: self.visit(i, o)

        forIncrement = self.emit.emitLABEL(labelIncrement, frame) + self.visit(ast.id, Access(frame, o.sym, False, True))[0] + self.emit.emitPUSHICONST(1,frame)
        forIncrement += self.emit.emitADDOP('+' if ast.up else '-',IntType(),frame)
        forIncrement += self.visit(ast.id, Access(frame, o.sym, True, True))[0]
        forIncrement += self.emit.emitGOTO(labelCondition, frame)
        self.emit.printout(forIncrement)
        self.emit.printout(self.emit.emitLABEL(labelExit, frame))
        frame.conLabel = frame.conLabel[:-1]
        frame.brkLabel = frame.brkLabel[:-1]

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.brkLabel[-1], o.frame))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.conLabel[-1], o.frame))

    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        if not ast.expr:
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
            return
        strExpr, typeExpr = self.visit(ast.expr,Access(frame, nenv, False, True))
        self.emit.printout(strExpr)
        if type(frame.returnType) is FloatType and type(typeExpr) is IntType:
            self.emit.printout(self.emit.emitI2F(frame))
            typeExpr = frame.returnType
        self.emit.printout(self.emit.emitRETURN(typeExpr,frame))

    def visitWith(self, ast, o):
        a=5
        frame = o.frame
        nenv = o.sym[:]
        frame.enterScope(False)
        varDecl = ""
        for i in ast.decl:
            index = frame.getNewIndex()
            varDecl += self.emit.emitVAR(index, i.variable.name, i.varType, frame.getStartLabel(),frame.getEndLabel(), nenv)
            nenv = [Symbol(i.variable.name, i.varType, Index(index))] + nenv
        self.emit.printout(varDecl)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        for i in ast.stmt: self.visit(i,SubBody(frame,nenv))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ""
        for i, x in enumerate(ast.param):
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(0)
            in_ = in_ + str1
        self.emit.printout(in_ + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))
        
############## EXPRs ################
    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        left, typeLeft = self.visit(ast.left, o)
        right, typeRight = self.visit(ast.right, o)
        if not(type(typeLeft) == type(typeRight)):
            if type(typeLeft) is IntType and type(typeRight) is FloatType:
                left += self.emit.emitI2F(frame)
                typeLeft = FloatType()
            elif type(typeLeft) is FloatType and type(typeRight) is IntType:
                right += self.emit.emitI2F(frame)
                typeRight = FloatType()
        if ast.op in ['+','-']: return left + right + self.emit.emitADDOP(ast.op, typeLeft, frame), typeLeft
        elif ast.op == '*': return left + right + self.emit.emitMULOP(ast.op, typeLeft, frame), typeLeft
        elif ast.op == '/':
            if type(typeLeft) is IntType: return left + self.emit.emitI2F(frame) + right + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
            else: return left + right + self.emit.emitMULOP(ast.op, typeLeft, frame), typeLeft
        elif ast.op.lower() == 'div': return left + right + self.emit.emitDIV(frame), IntType()
        elif ast.op.lower() == 'mod': return left + right + self.emit.emitMOD(frame), IntType()
        elif ast.op in ['>','>=','<','<=','<>','=']: return left + right + self.emit.emitREFOP(ast.op, typeLeft, frame), BoolType()
        elif ast.op.lower() == 'and': return left + right + self.emit.emitANDOP(frame), BoolType()
        elif ast.op.lower() == 'or': return left + right + self.emit.emitOROP(frame), BoolType()
        elif ast.op.lower() == 'andthen':
            falseLabel = frame.getNewLabel()
            exitLabel = frame.getNewLabel()
            ret = left + self.emit.emitIFFALSE(falseLabel,frame) + right + self.emit.emitIFFALSE(falseLabel,frame) + self.emit.emitPUSHICONST(1,frame) + self.emit.emitGOTO(exitLabel,frame) + self.emit.emitLABEL(falseLabel,frame) + self.emit.emitPUSHICONST(0,frame) + self.emit.emitLABEL(exitLabel,frame)
            return ret, BoolType()
        elif ast.op.lower() == 'orelse':
            trueLabel = frame.getNewLabel()
            exitLabel = frame.getNewLabel()
            ret = left + self.emit.emitIFTRUE(trueLabel,frame) + right + self.emit.emitIFTRUE(trueLabel,frame) + self.emit.emitPUSHICONST(0,frame) + self.emit.emitGOTO(exitLabel,frame) + self.emit.emitLABEL(trueLabel,frame) + self.emit.emitPUSHICONST(1,frame) + self.emit.emitLABEL(exitLabel,frame)
            return ret, BoolType()
        else: raise Exception("Wrong binop: " + str(ast.op))

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        body, typeBody = self.visit(ast.body, o)
        if ast.op.lower() =='not':
            return body + self.emit.emitNOT(typeBody,frame), typeBody
        elif ast.op == '-':
            return body + self.emit.emitNEGOP(typeBody,frame), typeBody

    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        if not sym: raise Undeclared(Function(),ast.method.name)
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ""
        for i, x in enumerate(ast.param):
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(0)
            in_ = in_ + str1
        return in_ + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), sym.mtype.rettype

    def visitId(self, ast, o):
        sym = self.lookup(ast.name.lower(), o.sym, lambda x:x.name.lower())
        if not sym: raise Undeclared(Variable(), ast.name)
        if o.isLeft:
            if type(sym.value) is CName: return self.emit.emitPUTSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o.frame), sym.mtype
            else: return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            if type(sym.value) is CName: return self.emit.emitGETSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o.frame), sym.mtype
            else: return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype

    def visitArrayCell(self, ast, o):
        raise Exception("Arraycell found")

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame), BoolType()

    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        a = self.emit.emitPUSHCONST(str(ast.value), StringType(), frame), StringType()