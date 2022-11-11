// WEB 335 Introduction to NoSQL
// Contributors

// Richard Krasso
// Thomas James Schultz


load("users.js");

// find all users
db.users.find();

// find the email provided
db.users.find({ email: "jbach@me.com" });

// find the last name provided
db.users.find({ lastName: "Mozart" });

// find the first name provided
db.users.find({ firstName: "Richard" });

// find the employee id provided
db.users.find({ employeeId: "1010" });