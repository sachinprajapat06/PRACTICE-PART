"""
def m(num1,num2,num3):
    if (num1 > num2):
        if (num1 > num3):
            print(f'{num1} is the greatest')
        else:
            print(f'{num3} is the greatest')
    elif (num2 > num3):
        print(f'{num2} is the greatest')
    else:
        print(f'{num3} is the greatest')
a = m(230,88,62)


def conv(c):
    f = c * 1.8 + 32
    print(f'{c} degree celcius is equal to {f} degree faranheite ')

a = conv(45)


print("hello", end=" ")
print("hello", end=" ")
print("hello", end=" ")
print("hello", end=" ")



def s(n):
    if (n==1):
        return 1
    else:
        return n + s(n - 1)

a = s(6)
print(f' your sum is {a}')



def s(n):
    for n in range(n,0,-1):
        print(" ")
        for n in range(n,0,-1):
            print("*", end="")

a = s(5)



def f(string,word):
    b = string.replace(word," ")
    print(b)
a = "hey how are you sachin"
word = "sachin"
f(a,word)


def f1(n):
    for i in range(0, 11):
        a = i * n
        c = str(n)
        q = str(a)
        w = str(i)
        print(c + " times " + w + " = " + q)

l = input("write a no :")
n = int(l)
f1(n)

"""


