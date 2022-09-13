class vec2d():

    def __init__(self,i ,j):
        self.i = i
        self.j = j
    @staticmethod
    def pr():
        print(f"{i}i, {j}j")

class vec3d(vec2d):

    def __init__(self,i ,j ,k):
        super().__init__(i,j)
        self.k = k
    def pr(self):
        print(f"{self.i}i, {self.j}j, {self.k}k")


vec2d(1, 2)
vec3d(3, 4, 5)
vec2d.pr()
vec3d.pr()
