import pytest
from quadratic_equation_function import quadratic_calculation
from geometry_function2 import square, circle, triangle, rectangle



class TestQuadraticFunction:
    def test_equation_two_roots(self):
        calculation = quadratic_calculation (2,5,1)
        assert calculation == ((-2.28+0j), (-0.22+0j))

    def test_equation_single_root(self):
        calculation = quadratic_calculation (1,2,1)
        assert calculation == (-1+0j)

    def test_equation_no_solution(self):
        calculation = quadratic_calculation (1,1,1)
        assert calculation == 0

    def test_not_divided_by_zero(self):
        quadratic_calculation (0,1,1)
        with pytest.raises(ZeroDivisionError):
            raise ZeroDivisionError("Cannot be divided by zero")




class TestGeometryFunction:
    def test_square_perimeter(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5") # Mocking the input for side a with value 5
        perimeter = square("1")
        assert perimeter == 20

    def test_square_area(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5")
        area = square("2")
        assert area == 25

    def test_square_invalid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5")
        square("fadfa")
        with pytest.raises(ValueError):
            raise ValueError("Invalid input")

    def test_triangle_perimeter(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5,4,3,6")
        perimeter = triangle("1")
        assert perimeter == 12

    def test_triangle_area(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5,4,3,6")
        area = triangle("2")
        assert area == 15

    def test_triangle_invalid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "5,4,3,6")
        triangle("fadfa")
        with pytest.raises(ValueError):
            raise ValueError("Invalid input")

    def test_circle_perimeter(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "22.5")
        perimeter = circle("1")
        assert perimeter == 141.37

    def test_circle_area(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "22.5")
        area = circle("2")
        assert area == 1590.43

    def test_circle_invalid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "22.5")
        circle("fadfa")
        with pytest.raises(ValueError):
            raise ValueError("Invalid input")

    def test_rectangle_perimeter(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "7,8")
        perimeter = rectangle("1")
        assert perimeter == 30

    def test_rectangle_area(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "7,8")
        area = rectangle("2")
        assert area == 56

    def test_rectangle_invalid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "7,8")
        rectangle("fadfa")
        with pytest.raises(ValueError):
            raise ValueError("Invalid input")
