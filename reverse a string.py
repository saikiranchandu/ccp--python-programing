my_str = input("Please enter your own string : ")
str = ''
for i in my_str:
    str = i + str
print("\nThe Original String is: ", my_str)
print("The Reversed string is: ", str)
