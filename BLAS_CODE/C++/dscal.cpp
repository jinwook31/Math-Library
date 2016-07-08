#include <cstdlib>
#include <vector>
#include <iostream>
 
extern "C"
{
       #include <cblas.h>
}
 
using namespace std;
int main ()
{
  int i;
  vector<double> x(3,1);
 
  cblas_dscal (x.size(), 4.323, &x[0], 1);
 
  for (i = 0; i < x.size(); ++i)
    cout << x[i] << endl;
  return 0;
}
