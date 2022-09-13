
#lcm of 3 no

"""
a = int(input("please enter your first no :"))
b = int(input("please enter your second no :"))
c = int(input("please enter your third no :"))

lar = max(a, b, c)
while True:
    if ( lar%a==0 and lar%b==0 and lar%c==0 ):
        l = str(lar)
        print("the lcm is :" + l)
        break
    lar = lar+1



#hcf of 3 no


a = int(input("please enter your first no :"))
b = int(input("please enter your second no :"))
c = int(input("please enter your third no :"))

lar = min(a, b, c)
while True:
    if ( a%lar==0 and b%lar==0 and c%lar==0 ):
        l = str(lar)
        print("the hcm is :" + l)
        break
    lar = lar-1



#factorial of n

def fac(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fac(num-1)

num = int(input("please enter a number :\n"))
f = fac(num)
print(f"the factorial of {num} is {f}")

#trailing no of zeros
count = 0
for num in range(num,0,-1):
    if num % 625 == 0:
        count += 4
    elif num % 125 == 0:
        count += 3
    elif num % 25 == 0:
        count += 2
    elif num % 5 == 0:
        count += 1
print(f"the no of zeros are {count}")

"""



