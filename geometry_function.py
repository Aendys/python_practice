import math


def input_data():
    print("Dear user, this program calculates the perimeter or area of specific geometry objects.")
    calc_type = input("Choose type of the calculation - perimeter or area: ")
    calc_object = input("Choose geometric figure - square, triangle, circle, rectangle: ")
    return calc_type, calc_object


def calculate(calc_object, calc_type):
    if calc_type == "perimeter" and calc_object == "square":
        a = float(input("Enter value for side a: "))
        perimeter = round (4 * a), 2
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "perimeter" and calc_object == "triangle":
        a, b, c = map(float, input("Enter values for sides a, b, c. Split the numbers with comma: ").split(","))
        perimeter = round(a + b + c), 2
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "perimeter" and calc_object == "circle":
        r = float(input("Enter the radius: "))
        perimeter = round(2 * math.pi * r, 2)
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "perimeter" and calc_object == "rectangle":
        a, b = map(float, input("Enter values for sides a, b. Split the numbers with comma: ").split(","))
        perimeter = round(2 * (a + b), 2)
        print(f"The {calc_type} of {calc_object} is {perimeter}")
        return None

    elif calc_type == "area" and calc_object == "square":
        a = float(input("Enter the value for side a: "))
        area = round(a * a, 2)
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    elif calc_type == "area" and calc_object == "triangle":
        a, b, c, h = map(float, input("Enter values for sides a, b, c and the height h. Split the numbers with comma: ").split(","))
        area = round((a * h) / 2, 2)
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    elif calc_type == "area" and calc_object == "circle":
        r = float(input("Enter the radius: "))
        area = round(math.pi * r * r, 2)
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    elif calc_type == "area" and calc_object == "rectangle":
        a, b = map(float, input("Enter values for sides a, b. Split the numbers with comma: ").split(","))
        area = round(a * b, 2)
        print(f"The {calc_type} of {calc_object} is {area}")
        return None

    else:

        return None

def result():
    calc_type, calc_object = input_data()
    if calc_type and calc_object is not None:
        calculate(calc_object, calc_type)
    else:
        print("Please enter a valid choice.")

result()

i = input("Do you wish to continue? (y/n): ")
while i == "y":
    result()
    i = input("Do you wish to continue? (y/n): ")





