# Day 4: Simple validator

## Task

Write a function that takes in 2 strings. The first one is the email address, the second one is the password and returns an object specified below.

 - Verify that the email adress is valid. If valid, create an object with property "email" and assign as true else, assign as false. 
 - For the password verify that it has at least one Uppercase letter, at least one lowercase letter, at least one non-alphanumeric character, at least one number and at least 8 character long. if the password is valid, let the object have property "password" assigned to true else, false.

## Example

`validate("akinwandeakiboluwarin@gmail.com","YOucan'tgetmyPassword2")==={
                                                                            email: true,
                                                                            Password:true
                                                                        }`


`validate("ichigokurosaki@gmail.com","getsugaTensho")==={
                                                            email: true,
                                                            Password:false
                                                        }`

`validate("ichigokurosakigmail.com","getsugaTensho")==={
                                                            email: false,
                                                            Password:false
                                                        }`


## Code Details

### Abstract
This task was developed with the C++ programming language. 
 - The input email is passed into the **validateEmail** function.If the input matches the specified pattern *true* is stored else *false*.
 - The input password is passed into the **validatePassword** function.If the input matches the specified pattern *true* is stored else *false*.

### Functions
 - Credentials struct
This stores collection of string email and string password which can be used in the code.

 - Main function
This is the first point of call when the program is run. It asks for email input and stores it as an *string*  variable, then ask for the password input, and stores it as an *string* also.

Then each of this inputs are passed into their corresponding functions.

 - validateEmail function
This function has a regex variable e with the required email pattern. If the input email  matches the regex variable it stores *true* in the struct variable email  else *false*.

	`regex e("^[A-Za-z0-9+_.-]+@(.+)$")`

 - validatePassword function
This function has a regex variable p with the required password pattern. If the input password  matches the regex variable it stores *true* in the struct variable password  else *false*.

    `regex p("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\]).{8,32}$")`