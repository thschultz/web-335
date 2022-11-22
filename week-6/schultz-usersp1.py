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

# print all documents in users collection
for user in db.users.find():
    print(user)

# print user document with employeeId equal to 1011
print(db.users.find_one( { "employeeId": "1011" } ))  

# print user document with lastName Mozart
print(db.users.find_one( { "lastName": "Mozart" } ))