#include<iostream>
using namespace std;
class A{
    public:
    int a = 1;
    void a(){
        cout << "A::a()" << endl;
    }
};

main(){
    A obj;
    cout << obj.a << endl;
}