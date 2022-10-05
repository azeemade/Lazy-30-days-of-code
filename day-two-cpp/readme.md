# Day 1: Jumping years

## Task

Write a function that takes in 2 integer parameters. 
 - The first parameter, Y, represents a year, while the second parameter, N, is the number of leap years after Y. 
 - Write a function that prints an array of the first N leap years after Y. 

## Example

LeapYear(2020,3)===[2024,2028,2032];

## Code Details

### Abstract
This task was developed with the C++ programming language. 
 - If the input year is a leap year, it increment by 4 and by the input number.
 - Else it increment by modulo and by 4 and by the input number.

### Functions

 - Main function
This is the first point of call when the program is run. It asks for year input and stores it as an **int**  variable, then ask for the number input, and stores it as an **int** also.

The modulo of the year variable is evaluated in the switch statement. The value of the switch expression is then compared to the 4 cases and the required operation is executed on the accurate case.

 - Increment function
This function loops through the number input and adds the year value to the array.

	`for(int j=0; j<num; j++)
    {
        year = year + 4;
        years.push_back(year);
    }`