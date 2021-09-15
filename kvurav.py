import math
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
x = []
x1 = []
x2 = []
print(a, "* x^2", "+(", b, "*x) +", c, "= 0")
D = (b*b)-(4*a*c)
if D < 0:
    print("D =", b*b, -4*a*c, "=", D)
    print("D<0. Нет корней")
elif D == 0:
    print("D =", b * b, -4 * a * c, "=", D)
    print("D=0")
    x = ((-1)*b)/(2*a)
    print("x=", (-1)*b, "/2", a, "     ", "x=", x)
elif D > 0:
    print("D =", b * b, -4 * a * c, "=", D)
    print("D>0")
    x1 = ((-1)*b - 1 * math.sqrt(D)) / (2 * a)
    x2 = ((-1)*b + math.sqrt(D)) / (2 * a)
    print("x1=", "-", b, "-", math.sqrt(D), "/2", a, "      ", "x1=", x1)
    print("x2=", "-", b, "+", math.sqrt(D), "/2", a, "      ", "x2=", x2)
print(":)")
