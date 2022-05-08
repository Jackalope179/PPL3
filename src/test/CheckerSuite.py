import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test0(self):
    #     input = """
    #     Class A{
    #         Val a: Int = 5;
    #         a(a,b,c:String; d:Float; e:Int){
    #             Val g:A = New A();
    #         }
    #         method(){
    #             If(True){

    #             } Elseif(1+1){

    #             } Else{

    #             }
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect ="Type Mismatch In Statement: If(BooleanLit(True),Block([]),If(BinaryOp(+,IntLit(1),IntLit(1)),Block([]),Block([])))"
    #     self.assertTrue(TestChecker.test(input,expect,0))
        
    # def test1(self):
    #     input = """
    #     Class A{
    #         Var expr:Boolean = True;
    #     }
    #     Class Program {
    #         Val expr:Boolean = True;
    #         Var $expr:Boolean = False;
    #         method(){
    #             Val a:Boolean = True;
    #             Val c:Boolean = True;
    #             Val obj:A = New A();
    #             Var d: Float = 2.0;
    #             If(a){
    #                 Val obj:A = New A();
    #                 {
    #                     Var obj:A= New A();
    #                     obj.expr = False;
    #                 }
    #             } Elseif (obj.expr){
    #                 d = d+1;
                    
    #             } Elseif(Self.expr){
    #                 d = d + 5.6e-2;
    #             } Elseif(Program::$expr){
    #                 d = d +5;
    #             } Else{
    #                 If (obj.expr){

    #                 } Else{
    #                     d = d + 1;
    #                     d = d * "Hello world";
    #                 }
    #             }

    #         }
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(*,Id(d),StringLit(Hello world))"
    #     self.assertTrue(TestChecker.test(input,expect,"1"))

    # def test2(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }

    #     Class Base{
    #         Val $a:Int = 1;
    #     }

    #     Class A:Base{
    #         main(){
    #             Var b:String ="Hello";
    #             A::$a = 1 + 1 + "Hello" - b;
    #         }
    #     }
        
    #     """
    #     expect = "Undeclared Attribute: $a"
    #     self.assertTrue(TestChecker.test(input,expect,2))

    # def test3(self):
    #     input = """
    #     Class D{
    #         method(){
    #             Return 1;
    #         }
    #         $static(){
    #             Val a: D = New D();
    #             Return a;
    #         }
    #     }
    #     Class A:D {
    #         Val $a:Int= 5;
    #         Var b: Float;
    #     }

    #     Class B:A{
    #         Var $a:Int = 1;
    #         getName(){
    #             Return "Hello world";
    #         }
    #         $staticMethod(){
    #             Return "Hello";
    #         }
    #         program(a,b,c:Float; e:String; f:Boolean){
    #             Return;
    #         }
    #     }
    #     Class Program{
    #         getName(){
    #             Var a:B = New B();
    #             Var b:String;
    #             Var c:Int = 1;
    #             b = B::$staticMethod();
    #             Var B:Float;
    #             B::$a = 1;
    #             a.program(1,2.0,3, "Hello", True);
    #             b = a.getName();
    #         }
    #         main(){
    #             Return;
    #         }
    #     }

    #     Class E:F{

    #     }
    #     """
    #     expect = "Undeclared Class: F"
    #     self.assertTrue(TestChecker.test(input,expect,3))

    def test4(self):
        input = """
        Class A{
            Var $static:Float = 1;
            Val $obj:A = New A();
            Val obj:A = New A();
            Var a: Int = 5;
            Var b: Int = 1 + A::$obj.a;
            Var c: Int = 1 + Self.obj.a;
            method(){
                Val a: Int = 5;
                Var b: Int = 1 + a;
                Var A:A;
                A = New A();
                A.a = 1;
                A::$static = 6;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        Class B{

        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,4))

    # def test4(self):
    #     input = """
    #     Class A{
    #         method(){
    #             Var i :Int;
    #             Foreach(i In 1 .. 100){
    #                 Break;
    #             }
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Var i :Int;
    #             Foreach(i In 1 .. 100){
    #                 Break;
    #                 Continue;
    #             }
    #             Return;
    #         }
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,4))

    # def test5(self):
    #     input = """
    #     Class A{
    #         method(){
    #             Var i :Int;
    #             Foreach(i In 1 .. 100){
    #                 Continue;
    #             }
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Var i :Int;
    #             Foreach(i In 1 .. 100){
    #                 Continue;
    #                 Break;
    #             }
    #             Return;
    #         }
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,5))

    # def test0(self):
    #     input = """
    #     Class A{
    #         Var $a: Int; 
    #         Var b: Int;
    #         getName(){}

    #         method(){
    #             Val A: A = New A();
    #             A::$a = 1;
    #         }
        
    #     }
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input,expect,5))


    # def test0(self):
    #     input = """
    #     Class A{
    #         ##Var a: Array[Float, 5] = Array(1, 2, 3, 4, 5);
    #         Val b: Array[Float, 5] = Array(1, 2, 3, 4, 1);##

    #         method(){
    #             ##Val b: Array[Float, 5] = Array(1, 2, 3, 4, 1);
    #             Var a: Array[Int, 5] = Array(1.0, 2.0, 3.6, 4.5, 1.2);
    #             Val c: Array[Array[Int,2],2] = Array(Array(1.0,2.0),Array(3,4));##
    #             Var a1: Int;
    #             Var a2: Int;
    #             Var a: Array[Array[Int,2],2] = Array(Array(a1,a2), Array(1,2));
    #         }
    #     }
        
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input,expect,6))

    # def test7(self):
    #     input = """
    #     Class A{
    #         Var a: Float;
    #         Var b: Int;
    #         program(){
    #             Self.b = Self.a;
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }


    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input,expect,7))


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


    # def test_array_function_9(self):
    #     input = """
    #         Class A{
    #             Var a: Array[Array[Int,2], 3] = Array(Array(1,2), Array(3,4), Array(5,6));
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 9'))
    
    # def test_array_function_10(self):
    #     input = """
    #         Class A{
    #             Var a: Array[Array[Int,2], 3] = Array(Array(1,2,3), Array(3,4), Array(5,6));
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = "Illegal Array Literal: [[IntLit(1),IntLit(2),IntLit(3)],[IntLit(3),IntLit(4)],[IntLit(5),IntLit(6)]]"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 10'))
    
    # def test_array_function_11(self):
    #     input = """
    #         Class A{
    #             Val a: Array[Array[Int,2], 3] = Array(1, Array(3,4), Array(5,6));
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = "Illegal Array Literal: [IntLit(1),[IntLit(3),IntLit(4)],[IntLit(5),IntLit(6)]]"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 11'))
    
    # def test_array_function_12(self):
    #     input = """
    #         Class A{
    #             Var a: Array[Array[Int,2], 3] = Array(Array(1,2), Array(3,4), Array(5,6), Array(7,8));
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(3,ArrayType(2,IntType)),[[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)],[IntLit(5),IntLit(6)],[IntLit(7),IntLit(8)]])"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 12'))
    
    # def test_array_function_13(self):
    #     input = """
    #         Class A{
    #             Var a: Array[Array[Int,2], 4] = Array(Array(1,2), Array(3,4), Array(5,6), Array(7,8));
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 13'))
    
    # def test_array_function_14(self):
    #     input = """
    #         Class A{
    #             Val a: Array[Array[Int,2], 3] = Array(Array(1, 2), Array(3,4), Array(5,6.5));
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = "Illegal Array Literal: [[IntLit(1),IntLit(2)],[IntLit(3),IntLit(4)],[IntLit(5),FloatLit(6.5)]]"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 14'))
    
    # def test_array_function_15(self):
    #     input = """
    #         Class A{
    #             Var a: Array[Float, 4] = Array(5.67, 1e10, 6.890, 2.5e-10);
    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 15'))
    
    # def test_array_function_16(self):
    #     input = """
    #         Class A{
    #             Val a: Array[Array[Array[String,2], 3], 1] = Array(Array(Array("khang", "best"), Array("heo","ngu"), Array("Hana", "cute")));
    #             Var a: Array[Array[Array[String,2], 3], 1] = Array(Array(Array("1", "best"), Array("heo","ngu"), Array("khang", "pro")));

    #         }
    #         Class Program{
    #             main(){
    #                 Return;
    #             }
    #         }
    #          """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 16'))

    # def test_array_function_17(self):
    #     input = """
    #     Class A{
    #         Var x:Int;
    #     }

    #     Class B{
    #         Var x:A;
    #     }

    #     Class Program{
    #         method(){
    #             Var x: B;
    #             x.x.x = 1;
    #             Return 1;
    #             Return 2;
    #         }

    #         main(){
    #             B = 1;
    #         }
    #     }
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 17'))

    # def test_array_function_18(self):
    #     input = """
    #     Class A{}
    #     Class Program{
    #         main(){
    #             Return;
    #         }
    #     }
    #     Class B:A{
    #         Var x:String;
    #         x(){}
    #         Var a:Int;
    #         Var b:Int;
    #         Var c:Int;
    #         x(){}
    #         Var x:String;

    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect,18))

    # def test0(self):
    #     input = """
    #     Class A{
    #         Constructor(a,b:Int; c:String; d:Float){
    #             Return;
    #         }
    #     }
    #     Class Program{
    #         program(){
    #             Val a:A = New A(1,2,"Hello", 1.5);
    #         }
    #         main(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 0'))

    # def test_attributeAccess_function_83(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }
                             
    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #            }

    #            Class C{
    #                Var a, b: Int = 4, 5;
    #                Var c: Float = 5.5;
    #                Var x: Khang;
    #                method(){
    #                    a = Khang::$a;
    #                    x.kk = c + 12.56 / 3;
    #                    x::$a = 10;
    #                }
    #            }

    #             """
    #     expect = "Illegal Member Access: FieldAccess(Id(x),Id($a))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 83'))

    # def test_attributeAccess_function_84(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }
                
    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #            }

    #            Class C{
    #                Var a, b: Int = 4, 5;
    #                Var x: Khang;
    #                method(){
    #                    a = x::$b + 12;
    #                }
    #            }

    #             """
    #     expect = "Illegal Member Access: FieldAccess(Id(x),Id($b))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 84'))

    # def test_attributeAccess_function_85(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             } 
                
    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #            }

    #            Class C{
    #                Var a, b: Int = 4, 5;
    #                Var x: Khang;
    #                method(){
    #                    a = Khang::$a + 12;
    #                    b = Khang::$c + 12;
    #                }
    #            }

    #             """
    #     expect = "Undeclared Attribute: $c"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 85'))

    # def test_attributeAccess_function_86(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }
        
    #            Class A {
    #                Var x: Int = 10;
    #            }

    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #            }

    #            Class C{
    #                Var a, b: Int = 4, 5;
    #                Var x: Khang;
    #                method(){
    #                    a = B::$a + 12;
    #                }
    #            }

    #             """
    #     expect = "Undeclared Class: B"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 86'))

    # def test_attributeAccess_function_87(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }
        
    #            Class A {
    #                Var x: Int = 10;
    #            }

    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #            }

    #            Class C{
    #                Var x, y: Int = 4, 5;
    #                Var z: Khang;
    #                method(){
    #                    x = y::$a + 12;
    #                }
    #            }

    #             """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(y),Id($a))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 87'))


    # def test_attributeAccess_function_88(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }

    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #                Val ss: String = "Bug";
    #            }

    #            Class C{
    #                Var x, y: Int = 4, 5;
    #                Var z: Khang;
    #                method(){
    #                    x = x.kk + 12;
    #                }
    #            }

    #             """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(x),Id(kk))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 88'))

    # def test_attributeAccess_function_89(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }

    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #                Val ss: String = "Bug";
    #            }

    #            Class C{
    #                Var x, y: Int = 4, 5;
    #                Var z: Khang;
    #                method(){
    #                    x = (1+1).kk + 12;
    #                }
    #            }

    #             """
    #     expect = "Type Mismatch In Expression: FieldAccess(BinaryOp(+,IntLit(1),IntLit(1)),Id(kk))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 89'))


    # def test_attributeAccess_function_90(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }

    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #                Var ss: String = "Bug";
    #            }

    #            Class C{
    #                Var x, y: Int = 4, 5;
    #                Var tmp: Float;
    #                method(){
    #                     Var Khang: Khang;
    #                     Self.tmp = Khang.kk + 12;
    #                     Self.Khang.ss = "yeyeye";
    #                     Self.tmp = Khang::$a + 10;
    #                }
    #            }

    #             """
    #     expect = "Illegal Member Access: FieldAccess(Id(Khang),Id($a))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 90'))


    # def test_attributeAccess_function_91(self):
    #     input = """
    #             Class Program{
    #                 main() { 
    #                     Return;
    #                 }
    #             }

    #            Class Khang {
    #                Var $a: Int = 5;
    #                Var kk: Float;
    #                Val ss: String = "Bug";
    #            }

    #            Class C{
    #                Var x, y: Int = 4, 5;
    #                Var tmp: Float;
    #                Var h: Khang;

    #                method(){
    #                    Var obj: C;
    #                    obj.x = Khang::$a + 10 / 5;
    #                    obj.h.kk = 12 * 56;
    #                    obj.h.ss = "yeye";
    #                }
    #            }

    #             """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(h),Id(ss)),StringLit(yeye))"
    #     self.assertTrue(TestChecker.test(input, expect, 'Test 91'))

    # def test3(self):
    #     input = """
    #     Class A {
    #         Val a: A = New A();
    #     }
    #     Class Program {
    #         main() {
    #             Val a: A = New A().a;
    #             New A().a = 5;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(NewExpr(Id('A'),[]),Id('a')),IntLit(5))"
    #     self.assertTrue(TestChecker.test(input,expect,"Test_3"))

    # def test_12(self):
    #     input = """
    #     Class Program {
    #         Var a: Float;
    #         main() {
    #             Self.a();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,"Test_12"))

# import unittest
# from TestUtils import TestChecker
# from AST import *


# class CheckerSuite(unittest.TestCase):
    # def test_1(self):
    #     input = """
    #     Class Program {}
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_1"))

    # def test_2(self):
    #     input = """
    #     Class Program {
    #         main(a: Int) {}
    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_2"))

    # def test_3(self):
    #     input = """
    #     Class A {
    #         Val a: A = New A();
    #     }
    #     Class Program {
    #         main() {
    #             Val a: A = New A().a;
    #             New A().a = a;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(NewExpr(Id(A),[]),Id(a)),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_3"))

    # def test_4(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Val a: Int = 5.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(5.5))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_4"))

    # def test_5(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Val a: Int;
    #         }
    #     }
    #     """
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_5"))

    # def test_6(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: Int;
    #             a = 5.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLit(5.5))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_6"))

    # def test_7(self):
    #     input = """
    #     Class Program {
    #         Var a: Float;
    #         main() {
    #             Var a: Int;
    #             Self.a = 10;
    #             a = 5 + 5.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLit(5),FloatLit(5.5)))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_7"))

    # def test_8(self):
    #     input = """
    #     Class Program {
    #         Var a: Float;
    #         main() {
    #             Var a: Int;
    #             Self.a = 10;
    #             a = 5 + 5.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLit(5),FloatLit(5.5)))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_8"))

    # def test_9(self):
    #     input = """
    #     Class Program {
    #         Var a: Float;
    #         main() {
    #             Self.a = 10;
    #             a = 5 + 5.5;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_9"))

    # def test_10(self):
    #     input = """
    #     Class Program {
    #         Var a: Float;
    #         main() {
    #             Self.b = 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Attribute: b"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_10"))

    # def test_11(self):
    #     input = """
    #     Class B : A{}
    #     Class Program {
    #         Var a: Float;
    #         main() {
    #             Self.a = 10;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: A"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_11"))

    # def test_12(self):
    #     input = """
    #     Class Program {
    #         Val a: Float = 5;
    #         main() {
    #             Self.a();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_12"))

    # def test_13(self):
    #     input = """
    #     Class Program {
    #         Val a: Float = 5;
    #         main() {
    #             Var a: Program;
    #             a.a = 10;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(a),Id(a)),IntLit(10))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_13"))

    # def test_14(self):
    #     input = """
    #     Class Program {
    #         Var a: Float;
    #         a(a: Int) {
    #             Return Self.a;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_14"))

    # def test_15(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {
    #             Var a: Float;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_15"))

    # def test_16(self):
    #     input = """
    #     Class Program {}
    #     Class Program {
    #         a(a: Int) {
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_16"))

    # def test_17(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {}
    #         Var a: Float;
    #         main(){}
    #     }
    #     """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_17"))

    # def test_18(self):
    #     input = """
    #     Class Program {
    #         a(a: Int; a: Float) {}
    #         main(){}
    #     }
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_18"))

    # def test_19(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {
    #             Val a: Float = 5.5;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Redeclared Constant: a"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_19"))

    # def test_20(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {
    #             Var b: Int = 5;
    #             Val c: Float = 5.5e3;
    #             b = 1 + c;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(b),BinaryOp(+,IntLit(1),Id(c)))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_20"))

    # def test_21(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {
    #             Var b: String = "Hello ";
    #             b = b + a;
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(b),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_21"))

    # def test_22(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {
    #             Return a;
    #         }
    #         main(){
    #             Self.a(10.5);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(a),[FloatLit(10.5)])"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_22"))

    # def test_23(self):
    #     input = """
    #     Class Program {
    #         a(a: Int) {
    #             Return a;
    #         }
    #         main(){
    #             Self.a(10, 20);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(a),[IntLit(10),IntLit(20)])"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_23"))

    # def test_24(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 4];
    #         setArr(a: Array[Int, 3]) {
    #             Self.a = a;
    #             Return;
    #         }
    #         main(){
    #             Self.setArr(Array(1, 2, 3));
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_24"))

    # def test_25(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 4];
    #         setArr(a: Array[Int, 4]) {
    #             Self.a = a;
    #             Return;
    #         }
    #         main(){
    #             Self.setArr(Array(1, 2, 3));
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(setArr),[[IntLit(1),IntLit(2),IntLit(3)]])"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_25"))

    # def test_26(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 4];
    #         setArr(a: Array[Float, 4]) {
    #             Self.a = a;
    #             Return;
    #         }
    #         main(){
    #             Self.setArr(Array(1.2, 2.3, 3.4, 4.5));
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(a)),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_26"))

    # def test_27(self):
    #     input = """
    #     Class Program {
    #         func(a, b: Float) {
    #             Return b + a;
    #         }
    #         main(){
    #             Var x: Int;
    #             x = Self.func(5, 5);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Self(),Id(func),[IntLit(5),IntLit(5)]))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_27"))

    # def test_28(self):
    #     input = """
    #     Class Program {
    #         func(a, b: Float) {
    #             Return b + a;
    #         }
    #         main(){
    #             Var x: Int;
    #             x = Self.func(5, 5);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Self(),Id(func),[IntLit(5),IntLit(5)]))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_28"))

    # def test_29(self):
    #     input = """
    #     Class Shape {
    #         Var width: Float;
    #         Var height: Float;

    #         Constructor(width, height: Float) {
    #             Self.width = width;
    #             Self.height = height;
    #         }

    #         calArea() {
    #             Return Self.width * Self.height;
    #         }
    #     }
        
    #     Class Program {
    #         main(){
    #             Var shape: Shape = New Shape(5, 5.5);
    #             Var res: Int;
    #             res = shape.calArea();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(res),CallExpr(Id(shape),Id(calArea),[]))"
    #     self.assertTrue(TestChecker.test(input, expect, "Test_29"))
