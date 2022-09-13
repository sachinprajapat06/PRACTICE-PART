"""
print("this is a game here you can enter 4 no and i will tell you thr greatest among them")
a = input("your first no:")
b = input("your second no:")
c = input("your third no:")
d = input("your fourth no:")
if a > b and a > c and a > d:
    print("a is the greatest")
if b > a and b > c and b > d:
    print("b is the greatest")
if c > b and c > a and c > d:
    print("c is the greatest")
if d > b and d > c and d > a:
    print("d is the greatest")


print("here i will tell you that you are pass or not")
a = input("your first no:")
b = input("your second no:")
c = input("your third no:")
if int(a) > 33 and int(b) > 33 and int(c) < 33:
    print("you are fail in your third subject")
if int(a) > 33 and int(b) < 33 and int(c) > 33:
    print("you are fail in your second subject")
if int(a) < 33 and int(b) > 33 and int(c) > 33:
    print("you are fail in your first subject")
d = (int(a)+int(b)+int(c))/3
if int(a) > 33 and int(b) > 33 and int(c) > 33 and int(d) > 40:
    print("you are pass with" + d + "% marks")
if int(a) > 33 and int(b) > 33 and int(c) > 33 and int(d) < 40:
    print("you are pass in subjects but fail overall")


comment = input("please enter your comment")
a = comment.find("buy now")
b = comment.find("subscribe me")
c = comment.find("please like")
print(a)
print(b)
print(c)
if a == -1 and b == -1 and c == -1:
    print("your comment is good")
else :
    print("your commment is spam it contain spam words")


user = input("please enter your username :")
a = len(user)
print(a)
if a < 10:
    print("your username is not valid")
else:
    print("ok")


platforms = ["netflix", "amazon", "alt balaji", "hulu", "tvf", "tsp"]
find = input("please enter the platform name you want :")
a = platforms.index(find)
if a > 0:
    a = a+1
    d = str(a)
    print("the platform services are on at no" + d)


print("please enter your marks line wise  :")
m = input("maths:")
h = input("hindi:")
e = input("english:")
sc = input("science:")
ss = input("sst:")
c = input("computer:")
tot = int(m)+int(h)+int(e)+int(ss)+int(sc)+int(c)
per = tot/6
p = str(per)
print("your % marks are :" + p)
if per>90:
    print("you get an excellent grade ")
elif per>80:
    print("you get an 'A' grade ")
elif per>70:
    print("you get an 'b+' grade ")
elif per>60:
    print("you get an 'b' grade ")
elif per>50:
    print("you get an 'c+' grade ")
elif per>40:
    print("you get an 'c' grade ")
elif per<33:
    print("you get an 'f' grade and you are fail ")

"""










