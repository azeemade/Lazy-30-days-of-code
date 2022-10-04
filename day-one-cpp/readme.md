# Day 1: Bolu or Odun

## Task

Write a function that takes in a string of one word without any spaces or special character. 

 - If the string contains any special character, **print “Please remove all spaces or special characters”.** 
 - If the string passed to the function is either Bolu or Odun, **print “Welcome back, Bolu” or “Welcome back, Odun”.**
 - If the string passed is none of the two, **print “It is nice to meet you, ” concatenated with the string passed.**

## Example

BoO(“Micheal Jackson”) === “Please re# Day 1: Bolu or Odun

## Task

Write a function that takes in a string of one word without any spaces or special character. 

 - If the string contains any special character, **print “Please remove all spaces or special characters”.** 
 - If the string passed to the function is either Bolu or Odun, **print “Welcome back, Bolu” or “Welcome back, Odun”.**
 - If the string passed is none of the two, **print “It is nice to meet you, ” concatenated with the string passed.**

## Example

BoO(“Micheal Jackson”) === “Please remove all spaces or special characters”

BoO(“Micheal”) === “It is nice to meet you, Micheal”;

BoO(“Bolu”) === “Welcome back, Bolu”;

## Code Details

### Abstract
This task was developed with the C++ programming language. It performs functions such as checking if the user input is not a special character or whitespace and print the required output or throws an exception.

### Functions

 - Main function
This is the first point of call when the program is run. It asks for user input, collects input and stores it as a **str** string variable.
	> Then it uses the C++ exception keywords.The **try**  statement examines the **check function** to see if it returns **False**, itthen calls the **print function**. Else if throws an error to be executed with the **catch** statement.

 - Check function
This function ensures that the string parameter adhere to the task rules and returns a bool. 

	`str.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_") != std::string::npos`
	
	The code above has the **find_first_not_of** function which searches the **str** string for the first character that does not match the characters specified in the string.

 - Print function
This function examines the input after passing the check function and displays the required output.
 
move all spaces or special characters”

BoO(“Micheal”) === “It is nice to meet you, Micheal”;

BoO(“Bolu”) === “Welcome back, Bolu”;

## Code Details

### Abstract
This task was developed with the C++ programming language. It performs functions such as checking if the user input is not a special character or whitespace and print the required output or throws an exception.

### Functions

 - Main function
This is the first point of call when the program is run. It asks for user input, collects input and stores it as a **str** string variable.
	> Then it uses the C++ exception keywords.The **try**  statement examines the **check function** to see if it returns **False**, itthen calls the **print function**. Else if throws an error to be executed with the **catch** statement.

 - Check function
This function ensures that the string parameter adhere to the task rules and returns a bool. 

	`str.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890_") != std::string::npos`
	
	The code above has the **find_first_not_of** function which searches the **str** string for the first character that does not match the characters specified in the string.

 - Print function
This function examines the input after passing the check function and displays the required output.
 
