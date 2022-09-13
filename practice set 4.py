# practice set 4

def f1():
    a = input("enter subject marks ")
    l1.append(int(a))
    print("updated list :")
    print(l1)
    f2()

def f2():
    answer = input("do you wanna enter more? please answer yes or no")
    if answer == "yes":
        f1()
    elif answer == "no":
        print("thank you")
        print(sum(l1))
    else:
        print("please enter a valid input!")
        f2()

l1 = []
print(l1)
print("here you can store your marks like this : eg: 45")
f1()
f2()
