# Day 9: Mongo way

## Task

Setup mongoDB for your project. Create a local mongo instance, and a user collection to store the user data. Create an endpoint “/popopulate”, such that when it is accessed via GET, all the data in your JSON file or anyform of persistence formerly used is migrated to the database per user. All other routes from the previous task still apply.

## Code Details

### Abstract

This task was developed with the flask framework of the python programming language and the mongodb.
- The MongoClient reads the database url along with the port. Then the users collection is created.
- When the **/populate** endpoint is called, using the GET method, the users collection is seeded from the json API.

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

-Add function
This function uses the **insert_one** keyword to add new a user object to the collection through user request.
