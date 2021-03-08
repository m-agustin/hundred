from datetime import datetime

#Asks user to input their name & age
name = input("What is your name: ")
print("Your name is " + name)

age = int(input("What is you age: "))
print("Your age is " + str(age))


#Checks the current year we are on and subtracts it with the user's age and adds 100
#Determines what year the user will turn 100
hundred = str((datetime.now().year - age) + 100)

#Informs the user's results
print(name + " you will turn 100 in year " + hundred)
