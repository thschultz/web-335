# WEB 335 Introduction to NoSQL
# Contributors

# Richard Krasso
# Thomas James Schultz

#Hobbies list
hobbies = ["photography", "golf", "movies", "cycling", "hiking"]
#For loop to print my hobbies
for x in hobbies:
  #print x
  print(x)


#Days list
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Days for loop
for day in days:
  #if statement for Sunday and Sunday, printing to enjoy your days with hobbies
  if day == "Sunday" or day =="Saturday":
    print( day + ": You are off and should enjoy your hobbies. Enjoy a beer.")
  #else statement with the statement telling you have to work.   
  else:
    print(day + ": Boo! You have to work today.")