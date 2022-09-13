"""
class employee:
    company = "microsoft"
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year

    def getinfo(self):
        print(f"name of the person is {self.name} his position is {self.position} and he joined {self.year} ago")

google = employee("google", "ceo", "9")
facebook = employee("facebook", "junior", "2")
microsoft = employee("microsoft", "senior", "4")

google.getinfo()
facebook.getinfo()
microsoft.getinfo()


class num:
    def __init__(self, n):
        n = int(input("print enter your number :"))
        m = n**2
        o = n**3
        p = n**0.5
        print(f"Square of the number is {m} \nCube is this {o} \nSquare root is this {p} ")
    @staticmethod
    def greet():
        print("welcome to our calculator")
a = num(0)
a.greet()
"""


class train:
    catogry = "indian railways"
    def __init__(self, name, fair, seat):
        self.name = name
        self.fair = fair
        self.seat = seat
    @staticmethod
    def train_detail():
        x = int(input("please choose your train number :"))
        if x == 1:
            a.getinfo()
        elif x == 2:
            b.getinfo()
        elif x == 3:
            c.getinfo()
        else:
            print("Choose a correct parameter")
            train.train_detail()
    @staticmethod
    def discount_detail():
        m = int(input("Enter your fair :"))
        l = int(input("Select your type  \n1. genral\n2. student\n3. old\n4. child\n5. ladies\n :"))
        if (l == 1):
            print(f"you get no discount\nYour final is {m}")
        elif (l == 2):
            print(f"you get 50% off\nYour final is {m / 2}")
        elif (l == 3):
            print(f"you get 50% off\nYour final is {m / 2}")
        elif (l == 4):
            print(f"you get 30% off\nYour final is {3 * m / 10}")
        elif (l == 5):
            print(f"you get 30% off\nYour final is {3 * m / 10}")
        else:
            print("Choose a correct perameter!")
            train.discount_detail()
    def names(self):
        print(f"Name : {self.name}")
    def getinfo(self):
        print(f"Name : {self.name} \nFair is : {self.fair} \nSeats avilable : {self.seat} ")

print("welcome to indaian railways")
print("Total 3 trains are avilable")

a = train("1. Rajdhani", "8000", "50")
b = train("2. Garib rath", "10000", "40")
c = train("3. Rajhans", "15000", "20")
a.names()
b.names()
c.names()
train.train_detail()
train.discount_detail()











