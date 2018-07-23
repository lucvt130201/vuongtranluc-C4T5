a = int(input("value of a ?"))
b = int(input("value of b ?"))
c = int(input("value of c ?"))

delta = b*b - 4*a*c

delta_sqrt = delta**0.5

g = -b + delta_sqrt
h = -b - delta_sqrt

x1 = 0.5 * a * g
x2 = 0.5 * a * h

print("x1="x1,"x2=" x2)

