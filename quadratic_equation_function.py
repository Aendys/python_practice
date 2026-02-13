import cmath

def input_data():
    print("Dear user, this program calculates a quadratic equation. Insert a values for variables A,B and C to calculate.")
    a = input("Please enter a number for variable a: ")
    b = input("Please enter a number for variable b: ")
    c = input("Please enter a number for variable c: ")
    return a, b, c


def quadratic_calculation(a, b, c):
    a, b, c = float(a), float(b), float (c)

    if a == 0:
        print("Cannot be divided by zero.")
    else:
        print("Calculating ", a, "x2 + ", b, "x + ", c, "= 0 ...")
        d = (b ** 2) - (4* a *c ) #discrimininat

        if d > 0:
            x1 = (- b - cmath.sqrt(d)) / (2 * a)
            x2 = (- b + cmath.sqrt(d)) / (2 * a)
            print(f"The equation has 2 solutions: {x1} and {x2}.")

        elif d == 0:
            x = (- b + cmath.sqrt(d)) / (2 * a)
            print (f"The equations has 1 solution: {x}.")
        else:
            print ("The equations has 0 solutions.")

def output():
    a, b, c = input_data()
    if a and b and c is not None:
        quadratic_calculation(a, b, c)
    else:
        print("Please enter valid data.")


output()
