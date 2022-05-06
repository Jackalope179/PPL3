import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test1(self):
        """Simple program: int main() {} """
        input = """
        Class A{
            Var a: Int;
            program(){
                Self.a = 1;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),Id(B),[])])"
        self.assertTrue(TestAST.test(input,expect,1))

    # def test2(self):
    #     input ="""
    #     Class A:B{
    #         Val a:Int;
    #         Var b: Int;
    #         Val c:String;
    #     }
    #     """
    #     expect ="Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,ConstDecl(Id(c),StringType,None))])])"
    #     self.assertTrue(TestAST.test(input,expect,2))

    # def test3(self):
    #     input = """
    #     Class A{
    #         Val a,b:Int=1,2;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(2)))])])"
    #     self.assertTrue(TestAST.test(input,expect, 3))

    # def test4(self):
    #     input = """
    #     Class A{
    #         Val a,b:Int=1,2;
    #         getName(){
    #             Val c,d,e:String = "Hello","World","Machine";
    #             c = c + 1;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(2))),MethodDecl(Id(getName),Instance,[],Block([ConstDecl(Id(c),StringType,StringLit(Hello)),ConstDecl(Id(d),StringType,StringLit(World)),ConstDecl(Id(e),StringType,StringLit(Machine)),AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(1)))]))])])"
    #     self.assertTrue(TestAST.test(input,expect, 4))

    # def test5(self):
    #     input ="""
    #     Class A{
    #         A(){
    #             a = "Hello" +. "World";
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(Hello),StringLit(World)))]))])])"
    #     self.assertTrue(TestAST.test(input,expect, 5))

    # def test6(self):
    #     input ="""
    #     Class A{
    #         A(){
    #             a = "Hello" +. "World";
    #             a = c ==. 4;
    #             b = a + 1;
    #             Val c:Int = 1;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(Hello),StringLit(World))),AssignStmt(Id(a),BinaryOp(==.,Id(c),IntLit(4))),AssignStmt(Id(b),BinaryOp(+,Id(a),IntLit(1))),ConstDecl(Id(c),IntType,IntLit(1))]))])])"
    #     self.assertTrue(TestAST.test(input,expect, 6))

    # def test7(self):
    #     input = """
    #     Class A{
    #         Constructor(){
    #             a = New X();
    #             Return a;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(X),[])),Return(Id(a))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,7))

    # def test8(self):
    #     input = """
    #     Class A{
    #         $_(){
    #             a = 123.456E+12;
    #             Foreach(a In 1.e+2..12.4E-12){
    #                 Out.printInt(a,b,c);
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id($_),Static,[],Block([AssignStmt(Id(a),FloatLit(123456000000000.0)),For(Id(a),FloatLit(100.0),FloatLit(1.24e-11),IntLit(1),Block([Call(Id(Out),Id(printInt),[Id(a),Id(b),Id(c)])])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,8))

    # def test9(self):
    #     input = """
    #     Class A{
    #         $_(){
    #             a = 123.456E+12;
    #             Foreach(a In 1.e+2..12.4E-12){
    #                 Foreach(j In 1 .. 10 By 2){
    #                     Out.printInt(i,j);
    #                     }
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id($_),Static,[],Block([AssignStmt(Id(a),FloatLit(123456000000000.0)),For(Id(a),FloatLit(100.0),FloatLit(1.24e-11),IntLit(1),Block([For(Id(j),IntLit(1),IntLit(10),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i),Id(j)])])])])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,9))

    # def test10(self):
    #     input = """
    #     Class Number{
    #         Var a: Array[Array[Int, 5], 5];

    #         print(a,b: Int; c: String){
    #             Out.printInt(a[0][0]);
    #         }
            
    #         getValue() {
    #         a = Array("Hello", "Hi", "HelloWorld");
    #         Var Nonstatic: Int = 5;
    #         Val var1, var2, var3: Int = 5, 5 > 6, Self.a;
    #         Self.print(e,d,g);
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))),MethodDecl(Id(print),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),StringType)],Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(a),[IntLit(0),IntLit(0)])])])),MethodDecl(Id(getValue),Instance,[],Block([AssignStmt(Id(a),[StringLit(Hello),StringLit(Hi),StringLit(HelloWorld)]),VarDecl(Id(Nonstatic),IntType,IntLit(5)),ConstDecl(Id(var1),IntType,IntLit(5)),ConstDecl(Id(var2),IntType,BinaryOp(>,IntLit(5),IntLit(6))),ConstDecl(Id(var3),IntType,FieldAccess(Self(),Id(a))),Call(Self(),Id(print),[Id(e),Id(d),Id(g)])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,10))

    # def test11(self):
    #     input ="""
    #     Class A{
    #         getA(){
    #             Val var1, var2, var3: Int = 5, 5 > 6, Self.a;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(getA),Instance,[],Block([ConstDecl(Id(var1),IntType,IntLit(5)),ConstDecl(Id(var2),IntType,BinaryOp(>,IntLit(5),IntLit(6))),ConstDecl(Id(var3),IntType,FieldAccess(Self(),Id(a)))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,11))
    
    # def test12(self):
    #     input ="""
    #     Class A{
    #         getA(){
    #             {
    #                 Val a:Int = 1;
    #                 a = a + 1;
    #             }
    #             {
    #                 b = b + 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(getA),Instance,[],Block([Block([ConstDecl(Id(a),IntType,IntLit(1)),AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,12))

    # def test13(self):
    #     input ="""
    #     Class Number{
    #         getValue() {
    #         If(Self.a < 0){
    #             a = a + 1;
    #         }
    #         Elseif (a < 10){
    #             a = a - 1;
    #         }
    #         Elseif (a >  100){
    #             a = a - 1;
    #         }
    #         Else {
    #          Out.printInt(a);   
    #         }
    #         }            
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Number),[MethodDecl(Id(getValue),Instance,[],Block([If(BinaryOp(<,FieldAccess(Self(),Id(a)),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<,Id(a),IntLit(10)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]),If(BinaryOp(>,Id(a),IntLit(100)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]),Block([Call(Id(Out),Id(printInt),[Id(a)])]))))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,13))


    # def test14(self):
    #     input ="""
    #     Class A{
    #         Val a: Int = a[1+1][Self.a][1+1];
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1)),FieldAccess(Self(),Id(a)),BinaryOp(+,IntLit(1),IntLit(1))])))])])"
    #     self.assertTrue(TestAST.test(input,expect,14))

    # def test16(self):
    #     input ="""
    #     Class A{
    #         getA(){
    #             a = Array("Hello", "Hi", "HelloWorld");
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(getA),Instance,[],Block([AssignStmt(Id(a),[StringLit(Hello),StringLit(Hi),StringLit(HelloWorld)])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,16))


    # def test17(self):
    #     input ="""
    #     Class A{
    #         B(){
    #             Val a: A;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(B),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NullLiteral())]))])])"
    #     self.assertTrue(TestAST.test(input,expect,17))

    # def test18(self):
    #     input ="""
    #     Class Program{
    #         main(){
    #             Val a: A;
    #             {
    #                 a = a +1;
    #                 {
    #                     a = a + 2;
    #                     Val a,c,d: B = 1+1, Array("Hello", "Hi", "HelloWorld"), 0x123;
    #                 }
    #                 {
    #                     If (Self.a > 5){
    #                         a = a + 1;
    #                     }
    #                     Elseif (a < 10){
    #                         a = a - 1;
    #                     }
    #                     {
    #                         Foreach(item In 1 .. 100 By 2){
    #                             ##Out.log("Hello");##
    #                         }
    #                     }
    #                 }

    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NullLiteral()),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(2))),ConstDecl(Id(a),ClassType(Id(B)),BinaryOp(+,IntLit(1),IntLit(1))),ConstDecl(Id(c),ClassType(Id(B)),[StringLit(Hello),StringLit(Hi),StringLit(HelloWorld)]),ConstDecl(Id(d),ClassType(Id(B)),IntLit(291))]),Block([If(BinaryOp(>,FieldAccess(Self(),Id(a)),IntLit(5)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<,Id(a),IntLit(10)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]))),Block([For(Id(item),IntLit(1),IntLit(100),IntLit(2),Block([])])])])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,18))

    # def test19(self):
    #     input ="""
    #     Class A{
    #         getA(){
    #             {
    #                 Foreach(a In 1 .. 100){
    #                  Out.printInt(a,b,c);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(getA),Instance,[],Block([Block([For(Id(a),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(printInt),[Id(a),Id(b),Id(c)])])])])]))])])"
    #     self.assertTrue(TestAST.test(input,expect,19))

    # def test20(self):
    #     input = """
    #     Class Program
    #     {
    #         Val a,b,c,d,e,f,g,h,i,k: Int = 1 ==.1, x && y, x - y + z, 
    #                                         x * (y / z), !x + (y - z),
    #                                         - 5 + x / 2, arr[2] + (r || t),
    #                                         (Car.tire) + 100, Bruh::$Cheems + 10 && 3 - 5 > 0,
    #                                         (100 >= 99) && (45 <= 50);
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(==.,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(&&,Id(x),Id(y)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(+,BinaryOp(-,Id(x),Id(y)),Id(z)))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,BinaryOp(*,Id(x),BinaryOp(/,Id(y),Id(z))))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,BinaryOp(+,UnaryOp(!,Id(x)),BinaryOp(-,Id(y),Id(z))))),AttributeDecl(Instance,ConstDecl(Id(f),IntType,BinaryOp(+,UnaryOp(-,IntLit(5)),BinaryOp(/,Id(x),IntLit(2))))),AttributeDecl(Instance,ConstDecl(Id(g),IntType,BinaryOp(+,ArrayCell(Id(arr),[IntLit(2)]),BinaryOp(||,Id(r),Id(t))))),AttributeDecl(Instance,ConstDecl(Id(h),IntType,BinaryOp(+,FieldAccess(Id(Car),Id(tire)),IntLit(100)))),AttributeDecl(Instance,ConstDecl(Id(i),IntType,BinaryOp(>,BinaryOp(&&,BinaryOp(+,FieldAccess(Id(Bruh),Id($Cheems)),IntLit(10)),BinaryOp(-,IntLit(3),IntLit(5))),IntLit(0)))),AttributeDecl(Instance,ConstDecl(Id(k),IntType,BinaryOp(&&,BinaryOp(>=,IntLit(100),IntLit(99)),BinaryOp(<=,IntLit(45),IntLit(50)))))])])"
    #     self.assertTrue(TestAST.test(input,expect,20))

    # def test21(self):
    #     input = """
    #             Class Program{
    #                 main() {
    #                     Val a,b,c:Float = 1.e9,1.e-0,1.e1-2;
    #                     Var d,e:Float = .1e9,.2e-8;
    #                     Val f,g,h:Float = 0.e12,1.e-12,10.e+5;
    #                     Var i,j,k:Float = 0.,1.,1.12;
    #                 } 
    #             }
    #             """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),FloatType,FloatLit(1000000000.0)),ConstDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),FloatType,BinaryOp(-,FloatLit(10.0),IntLit(2))),VarDecl(Id(d),FloatType,FloatLit(100000000.0)),VarDecl(Id(e),FloatType,FloatLit(2e-09)),ConstDecl(Id(f),FloatType,FloatLit(0.0)),ConstDecl(Id(g),FloatType,FloatLit(1e-12)),ConstDecl(Id(h),FloatType,FloatLit(1000000.0)),VarDecl(Id(i),FloatType,FloatLit(0.0)),VarDecl(Id(j),FloatType,FloatLit(1.0)),VarDecl(Id(k),FloatType,FloatLit(1.12))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 21))
    
    # def test22(self):
    #     input ="""
    #     Class Program{
    #         Val a,b,c: Int = New A(1+1, Self.a, "Hello World", !x), 1, 2;
    #         Var d,e: Array[Array[Array[Int, 5],5],5];
    #         main() {
    #             Val a,b,c,d,e,f,g,h,i,k: Int = 1 ==.1, x && y, x - y + z, 
    #                                          x * (y / z), !x + (y - z),
    #                                          - 5 + x / 2, arr[2] + (r || t),
    #                                          (Car.tire) + 100, Bruh::$Cheems + 10 && 3 - 5 > 0,
    #                                          (100 >= 99) && (45 <= 50);

    #             a = (car.tire) + 100;
    #             b = (100 >= 99) && (45 <= 50);
    #             Foreach(a In 1 .. Self.a By 5){
    #                 Out.printInt(a,b,c);
    #                 Val a,b,c:Boolean = 1,2,3;
    #                 Continue;
    #             }
    #             Return;

    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,NewExpr(Id(A),[BinaryOp(+,IntLit(1),IntLit(1)),FieldAccess(Self(),Id(a)),StringLit(Hello World),UnaryOp(!,Id(x))]))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(5,ArrayType(5,ArrayType(5,IntType))))),AttributeDecl(Instance,VarDecl(Id(e),ArrayType(5,ArrayType(5,ArrayType(5,IntType))))),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,BinaryOp(==.,IntLit(1),IntLit(1))),ConstDecl(Id(b),IntType,BinaryOp(&&,Id(x),Id(y))),ConstDecl(Id(c),IntType,BinaryOp(+,BinaryOp(-,Id(x),Id(y)),Id(z))),ConstDecl(Id(d),IntType,BinaryOp(*,Id(x),BinaryOp(/,Id(y),Id(z)))),ConstDecl(Id(e),IntType,BinaryOp(+,UnaryOp(!,Id(x)),BinaryOp(-,Id(y),Id(z)))),ConstDecl(Id(f),IntType,BinaryOp(+,UnaryOp(-,IntLit(5)),BinaryOp(/,Id(x),IntLit(2)))),ConstDecl(Id(g),IntType,BinaryOp(+,ArrayCell(Id(arr),[IntLit(2)]),BinaryOp(||,Id(r),Id(t)))),ConstDecl(Id(h),IntType,BinaryOp(+,FieldAccess(Id(Car),Id(tire)),IntLit(100))),ConstDecl(Id(i),IntType,BinaryOp(>,BinaryOp(&&,BinaryOp(+,FieldAccess(Id(Bruh),Id($Cheems)),IntLit(10)),BinaryOp(-,IntLit(3),IntLit(5))),IntLit(0))),ConstDecl(Id(k),IntType,BinaryOp(&&,BinaryOp(>=,IntLit(100),IntLit(99)),BinaryOp(<=,IntLit(45),IntLit(50)))),AssignStmt(Id(a),BinaryOp(+,FieldAccess(Id(car),Id(tire)),IntLit(100))),AssignStmt(Id(b),BinaryOp(&&,BinaryOp(>=,IntLit(100),IntLit(99)),BinaryOp(<=,IntLit(45),IntLit(50)))),For(Id(a),IntLit(1),FieldAccess(Self(),Id(a)),IntLit(5),Block([Call(Id(Out),Id(printInt),[Id(a),Id(b),Id(c)]),ConstDecl(Id(a),BoolType,IntLit(1)),ConstDecl(Id(b),BoolType,IntLit(2)),ConstDecl(Id(c),BoolType,IntLit(3)),Continue])]),Return()]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 22))

    # def test23(self):
    #     input ="""
    #     Class Program{
    #         $B(){
    #             Val a:Int = A[1+2][3+4][A[1][2][3]];
    #         }
    #         $A(){
    #         }
    #         main(){
    #             Val a:Int = A::$B();
    #         }
    #     }

    #     Class A{
    #         main(){
    #             Val a,b,c: Int = 1,2,3;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($B),Static,[],Block([ConstDecl(Id(a),IntType,ArrayCell(Id(A),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,IntLit(3),IntLit(4)),ArrayCell(Id(A),[IntLit(1),IntLit(2),IntLit(3)])]))])),MethodDecl(Id($A),Static,[],Block([])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,CallExpr(Id(A),Id($B),[]))]))]),ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),ConstDecl(Id(c),IntType,IntLit(3))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 23))

    
  
    # def test24(self):
    #     input ='''
    #     Class A{
    #         Constructor(){
    #             Val a:Int = 1 && 2 + 1 || 2 - (3 ==.4);
    #             Var a,b,c:Int = a::$b(a,b,c), a.function(a[2][2][2]), 3 == (5 + 6);
    #             Return;
    #         }
    #         Destructor(){
    #             a = 1.e123 + .1e-2;
    #             b = New A(a[1][2]);
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([ConstDecl(Id(a),IntType,BinaryOp(||,BinaryOp(&&,IntLit(1),BinaryOp(+,IntLit(2),IntLit(1))),BinaryOp(-,IntLit(2),BinaryOp(==.,IntLit(3),IntLit(4))))),VarDecl(Id(a),IntType,CallExpr(Id(a),Id($b),[Id(a),Id(b),Id(c)])),VarDecl(Id(b),IntType,CallExpr(Id(a),Id(function),[ArrayCell(Id(a),[IntLit(2),IntLit(2),IntLit(2)])])),VarDecl(Id(c),IntType,BinaryOp(==,IntLit(3),BinaryOp(+,IntLit(5),IntLit(6)))),Return()])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,FloatLit(1e+123),FloatLit(0.001))),AssignStmt(Id(b),NewExpr(Id(A),[ArrayCell(Id(a),[IntLit(1),IntLit(2)])]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 24))
    
    # def test25(self):
    #     input ='''
    #     Class A{
    #         Constructor(){
    #             {
    #                 If(a == 1.e-123){
    #                     {
    #                         a = 1;
    #                         b = 2;
    #                     }
    #                 }
    #                 Else{
    #                     {
    #                         a = 2;
    #                         b = 3;
    #                     }
    #                 }

    #                 If(a >= 100){
    #                     {
    #                         Out.print(a);
    #                     }
    #                 }
    #                 Elseif(a <= 100){
    #                     Out.print(a);
    #                 }
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([Block([If(BinaryOp(==,Id(a),FloatLit(1e-123)),Block([Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(b),IntLit(2))])]),Block([Block([AssignStmt(Id(a),IntLit(2)),AssignStmt(Id(b),IntLit(3))])])),If(BinaryOp(>=,Id(a),IntLit(100)),Block([Block([Call(Id(Out),Id(print),[Id(a)])])]),If(BinaryOp(<=,Id(a),IntLit(100)),Block([Call(Id(Out),Id(print),[Id(a)])])))])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 25))
    
    # def test26(self):
    #     input ='''
    #     Class A{
    #         A(){
    #             A::$gertShape();
    #             A::$getShape(1,2,3);
    #             B.Hello();
    #             c.Hello(1,2,3);
    #             Return;
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([Call(Id(A),Id($gertShape),[]),Call(Id(A),Id($getShape),[IntLit(1),IntLit(2),IntLit(3)]),Call(Id(B),Id(Hello),[]),Call(Id(c),Id(Hello),[IntLit(1),IntLit(2),IntLit(3)]),Return()]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 26))
    
    # def test27(self):
    #     input ='''
    #     Class Program{
    #         main(){
    #             Val a:Int = Array(Array(1,2,3), Array("hi", "Hello", "Hi")) + 0x123;
    #             a = Array(
    #                 Array(1,2,3),
    #                 Array(1+1, a[1][2], a[1][2][3]),
    #                 Array(a[a[1][1]][Self.a])
    #             );

    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,BinaryOp(+,[[IntLit(1),IntLit(2),IntLit(3)],[StringLit(hi),StringLit(Hello),StringLit(Hi)]],IntLit(291))),AssignStmt(Id(a),[[IntLit(1),IntLit(2),IntLit(3)],[BinaryOp(+,IntLit(1),IntLit(1)),ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])],[ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1),IntLit(1)]),FieldAccess(Self(),Id(a))])]])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 27))
    
    # def test28(self):
    #     input ='''
    #     Class A{
    #         Val a,b,c:String;
    #         main(){
    #             Val c,d,e: String;
    #         }

    #         $getShape(a,b,c:String; c,d:Int){
    #             Val a,b,c:String;
    #         }
    #     }

    #     Class B:Parent{
    #         getShape(){
    #             Val a,b,c:A = 1,1,1;
    #         }
    #         Constructor(a,c:String; d:Float){
    #             Out.printLn("Hello");
    #         }

    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(b),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(c),StringType,None)),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c),StringType,None),ConstDecl(Id(d),StringType,None),ConstDecl(Id(e),StringType,None)])),MethodDecl(Id($getShape),Static,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType),param(Id(c),IntType),param(Id(d),IntType)],Block([ConstDecl(Id(a),StringType,None),ConstDecl(Id(b),StringType,None),ConstDecl(Id(c),StringType,None)]))]),ClassDecl(Id(B),Id(Parent),[MethodDecl(Id(getShape),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(A)),IntLit(1)),ConstDecl(Id(b),ClassType(Id(A)),IntLit(1)),ConstDecl(Id(c),ClassType(Id(A)),IntLit(1))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),StringType),param(Id(c),StringType),param(Id(d),FloatType)],Block([Call(Id(Out),Id(printLn),[StringLit(Hello)])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 28))
    
    # def test29(self):
    #     input ='''
    #     Class Program{
    #         main(){
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 29))
    
    # def test30(self):
    #     input ='''
    #     Class Program{
    #         main(){
    #             a = True + False;
    #             b = Null + 1;
    #             {
    #                 (Self.a)[1][2][3] = 1;
    #                 (A.Hello)[Self.s][A[1][2]] = Null ;
    #                 (1 > 2)[1] = (3 > 4)[2];
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),BinaryOp(+,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(b),BinaryOp(+,NullLiteral(),IntLit(1))),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(Id(A),Id(Hello)),[FieldAccess(Self(),Id(s)),ArrayCell(Id(A),[IntLit(1),IntLit(2)])]),NullLiteral()),AssignStmt(ArrayCell(BinaryOp(>,IntLit(1),IntLit(2)),[IntLit(1)]),ArrayCell(BinaryOp(>,IntLit(3),IntLit(4)),[IntLit(2)]))])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 30))
    
    # def test31(self):
    #     input ='''
    #     Class A{
    #         main(){
    #             Foreach(A In 1+1 .. 5+6>7 ){
    #                 Out.printLn(1.e123);
    #             }
    #         }

    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([For(Id(A),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(>,BinaryOp(+,IntLit(5),IntLit(6)),IntLit(7)),IntLit(1),Block([Call(Id(Out),Id(printLn),[FloatLit(1e+123)])])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 31))
    
    # def test32(self):
    #     input ='''
    #     Class A{
    #         Val a:A;
    #         Val a: A = New A();
    #         Val a: B = New A(a,b,c);
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(A)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[]))),AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(B)),NewExpr(Id(A),[Id(a),Id(b),Id(c)])))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 32))
    
    # def test33(self):
    #     input ='''
    #     Class Program{
    #         main(a,b,c:C){
    #             a = a + 1;
    #             Foreach(A In 0x123 .. 0x456 By 0x123){
    #                 a[1]["heeloo"] = a[1]["heeloo"] + 1;
    #             }
            
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),ClassType(Id(C))),param(Id(b),ClassType(Id(C))),param(Id(c),ClassType(Id(C)))],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),For(Id(A),IntLit(291),IntLit(1110),IntLit(291),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),StringLit(heeloo)]),BinaryOp(+,ArrayCell(Id(a),[IntLit(1),StringLit(heeloo)]),IntLit(1)))])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 33))
    
    # def test34(self):
    #     input ='''
    #     Class A{
    #         A(){
    #             A[1][2][3] = Self.a;
    #             (1+1).A = Self.A();
    #             (A[1][2][3]).A = 1+1;
    #             A::$A = 1+1;
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([AssignStmt(ArrayCell(Id(A),[IntLit(1),IntLit(2),IntLit(3)]),FieldAccess(Self(),Id(a))),AssignStmt(FieldAccess(BinaryOp(+,IntLit(1),IntLit(1)),Id(A)),CallExpr(Self(),Id(A),[])),AssignStmt(FieldAccess(ArrayCell(Id(A),[IntLit(1),IntLit(2),IntLit(3)]),Id(A)),BinaryOp(+,IntLit(1),IntLit(1))),AssignStmt(FieldAccess(Id(A),Id($A)),BinaryOp(+,IntLit(1),IntLit(1)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 34))
    
    # def test35(self):
    #     input ='''
    #     Class B{
    #         B(){
    #             Val a: Array[Int, 5] =  "Hello";
    #         }
    #         Val a:Int = 1+1;
    #         C(a,b:String){
    #             Val b:Boolean = True + False;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(B),[MethodDecl(Id(B),Instance,[],Block([ConstDecl(Id(a),ArrayType(5,IntType),StringLit(Hello))])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1)))),MethodDecl(Id(C),Instance,[param(Id(a),StringType),param(Id(b),StringType)],Block([ConstDecl(Id(b),BoolType,BinaryOp(+,BooleanLit(True),BooleanLit(False)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 35))
    
    # def test36(self):
    #     input ='''
    #     Class A{
    #         A(){
    #             a = 1.e+123 + .1e-123;
    #             b = 0.123E123;
    #             c = 0B1100001;
    #             d = 0b1111111;
    #             e = 0X123 + 0x123;
    #             f = 012345 + 012345667;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,FloatLit(1e+123),FloatLit(1e-124))),AssignStmt(Id(b),FloatLit(1.23e+122)),AssignStmt(Id(c),IntLit(97)),AssignStmt(Id(d),IntLit(127)),AssignStmt(Id(e),BinaryOp(+,IntLit(291),IntLit(291))),AssignStmt(Id(f),BinaryOp(+,IntLit(5349),IntLit(2739127)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 36))
    
    # def test37(self):
    #     input ="""
    #     Class Number{
    #         Var a: Int;
    #         getValue() {
    #         Foreach(i In 1 .. 10 By 2){
    #             Out.printInt(i);
    #             If(i > 5){
    #                 Return 1+1;
    #                 Break;
    #             }
    #             Else{
    #                 Return Self.a;
    #                 Continue;
    #             }
    #             Return "Hello";
    #         }
    #         }            
    #     }
    #     """
    #     expect = '''Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(getValue),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)]),If(BinaryOp(>,Id(i),IntLit(5)),Block([Return(BinaryOp(+,IntLit(1),IntLit(1))),Break]),Block([Return(FieldAccess(Self(),Id(a))),Continue])),Return(StringLit(Hello))])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 37))
    
    # def test38(self):
    #     input ='''
    #     Class A{
    #         $A(){
    #             If(a[1][a[1][2]] > 5)
    #             {
    #                 If(a < 5){
    #                     a = a + 1;
    #                     b = b + 1;
    #                 }
    #                 Elseif(Null){
    #                     a = Null + 1;
    #                 }
    #                 Elseif(True){
    #                     main = Null + 1;
    #                     Program = Null - 1;
    #                 }
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id($A),Static,[],Block([If(BinaryOp(>,ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[IntLit(1),IntLit(2)])]),IntLit(5)),Block([If(BinaryOp(<,Id(a),IntLit(5)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))]),If(NullLiteral(),Block([AssignStmt(Id(a),BinaryOp(+,NullLiteral(),IntLit(1)))]),If(BooleanLit(True),Block([AssignStmt(Id(main),BinaryOp(+,NullLiteral(),IntLit(1))),AssignStmt(Id(Program),BinaryOp(-,NullLiteral(),IntLit(1)))]))))]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 38))
    
    # def test39(self):
    #     input = """
    #     Class FindIndex: Utils
    #     {
    #         Var $index: Int = 0;
    #         findAllIndex(s1: String; s2: String)
    #         {
    #             index = s1.find(s2);
    #             If(index == string::$npos)
    #             {
    #                 Out.Print(-1);
    #             }
    #             Else
    #             {
    #                 Out.Print(index);
    #                 index = s1.find(s2, index + 1);
    #                 Foreach(index In index .. string::$npos By s1.find(s2, index + 1))
    #                 {
    #                     Out.Print(" ");
    #                     Out.Print(index);
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(FindIndex),Id(Utils),[AttributeDecl(Static,VarDecl(Id($index),IntType,IntLit(0))),MethodDecl(Id(findAllIndex),Instance,[param(Id(s1),StringType),param(Id(s2),StringType)],Block([AssignStmt(Id(index),CallExpr(Id(s1),Id(find),[Id(s2)])),If(BinaryOp(==,Id(index),FieldAccess(Id(string),Id($npos))),Block([Call(Id(Out),Id(Print),[UnaryOp(-,IntLit(1))])]),Block([Call(Id(Out),Id(Print),[Id(index)]),AssignStmt(Id(index),CallExpr(Id(s1),Id(find),[Id(s2),BinaryOp(+,Id(index),IntLit(1))])),For(Id(index),Id(index),FieldAccess(Id(string),Id($npos)),CallExpr(Id(s1),Id(find),[Id(s2),BinaryOp(+,Id(index),IntLit(1))]),Block([Call(Id(Out),Id(Print),[StringLit( )]),Call(Id(Out),Id(Print),[Id(index)])])])]))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,39))
    
    # def test40(self):
    #     input ='''
    #     Class A{
    #         a(){
    #             If(a ==. Self.A() + A[1][A[1][2]])
    #             {
    #                 Foreach(index In a==.b .. a + c By 0x123){
    #                     {
    #                         Out.printInt("Hello");
    #                     }
    #                 }
    #                 Return a && b || c;
    #             }
    #         }

    #     }
    #     Class Program{
    #         main(a,b: String; c:Float; d,e,f:A){
    #             Val a,b,c:A;
    #             Return;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==.,Id(a),BinaryOp(+,CallExpr(Self(),Id(A),[]),ArrayCell(Id(A),[IntLit(1),ArrayCell(Id(A),[IntLit(1),IntLit(2)])]))),Block([For(Id(index),BinaryOp(==.,Id(a),Id(b)),BinaryOp(+,Id(a),Id(c)),IntLit(291),Block([Block([Call(Id(Out),Id(printInt),[StringLit(Hello)])])])]),Return(BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),FloatType),param(Id(d),ClassType(Id(A))),param(Id(e),ClassType(Id(A))),param(Id(f),ClassType(Id(A)))],Block([ConstDecl(Id(a),ClassType(Id(A)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(A)),NullLiteral()),ConstDecl(Id(c),ClassType(Id(A)),NullLiteral()),Return()]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 40))
    
    # def test41(self):
    #     input ='''
    #     Class A{
    #         A(){
    #             Return;
    #             Break;
    #             Return;
    #             Var c,d,e:Boolean = True, False, True;
    #         }
    #         Val a,b,c:Int;
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([Return(),Break,Return(),VarDecl(Id(c),BoolType,BooleanLit(True)),VarDecl(Id(d),BoolType,BooleanLit(False)),VarDecl(Id(e),BoolType,BooleanLit(True))])),AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 41))
    
    # def test42(self):
    #     input ='''
    #     Class A{
    #         Val a: Int = 1;
    #         $main(){
    #             Foreach(i In 1 .. 10){
    #                 Out.println(i);
    #                 If(1+2 && (5+7)){
    #                     Break;
    #                     If( Self.a >5){
    #                         Continue;
    #                     }
    #                 }
    #             }
    #             Return Self.a() + 1>5 ;  
    #         }
    #     }
    #     Class B{
    #         main(){
    #             Return;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id($main),Static,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([Call(Id(Out),Id(println),[Id(i)]),If(BinaryOp(&&,BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,IntLit(5),IntLit(7))),Block([Break,If(BinaryOp(>,FieldAccess(Self(),Id(a)),IntLit(5)),Block([Continue]))]))])]),Return(BinaryOp(>,BinaryOp(+,CallExpr(Self(),Id(a),[]),IntLit(1)),IntLit(5)))]))]),ClassDecl(Id(B),[MethodDecl(Id(main),Instance,[],Block([Return()]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 42))
    
    # def test43(self):
    #     input ='''
    #     Class A{
    #         Val a,b,c:String = 1+1, New X() + 1, 123;
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,BinaryOp(+,NewExpr(Id(X),[]),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,IntLit(123)))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 43))
    
    
    # def test45(self):
    #     input ='''
    #     Class A{
    #         A(){
    #            Out.printIn(a[0][1][2]);
    #             a[0][a[1][2]][a[2][2]] = 1;
    #             A[Self.a()][Self.a()][Self.a()] = 1;
    #             A[a[Self.a]][a[1+1]] = 5;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([Call(Id(Out),Id(printIn),[ArrayCell(Id(a),[IntLit(0),IntLit(1),IntLit(2)])]),AssignStmt(ArrayCell(Id(a),[IntLit(0),ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(Id(a),[IntLit(2),IntLit(2)])]),IntLit(1)),AssignStmt(ArrayCell(Id(A),[CallExpr(Self(),Id(a),[]),CallExpr(Self(),Id(a),[]),CallExpr(Self(),Id(a),[])]),IntLit(1)),AssignStmt(ArrayCell(Id(A),[ArrayCell(Id(a),[FieldAccess(Self(),Id(a))]),ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1))])]),IntLit(5))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 45))
    
    # def test46(self):
    #     input = """
    #     Class Program
    #     {
    #         Var arr: Array[Array[Int, 1000], 1000];

    #         initalize()
    #         {
    #             Foreach(row In 0 .. 1000 By 1)
    #             {
    #                 Foreach(col In 0 .. 1000 By 1)
    #                 {
    #                     arr[row][col] = 0;
    #                 }
    #             }
    #         }

    #         findMaxColumn()
    #         {
    #             Var sum: Array[Int, 1000];

    #             Foreach(i In 0 .. 1000 By 1)
    #             {
    #                 sum[i] = 0;
    #             }

    #             Var index: Int = -1;

    #             Foreach(i In 0 .. 1000 By 1)
    #             {
    #                 Foreach(j In 0 .. 1000 By 1)
    #                 {
    #                     sum[i] = sum[i] + arr[j][i];
    #                 }
    #             }

    #             Var max: Int = 0;

    #             Foreach(i In 0 .. 1000 By 1)
    #             {
    #                 If(sum[i] >= max)
    #                 {
    #                     max = sum[i];
    #                     index = i;
    #                 }
    #             }

    #             Return index;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1000,ArrayType(1000,IntType)))),MethodDecl(Id(initalize),Instance,[],Block([For(Id(row),IntLit(0),IntLit(1000),IntLit(1),Block([For(Id(col),IntLit(0),IntLit(1000),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(row),Id(col)]),IntLit(0))])])])])])),MethodDecl(Id(findMaxColumn),Instance,[],Block([VarDecl(Id(sum),ArrayType(1000,IntType)),For(Id(i),IntLit(0),IntLit(1000),IntLit(1),Block([AssignStmt(ArrayCell(Id(sum),[Id(i)]),IntLit(0))])]),VarDecl(Id(index),IntType,UnaryOp(-,IntLit(1))),For(Id(i),IntLit(0),IntLit(1000),IntLit(1),Block([For(Id(j),IntLit(0),IntLit(1000),IntLit(1),Block([AssignStmt(ArrayCell(Id(sum),[Id(i)]),BinaryOp(+,ArrayCell(Id(sum),[Id(i)]),ArrayCell(Id(arr),[Id(j),Id(i)])))])])])]),VarDecl(Id(max),IntType,IntLit(0)),For(Id(i),IntLit(0),IntLit(1000),IntLit(1),Block([If(BinaryOp(>=,ArrayCell(Id(sum),[Id(i)]),Id(max)),Block([AssignStmt(Id(max),ArrayCell(Id(sum),[Id(i)])),AssignStmt(Id(index),Id(i))]))])]),Return(Id(index))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,46))
    
    # def test47(self):
    #     input ='''
    #     Class A{
    #         main(){
    #             Self.a = A[2][2];
    #             A.C = A[1][2];
    #             A::$x = B[1][2];
    #             (1+1).x = "Hello";
    #             a[1][2].x = "Helo World";
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),ArrayCell(Id(A),[IntLit(2),IntLit(2)])),AssignStmt(FieldAccess(Id(A),Id(C)),ArrayCell(Id(A),[IntLit(1),IntLit(2)])),AssignStmt(FieldAccess(Id(A),Id($x)),ArrayCell(Id(B),[IntLit(1),IntLit(2)])),AssignStmt(FieldAccess(BinaryOp(+,IntLit(1),IntLit(1)),Id(x)),StringLit(Hello)),AssignStmt(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),Id(x)),StringLit(Helo World))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 47))
    
    # def test48(self):
    #     input ='''
    #     Class A{
    #         Val a,b,c:Array[Int, 0x123] = 1+1, "Hello World", Self.a();
    #         Val a:Int = Array();
    #         main(){
    #             Return Null;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(291,IntType),BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(291,IntType),StringLit(Hello World))),AttributeDecl(Instance,ConstDecl(Id(c),ArrayType(291,IntType),CallExpr(Self(),Id(a),[]))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,[])),MethodDecl(Id(main),Instance,[],Block([Return(NullLiteral())]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 48))
    
    # def test49(self):
    #     input =''' 
    #     Class A: Program{
    #         main(){
    #             a[0x123][0X123] = 123;
    #             Return;
    #             Return a[0b11100][0B111];
    #             Continue;
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),Id(Program),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(291),IntLit(291)]),IntLit(123)),Return(),Return(ArrayCell(Id(a),[IntLit(28),IntLit(7)])),Continue]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 49))
    
    # def test50(self):
    #     input ='''
    #     Class main{
    #         Val a, b: Array[Int, 123_456_789] = Array(1,2,3), Array(0x123ABC, 0x456, 0x789);
    #         Var c: Int = a[0] + b[0] + C[1];
             
    #         $GETsHAPE(){
    #             Foreach(i In 1 .. 10){
    #             Val a: Int = Array(
    #                 Array(1,2,3),
    #                 Array(4,5,6)
    #             );
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(main),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(123456789,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(123456789,IntType),[IntLit(1194684),IntLit(1110),IntLit(1929)])),AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(+,BinaryOp(+,ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(b),[IntLit(0)])),ArrayCell(Id(C),[IntLit(1)])))),MethodDecl(Id($GETsHAPE),Static,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([ConstDecl(Id(a),IntType,[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)]])])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 50))
    
    # def test51(self):
    #     input =''' 
    #     Class A{
    #         Var $New , $Constructor: Array[Int, 5] = Self.a , True;
    #         Val a:Array[Array[String,1],5] = Array(Array("Hello"));

    #         Constructor(a,b,c:String; d,e: Float; g:Int){
    #             print.Out("Hello");
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($New),ArrayType(5,IntType),FieldAccess(Self(),Id(a)))),AttributeDecl(Static,VarDecl(Id($Constructor),ArrayType(5,IntType),BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,ArrayType(1,StringType)),[[StringLit(Hello)]])),MethodDecl(Id(Constructor),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType),param(Id(d),FloatType),param(Id(e),FloatType),param(Id(g),IntType)],Block([Call(Id(print),Id(Out),[StringLit(Hello)])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 51))
    
    # def test52(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             a = -a;
    #             b = !a;
    #         }
    #         main(a,b,c:String){
    #             Val a,b,c:Int;
    #             Var a,b,c:Int;
    #             Val a,b: Int = 1,2;
    #             Var c,d :A = 1+1, -a;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),UnaryOp(-,Id(a))),AssignStmt(Id(b),UnaryOp(!,Id(a)))])),MethodDecl(Id(main),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType)],Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),ConstDecl(Id(c),IntType,None),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),VarDecl(Id(c),ClassType(Id(A)),BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(d),ClassType(Id(A)),UnaryOp(-,Id(a)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 52))
    
    # def test54(self):
    #     input = """
    #     Class Prototype
    #     {
    #         Var $prototypeName: String;
    #         Var prototypeField: Float;

    #         Destructor(){}
    #         Clone(){}
    #         Constructor(prototypeField: Float)
    #         {
    #             Self.prototypeField = prototypeField;
    #             Out.Print(("Call Method from " +. Prototype::$prototypeName) +. ("with field : " +. prototypeField));
    #         }
    #     }

    #     Class ConcretePrototype1: Prototype
    #     {
    #         Var concrete_prototype_field1_: Float;

    #         Clone()
    #         {
    #             Return New ConcretePrototype1(Self);
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),UnaryOp(-,Id(a))),AssignStmt(Id(b),UnaryOp(!,Id(a)))])),MethodDecl(Id(main),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType)],Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),ConstDecl(Id(c),IntType,None),VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),VarDecl(Id(c),ClassType(Id(A)),BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(d),ClassType(Id(A)),UnaryOp(-,Id(a)))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,54))

    # def test53(self):
    #     input =''' 
    #     Class C:Parent{
    #         Destructor(){
    #             Val a:Int;
    #         }

    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(C),Id(Parent),[MethodDecl(Id(Destructor),Instance,[],Block([ConstDecl(Id(a),IntType,None)]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 53))
    
    # def test54(self):
    #     input = """
    #     Class a{
    #         Val b, c, d, e: Int = 12_12_43, 0X1_FA21_1, 0b11_001_1, 012_2123_47;
    #         Val $f: Float = 0.124 + 1.53e632 + 12.E32 - 1;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(a),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(121243))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(2073105))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(51))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(2692327))),AttributeDecl(Static,ConstDecl(Id($f),FloatType,BinaryOp(-,BinaryOp(+,BinaryOp(+,FloatLit(0.124),FloatLit(inf)),FloatLit(1.2e+33)),IntLit(1))))])])"
    #     self.assertTrue(TestAST.test(input,expect,54))

    # def test55(self):
    #     input =''' 
    #     Class A{
    #         Val a,b:Float = 0x1_2_3, 0b1_1_1_1;
    #         Var $b,$c,$d:String = 0.123, 0.123E-112, 0123_456;
    #         main(){
    #             Var b,c,d:String = 0.123, 0.123E-112, 01_2_3_4;
    #             Val b,c,d:String = 0.123, 0.123E-112, 0B1111_111;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,IntLit(291))),AttributeDecl(Instance,ConstDecl(Id(b),FloatType,IntLit(15))),AttributeDecl(Static,VarDecl(Id($b),StringType,FloatLit(0.123))),AttributeDecl(Static,VarDecl(Id($c),StringType,FloatLit(1.23e-113))),AttributeDecl(Static,VarDecl(Id($d),StringType,IntLit(42798))),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(b),StringType,FloatLit(0.123)),VarDecl(Id(c),StringType,FloatLit(1.23e-113)),VarDecl(Id(d),StringType,IntLit(668)),ConstDecl(Id(b),StringType,FloatLit(0.123)),ConstDecl(Id(c),StringType,FloatLit(1.23e-113)),ConstDecl(Id(d),StringType,IntLit(127))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 55))
    
    # def test56(self):
    #     input = """
    #     Class Program
    #     {
    #         isSymmetric(arr: Array[Array[Int, 1000], 1000]; row, col: Int)
    #         {
    #             Foreach(row In 0 .. 1000 By 1)
    #             {
    #                 Foreach(col In 0 .. 1000 By 1)
    #                 {
    #                     If(arr[row][col] != arr[col][row])
    #                     {
    #                         Return False;
    #                     }
    #                 }
    #             }

    #             Return True;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(isSymmetric),Instance,[param(Id(arr),ArrayType(1000,ArrayType(1000,IntType))),param(Id(row),IntType),param(Id(col),IntType)],Block([For(Id(row),IntLit(0),IntLit(1000),IntLit(1),Block([For(Id(col),IntLit(0),IntLit(1000),IntLit(1),Block([If(BinaryOp(!=,ArrayCell(Id(arr),[Id(row),Id(col)]),ArrayCell(Id(arr),[Id(col),Id(row)])),Block([Return(BooleanLit(False))]))])])])]),Return(BooleanLit(True))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,56))
    
    # def test57(self):
    #     input =''' 
    #     Class A{
    #         Constructor(a,b,c:String){
    #             Foreach(item In 0x123 .. 0x456){
    #                 Var a:Int = item;
    #                Val b,c:Boolean = Self.a(item), A::$A("Hello", "Hi");
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType)],Block([For(Id(item),IntLit(291),IntLit(1110),IntLit(1),Block([VarDecl(Id(a),IntType,Id(item)),ConstDecl(Id(b),BoolType,CallExpr(Self(),Id(a),[Id(item)])),ConstDecl(Id(c),BoolType,CallExpr(Id(A),Id($A),[StringLit(Hello),StringLit(Hi)]))])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 57))
    
    # def test58(self):
    #     input =''' 
    #     Class A{
    #     }
    #     Class B{}
    #     Class main{}
    #     Class Program{}
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(main),[]),ClassDecl(Id(Program),[])])'''
    #     self.assertTrue(TestAST.test(input, expect, 58))
    
    # def test59(self):
    #     input =''' 
    #     Class Program{
    #         main(){
    #             Val a,b,c:Program = 1,2,3;
    #             Return;
    #         }
    #         Constructor(){
    #             Foreach(A In a[1][2][3] .. B[5][6][7] By Self.B[5][6][7]){
    #                 Out.printLn("Hello");
    #                 Self.a[5][6][7] = 1+1;
    #                 Val a,b,c:Int = 1,2,3;
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(Program)),IntLit(1)),ConstDecl(Id(b),ClassType(Id(Program)),IntLit(2)),ConstDecl(Id(c),ClassType(Id(Program)),IntLit(3)),Return()])),MethodDecl(Id(Constructor),Instance,[],Block([For(Id(A),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(B),[IntLit(5),IntLit(6),IntLit(7)]),ArrayCell(FieldAccess(Self(),Id(B)),[IntLit(5),IntLit(6),IntLit(7)]),Block([Call(Id(Out),Id(printLn),[StringLit(Hello)]),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(5),IntLit(6),IntLit(7)]),BinaryOp(+,IntLit(1),IntLit(1))),ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),ConstDecl(Id(c),IntType,IntLit(3))])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 59))
    
    # def test60(self):
    #     input =''' 
    #     Class A{
    #         Val a,b: Int = A::$A, A.C.D;
    #         Var c,d: String = A::$A(1,2,3), A.C(1,2,3).B();
    #         Val e,f: C = A.C.D(1,2,3), E.F().G();

    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,FieldAccess(Id(A),Id($A)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,FieldAccess(FieldAccess(Id(A),Id(C)),Id(D)))),AttributeDecl(Instance,VarDecl(Id(c),StringType,CallExpr(Id(A),Id($A),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(Instance,VarDecl(Id(d),StringType,CallExpr(CallExpr(Id(A),Id(C),[IntLit(1),IntLit(2),IntLit(3)]),Id(B),[]))),AttributeDecl(Instance,ConstDecl(Id(e),ClassType(Id(C)),CallExpr(FieldAccess(Id(A),Id(C)),Id(D),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(Instance,ConstDecl(Id(f),ClassType(Id(C)),CallExpr(CallExpr(Id(E),Id(F),[]),Id(G),[])))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 60))
    
    # def test61(self):
    #     input =''' 
    #     Class A{
    #         Val a,b:Program = New X(), New X(1+1, Self.a, Null);
    #         Var a: Program = - Self.a;
    #         main(){
    #             (1+1).A = 1+2-3;
    #             (Self.a[1][2][3]).B = 1+2-3;
    #         }

    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(Program)),NewExpr(Id(X),[]))),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(Program)),NewExpr(Id(X),[BinaryOp(+,IntLit(1),IntLit(1)),FieldAccess(Self(),Id(a)),NullLiteral()]))),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Program)),UnaryOp(-,FieldAccess(Self(),Id(a))))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(BinaryOp(+,IntLit(1),IntLit(1)),Id(A)),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),AssignStmt(FieldAccess(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),Id(B)),BinaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 61))
    
    # def test62(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             {
    #                 {
    #                     a = Null + 1;
    #                     b = Self.A + 1;
    #                     c = Array(Null, Null, Null);
    #                     d = Array();
    #                 }
    #             }
    #             {
    #                 Return;
    #                 Continue;
    #                 Break;
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([Block([Block([AssignStmt(Id(a),BinaryOp(+,NullLiteral(),IntLit(1))),AssignStmt(Id(b),BinaryOp(+,FieldAccess(Self(),Id(A)),IntLit(1))),AssignStmt(Id(c),[NullLiteral(),NullLiteral(),NullLiteral()]),AssignStmt(Id(d),[])])]),Block([Return(),Continue,Break])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 62))
    
    # def test63(self):
    #     input =''' 
    #     Class Program:Program{
    #         main(a,b,c: Array[Array[Int,4], 5]){
    #             Out.println(a.Hello());
    #             Out.printLn(b.Hello);
    #             A::$Hello = "Hello" +1;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),ArrayType(5,ArrayType(4,IntType))),param(Id(b),ArrayType(5,ArrayType(4,IntType))),param(Id(c),ArrayType(5,ArrayType(4,IntType)))],Block([Call(Id(Out),Id(println),[CallExpr(Id(a),Id(Hello),[])]),Call(Id(Out),Id(printLn),[FieldAccess(Id(b),Id(Hello))]),AssignStmt(FieldAccess(Id(A),Id($Hello)),BinaryOp(+,StringLit(Hello),IntLit(1)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 63))
    
    # def test64(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             Foreach(i In 1 .. 2){

    #             }

    #             If(Null){
    #                 Foreach(i In 1 .. 2){

    #                 }
    #             }
    #             If(Self){

    #             }
    #             If(Self){

    #             }
    #             Else{
    #                 A = Self + 1; 
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(2),IntLit(1),Block([])]),If(NullLiteral(),Block([For(Id(i),IntLit(1),IntLit(2),IntLit(1),Block([])])])),If(Self(),Block([])),If(Self(),Block([]),Block([AssignStmt(Id(A),BinaryOp(+,Self(),IntLit(1)))]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 64))
    
    # def test65(self):
    #     input =''' 
    #     Class A{
    #     }
    #     Class D{
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[]),ClassDecl(Id(D),[])])'''
    #     self.assertTrue(TestAST.test(input, expect, 65))
    
    # def test66(self):
    #     input =''' 
    #     Class A{
    #         $staticMethod(){
    #             Val __,_,_: String = 1,2,3;
    #             Foreach(id In Null..Null){
    #                 Out.printLn("Hello");
    #             }
    #             If(Null.A + 1 > 4){
    #                 Out.printLn("Hello World");
    #                 Hello[1][a[1][2]] = "My world";
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id($staticMethod),Static,[],Block([ConstDecl(Id(__),StringType,IntLit(1)),ConstDecl(Id(_),StringType,IntLit(2)),ConstDecl(Id(_),StringType,IntLit(3)),For(Id(id),NullLiteral(),NullLiteral(),IntLit(1),Block([Call(Id(Out),Id(printLn),[StringLit(Hello)])])]),If(BinaryOp(>,BinaryOp(+,FieldAccess(NullLiteral(),Id(A)),IntLit(1)),IntLit(4)),Block([Call(Id(Out),Id(printLn),[StringLit(Hello World)]),AssignStmt(ArrayCell(Id(Hello),[IntLit(1),ArrayCell(Id(a),[IntLit(1),IntLit(2)])]),StringLit(My world))]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 66))
    
    # def test67(self):
    #     input =''' 
    #     Class A{
    #         $NonStatic(){
    #             {
    #                 a[Null][Null][Self.a] = 1;
    #                 If ( a[1][2][3] > 5){
    #                     Out.printLn("Hello world");
    #                 }
    #                 Elseif(a < 100){
    #                     a[Self.a][Self.b] = (1 ==. 1); 
    #                 }
    #                 Else{

    #                 }
    #             }
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id($NonStatic),Static,[],Block([Block([AssignStmt(ArrayCell(Id(a),[NullLiteral(),NullLiteral(),FieldAccess(Self(),Id(a))]),IntLit(1)),If(BinaryOp(>,ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(5)),Block([Call(Id(Out),Id(printLn),[StringLit(Hello world)])]),If(BinaryOp(<,Id(a),IntLit(100)),Block([AssignStmt(ArrayCell(Id(a),[FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(b))]),BinaryOp(==.,IntLit(1),IntLit(1)))]),Block([])))])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 67))
    
    # def test68(self):
    #     input =''' 
    #     Class C{
    #         Val a,b,c:String = a + 1 - 2 , x*y/z%1, a && b || c;
    #         Var a:Array[Int, 5] = a[1][2][3];
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(C),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,BinaryOp(-,BinaryOp(+,Id(a),IntLit(1)),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(x),Id(y)),Id(z)),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 68))
    
    # def test69(self):
    #     input =''' 
    #     Class Program{
    #         main(){
    #             a[a][b][c] = 1+1+2;
    #             a.Hello = 1+2+3;
    #             Self.HelloWorld = 1+2+3;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[Id(a),Id(b),Id(c)]),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),IntLit(2))),AssignStmt(FieldAccess(Id(a),Id(Hello)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),AssignStmt(FieldAccess(Self(),Id(HelloWorld)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 69))
    
    # def test70(self):
    #     input ='''
    #     Class B:C{
    #         main(){ 
    #             If(a>5){
    #                 Out.printLn("Hello");
    #                 {
    #                     Foreach(main In 1 .. 0x123){
    #                         Out.printLn("Hello");
    #                         Foreach(main In Self.a+1 .. Self.A() By Null){
    #                             Out.printLn("Hello");
    #                             a[1][2][3] = "Nice"+ "Clean";
    #                             Foreach(main In Self.a[1][2][3]..Self.a)
    #                             {
    #                                 {
    #                                     a[1][a[2][2]] = True +False;
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
            
            
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(B),Id(C),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(>,Id(a),IntLit(5)),Block([Call(Id(Out),Id(printLn),[StringLit(Hello)]),Block([For(Id(main),IntLit(1),IntLit(291),IntLit(1),Block([Call(Id(Out),Id(printLn),[StringLit(Hello)]),For(Id(main),BinaryOp(+,FieldAccess(Self(),Id(a)),IntLit(1)),CallExpr(Self(),Id(A),[]),NullLiteral(),Block([Call(Id(Out),Id(printLn),[StringLit(Hello)]),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),BinaryOp(+,StringLit(Nice),StringLit(Clean))),For(Id(main),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2),IntLit(3)]),FieldAccess(Self(),Id(a)),IntLit(1),Block([Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[IntLit(2),IntLit(2)])]),BinaryOp(+,BooleanLit(True),BooleanLit(False)))])])])])])])])])]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 70))
    
    # def test71(self):
    #     input =''' 
    #     Class A{
    #         Val a, b, c:String = Array(3,4,5) + 1, Array(Null, Null, Null) + a.Static, 1+1;
    #         main(){
    #         }
    #         main(a,b,c:String){
    #         }
    #     }
    #     Class Program{
    #         main(){

    #         }
    #         Val a,b:String = 1+1, 2+2;
    #         A(){
    #             A.a = 1+2;
    #         }
    #     } 
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,BinaryOp(+,[IntLit(3),IntLit(4),IntLit(5)],IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,BinaryOp(+,[NullLiteral(),NullLiteral(),NullLiteral()],FieldAccess(Id(a),Id(Static))))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,IntLit(1),IntLit(1)))),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType)],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(a),StringType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,BinaryOp(+,IntLit(2),IntLit(2)))),MethodDecl(Id(A),Instance,[],Block([AssignStmt(FieldAccess(Id(A),Id(a)),BinaryOp(+,IntLit(1),IntLit(2)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 71))
    
    # def test72(self):
    #     input =''' 
    #     Class A{
    #         Val $a, b:Boolean = True, False;
    #         Val c,d: String = 1+1, 2+2;
    #         main(){
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(d),StringType,BinaryOp(+,IntLit(2),IntLit(2)))),MethodDecl(Id(main),Instance,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 72))
    
    # def test73(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             Foreach(i In 1 .. Self.a By 0x123){
    #                 Val _,__,___ : Array[Int,5] = 1.1e+123, 1.e123, 0x1_2_4;
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),FieldAccess(Self(),Id(a)),IntLit(291),Block([ConstDecl(Id(_),ArrayType(5,IntType),FloatLit(1.1e+123)),ConstDecl(Id(__),ArrayType(5,IntType),FloatLit(1e+123)),ConstDecl(Id(___),ArrayType(5,IntType),IntLit(292))])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 73))
    
    # def test74(self):
    #     input ="""
    #     Class A{
    #         main(){
    #             ##a = (a[0][1])[2][3];
    #             a = (Self.a)[0][1][2];
    #             a = a[0][1][2];##
    #             (a[3])[1][2] = 1;
    #             ##a[1][2][3] = 123;
    #             (Self.a)[1][2] = 0x123;##

    #         }
    #     }

    #     """
    #     expect ="Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(3)]),[IntLit(1),IntLit(2)]),IntLit(1))]))])])"
    #     self.assertTrue(TestAST.test(input,expect,74))
    
    # def test75(self):
    #     input =''' 
    #     Class A:Parent{
    #         Val a:Array[Boolean, 0x123] = 1+1;
    #         main(){
    #             Val a,b,c:Array[Float, 0B111] = Self.a, a[1][2][3], Array(1,2,3);

    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),Id(Parent),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(291,BoolType),BinaryOp(+,IntLit(1),IntLit(1)))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),ArrayType(7,FloatType),FieldAccess(Self(),Id(a))),ConstDecl(Id(b),ArrayType(7,FloatType),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])),ConstDecl(Id(c),ArrayType(7,FloatType),[IntLit(1),IntLit(2),IntLit(3)])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 75))

    # def test76(self):
    #     input = """
    #     Class MulArr: Arr
    #     {
    #         Var a, b: Array[Array[Array[Int, 3], 3], 3] = Array(
    #             Array(
    #                 Array(1,2,3),
    #                 Array(4,5,6),
    #                 Array(7,8,9)
    #             )
    #         ), Array(
    #             Array(
    #                 Array(1,2,3),
    #                 Array(4,5,6),
    #                 Array(7,8,9)
    #             )
    #         );
    #         CalSum(size: Int)
    #         {
    #             Foreach(i In 0 .. size By Sys.Count(1))
    #             {
    #                 Foreach(j In 0 .. size By 1.0000e1)
    #                 {
    #                     Foreach(k In 0 .. size By Mul.multi(1,1.00e-12) / (1 * 2))
    #                     {
    #                         a[b[i][j][k]] = b[a[a[i][j][k]]] * 0X123AFB;
    #                     }
    #                 }
    #             }
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(MulArr),Id(Arr),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,ArrayType(3,ArrayType(3,IntType))),[[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(7),IntLit(8),IntLit(9)]]])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(3,ArrayType(3,ArrayType(3,IntType))),[[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(7),IntLit(8),IntLit(9)]]])),MethodDecl(Id(CalSum),Instance,[param(Id(size),IntType)],Block([For(Id(i),IntLit(0),Id(size),CallExpr(Id(Sys),Id(Count),[IntLit(1)]),Block([For(Id(j),IntLit(0),Id(size),FloatLit(10.0),Block([For(Id(k),IntLit(0),Id(size),BinaryOp(/,CallExpr(Id(Mul),Id(multi),[IntLit(1),FloatLit(1e-12)]),BinaryOp(*,IntLit(1),IntLit(2))),Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(b),[Id(i),Id(j),Id(k)])]),BinaryOp(*,ArrayCell(Id(b),[ArrayCell(Id(a),[ArrayCell(Id(a),[Id(i),Id(j),Id(k)])])]),IntLit(1194747)))])])])])])]),Return()]))])])"
    #     self.assertTrue(TestAST.test(input,expect,76))
    
    # def test77(self):
    #     input =''' 
    #     Class A{
    #         Val a,b:String = (1+1)[1][2][3], (a[1][2]);
    #         main(){
    #             (a[3][4])[1][2] = 1;
    #             (Self.a)[5][6] = 1+1;
    #             Foreach(i In (a[1])[1][2] .. (a[2])[1][2] By 1){
    #                 Out.printLn(1+1);
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(BinaryOp(+,IntLit(1),IntLit(1)),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,ArrayCell(Id(a),[IntLit(1),IntLit(2)]))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(3),IntLit(4)]),[IntLit(1),IntLit(2)]),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(5),IntLit(6)]),BinaryOp(+,IntLit(1),IntLit(1))),For(Id(i),ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(1),IntLit(2)]),ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[IntLit(1),IntLit(2)]),IntLit(1),Block([Call(Id(Out),Id(printLn),[BinaryOp(+,IntLit(1),IntLit(1))])])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 77))
    
    # def test78(self):
    #     input =''' 
    #     Class A{
    #         Val a,b:String = (1+1)[1][2][3], (a[1][2]);
    #         main(){
    #             Out.printLn("Hello");
    #             Val _,__:Float = 1,2;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(BinaryOp(+,IntLit(1),IntLit(1)),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,ArrayCell(Id(a),[IntLit(1),IntLit(2)]))),MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(printLn),[StringLit(Hello)]),ConstDecl(Id(_),FloatType,IntLit(1)),ConstDecl(Id(__),FloatType,IntLit(2))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 78))
    
    # def test79(self):
    #     input ="""
    #     Class A{
    #         main(){
    #             a[2][3][1] = 1;
    #             (a[2])[3] = 1;
    #             (a[2])[3][4] = 1;
    #             (a[2][3])[3] = 1;
    #         }
    #     }
    #     """
    #     expect ="Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(2),IntLit(3),IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[IntLit(3)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[IntLit(3),IntLit(4)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(2),IntLit(3)]),[IntLit(3)]),IntLit(1))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 79))

    # def test80(self):
    #     input =''' 
    #     Class A{
    #         Val a,b,c:Int = a[1][2], (a[1])[2], (a[1][2])[3];
    #         main(){
    #             Foreach(item In (Self.a)[1][2] .. 0x123 ){
    #                 Print.Out(item);
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(Id(a),[IntLit(1),IntLit(2)]))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),[IntLit(3)]))),MethodDecl(Id(main),Instance,[],Block([For(Id(item),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2)]),IntLit(291),IntLit(1),Block([Call(Id(Print),Id(Out),[Id(item)])])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 80))
    
    # def test81(self):
    #     input =""" 
    #     Class A{
    #         main(){
    #             a = (a[1])[2];
    #             a = (a[1][2])[2];
    #             a = (a[1][2])[2][3];
    #             a = a[1][2][3][4];

    #             a[1][1] = 1;
    #             (a[1][2])[1][2][1] = 1;
    #             a[1][2][3][4] = 1;
    #             (a[1][2][3])[4] = 1;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)])),AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),[IntLit(2)])),AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),[IntLit(2),IntLit(3)])),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),[IntLit(1),IntLit(2),IntLit(1)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),[IntLit(4)]),IntLit(1))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,81))
    
    # def test82(self):
    #     input = """
    #     Class Prototype
    #     {
    #         Main()
    #         {
    #             Var a,b,c: Int = Self.Method(), Shape::$Radius, 1_541_3 + 0X534 * 02_3237 / 0b111_01;
    #         }
    #     }

    #     Class Program
    #     {
    #         Main(a: Int){}
    #         Main(){}
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Prototype),[MethodDecl(Id(Main),Instance,[],Block([VarDecl(Id(a),IntType,CallExpr(Self(),Id(Method),[])),VarDecl(Id(b),IntType,FieldAccess(Id(Shape),Id($Radius))),VarDecl(Id(c),IntType,BinaryOp(+,IntLit(15413),BinaryOp(/,BinaryOp(*,IntLit(1332),IntLit(9887)),IntLit(29))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[param(Id(a),IntType)],Block([])),MethodDecl(Id(Main),Instance,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input,expect,82))
    
    # def test83(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             (a[2][3])[3][4][5] = 1;
    #             ((a[2][3])[2][3])[2] = 1;
    #             ((a[2][3])[2][3])[2][3] = 1;
    #             (Self.a)[2][3][4] = 1;
    #             (-a)[2] = 1;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(2),IntLit(3)]),[IntLit(3),IntLit(4),IntLit(5)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(2),IntLit(3)]),[IntLit(2),IntLit(3)]),[IntLit(2)]),IntLit(1)),AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(2),IntLit(3)]),[IntLit(2),IntLit(3)]),[IntLit(2),IntLit(3)]),IntLit(1)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2),IntLit(3),IntLit(4)]),IntLit(1)),AssignStmt(ArrayCell(UnaryOp(-,Id(a)),[IntLit(2)]),IntLit(1))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 83))
    
    # def test84(self):
    #     input =''' 
    #     Class Program{
    #         Destructor(){
    #             Val a,b,c:Float = (New X())[1][2][2], (1+1)[2][3], ((a[2][2])[2])[3];
    #             ((a[2])[3])[4][5] = True;
    #             ((a[2])[3])[4] = Null;
    #             a[1][2][3] = Null +1;
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([ConstDecl(Id(a),FloatType,ArrayCell(NewExpr(Id(X),[]),[IntLit(1),IntLit(2),IntLit(2)])),ConstDecl(Id(b),FloatType,ArrayCell(BinaryOp(+,IntLit(1),IntLit(1)),[IntLit(2),IntLit(3)])),ConstDecl(Id(c),FloatType,ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(2),IntLit(2)]),[IntLit(2)]),[IntLit(3)])),AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[IntLit(3)]),[IntLit(4),IntLit(5)]),BooleanLit(True)),AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(2)]),[IntLit(3)]),[IntLit(4)]),NullLiteral()),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),BinaryOp(+,NullLiteral(),IntLit(1)))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 84))
    
    # def test85(self):
    #     input =''' 
    #     Class Program{
    #         main(){
    #             (Self.a)[1][2][2] = 1+1;
    #             If(a[1][2] > 5){
    #                 Out.printLn("Hello World");
    #             }
    #             Elseif( ((a[1])[2])[3] > 5){
    #                 Out.println("Hello world");
    #             }
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2),IntLit(2)]),BinaryOp(+,IntLit(1),IntLit(1))),If(BinaryOp(>,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),IntLit(5)),Block([Call(Id(Out),Id(printLn),[StringLit(Hello World)])]),If(BinaryOp(>,ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]),[IntLit(3)]),IntLit(5)),Block([Call(Id(Out),Id(println),[StringLit(Hello world)])])))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 85))
    
    # def test86(self):
    #     input =''' 
    #     Class A{
    #         Val a,b:String = Array(Array(1,2,3), Array("Hi", "Hello", "World")), a[a[1][2]][(a[1])[2]];
    #         main(){
    #             Out.println("Hello World");
    #             Return a[1][2][3];
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,[[IntLit(1),IntLit(2),IntLit(3)],[StringLit(Hi),StringLit(Hello),StringLit(World)]])),AttributeDecl(Instance,ConstDecl(Id(b),StringType,ArrayCell(Id(a),[ArrayCell(Id(a),[IntLit(1),IntLit(2)]),ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)])]))),MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(println),[StringLit(Hello World)]),Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 86))
    
    # def test87(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             (((a[1])))[2] = 1;
    #             Out.printLn("Hello World");
    #             (!a)[0x123][0x123] = "Hello World";
    #             (-a)[1][2] = "Hi";
    #             (-a[1])[2] = "Hi";
    #             (-a[1])[2][3] = "Hi";
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]),IntLit(1)),Call(Id(Out),Id(printLn),[StringLit(Hello World)]),AssignStmt(ArrayCell(UnaryOp(!,Id(a)),[IntLit(291),IntLit(291)]),StringLit(Hello World)),AssignStmt(ArrayCell(UnaryOp(-,Id(a)),[IntLit(1),IntLit(2)]),StringLit(Hi)),AssignStmt(ArrayCell(UnaryOp(-,ArrayCell(Id(a),[IntLit(1)])),[IntLit(2)]),StringLit(Hi)),AssignStmt(ArrayCell(UnaryOp(-,ArrayCell(Id(a),[IntLit(1)])),[IntLit(2),IntLit(3)]),StringLit(Hi))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 87))
    
    # def test88(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             a[1][2] = "Hi";
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),StringLit(Hi))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 88))
    
    # def test89(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             (-a)[1]= "Hi";
    #             Out.printLn("Hello world");
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(UnaryOp(-,Id(a)),[IntLit(1)]),StringLit(Hi)),Call(Id(Out),Id(printLn),[StringLit(Hello world)])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 89))
    
    # def test90(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             a = a[1][2][3];
    #             (a)[1][2][3] = "Hi";
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),StringLit(Hi))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 90))
    
    # def test91(self):
    #     input =''' 
    #      Class A{
    #         main(){

    #         }
    #         Main(){

    #         }
    #         $Static(){
                
    #         }
    #     }

    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(Main),Instance,[],Block([])),MethodDecl(Id($Static),Static,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 91))
    
    # def test92(self):
    #     input =''' 
    #      Class A{
    #         main(){
    #             a = a+1;
    #         }
    #         Main(){
    #             c = c+1;
    #         }
    #         $Static(){
                
    #         }
    #     }

    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])),MethodDecl(Id(Main),Instance,[],Block([AssignStmt(Id(c),BinaryOp(+,Id(c),IntLit(1)))])),MethodDecl(Id($Static),Static,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 92))
    
    # def test93(self):
    #     input =''' 
    #      Class A{
    #         main(){
    #             a[1] = a[1];
    #         }
    #         Main(){
    #             b[1] = b[1];
    #         }
    #         $Static(){
                
    #         }
    #     }

    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(1)]))])),MethodDecl(Id(Main),Instance,[],Block([AssignStmt(ArrayCell(Id(b),[IntLit(1)]),ArrayCell(Id(b),[IntLit(1)]))])),MethodDecl(Id($Static),Static,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 93))
    
    # def test94(self):
    #     input =''' 
    #      Class A{
    #         main(){
    #             c[1][2] = c[1][2];
    #         }
    #         Main(){
    #             c[2][3]= Self.a;
    #         }
    #         $Static(){
                
    #         }
    #     }

    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(c),[IntLit(1),IntLit(2)]),ArrayCell(Id(c),[IntLit(1),IntLit(2)]))])),MethodDecl(Id(Main),Instance,[],Block([AssignStmt(ArrayCell(Id(c),[IntLit(2),IntLit(3)]),FieldAccess(Self(),Id(a)))])),MethodDecl(Id($Static),Static,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 94))
    
    # def test95(self):
    #     input =''' 
    #      Class A{
    #         main(){
    #             a = 1+1+1;
    #         }
    #         Main(){
    #             Foreach(I In 1 .. 100){
    #                 Out.println("Hello");
    #             }
    #         }
    #         $Static(){
                
    #         }
    #     }

    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),IntLit(1)))])),MethodDecl(Id(Main),Instance,[],Block([For(Id(I),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(println),[StringLit(Hello)])])])])),MethodDecl(Id($Static),Static,[],Block([]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 95))
    
    # def test96(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             Foreach(i In 1 .. 0B111){
    #                 Out.printLn("Hello world");
    #                 a = (a[1])[2] + 1;
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(7),IntLit(1),Block([Call(Id(Out),Id(printLn),[StringLit(Hello world)]),AssignStmt(Id(a),BinaryOp(+,ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]),IntLit(1)))])])]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 96))
    
    # def test97(self):
    #     input =''' 
    #     Class A{
    #         main(){
    #             a[1][2] = 1+1;
    #             a = a[1][2];
    #             (a[1])[2] = a[1][2];
    #             (a[1][2])[2] = a[2];
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(+,IntLit(1),IntLit(1))),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1),IntLit(2)])),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]),ArrayCell(Id(a),[IntLit(1),IntLit(2)])),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),[IntLit(2)]),ArrayCell(Id(a),[IntLit(2)]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 97))
    
    # def test98(self):
    #     input =''' 
    #     Class Program{
    #         Destructor(){
    #             a = a[1] + 2;
    #             a = a[1] ==. 2;
    #             Val a,b :String = 1,1;
    #         }
    #     }
        
    #     '''
    #     expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,ArrayCell(Id(a),[IntLit(1)]),IntLit(2))),AssignStmt(Id(a),BinaryOp(==.,ArrayCell(Id(a),[IntLit(1)]),IntLit(2))),ConstDecl(Id(a),StringType,IntLit(1)),ConstDecl(Id(b),StringType,IntLit(1))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 98))
    
    # def test99(self):
    #     input ='''
    #     Class A{
    #         main(){
    #             Out.printLn("Hello world");
    #             If( a ==. 1){
    #                 Ouit.Println("Hello world");
    #                 If(a == 1){
    #                     Out.printLn("Hello world");
    #                     a[1][2][3] = (a[1])[2][3];
    #                     ((a[1][2])[3][4])[2] = a[1][2][3];
    #                     (a[1][2][3])[2] = 1+1;

    #                 }
    #             }
    #         }
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(printLn),[StringLit(Hello world)]),If(BinaryOp(==.,Id(a),IntLit(1)),Block([Call(Id(Ouit),Id(Println),[StringLit(Hello world)]),If(BinaryOp(==,Id(a),IntLit(1)),Block([Call(Id(Out),Id(printLn),[StringLit(Hello world)]),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2),IntLit(3)])),AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2)]),[IntLit(3),IntLit(4)]),[IntLit(2)]),ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),[IntLit(2)]),BinaryOp(+,IntLit(1),IntLit(1)))]))]))]))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 99))
    
    # def test100(self):
    #     input ='''
    #     Class A{
    #         Val a,b,c:Boolean = 1%2, 1/2, 1+1;
    #         Var a,b,c:Boolean;
    #         Val a,b:String = a || b && c, 1+1;
    #     }
    #     '''
    #     expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BinaryOp(%,IntLit(1),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,BinaryOp(/,IntLit(1),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(c),BoolType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AttributeDecl(Instance,VarDecl(Id(b),BoolType)),AttributeDecl(Instance,VarDecl(Id(c),BoolType)),AttributeDecl(Instance,ConstDecl(Id(a),StringType,BinaryOp(&&,BinaryOp(||,Id(a),Id(b)),Id(c)))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,BinaryOp(+,IntLit(1),IntLit(1))))])])'''
    #     self.assertTrue(TestAST.test(input, expect, 100))

    # def test101(self):
    #     input ="""
    #     Class A{
    #         Destructor(){
    #             a = a[1] + 2;
    #         }
    #         Val a,b,c:String = 1.E-123, 1.e+123, 1.e123;
    #         Var a,b,c:String;
    #         Val a,b:String = a || b && c, 1+1;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,ArrayCell(Id(a),[IntLit(1)]),IntLit(2)))])),AttributeDecl(Instance,ConstDecl(Id(a),StringType,FloatLit(1e-123))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,FloatLit(1e+123))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,FloatLit(1e+123))),AttributeDecl(Instance,VarDecl(Id(a),StringType)),AttributeDecl(Instance,VarDecl(Id(b),StringType)),AttributeDecl(Instance,VarDecl(Id(c),StringType)),AttributeDecl(Instance,ConstDecl(Id(a),StringType,BinaryOp(&&,BinaryOp(||,Id(a),Id(b)),Id(c)))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,BinaryOp(+,IntLit(1),IntLit(1))))])])"
    #     self.assertTrue(TestAST.test(input, expect, 101))
    
    # def test102(self):
    #     input ="""
    #     Class A{
    #         Destructor(){
    #             a = (Self.a)[2];
    #             a = (Self.a)[2][3];
    #             a = ((Self.a)[2][3])[4];
    #             a = ((Self.a)[2][3])[(Self.a)[2]][(Self.a)[2]];
    #             a = ((Self.a)[2][3])[(Self.a)[2]][(Self.a)[2]][(Self.a)[2]];
    #             a = (((Self.a)[2][3])[(Self.a)[2]][(Self.a)[2]][(Self.a)[2]])[9];
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(a),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)])),AssignStmt(Id(a),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2),IntLit(3)])),AssignStmt(Id(a),ArrayCell(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2),IntLit(3)]),[IntLit(4)])),AssignStmt(Id(a),ArrayCell(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2),IntLit(3)]),[ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)]),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)])])),AssignStmt(Id(a),ArrayCell(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2),IntLit(3)]),[ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)]),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)]),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)])])),AssignStmt(Id(a),ArrayCell(ArrayCell(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2),IntLit(3)]),[ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)]),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)]),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(2)])]),[IntLit(9)]))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 102))



