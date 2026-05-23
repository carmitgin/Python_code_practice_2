##Slide26B
##
texttocheck = input("Please enter any word: ")
if texttocheck[0] == "A":
    texttocheck = "a" + texttocheck[1:]
    print(texttocheck)
else:
    print("The word does not start with A")