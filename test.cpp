#include<bits/stdc++.h>
using namespace std;
int n,m;
void ql(string str,int k)
{
    if(str.size()==m)
    {
        cout<<str<<" ";
        return;
    }
    for(int i=k;i<=n;i++)
    {
        string tmp=str;
        str+= to_string(i);
        ql(str,i+1);
        str=tmp;
    }
}
main()
{
    cin>>n>>m;
    ql("",1);
}