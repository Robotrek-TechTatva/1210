
#include <iostream>


bool isBouncy(unsigned long long x)
{

  bool ascending  = true;
  bool descending = true;

  
  auto previous = x % 10;
  x /= 10;

  
  while (x > 0)
  {
    
    auto current = x % 10;

    
    descending &= previous >= current;
    ascending  &= previous <= current;

    
    if (!ascending && !descending)
      return true;

    
    x /= 10;
    previous = current;
  }

  
  return false;
}


int main()
{
  unsigned int tests = 1;
  std::cin >> tests;

  while (tests--)
  {
    
    unsigned long long p =  99;
    unsigned long long q = 100;
    std::cin >> p >> q;

    
    unsigned long long current   = 100; 
    unsigned long long numBouncy =   0;
    do
    {
      
      current++;
      if (isBouncy(current))
        numBouncy++;
    } while (numBouncy * q < current * p); 

   
    std::cout << current << std::endl;
  }

  return 0;
}
