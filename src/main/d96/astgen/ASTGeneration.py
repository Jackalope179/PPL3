from functools import reduce
from urllib.parse import parse_qsl
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

class ASTGeneration(D96Visitor):

    # program: decls EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    # decls: class_declaration decls | class_declaration;
    def visitDecls(self, ctx: D96Parser.DeclsContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.class_declaration())
        return self.visit(ctx.class_declaration()) + self.visit(ctx.decls())

    # class_declaration: CLASS ID (':' ID | ) LP (class_members | )  RP ;
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.class_members()) if ctx.class_members() else []
        parentname = Id(ctx.ID(1).getText()) if ctx.ID(1) else None
        if classname.name == "Program" :
            for i in range(memlist.__len__()):
                if isinstance(memlist[i], MethodDecl):
                    if memlist[i].name.name == "main" and memlist[i].param == []:
                        memlist[i] = MethodDecl(Static(), memlist[i].name, memlist[i].param, memlist[i].body)

        return [ClassDecl(classname, memlist, parentname)]
    
    # class_members: cl_member class_members | cl_member;
    def visitClass_members(self, ctx: D96Parser.Class_membersContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.cl_member())
        return self.visit(ctx.cl_member()) + self.visit(ctx.class_members())
    
    # cl_member: attr_decl | method_decl ;
    def visitCl_member(self, ctx: D96Parser.Cl_memberContext):
        if ctx.attr_decl(): return self.visit(ctx.attr_decl())
        return self.visit(ctx.method_decl())

    # attr_decl: (VAL | VAR) (((ID | SID) decl_part expr) | (idlist ':' type_name)) SEMI;
    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        if ctx.idlist():
            ids = self.visit(ctx.idlist()) #[SID, ID]
            varType = self.visit(ctx.type_name())
            if ctx.VAR(): 
                vardecls = [(VarDecl(variable, varType, NullLiteral() if isinstance(varType, ClassType) else None), Static() if variable.name.startswith("$") else Instance() ) for variable in ids]
            else:
                vardecls = [(ConstDecl(variable, varType, NullLiteral() if isinstance(varType, ClassType) else None), Static() if variable.name.startswith("$") else Instance() ) for variable in ids]
            return [AttributeDecl(decl[1], decl[0]) for decl in vardecls]
        else:
            decl_list = self.visit(ctx.decl_part())
            typ = decl_list.pop()
            ids = [Id(ctx.SID().getText()) if ctx.SID() else Id(ctx.ID().getText())] + [i[0] for i in decl_list]
            exprs = [i[1] for i in decl_list][::-1] + [self.visit(ctx.expr())]

            decls = []
            for i in range(ids.__len__()):
                decls += [(ids[i], exprs[i])]

            if ctx.VAR():
                varType = typ
                vardecls = [(VarDecl(decl[0], varType, decl[1]), Static() if decl[0].name.startswith("$") else Instance())  for decl in decls]
            else: 
                constType = typ
                vardecls = [(ConstDecl(decl[0], constType, decl[1]), Static() if decl[0].name.startswith("$") else Instance()) for decl in decls]
            return [AttributeDecl(decl[1], decl[0]) for decl in vardecls]
            
    # decl_part: COMMA (ID|SID) decl_part expr COMMA | ':' type_name '=' ; 
    def visitDecl_part(self, ctx: D96Parser.Decl_partContext):
        if ctx.type_name(): return [self.visit(ctx.type_name())]
        id = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.SID().getText())
        exp = self.visit(ctx.expr())
        return [(id,exp)] + self.visit(ctx.decl_part())


    # method_decl: (SID | ID) LB (paramslist | ) RB blk_stmt | constructor | destructor;
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        if ctx.constructor(): return self.visit(ctx.constructor())
        elif ctx.destructor(): return self.visit(ctx.destructor())
        else:
            kind = Static() if ctx.SID() else Instance()
            name = Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.SID().getText())
            param = self.visit(ctx.paramslist()) if ctx.paramslist() else []
            body = self.visit(ctx.blk_stmt())
            return [MethodDecl(kind, name, param, body)]
    
    # exprlist: expr COMMA exprlist | expr;
    def visitExprlist(self, ctx: D96Parser.ExprlistContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())

    # idlist: (ID | SID) COMMA idlist | ID | SID;
    def visitIdlist(self, ctx: D96Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())] if ctx.ID() else [Id(ctx.SID().getText())]
        return [Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.SID().getText())] + self.visit(ctx.idlist())

    # constructor: CONSTRUCTOR LB (paramslist | ) RB blk_stmt;
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        name = Id("Constructor")
        param = self.visit(ctx.paramslist()) if ctx.paramslist() else []
        body = self.visit(ctx.blk_stmt())
        return [MethodDecl(kind, name, param, body)]

    # destructor:  DESTRUCTOR LB RB blk_stmt;	
    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        name = Id("Destructor")
        param = []
        body = self.visit(ctx.blk_stmt())
        return [MethodDecl(kind, name, param, body)]

    # paramslist: params SEMI paramslist | params;
    def visitParamslist(self, ctx: D96Parser.ParamslistContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.params())
        return self.visit(ctx.params()) + self.visit(ctx.paramslist())

    # params: non_st_idlist ':' type_name;
    def visitParams(self, ctx: D96Parser.ParamsContext):
        ids = self.visit(ctx.non_st_idlist())
        varType = self.visit(ctx.type_name())
        return [VarDecl(variable, varType) for variable in ids] # List[param(variable, type)]
    
    # non_st_idlist:  ID COMMA non_st_idlist | ID ;
    def visitNon_st_idlist(self, ctx: D96Parser.Non_st_idlistContext):
        if ctx.getChildCount() == 1: return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.non_st_idlist())
            
    # expr:  expr1  (STR_CONCAT | STR_COMPARE) expr1 | expr1;
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr1(0))
        if ctx.STR_CONCAT(): op = ctx.STR_CONCAT().getText()
        elif ctx.STR_COMPARE(): op = ctx.STR_COMPARE().getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)

    # expr1: expr2 (EQ |  NEQ | LT | GT | LTE | GTE) expr2 | expr2;
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr2(0))
        if ctx.EQ(): op = ctx.EQ().getText()
        elif ctx.NEQ(): op = ctx.NEQ().getText()
        elif ctx.LT(): op = ctx.LT().getText()
        elif ctx.GT(): op = ctx.GT().getText()
        elif ctx.LTE(): op = ctx.LTE().getText()
        elif ctx.GTE(): op = ctx.GTE().getText()
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinaryOp(op, left, right)


    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr3())
        if ctx.AND(): op = ctx.AND().getText()
        elif ctx.OR(): op = ctx.OR().getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)


    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr4())
        if ctx.ADD(): op = ctx.ADD().getText()
        elif ctx.SUB(): op = ctx.SUB().getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)

    # expr4: expr4 (MUL | DIV | RM) expr5 | expr5;
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr5())
        if ctx.MUL(): op = ctx.MUL().getText()
        elif ctx.DIV(): op = ctx.DIV().getText()
        elif ctx.RM(): op = ctx.RM().getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)
    
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        body = self.visit(ctx.expr5())
        return UnaryOp(op, body)
    
    # expr6: SUB expr6 | expr7;
    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr7())
        op = ctx.SUB().getText()
        body = self.visit(ctx.expr6())
        return UnaryOp(op, body)


    def getEXpr(context, array):
        if context.index_op() is None:
            return context.expr8(), array
        array.append(context.index_op())
        return ASTGeneration.getEXpr(context.expr7(), array)


    # expr7: expr7  index_op | expr8;
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.expr8())
        res, array = ASTGeneration.getEXpr(ctx, [])
        result = self.visit(res)
        arr = reduce(lambda pre, curr: pre + self.visit(curr), array, [])[::-1]
        return ArrayCell(result, arr)
    
    # index_op: LS expr RS | LS expr RS index_op ;
    def visitIndex_op(self, ctx: D96Parser.Index_opContext):
        if ctx.getChildCount() == 3: return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.index_op())

    # expr8: expr8 DOT ID | expr8 DOT ID LB (exprlist | ) RB | expr9;
    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 3:
            obj = self.visit(ctx.expr8())
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        elif ctx.getChildCount() == 1: return self.visit(ctx.expr9())
        else:
            obj = self.visit(ctx.expr8())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
            return CallExpr(obj, method, param)

    # expr9: ID ACCESS SID | ID ACCESS SID LB (exprlist| ) RB | expr10;
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 3:
            obj = Id(ctx.ID().getText())
            fieldname = Id(ctx.SID().getText())
            return FieldAccess(obj, fieldname)
        elif ctx.getChildCount() == 1: return self.visit(ctx.expr10())
        else:
            obj = Id(ctx.ID().getText())
            method = Id(ctx.SID().getText())
            param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
            return CallExpr(obj, method, param)

    # expr10: NEW ID LB (exprlist | ) RB | operands;
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.operands(): return self.visit(ctx.operands())
        classname = Id(ctx.ID().getText())
        param = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        return NewExpr(classname, param)
        

    # operands: LB expr RB | literals | ID | SELF | NULL;
    def visitOperands(self, ctx: D96Parser.OperandsContext):
        if ctx.literals(): return self.visit(ctx.literals())
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.SELF(): return SelfLiteral()
        if ctx.NULL(): return NullLiteral()
        return self.visit(ctx.expr())

    # stmt: assg_stm | if_stm | for_stm | break_stm | continue_stm | return_stm | invocatoin_stm | decl_stm | blk_stmt;
    def visitStmt(self, ctx: D96Parser.StmtContext):
        if ctx.assg_stm(): return self.visit(ctx.assg_stm())
        elif ctx.if_stm(): return self.visit(ctx.if_stm())
        elif ctx.for_stm(): return self.visit(ctx.for_stm())
        elif ctx.break_stm(): return self.visit(ctx.break_stm())
        elif ctx.continue_stm(): return self.visit(ctx.continue_stm())
        elif ctx.return_stm(): return self.visit(ctx.return_stm())
        elif ctx.invocatoin_stm(): return self.visit(ctx.invocatoin_stm())
        elif ctx.decl_stm(): return self.visit(ctx.decl_stm())
        else : return [self.visit(ctx.blk_stmt())]

    # decl_stm: (VAL | VAR) ((ID decl_stm_part expr) | (non_st_idlist ':' type_name)) SEMI;
    def visitDecl_stm(self, ctx: D96Parser.Decl_stmContext):  # [VarDecl] || [ConstDecl]
        if ctx.non_st_idlist():
            ids = self.visit(ctx.non_st_idlist())
            typ = self.visit(ctx.type_name())
            if ctx.VAR():
                varType = typ
                return [VarDecl(variable, varType, NullLiteral() if isinstance(typ, ClassType) else None) for variable in ids]
            else: 
                constType = typ
                return [ConstDecl(constant, constType, NullLiteral() if isinstance(typ, ClassType) else None) for constant in ids]
        else:
            decl_list = self.visit(ctx.decl_stm_part())
            typ = decl_list.pop()
            ids =  [Id(ctx.ID().getText())] + [i[0] for i in decl_list]
            exprs = [i[1] for i in decl_list][::-1] + [self.visit(ctx.expr())]

            decls = []
            for i in range(ids.__len__()):
                decls += [(ids[i], exprs[i])]

            if ctx.VAR():
                varType = typ
                return [VarDecl(decl[0], varType, decl[1])  for decl in decls]
            else: 
                constType = typ
                return [ConstDecl(decl[0], constType, decl[1]) for decl in decls]
                
    # decl_stm_part: COMMA ID decl_stm_part expr COMMA | ':' type_name '='; 
    def visitDecl_stm_part(self, ctx: D96Parser.Decl_stm_partContext):
        if ctx.getChildCount() == 3: return [self.visit(ctx.type_name())] 
        return [(Id(ctx.ID().getText()), self.visit(ctx.expr()))] + self.visit(ctx.decl_stm_part()) # [(ID, expr),..., type]

    def Recursive(ctx):
        if ctx.getChildCount() == 2 and ctx.index_op():
            return ctx, False
        if ctx.getChildCount() == 3 and ctx.LB() and ctx.expr() and ctx.RB():
            return ctx.expr(), True
        if ctx.getChildCount() == 1: 
            return ASTGeneration.Recursive(ctx.getChild(0))



    # assg_stm: (ID | expr DOT ID | ID ACCESS SID | expr index_op) '=' expr SEMI;
    def visitAssg_stm(self, ctx: D96Parser.Assg_stmContext):
        # lhs: Expr
        # exp: Expr
        exp = self.visit(ctx.expr(0))
        if ctx.DOT():
            obj = self.visit(ctx.expr(0))
            fieldname = Id(ctx.ID().getText())
            lhs = FieldAccess(obj, fieldname)
            exp = self.visit(ctx.expr(1))
        elif ctx.SID():
            obj = Id(ctx.ID().getText())
            fieldname = Id(ctx.SID().getText())
            lhs = FieldAccess(obj, fieldname)
        elif ctx.ID(): 
            lhs = Id(ctx.ID().getText())
        else: 
            if not isinstance(self.visit(ctx.expr(0)), ArrayCell):
                arr = self.visit(ctx.expr(0))
                idx = self.visit(ctx.index_op()) 
            else:
                ele, check = ASTGeneration.Recursive(ctx.expr(0))
                if check == False:
                    if isinstance(self.visit(ele), ArrayCell):
                        arr = self.visit(ele).arr
                        idx = self.visit(ele).idx + self.visit(ctx.index_op())
                else:
                    arr = self.visit(ele)
                    idx = self.visit(ctx.index_op()) 

            lhs = ArrayCell(arr, idx)
            exp = self.visit(ctx.expr(1))

        return [Assign(lhs, exp)]


    # if_stm: IF LB expr RB blk_stmt else_if_stm;
    def visitIf_stm(self, ctx: D96Parser.If_stmContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.blk_stmt())
        elseStmt = self.visit(ctx.else_if_stm())  # => if statement || None || statement
        return [If(expr, thenStmt, elseStmt)]  

    # else_if_stm: ELSEIF LB expr RB blk_stmt else_if_stm | ELSE blk_stmt | ;
    def visitElse_if_stm(self, ctx: D96Parser.Else_if_stmContext):
        if ctx.getChildCount() == 0: return None
        elif ctx.getChildCount() == 2:
            return self.visit(ctx.blk_stmt()) # => Block(statement)
        else: 
            expr = self.visit(ctx.expr())
            thenStmt = self.visit(ctx.blk_stmt())
            elseStmt = self.visit(ctx.else_if_stm()) # => if statement || None || statement
            return If(expr, thenStmt, elseStmt)  

    # fix for statement
    # for_stm: FOREACH LB ID IN expr DOTDOT expr (BY expr | ) RB blk_stmt;
    def visitFor_stm(self, ctx: D96Parser.For_stmContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr(0))
        expr2 = self.visit(ctx.expr(1))
        expr3 = self.visit(ctx.expr(2)) if len(ctx.expr()) == 3 else IntLiteral(1)
        loop = self.visit(ctx.blk_stmt())
        return [For(id, expr1, expr2, loop, expr3)]

    # break_stm: BREAK SEMI;
    def visitBreak_stm(self, ctx: D96Parser.Break_stmContext):
        return [Break()]

    # continue_stm: CONTINUE SEMI;
    def visitContinue_stm(self, ctx: D96Parser.Continue_stmContext):
        return [Continue()]

    # return_stm: RETURN (expr | ) SEMI;
    def visitReturn_stm(self, ctx: D96Parser.Return_stmContext):
        if ctx.expr(): return [Return(self.visit(ctx.expr()))]
        return [Return()]

    # invocatoin_stm: expr DOT ID LB (exprlist | ) RB SEMI | ID ACCESS SID LB (exprlist | ) RB SEMI;
    def visitInvocatoin_stm(self, ctx: D96Parser.Invocatoin_stmContext):
        obj = Id(ctx.ID().getText()) if ctx.SID() else self.visit(ctx.expr())
        param  = self.visit(ctx.exprlist()) if ctx.exprlist() else []
        method = Id(ctx.SID().getText()) if ctx.SID() else Id(ctx.ID().getText())
        return [CallStmt(obj, method, param)]
        
    # blk_stmt: LP (stmtlist| ) RP;
    def visitBlk_stmt(self, ctx: D96Parser.Blk_stmtContext):
        return Block(self.visit(ctx.stmtlist())) if ctx.stmtlist() else Block([])

    # stmtlist: stmt stmtlist| stmt; 
    def visitStmtlist(self, ctx: D96Parser.StmtlistContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.stmt())
        return self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())

    # type_name: primitive_typ | array_typ | class_typ;
    def visitType_name(self, ctx: D96Parser.Type_nameContext):
        if ctx.primitive_typ(): return self.visit(ctx.primitive_typ())
        elif ctx.array_typ(): return self.visit(ctx.array_typ())
        return self.visit(ctx.class_typ())

    # array_typ: ARRAY LS typ ',' INT_GT RS;
    def visitArray_typ(self, ctx: D96Parser.Array_typContext):
        size = ctx.INT_GT().getText()
        if size.startswith("0x") or size.startswith("0X"): size = int(size, 16)
        elif size.startswith("0b") or size.startswith("0B"): size = int(size, 2)
        elif size.startswith("0") and len(size) > 1: size = int(size, 8)
        else: size = int(size)
        eleType = self.visit(ctx.typ())
        return ArrayType(size, eleType)
    
    # primitive_typ: INTTYPE | FLOATTYPE | STRINGTYPE | BOOLTYPE ;
    def visitPrimitive_typ(self, ctx: D96Parser.Primitive_typContext):
        if ctx.INTTYPE(): return IntType()
        elif ctx.FLOATTYPE(): return FloatType()
        elif ctx.STRINGTYPE(): return StringType()
        return BoolType()

    # typ: primitive_typ | array_typ;
    def visitTyp(self, ctx: D96Parser.TypContext):
        if ctx.primitive_typ(): return self.visit(ctx.primitive_typ())
        return self.visit(ctx.array_typ())

    # class_typ: ID;
    def visitClass_typ(self, ctx: D96Parser.Class_typContext):
        return ClassType(Id(ctx.ID().getText()))


    # literals: FLOAT | INT_GT | INT_ZERO | STR | BOOL | array_literal;
    def visitLiterals(self, ctx: D96Parser.LiteralsContext):
        if ctx.FLOAT(): return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.INT_GT() or ctx.INT_ZERO():
            number = ctx.INT_GT().getText() if ctx.INT_GT() else ctx.INT_ZERO().getText()
            if number.startswith("0x") or number.startswith("0X"): return IntLiteral(int(number, 16))
            elif number.startswith("0b") or number.startswith("0B"): return IntLiteral(int(number, 2))
            elif number.startswith("0") and len(number) > 1: return IntLiteral(int(number, 8))
            return IntLiteral(int(number))
        elif ctx.STR(): return StringLiteral(ctx.STR().getText())
        elif ctx.BOOL(): return BooleanLiteral(ctx.BOOL().getText() == 'True')
        return self.visit(ctx.array_literal())


    # array_literal: idxlit | mullit;
    def visitArray_literal(self, ctx: D96Parser.Array_literalContext):
        if ctx.idxlit(): return self.visit(ctx.idxlit())
        return self.visit(ctx.mullit())


    # arrlist: arr COMMA arrlist | arr;
    def visitArrlist(self, ctx: D96Parser.ArrlistContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.arr())
        return self.visit(ctx.arr()) + self.visit(ctx.arrlist())

    # arr: idxlit | mullit;
    def visitArr(self, ctx: D96Parser.ArrContext):
        if ctx.idxlit(): return [self.visit(ctx.idxlit())]  
        return [self.visit(ctx.mullit())] 
    
    # idxlit: ARRAY LB (exprlist| ) RB;
    def visitIdxlit(self, ctx: D96Parser.IdxlitContext):
        return ArrayLiteral(self.visit(ctx.exprlist())) if ctx.exprlist() else ArrayLiteral([]) 

    # mullit: ARRAY LB arrlist RB;
    def visitMullit(self, ctx: D96Parser.MullitContext):
        return ArrayLiteral(self.visit(ctx.arrlist()))