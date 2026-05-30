#slide 22
#Input a string, type first, last , middle letters
from ast import If


name1 = input("1st person please enter your first name: ")
print(name1 [0])
print(name1[-1])
letter_number=len(name1)//2
print(name1[letter_number])

##2. Input a string with a length of at least 5 characters:
#a. Cut it so the result is from the third character to the last.
#b. Print the length of the string.
#c. Replace all spaces with -.
name2 = input("Please enter a string with a length of at least 5 characters: ")
if len(name2) < 5:
    print("too short")
else:
    print(name2[2:])
    print("length of name: ", len(name2))
    print(name2.replace(" ", "-"))

##Slide26A
##Write a program that receives a number from the user.
#The program will print whether the number is positive or negative
number = int(input("Please enter a number: "))
if number > 0:
    print("The number is positive")         
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
    
