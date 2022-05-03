import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    # def test0(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class D{
    #         method(){
    #             Return 1;
    #         }

    #     }
    #     Class A:D {
    #         Val $a:Int;
    #         Var b: Float;
    #         getName(){

    #         }
    #     }

    #     Class B:A{

    #     }
    #     Class Program{
    #         getName(){
    #             Var obj_d: D = New B();
    #             Var a:Int = 1;
    #             ##Var obj_b: B = New B();
    #             Val obj:A = New A();
    #             Var b:Float = 1;
    #             Var c:Int = 100;
    #             Var d:Boolean = True;
    #             Var e:Boolean = True;
    #             obj.b = 3.0;
    #             Val i:String;
    #             Foreach(a In 1 .. 100){
    #                 #a = a + 1;
    #             }
    #             If(a >1){
    #                 ##i = "Hello";
    #             }
    #             Foreach(c In 1+100 .. 1+1 ){
    #                 a = a + 1;
    #             }
    #             obj_d = obj_b;##
    #             a = obj_d.method_();
    #         }
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,1))

    def test0(self):
        input = """
        Class D{
            method(){
                Return 1;
            }
            $static(){
                Val a: D = New D();
                Return a;
            }
            program(){
                Return;
            }

        }
        Class A:D {
            Val $a:Int;
            Var b: Float;
            getName(){
                Return 1;
            }
            $staticMethod(){
                Return "Hello";
            }
        }

        Class B:A{

        }
        Class Program{
            getName(){
                Var a:B = New B();
                Var b:String;
                Var c:Int = 1;
                ##b = a.getName();##
                b = B::$staticMethod();
                a.program();

            }
            main(){
                Return;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,2))

    # def test0(self):
    #     input ="""
    #     Class A{
    #         Var $a: Int;
    #         Val $b: String;
    #         Val a: String = "Hello";
    #         Var b: Int = 1;
    #         Var c: Int = 3;
    #         Val d: Float = 2.0;
    #         getName(a,b,c: Int){
    #             Val obj: A = New A();
    #             obj.b = obj.c + 1;
    #             c = c + 1;
    #             {
    #                 Var x: Int;
    #                 obj.d = obj.d + 1;
    #             }
    #         }
    #     }

    #     Class B:A{
    #         Val $c: Float;
    #         getName(a,b,c: Int){
    #             c = c + 1;
    #             Val obj:B = New B();
    #             obj.b = obj.c + 1;
    #             obj.d = c + 1; 
    #         }
    #     }

    #     Class D: B{
    #         Val $d:Float;
    #         Val e: String;
    #         Val obj3: Int;
    #         getName(a,b,c: Int){
    #             c = c + 1;
    #             Val obj:D = New D();
    #             obj.b = obj.c + 1;
    #             obj.d = c + 1; 

    #             Val obj2:A = New D();
    #             obj2.b = obj2.c + 1;

    #             Val obj1:B = New D();
    #             obj2.b = obj2.c + 1;
    #             D::$a = 1 + 1 * 2;
    #         }
    #     }
    #     Class E{
    #         Val e: Int;
    #     }
    #     Class Program{
    #         main(){
    #             D::$a = 1 + 1 * 2;
    #             D::$b = "Hello";
    #             B::$c = 2.0;
    #             Val D: D = New D();
    #             D::$a = 1;
                
    #             D::$d = "Hello" +. "World";
    #             Return;
    #         }
    #     }
    #     """
    #     expect =""
    #     self.assertTrue(TestChecker.test(input,expect,0))



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

    # def test2(self):
    #     input ="""
    #     Class C{
    #         Val c: Int;
    #         Val g,h,i, j, f,w: Int;
    #         Var k, l, m: Boolean;
    #         method(){
    #             Val object: C = New C();

    #             object.c = 1;
    #             object.g = 1;
    #             object.w = 1;
                
    #         }
    #     }
    #     Class A:C{
    #         Val a: Int;
    #         Var b: String;
    #         method(){
    #             Val obj:A = New A();
    #             obj.att = 1;
    #             Val a:String;
    #             Var b:A;
    #             c = c + 1;
    #             Val d: C = New A();
    #             g  = g * 2;
    #             h  = h % 2;
    #             i  = i + 2;
    #             w= w + 1;
    #         }
    #         Var d: Int;
    #     }
    #     Class B:C{
    #         Val a: Int;
    #         method(a,b,c:A; d:Int; e:String){
    #             Val f: C = New A();
    #             m = !m ;
    #         }
    #     }
    #     Class D:B{
    #         getName(){
    #             m = g + 1;
    #             Val a:B = New D();
    #             c = g * h + i /j - f;
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Val test:C = New B();
    #             Val test_:C = New D();
    #             Return ;
    #         }
    #     }
    #     """
    #     expect =""
    #     self.assertTrue(TestChecker.test(input,expect,2))

    # def test1(self):
    #     input ="""
    #     Class A{
    #         Val a:Int;
    #         Var b:String;
    #         getName(){
    #             Val obj: A = New A();
    #             obj.b = obj.a + 1; 
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect =""
    #     self.assertTrue(TestChecker.test(input,expect,1))

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
    