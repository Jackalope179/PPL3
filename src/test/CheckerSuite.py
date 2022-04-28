import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test1(self):
    #     input = """
    #     Class A{
    #         Val a:String;
    #         getName(a:String; b: Int; d: Boolean ){
    #             Val e:String;
    #         }
    #     }
    #     Class A{

    #     }
    #     """
    #     expect = "Redeclared Class: A"
    #     self.assertTrue(TestChecker.test(input,expect,1))
    
    # def test2(self):
    #     input = """
    #     Class A{
    #         getName(a:String; b: Int; d: Boolean ){}
    #         Val a:String;
    #         Var b:Int;
    #         getName(){}
    #     }
    #     """
    #     expect = "Redeclared Method: getName"
    #     self.assertTrue(TestChecker.test(input,expect,2))

    # def test12(self):
    #     input ="""
    #     Class A{
    #         getName(a:String; b: Int; d: Boolean ){
    #             Val e:String;
    #             {
    #                 Val a: Int;
    #                 Var e: Boolean;
    #             }
    #             {
    #                 Var a: String;
    #                 Val b: Boolean;
    #                 {
    #                     Val c: Int;
    #                     Var d:Boolean;
    #                     {
    #                         Val b:Int;
    #                         Var b:String;
    #                     }
    #                 }
    #             }

                
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,12))

    # def test13(self):
    #     input ="""
    #     Class A{}
    #     Class B:A{}
    #     Class C:D{}
    #     """
    #     expect = "Undeclared Class: D"
    #     self.assertTrue(TestChecker.test(input,expect,13))

    def test14(self):
        input ="""
        Class A{
            getName(){
                Val a:C = New A();
            }
        }
        """
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,14))
    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    