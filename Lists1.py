my_list=["apple","banana","cherry","apple","avocado"]
len_list=len(my_list)
print("the list length is: ", len_list)
my_list.append(str(len_list))
print(my_list)
len_list=len(my_list)
print("the list length is: ", len_list)


find_name='avi'
students=["ronen","max","shlomit","avi","boris"]
exist=0
for name in students:
    if name == find_name:
        exist=1
        break
print("exist: ", exist)