##################              IMPORT LIBRARY     #####################
#import math as m
from Figures import Rectangle
from Figures import Triangle


def main():
    print('##############    RECTANGLE OPERATIONS    ################')
    length = float(input('Enter Length of Rectangle: '))
    bredth = float(input('Enter Breadth of Rectangle : '))
    Rect = Rectangle(length,bredth)
    print('length rectangle = ',Rect.length)
    print('bredth rectangle =', Rect.bredth)
    rect_area = Rect.Area()
    print('Area of the Rectangle is {:.2f}'.format(rect_area))
    rect_perm = Rect.Perimater()
    print('Perimeter of Rectangle is {:.2f}'.format(rect_perm))
    print('##############    TRIANGLE OPERATIONS    ################')
    a = float(input('Enter Side a : '))
    b = float(input('Enter Side b : '))
    c = float(input('Enter Side c : '))
    tri = Triangle(a,b,c)
    print('Side a is {:.2f}\n Side b is {:.2f}\n Side c is {:.2f}'.format(tri.a, tri.b, tri.c))
    tr_area = tri.Area()
    print('Area of the given Triangle is {:.2f}'.format(tr_area))
    tr_per = tri.Perimeter()
    print('Perimeter of the given Triangle is {:.2f}'.format(tr_per))

#main()
if __name__ == '__main__':
    main()