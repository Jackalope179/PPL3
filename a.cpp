#include<iostream>
using namespace std;

void f(int* x) {
    x = new int[1] ;
    x[0] = 5;
}
int main ( ) {
    int *x = nullptr;
    f(x);
    cout << x[0] << endl ;
}


.aload_3
.iconst_4
.aload_1
.iconst_2
.iaload
.iload2
.icmple
.ifeq Label2

.aload_1
.iconst_1
.iaload

.iand

.Label2:
.iastore