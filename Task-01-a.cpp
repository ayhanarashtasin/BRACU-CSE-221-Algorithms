#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
#ifndef ONLINE_JUDGE
freopen("input1a.txt","r",stdin);
freopen("output1a.txt","w",stdout);
#endif
int T;
cin>>T;
for(int i=0; i<T; i++){
  int n;
  cin>>n;

  if((n&1)==1){
    cout << n << " is an ODD number." << endl;
  }
  else{
    cout << n << " is an Even number." << endl;
  }
}

  return 0;
}



