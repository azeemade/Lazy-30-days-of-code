# Day 6: Simple User API

## Task

Without using a database, retrieve user data for only “id”, “name”, “Username”, “email” from the api below and store it on your server it must be persistent, therefore i recommend JSON.
[jsonplaceholder](http://jsonplaceholder.typicode.com/users)

- Create an api such that when the "/users" endpoint is accessed, an array containing all the user objects is the response.
- When the route with the name of any of the object keys in the array of objects is accessed, like "/name" or "/username" or "/email" is accessed, respond with an array of all the corresponding properties of the array of user objects.
- When the route “/delete” is accessed, the last object in the array is deleted.
- When the route “/deleteall” is accessed, let all the objects in the array be deleted
- A new user object can be added to the array via post request on the route “/newuser”. The expected data is
  `{ "name": "name", "username": "username", "email": "email" }`
  The id would be automatically generated.

## Code Details

### Abstract

This task was developed with the flask framework of the python programming language.

- When the **/users** endpoint is called, the response is users objects with name, username, id and email.
- When the **/query** endpoint is called, the response is the user object that matches the query parameter.
- When the **/delete** endpoint is called, the response is the array of users except the last object.
- When the **/deleteall** endpoint is called, the response is an empty array with all the user objecs deleted.
- When the **/newuser** endpoint is called with request data, a new object is added to the array.

### Functions

- The given url is read and then stored in the **dict** variable which is then accessed throughout the script.

- All function
  This function accesses the **dict** variable and the extract the reuired keys and values and append them to the users array and returns it.

- Index function
  This function return all for the **/users** route using the GET method.

- Get function
  This function accept a query parameter which can be name, username or email. If the parameter does not match the user keys, _User not found_ is returned else the user object is returned.

- Delete function
  This function pops the last object in the array and returns the new array.

- DeleteAll function
  This function clears all the objects in the array and returns empty array.

- Add function
This function appends new user object to array and increments the id by 1.
