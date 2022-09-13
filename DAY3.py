#DAY 3
#set as data type
"""
s1 = {1,2,3,4}   #initialise a set
#now we can do many operations like delete append add and many other with sets
s1.add(8)  #add 8 in set 1
print (s1)
s2 = {3,4,5,6}
print (s2)
s1.add(2)
"""

#ifelse
"""
print("Do you want to test! please enter yes or no")
i2 = input()
if  (i2 == "y" or i2 == "Y"  or i2 == "yes" or i2 == "Yes" or i2 == "YES"):
    #checking condition
    print("Thank you") #true then execute
elif (i2 == "n" or i2 == "N"  or i2 == "no" or i2 == "NO" or i2 == "No"):
    print("Sad to listen! But thank you and visit again")
else:
    print("please enter a valid input")
"""

#for loops
"""
list2 = [5, 7, 3, 8, 2, "abs", "ram"]
for item in list2:
    if str(item).isnumeric() and item<=7:
        print(item)
    elif str(item).isnumeric():
        print("that was a different data type")
    elif str(item).isnumeric() and item>7:
        print(item)
"""


#while loop with break and continue
"""
i = 0    #initialising value of i
while(True):  #while loop for infinity
    if i<=5:        #if i is smaller then 5 only then
        i=i+1
        continue    #continue printing otherwise go back
    print(i)
    if(i==20):       #if i=20 so stop the loop here
        break
    i=i+1
    """
