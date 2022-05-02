import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    
    # def test0(self):
    #     input ="""
    #     Class A{
    #         Val a: Int;
    #         Var b: String;
    #         method(){
    #             Val a:String;
    #             Var b:A;

    #         }
    #         Var c: String;
    #     }
    #     Class B{
    #         Val a: Int;
    #     }
    #     Class Program{
    #         main(){}
    #     }
    #     """
    #     expect =""""""
    #     self.assertTrue(TestChecker.test(input,expect,1))

    # def test1(self):
    #     input ="""
    #     Class C{
    #         Val c: Int;
    #     }
    #     Class A:C{
    #         Val a: Int;
    #         Var b: String;
    #         method(){
    #             Val a:String;
    #             Var b:A;
    #             c = c + 1;
    #             Val d: A = New C();
    #         }
    #         Var d: Int;
    #     }
    #     Class B:A{
    #         Val a: Int;
    #         method(a,b,c:A; d:Int; e:String){
    #             Val f: A = New B();
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Return ;
    #         }
    #     }
    #     """
    #     expect ="""Type Mismatch In Constant Declaration: ConstDecl(Id('d'),ClassType(Id('A')),NewExpr(Id('C'),[]))"""
    #     self.assertTrue(TestChecker.test(input,expect,1))

    def test2(self):
        input ="""
        Class C{
            Val c: Int;
            Val g,h,i, j, f,w: Int;
            Var k, l, m: Boolean;
            method(){
                Val object: C = New C();

                object.c = 1;
                object.g = 1;
                object.w = 1;
                
            }
        }
        Class A:C{
            Val a: Int;
            Var b: String;
            method(){
                Val obj:A = New A();
                obj.att = 1;
                Val a:String;
                Var b:A;
                c = c + 1;
                Val d: C = New A();
                g  = g * 2;
                h  = h % 2;
                i  = i + 2;
                w= w + 1;
            }
            Var d: Int;
        }
        Class B:C{
            Val a: Int;
            method(a,b,c:A; d:Int; e:String){
                Val f: C = New A();
                m = !m ;
            }
        }
        Class D:B{
            getName(){
                m = g + 1;
                Val a:B = New D();
                c = g * h + i /j - f;
            }
        }
        Class Program{
            main(){
                Val test:C = New B();
                Val test_:C = New D();
                Return ;
            }
        }
        """
        expect =""
        self.assertTrue(TestChecker.test(input,expect,2))
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

    # def test14(self):
    #     input ="""
    #     Class A{
    #         Val a:Int;
            
    #         getName(a,b:String; c:Int){
    #             Val e:String;
    #             Val d:A = New X();

    #         }
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,14))

    # def test15(self):
    #     input ="""
    #     Class A{
    #         getName(){
    #             B::$a = 1;
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input,expect,15))

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
    