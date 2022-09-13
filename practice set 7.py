"""

for i in range (1,11):
    a = i*7
    q = str(a)
    w = str(i)
    print("7 times "+ w +" = " + q )


l = ["har", "ram", "kishore"]
for item in l:
    a=item[0:1]
    if "k"==a:
        print(item)


i = 1
while i < 11 :
    a = i*7
    q = str(a)
    w = str(i)
    print("7 times "+ w +" = " + q )
    i= i+1


for i in range (2,50):
    for j in range(2, i):

        if (i%j)==0:
            a=str(i)
            print(a + " is not prime")
            break
        else:
            print(i)


n = input("enter a no")
m=int(n)
k=0
for j in range(1, m):
    k=k+j
print(k)


n = input("enter a no")
m=int(n)
k=1
for j in range(1, m+1):
    k=k*j
print(k)


n = input("enter a no")
m = int(n)
m=m+1
for i in range(1, m):
    for j in range(1, (2*m)-1):
        if (i+j) <= m:
            print(" ",end="")
        elif j>=(m+i) :
            print(" ",end="")
        elif (i+j) > m:
            print("*",end="")

    print("\r")


l = input("write a no :")
n = int(l)
for i in range (10,0,-1):
    a = i*n
    c = str(n)
    q = str(a)
    w = str(i)
    print(c +" times "+ w +" = " + q )


"""


