# WEB 335 Introduction to NoSQL
# Contributors

# Richard Krasso
# Thomas James Schultz

# import the MongoClient 
from pymongo import MongoClient

# build a connection to MongoDB 
client = MongoClient("mongodb+srv://web335User:s3cret@web335db.mtckmhy.mongodb.net/testretryWrites=true&w=majority")

# configure a variable to access web335DB
db = client['test']

# create a new user document
newUserDoc = {
    "firstName": "James",
    "lastName": "Bond",
    "employeeId": "2007",
    "email": "jbond007@gmail.com",
    "dateCreated": datetime.utcnow()
}

# insert new user into database
db.users.insert_one(newUserDoc)

# display new user
print(db.users.find_one( { "employeeId": "2007" } ))

# update email address
db.users.update_one(
    { "employeeId": "2007" },
    {    "$set": {
            "email": "jbond007@aol.com"
        }
    }
)

# display user 
print(db.users.find_one( { "employeeId": "2007" } ))

# delete newly created document
db.users.delete_one( { "employeeId": "2007" } )

# display that user no longer exists
print(db.users.find_one( { "employeeId": "2007" } ))