
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the module and specific symbols
import quadratic_equation_solver as quadratic_module
from quadratic_equation_solver import (
    Quadratic,
    Quadratic_Equation_Problem,
    NotEnoughPrecisionException
)

import contextlib
import io
import json
import pytest

import math


# Load the HIGH coverage combinatorial tests
with open("HIGH_CT_quadratic_results.json") as f:
    test_cases = json.load(f)


def test_combinatorial_quadratic():
    """
    This test validates behavior case-by-case:
    - If expected status is EXCEPTION → solver must raise an exception
    - If expected status is PASS → solver must return matching output
    """

    for case in test_cases:
        a = case["input"]["a"]
        b = case["input"]["b"]
        c = case["input"]["c"]
        expected_status = case["status"]

        # capture solver printed output
        buffer = io.StringIO()

        if expected_status == "EXCEPTION":
            # Solver should raise an exception
            with pytest.raises(Exception):
                with contextlib.redirect_stdout(buffer):
                    Quadratic.solveQuadratic(a, b, c)

        elif expected_status == "PASS":
            # Solver should produce the expected printed output
            expected_output = case["output"].strip()

            with contextlib.redirect_stdout(buffer):
                Quadratic.solveQuadratic(a, b, c)

            actual = buffer.getvalue().strip()

            assert actual == expected_output, (
                f"For case {case['id']}: Expected:\n{expected_output}\nGot:\n{actual}"
            )


# --------------------- sign() ---------------------

def test_sign_positive():
    assert Quadratic.sign(5) == 1

def test_sign_negative():
    assert Quadratic.sign(-7) == -1

def test_sign_zero():
    # zero takes the "negative" branch in this implementation
    assert Quadratic.sign(0) == -1


# --------------------- formatDouble() ---------------------

def test_format_double_integer_values():
    assert Quadratic.formatDouble(4.0) == "4"
    assert Quadratic.formatDouble(0.0) == "0"
    assert Quadratic.formatDouble(-3.0) == "-3"

def test_format_double_float_values():
    assert Quadratic.formatDouble(3.25) == "3.25"
    assert Quadratic.formatDouble(-10.75) == "-10.75"


# --------------------- sqrtByNewton() ---------------------

def test_sqrt_by_newton_basic():
    assert pytest.approx(Quadratic.sqrtByNewton(4), rel=1e-6) == 2
    assert pytest.approx(Quadratic.sqrtByNewton(9), rel=1e-6) == 3

def test_sqrt_by_newton_zero_input():
    assert Quadratic.sqrtByNewton(0) == 0.0

def test_sqrt_by_newton_non_perfect():
    assert pytest.approx(Quadratic.sqrtByNewton(2), rel=1e-6) == math.sqrt(2)


# --------------------- validateInput() ---------------------

def test_validate_input_valid_numbers():
    assert Quadratic.validateInput("5") == 5.0
    assert Quadratic.validateInput("3.14") == 3.14

def test_validate_input_too_large():
    with pytest.raises(NotEnoughPrecisionException):
        Quadratic.validateInput("1e500")

def test_validate_input_too_small():
    with pytest.raises(NotEnoughPrecisionException):
        Quadratic.validateInput("1e-5000")


# --------------------- Discriminant overflow ---------------------

def test_discriminant_overflow_exception():
    # b*b == discriminant → overflow → exception
    with pytest.raises(NotEnoughPrecisionException):
        Quadratic.solveQuadratic(1, 1e308, 1)


# --------------------- Real roots tests ---------------------

def test_real_two_distinct_roots():
    result = Quadratic.solveQuadratic(1, 0, -4)
    assert result.strip() == "x1 = 2\nx2 = -2"

def test_real_repeated_root():
    result = Quadratic.solveQuadratic(1, 2, 1)
    assert result.strip() == "x1 = -1"


# --------------------- Complex roots tests ---------------------

def test_complex_roots():
    result = Quadratic.solveQuadratic(1, 0, 4)
    assert result.strip() == "x1 = 2j\nx2 = -2j"



# -------------------------------------------------------------------
#          EXTRA TESTS TO KILL SURVIVING MUTANTS
# -------------------------------------------------------------------

def test_constructor_scaling():
    """Covers lines 1–12 / constructor scaling branch."""
    p = Quadratic_Equation_Problem(2, 4, 6, k=2)
    assert p.a == 4 and p.b == 8 and p.c == 12

def test_constructor_no_scaling():
    p = Quadratic_Equation_Problem(3, 5, 7)
    assert p.a == 3 and p.b == 5 and p.c == 7


def test_custom_exception_message():
    """Covers lines 14–18."""
    e = NotEnoughPrecisionException("boom")
    assert str(e) == "boom"


# -------------------------------------------------------------------
# sign() tests (kills mutants in lines 77–79)
# -------------------------------------------------------------------

def test_sign_positive_value():
    assert Quadratic.sign(10) == 1

def test_sign_negative_value():
    assert Quadratic.sign(-2) == -1

def test_sign_zero_value():
    # Zero should return -1 (as per code)
    assert Quadratic.sign(0) == -1


# -------------------------------------------------------------------
# sqrtByNewton() tests (kills 85–98)
# -------------------------------------------------------------------

def test_sqrt_by_newton_zero():
    assert Quadratic.sqrtByNewton(0.0) == 0.0

def test_sqrt_by_newton_basic_square():
    val = Quadratic.sqrtByNewton(9)
    assert abs(val - 3) < 1e-5

def test_sqrt_by_newton_non_perfect_value():
    val = Quadratic.sqrtByNewton(2)
    assert abs(val - math.sqrt(2)) < 1e-5


# -------------------------------------------------------------------
# formatDouble() tests (kills 104–113)
# -------------------------------------------------------------------

def test_format_double_integer():
    assert Quadratic.formatDouble(5.0) == "5"

def test_format_double_float_value():
    assert Quadratic.formatDouble(3.14) == "3.14"


# -------------------------------------------------------------------
# validateInput() tests (kills 121–138)
# -------------------------------------------------------------------

def test_validate_input_valid_integer():
    assert Quadratic.validateInput("5") == 5.0

def test_validate_input_valid_float():
    assert Quadratic.validateInput("5.25") == 5.25

def test_validate_input_overflow_large():
    with pytest.raises(NotEnoughPrecisionException):
        Quadratic.validateInput("1e309")   # overflow

def test_validate_input_overflow_small():
    with pytest.raises(NotEnoughPrecisionException):
        Quadratic.validateInput("1e-5000")  # underflow


# -------------------------------------------------------------------
# solveQuadratic() additional branch coverage
# -------------------------------------------------------------------

def test_real_root_two_distinct():
    output = Quadratic.solveQuadratic(1, -3, 2)
    assert "x1 = 2" in output and "x2 = 1" in output

def test_real_root_repeated():
    output = Quadratic.solveQuadratic(1, 2, 1)
    assert output.strip() == "x1 = -1"

def test_complex_root_case():
    output = Quadratic.solveQuadratic(1, 0, 4)
    assert "j" in output and "x1" in output




