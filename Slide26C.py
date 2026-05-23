##slide 26
# write a program that receives an email address from the user.
#if the email address is shorter than 4 characters, it will print ERROR.
#if the first or last character of the address is '@', it will print ERROR."
email = input("Please enter your email address: ")
if len(email) < 4:
    print("ERROR")
elif email[0] == "@" or email[-1] == "@":
    print("ERROR")
else:
    print("Valid email address")    