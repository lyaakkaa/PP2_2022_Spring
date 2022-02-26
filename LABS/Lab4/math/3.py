

from math import tan,floor,pi
n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
s =floor(n*a**2/(4*tan(pi/n)))
print(f'The area of the polygon is: {s}')



