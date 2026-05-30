#Write a program with a list of words. The program will swap the last word with the first word, and then print the list
my_list = ["Apple", "Banana", "Carbon", "Dog"]
print("original list: ", my_list)           
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print("updated list: ", my_list)