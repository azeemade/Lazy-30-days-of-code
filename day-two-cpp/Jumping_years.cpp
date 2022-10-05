#include <iostream>
#include <string>
#include <vector>

void increment(int year, int num, std::vector<int>& years)
{
    for(int j=0; j<num; j++)
    {
        year = year + 4;
        years.push_back(year);
    }
}

int main() {
	int year, num;
	std::vector<int> years;
    
 	std::cout << "Enter a year: ";
    std::cin >> year;
    
    std::cout << "Enter the number leap years: ";
    std::cin >> num;
    
    switch(year % 4){
        case 0:
            increment(year, num, years);
            break;
        case 1: 
            years.push_back(year = year + 3);
            increment(year, num-1, years);
            break;
        case 2: 
            years.push_back(year = year + 2);
            increment(year, num-1, years);
            break;
        case 3: 
            years.push_back(year = year + 1);
            increment(year, num-1, years);
            break;
    }
    
    std::cout << "[";
    for (int i : years)
        std::cout << i << ",";
    std::cout << "]";
    
  	return 0;
}

