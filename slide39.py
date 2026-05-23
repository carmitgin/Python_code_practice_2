#Slide 39
#Write a program that receives a POSITIVE NUMBER.
#the program will print numbers from 1 to the number received.
number = int(input("Please enter a positive number: "))
if number > 0:
    for i in range(1, number + 1):
        print(i)
else:
    print("Please enter a positive number")
    