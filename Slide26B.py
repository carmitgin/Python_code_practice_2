##Slide26B
##"Write a program that receives a string.
##The program checks whether its first character is 'A'.
##If so, it changes it to 'a' and prints it."
texttocheck = input("Please enter any word: ")
if texttocheck[0] == "A":
    texttocheck = "a" + texttocheck[1:]
    print(texttocheck)
else:
    print("The word does not start with A")