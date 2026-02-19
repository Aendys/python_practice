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
        return 0
    else:
        print("Calculating ", a, "x2 + ", b, "x + ", c, "= 0 ...")
        d = (b ** 2) - (4* a *c ) #discrimininat

        if d > 0:
            x1 = (- b - cmath.sqrt(d)) / (2 * a)
            x2 = (- b + cmath.sqrt(d)) / (2 * a)
            x1 = complex(round(x1.real, 2), round(x1.imag))
            x2 = complex(round(x2.real, 2), round(x2.imag))
            print(f"The equation has 2 solutions: {x1} and {x2}.")
            return x1, x2

        elif d == 0:
            x = (- b + cmath.sqrt(d)) / (2 * a)
            x = complex(round(x.real, 2), round(x.imag))
            print (f"The equations has 1 solution: {x}.")
            return x
        else:
            print ("The equations has 0 solutions.")
            return 0

def result():
    a, b, c = input_data()
    if a and b and c is not None:
        quadratic_calculation(a, b, c)
    else:
        print("Please enter valid data.")

if __name__ == "__main__":
    result()


    i = input("Do you wish to continue? (y/n): ")
    while i == "y":
        result()
        i = input("Do you wish to continue? (y/n): ")

