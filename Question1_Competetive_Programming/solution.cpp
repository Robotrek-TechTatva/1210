#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

int main() {
    // your code goes
    int n;
    cin>>n;
    vector <int> h(n+1);
    int x=0;
    int i,j,c=0;
    for(i=2;i<((int)pow(n,0.5));i++)
    {
        for(j=2; j<((int)pow(n,0.33));j++)

        {
            //cout<<i<<" "<<j<<endl;
            x = pow(i,2)*pow(j,3);
            if(x<n)
            {
                if(h[x]==0){
                    c++;
                    h[x]=1;
                }
            }
        }
    }
    cout<<c;
    return 0;
}