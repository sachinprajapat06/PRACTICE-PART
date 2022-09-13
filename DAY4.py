#day 4

# Operators In Pythons
"""
#Arithmetic Operators
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 ** 3 is ", 5**3)
print("5 % 5 is ", 5%5)
print("15 // 6 is ", 15//6)

# Assignment Operators
print("Assignment Operators")
x = 5
print(x)
x %=7 # x = x%7
print(x)

# Comparison Operators
i = 5

# Logical Operators
a = True
b = False

# Identity Operators
# print(5 is not 5)

# Membership Operators
list = [3, 3,2, 2,39, 33, 35,32]
# print(324 not in list)

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2)
print(0 | 3)
 """

#SHORT IFELSE
"""
a = int(input("enter a\n"))
b = int(input("enter b\n"))
print("B IS GREATER") if a<b else print("A IS GREATER")
"""

#funtions
"""
a = 9
b = 8
c = sum((a, b)) # built in function
def function1(a, b):
    print("Hello you are in function 1", a+b)

def function2(a, b):
    This is a function which will calculate average of two numbers 
    this function doesnt work for three numbers
    this parragraph came under a multiline comment for ex (""" """)
    average = (a+b)/2
    # print(average)
    return average

v = function2(5, 7)
print(v)
print(function2.__doc__)
#Docstrings
#a brief knowledge about the functionality of the function. _doc_
"""

#Try Except Exception Handling In Python
"""
print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try:
    print("The sum of these two numbers is",
          int(num1)+int(num2))
except Exception as e:
    print(e)
    
print("This line is very important")
"""

#Python File IO Basics

"""
Modes of opening file in Python:
There are many modes of opening a file in Python, unlike other languages Python has provided its users a variety of options. We will discuss seven of them in this tutorial.

r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string.
b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include images, documents, or all other files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file.
"""

#Open(), Read() & Readline() For Reading File
"""
f = open("harry.txt", "rt")
print(f.readlines()) 
print(f.readline())

content = f.read()
for line in f:
    print(line, end="")
print(content)
content = f.read(34455)
print("1", content)
content = f.read(34455)
print("2", content)
f.close()
"""

#Writing And Appending To A File

"""
#write
f = open("harry.txt", "w")
a = f.write("Harry bhai bahut achhe hain\n")
print(a)
f.close()

#append
f = open("harry2.txt", "a")
a = f.write("Harry bhai bahut achhe hain\n")
print(a)
f.close()

# Handle read and write both
f = open("harry2.txt", "r+")
print(f.read())
f.write("thank you")
"""


