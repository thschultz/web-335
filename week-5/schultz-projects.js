// WEB 335 Introduction to NoSQL
// Contributors

// Richard Krasso
// Thomas James Schultz


load("users.js");

// find all users
db.users.find();

//This was to add another user to the user collection.
db.users.insert( { "_id": ObjectId("6373bff85800873e77f12e88"), "firstName" : "Thomas", "lastName" : "Schultz", "employeeId" : "1013", "email" : "tj@gmail.com", "dateCreated" : ISODate("2022-11-15T16:36:08.487Z")} )

//This updated the email provided
db.users.update({ "email" : "wmozart@me.com"},{$set:{"email" : "mozart@me.com"}})

//This was to display only the projections provided.
db.users.find({},{_id:0, "firstName":1, "lastName":1, "email":1, })
