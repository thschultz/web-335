// WEB 335 Introduction to NoSQL
// Contributors

// Richard Krasso
// Thomas James Schultz

//Load houses files
load("houses.js")

//Show Houses
db.houses.find()
//Show students
db.students.find()

//This is inserting my name to the file
db.students.insertOne({firstName: "Thomas", lastName: "Schultz", studentId: "s1018", houseId: "h1007"})

//Deleting my name
db.students.deleteOne({lastName : “Schultz"})

//Seperating the houses and showing the students within each house. 
db.houses.aggregate([{$lookup:{from: "students", localField: "houseId", foreignField: "houseId", as:"house_students"}}])

//Showing the students in the given houseID which is Gryffinhor. 
db.houses.aggregate([{$match: { "houseId": "h1007"}}, {$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "house_students"}}])

//Showing the students with the mascot Eagle. 
db.houses.aggregate([{ $match: {"mascot": "Eagle"}}, {$lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "mascot_students"}}])
