import math


def input_data():
    print("Dear user, this program calculates the perimeter or area of specific geometry objects.")
    calc_type = input("Choose type of the calculation, type 1 for perimeter or type 2 for area: ")
    calc_object = input( "Choose geometric figure type 1 for square, type 2 for triangle, type 3 for circle, type 4 for rectangle: ")
    while calc_type and calc_object is not None:
        return calc_type, calc_object
    return None


def square(calc_type):
    a = float(input("Enter value for side a: "))
    if calc_type == "1":
        perimeter = round((4 * a), 2)
        print(f"Perimeter of the square is {perimeter}")
        return perimeter
    elif calc_type == "2":
        area = round(a * a, 2)
        print(f"Area of the square is {area}")
        return area
    else:
        print("Invalid input.")
        return None


def triangle(calc_type):
    a, b, c, h = map(float, input("Enter values for sides a, b, c and height h. Split the numbers with comma: ").split(","))
    if calc_type == "1":
        perimeter = round(a + b + c, 2)
        print(f"Perimeter of the triangle is {perimeter}")
        return perimeter
    elif calc_type == "2":
        area = round((a * h) / 2, 2)
        print(f"Area of the triangle is {area}")
        return area
    else:
        print("Invalid input.")
        return None


def circle(calc_type):
    r = float(input("Enter the radius: "))
    if calc_type == "1":
        perimeter = round(2 * math.pi * r, 2)
        print(f"Perimeter of the circle is {perimeter}")
        return perimeter
    elif calc_type == "2":
        area = round(math.pi * r * r, 2)
        print(f"Area of the circle is {area}")
        return area
    else:
        print("Invalid input.")
        return None


def rectangle(calc_type):
    a, b = map(float, input("Enter values for sides a, b. Split the numbers with comma: ").split(","))
    if calc_type == "1":
        perimeter = round(2 * (a + b), 2)
        print(f"Perimeter of the rectangle is {perimeter}")
        return perimeter
    elif calc_type == "2":
        area = round(a * b, 2)
        print(f"Area of the rectangle is {area}")
        return area
    else:
        print("Invalid input.")
        return None


def result():
    calc_type, calc_object = input_data()
    if calc_object == "1":
        square(calc_type)
    elif calc_object == "2":
        triangle(calc_type)
    elif calc_object == "3":
        circle(calc_type)
    elif calc_object == "4":
        rectangle(calc_type)
    else:
        print("Invalid input.")

if __name__ == "__main__":
    result()

    i = input("Do you wish to continue? (y/n): ")
    while i == "y":
        result()
        i = input("Do you wish to continue? (y/n): ")
