print("hello world")

#basic vars 
a=2
b=3
print(a+b)
c="Hello"
d=" Carmit" 
print(c+d)

#strings
text="hello look at me" 
print(text[0:5])
print(text[5:-1])
print(text[-1])
print(text[5:])

#string from user
#slide32
name = input("Enter your name and last name: ")
namelen=len(name)
if namelen < 4:
    print("too short")
elif namelen > 9:
    print("too long")
else: 
    print("OK")
