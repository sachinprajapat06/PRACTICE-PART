# practice set 4

def f1():
    a = input("enter subject marks ")
    s.add(a)
    print("updated list :")
    print(s)
    f2()

def f2():
    answer = input("do you wanna enter more? please answer yes or no")
    if answer == "yes":
        f1()
    elif answer == "no":
        print("thank you")
        print(sum(s))
    else:
        print("please enter a valid input!")
        f2()

s = {0}

print(s)
print("here you can store your marks like this : eg: 45")
f1()
f2()