a =  int(input( "a="))
b = int(input("b= "))
c = int(input("c= "))

delta = b*b - 4*a*c
delta_sqrt = delta ** 0.5

if delta < 0 :
    print("no solution")

elif delta == 0 :
    x1 = 0.5 * (-b) * (2*a)
    print("x1 = x2 = ", x1)

else :
    x1 = 0.5 * a * (-b + delta_sqrt)
    x2 = 0.5 * a * (-b - delta_sqrt)
    print("x1 = ", x1, ",  ", "x2 = ", x2)