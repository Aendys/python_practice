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
    def test_square(self):
        perimeter_square = square (1)
        assert perimeter_square == 20