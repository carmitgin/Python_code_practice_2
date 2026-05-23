#slide30
#
inputnumber = int(input("Please enter a number: "))
if inputnumber > 0:
    print("The number is positive") 
elif inputnumber < 0:
    print("The number is negative")             
elif inputnumber == 0:
    print("The number is zero")
else:
    print("Invalid input")
if int(inputnumber) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")