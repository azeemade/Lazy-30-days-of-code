#include <iostream>

int main() {
    int prv1 = 0, prv2 = 1, i = 2, nxt;
    
    std::cout << prv1 << " " << prv2 << " ";
    while(i < 99)
    {
        nxt = prv1 + prv2;
        std::cout << nxt << " ";
        
        prv1 = prv2;
        prv2 = nxt;
        ++i;
    }

  	return 0;  
}
