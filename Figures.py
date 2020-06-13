from math import sqrt
###################     CLASS RECTANGLE      ####################
class Rectangle :
    def __init__(self,length, bredth):
        self.length = length
        self.bredth = bredth

    def Area(self):
        A = self.length * self.bredth
        return A

    def Perimater(self):
        P = (self.length + self.bredth) * 2
        return P
####################################################################
################         CLASS  TRIANGLE         ###################
class Triangle :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def Perimeter(self):
        P = self.a + self.b + self.c
        return P

    def Area(self):
        s = self.Perimeter() / 2
        A = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return A
###################################################################
