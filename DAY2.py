#day2

#class3

str1 = "abcdefghijklmnopq"
"""
print(str1[0:5])            #print from 0 to 5
print(str1[0:35])          #print from 0 to 35 but end is at 17 but no issue
print(len(str1))             #print whole lemth
print(str1[0:10:3])        #print from 0 to 10 every third digit
print(str1[0::2])           #print from 0 to end every 2nd digit
print(str1[:5:2])           #print from start to 5 every 2md digit
print(str1[::])               #print from 0 to end every digit    as last colom is by default us 1

#negetive operations
print(str1[-5:-2])           #- indicates backward   so it start countng as q=-1 & p=-2
print(str1[::-1])               #print whole string inverted
print(str1[::-2])                #print whole string inverted with a gap of 2
print(str1[5::-1])        #count from cackward and print inverted

#other operations
print(str1.endswith("q"))           #check that it ends with q and if yes then returns true
print(str1.count("a"))                #count how many time there is a
print(str1.capitalize())               #make 1st letter capital
print(str1.find("d"))                 #fnd the letter and give its location
print(str1.upper())                    #make whole string ito upper case
print(str1.lower())                      #make whole string ito lower case
print(str1.replace("d", "r"))           
"""

#class4 lists
"""
list1 = ["ab", "ocd", "ef", "gh"]
list2 = [5, 7, 3, 8, 2]
print(list1)
print(list2)
list1.sort()
list2.sort()
print(list1)
print(list2)
list2.reverse()
print(list2)
"""
#list = [1,2,3]    elwments can be change mutable
#tuple=(1,3,2)     elements will not change immutable
#dictionary={1,2,3}


#class 5
#dictionary
"""
d1 = {"a":"apple", "b":"ball", "c":"cat"}    #simple dictonary
print(d1["a"])              #print key value of a
d2 = {"a":"apple", "b":"ball", "c":{"ca":"cat", "cu":"cut", "co":"cop"}}   #nested dictionary
print(d2["c"])               #print key value of c but it is a dictionary so print whole
print(d2["c"]["cu"])        #print dictionary's key value of "cu"
d1["d"] = "dog"             #add d:dog as a string
d1[20] = "twenty"       #add 20 as twenty in our dictionary
"""


#exercise  make a dictionary
d3 = {"a":"apple",
      "b":"ball",
      "c":"cat",
      "d":"dog",
      "e":"elephant",
      "f":"fish",
      "g":"grape",
       "h":"hen",
      "i":"icecream",
      "j":"jam",
      "k":"kite",
      "l":"light",
      "m":"mouse",
      "n":"nest",
      "o":"owl",
      "p":"pea",
      "q":"queen",
      "r":"rat",
      "s":"stem",
      "t":"toy",
      "u":"umbrella",
      "v":"van",
      "w":"wax",
      "x":"x-mas",
      "y":"yak",
      "z":"zebra"
      }
print("welcome to our dictionary")
print("enter letter you want to learn about")
i1 = input()                    #getting input as string
print("you enter", i1)
print(d3[i1])