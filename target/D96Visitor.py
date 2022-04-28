# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decls.
    def visitDecls(self, ctx:D96Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_members.
    def visitClass_members(self, ctx:D96Parser.Class_membersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cl_member.
    def visitCl_member(self, ctx:D96Parser.Cl_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_decl.
    def visitAttr_decl(self, ctx:D96Parser.Attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decl_part.
    def visitDecl_part(self, ctx:D96Parser.Decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprlist.
    def visitExprlist(self, ctx:D96Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramslist.
    def visitParamslist(self, ctx:D96Parser.ParamslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#non_st_idlist.
    def visitNon_st_idlist(self, ctx:D96Parser.Non_st_idlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_op.
    def visitIndex_op(self, ctx:D96Parser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decl_stm.
    def visitDecl_stm(self, ctx:D96Parser.Decl_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#decl_stm_part.
    def visitDecl_stm_part(self, ctx:D96Parser.Decl_stm_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assg_stm.
    def visitAssg_stm(self, ctx:D96Parser.Assg_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stm.
    def visitIf_stm(self, ctx:D96Parser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_if_stm.
    def visitElse_if_stm(self, ctx:D96Parser.Else_if_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_stm.
    def visitFor_stm(self, ctx:D96Parser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stm.
    def visitBreak_stm(self, ctx:D96Parser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stm.
    def visitContinue_stm(self, ctx:D96Parser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stm.
    def visitReturn_stm(self, ctx:D96Parser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#invocatoin_stm.
    def visitInvocatoin_stm(self, ctx:D96Parser.Invocatoin_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blk_stmt.
    def visitBlk_stmt(self, ctx:D96Parser.Blk_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmtlist.
    def visitStmtlist(self, ctx:D96Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_typ.
    def visitPrimitive_typ(self, ctx:D96Parser.Primitive_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_typ.
    def visitArray_typ(self, ctx:D96Parser.Array_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_typ.
    def visitClass_typ(self, ctx:D96Parser.Class_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_literal.
    def visitArray_literal(self, ctx:D96Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idxlit.
    def visitIdxlit(self, ctx:D96Parser.IdxlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mullit.
    def visitMullit(self, ctx:D96Parser.MullitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrlist.
    def visitArrlist(self, ctx:D96Parser.ArrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr.
    def visitArr(self, ctx:D96Parser.ArrContext):
        return self.visitChildren(ctx)



del D96Parser