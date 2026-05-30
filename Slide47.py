# Write a program that contains a list of numbers.
# The program will print the first and last elements.

# After that, the program will assign the length of the list to a new variable.
# Finally, the program will add the length of the list as the last element and print the list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("first element: ", my_list[0])
print("last element: ", my_list[-1])
length = len(my_list)
my_list.append(length)
print("updated list: ", my_list)
print("last element: ", my_list[-1])
