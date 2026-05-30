my_list = []
i1=input("enter a number (positive or negative): ")
my_list.append(i1)
i2=input("enter a number (positive or negative): ")
my_list.append(i2)
i3=input("enter a number (positive or negative): ")
my_list.append(i3)
i4=input("enter a number (positive or negative): ")
my_list.append(i4)
#print("the created list is: ", my_list)
for i in my_list:
    if int(i) < 0:
        print("the negative number is: ", i)


