#include <iostream>
#include <string>
#include <regex>
using namespace std;

struct Credentials {
    string email;
    string password;
};

void validateEmail(Credentials &cred, string email){
    regex e("^[A-Za-z0-9+_.-]+@(.+)$");

    if(regex_match(email, e)){
        cred.email = true;
    }
    else{
        cred.email = false;
    }
}

void validatePassword(Credentials &cred, string password){
    regex p("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$");

    if(regex_match(password, p)){
        cred.password = true;
    }
    else{
        cred.password = false;
    }
}

int main() {
	string email, password;
    Credentials cred;

 	cout << "Enter a email: ";
    cin >> email;
    
    cout << "Enter a password: ";
    cin >> password;
    
    validateEmail(cred, email);
    validatePassword(cred, password);

  	return 0;
}

