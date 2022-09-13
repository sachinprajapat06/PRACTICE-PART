class Company:
    place = "earth"

    def __init__(self, name, build, place):
        self.name = name
        self.build = build
        self.place = place
        self.brics = 500000
        self.cement = 3000
        self.iron = 50000
        print(f"company is {self.name} and its build is {self.build} and it is sicuated at {self.place}")
    #def getsallery(self):
        #print(f"sallery of the company is {self.sallery}")

c1 = Company("google", "2000", "India")
c2 = Company("facebook", "2002", "china")
c3 = Company("microsoft", "2005", "nepal")

google = Company("google", "2000", "bihar")
facebook = Company("facebook", "2002", "china")
microsoft = Company("microsoft", "2005", "nepal")

print(google.place)       #it will first check instance attribute then move it to class attributes

"""
google.sallery = "50000"     #creating instance attribures for google
google.build = "2000"
google.place = "India"

facebook.sallery = "40000"     #creating instance attribures for facebook
facebook.build = "2003"
facebook.place = "china"

microsoft.sallery = "30000"     #creating instance attribures for microsft
microsoft.build = "2005"
microsoft.place = "nepal"
"""
