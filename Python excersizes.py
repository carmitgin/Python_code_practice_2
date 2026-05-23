#slide15
# Write a program that creates 3 variables according to 3 people:
#the variable name will be the first name, and the value will be the age (integer only).
#The program will store the average age in a new variable and then print it.
#
name1 = input("1st person please enter your first name: ")
age1 = input("1st person please enter your age: ")
name2 = input("2nd person please enter your first name: ")
age2 = input("2nd person please enter your age: ")
name3 = input("3rd person please enter your first name: ")
age3 = input("3rd person please enter your age: ")
ages= [int(age1), int(age2), int(age3)]
avg_age= [sum(ages)/len(ages)]
print("ages are:", name1, "-" , str(age1), name2, "-" , str(age2), name3, "-" , str(age3),)
print("avg age is: ", avg_age)


#slide 22
#Input a string, type first, last , middle letters
name1 = input("1st person please enter your first name: ")
print(name1 [0])