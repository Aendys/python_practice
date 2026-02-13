import math


def input_data():
    print("Dear user, this program calculates the perimeter or area of specific geometry objects.")
    calc_type = input("Choose type of the calculation - perimeter or area: ")
    calc_object = input("Choose geometric figure - square, triangle, circle, rectangle: ")
    return calc_type, calc_object


def calculate(calc_object, calc_type):
    if calc_type == "perimeter" and calc_object == "square":
        a = float(input("Enter value for side a: "))
        perimeter = 4 * a
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "perimeter" and calc_object == "triangle":
        a, b, c = map(float, input("Enter values for sides a, b, c. Split the numbers with comma: ").split(","))
        perimeter = a + b + c
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "perimeter" and calc_object == "circle":
        r = float(input("Enter the radius: "))
        perimeter = 2 * math.pi * r
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "perimeter" and calc_object == "rectangle":
        a, b = map(float, input("Enter values for sides a, b. Split the numbers with comma: ").split(","))
        perimeter = 2 * (a + b)
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "area" and calc_object == "square":
        a = float(input("Enter the perimeter: "))
        area = a * a
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    elif calc_type == "area" and calc_object == "triangle":
        a, b, c, h = map(float, input("Enter values for sides a, b, c and the height h. Split the numbers with comma: ").split(","))
        area = (a * h) / 2
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    elif calc_type == "area" and calc_object == "circle":
        r = float(input("Enter the radius: "))
        area = math.pi * r * r
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    elif calc_type == "area" and calc_object == "rectangle":
        a, b = map(float, input("Enter values for sides a, b. Split the numbers with comma: ").split(","))
        area = a * b
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    else:
        print("Please Enter a valid choice.")
        return None

def output_data():
    calc_type, calc_object = input_data()
    if calc_type and calc_object is not None:
        calculate(calc_object, calc_type)
    else:
        print("Please enter a valid choice.")



output_data()






