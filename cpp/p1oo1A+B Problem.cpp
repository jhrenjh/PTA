//#define LOCAL
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;
int n,m;
int a[100000];
int main(){
    #ifdef LOCAL
        freopen("data.in","r",stdin);
        freopen("data.out","w",stdout);
    #endif
    ios::sync_with_stdio(false);
    int a,b;
    cin>>a>>b;
    cout<<a+b;
    return 0;
}