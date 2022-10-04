#include <iostream>
#include <string>

bool check(std::string& str)
{
    if(str.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_") != std::string::npos)
    {
        return true;
    }
}

void print(std::string& str)
{
	if(str == "Bolu" || str == "Odun")
    {
    	std::cout << "Welcome back " << str;
    }
    else
    {
    	std::cout << "It is nice to meet you " << str;
    }
}


int main() {
	std::string str;
    
 	std::cout << "Enter a word: ";
    getline(std::cin, str);

    try {
        if(!check(str))
        {
            print(str); 
        }
        else
        {
            throw 500;
        }
    }
    catch (...) {
        std::cout << "Please remove all spaces or special characters";
    }
    
  	return 0;
}