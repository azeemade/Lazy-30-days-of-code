# Day 10: MongoDB Simple User API

## Task

Setup mongoDB for your project. Create a local mongo instance, and a user collection to store the user data. Create an endpoint “/popopulate”, such that when it is accessed via GET, all the data in your JSON file or anyform of persistence formerly used is migrated to the database per user. All other routes from the previous task still apply.

- Create an endpoint, “/login” that takes in data via POST in the form
    `{
        "username": "username",
        "email": "email"
    }`
 - If the data matches the data in the database, a session is created and the user is redirect the user to the “/status” route which when a user logs in, return a JSON response in the form 
    `{
        “Message”:”you are logged in”
    }`
 - If an unauthenticated user visits the “/status” endpoint, it return a JSON response in the form 
    `{
        “Message”:”please login”

    }`


## Code Details

### Abstract

This task was developed with the flask framework of the python programming language and the mongodb.
- The MongoClient reads the database url along with the port. Then the users collection is created.
- When the **/login** endpoint is called, using the POST method,the necessary action is performed either by printing error message or creating session.

### Functions

- Populate function
  This function accesses the **dict** variable and tloops the required keys and value into the users collection using **insert_many** keyword.

- Index function
  This function return all for the users in the collection using the GET method.

- Get function
  This function accept a query parameter which can be name, username or email. If the parameter does not match the user keys, _User not found_ is returned else the user object is returned.

- Delete function
  This function gets all the users in the collection along with its size. Then the **delete_one** keyword is used to delete the last user object.

- DeleteAll function
  This function clears all the objects in the collection by looping through the collection using **delete_one**  and returns empty array.

- Add function
This function uses the **insert_one** keyword to add new a user object to the collection through user request.

- Login function
This function loops through the users collection and finds the object that matches the one provided. The statement
    `len(list(result))`
convert the result of type **Cursor** to python list and then finds the length. If the lengtht is 0, that is, the object is not found in the collection, an error message is returned. Else, the result is stored as a session of variable user and redirected to the **/status** route.

- Status function
This function returns a message after successful login by checking if the user variable exist in session. Else, it returns an error message.