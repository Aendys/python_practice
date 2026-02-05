import cmath

#Text introduction
print("Hello user, this is a program for calculating a quadratic equation. Insert a values for variables A,B and C to calculate.")

#Ask for parameter inputs A,B,C
a = float(input("Please enter a number for variable A:"))
b = float(input("Please enter a number for variable B:"))
c = float(input("Please enter a number for variable C:"))

#Print equation Ax2 + Bx + C = 0
print("Calculating ",  a,"x2 + ", b,"x + ", c , "= 0:")

# Body with the program to calculate the equation
def quadratic(a, b, c):
    d = (b**2) - (4*a*c) #discrimininat

    if d > 0:
        x1 = (- b - cmath.sqrt(d)) / (2*a)
        x2 = (- b + cmath.sqrt(d)) / (2*a)
        print("The equation has 2 solutions: {0} and {1}".format(x1, x2))
    elif d == 0:
        x = (- b + cmath.sqrt(d)) / (2*a)
        print ("The equations has 1 solution: {0} ".format(x))
    else:
        print ("The equations has 0 solutions.")


if a == 0:
    print("Variable a cannot be 0. Enter correct value.")
else:
    quadratic(a, b, c)
