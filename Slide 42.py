#slide42
#Write a program that receives a string from the user.
#The program should check how many times the letter 'h' appears.
#If the letter appears at least 2 times, the program will print "ok".
text = input("Please enter a string: ")
h_count = text.count('h')
if h_count >= 2:
    print("ok")
else:
    print("The letter 'h' appears less than 2 times")   