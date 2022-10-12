# Day 5: First Time Up

## Task

Write and deploy a script to any hosting service of your choice. It must have the following end points. 
 - “/port” when this is accessed, a string response of “The script is running on [port]”, with the appropriate response header must be sent. 
 - If the endpoint accessed is “/fibonacci” is accessed, an array of the first 100 fibonacci numbers is sent as a string response.


## Code Details

### Abstract
This task was developed with the flask framework of the python programming language. 
 - By visiting the **/port** url, a web page displaying the app port is shown.
 - When the **/fibonacci** url is visited, a list of 100 fibonacci numbers are dislayed.

### Functions
 - Index function
 This is the first page displayed when the app starts running. The has a **/** route and **/port** route. This function return an HTML heading tag along with the present app port.

 - Fibonacci function
 This function return an array of the first 100 fibonacci numbers by looping between 2 and 98 to add the numbers which meet the specified operations to the array.