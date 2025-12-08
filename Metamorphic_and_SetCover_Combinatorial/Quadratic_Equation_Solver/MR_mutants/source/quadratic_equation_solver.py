import math
from source.notEnoughPrecisionException import NotEnoughPrecisionException

ERROR = 0.00000001  # acceptable error for Newton's Method
"""
* Solves the quadratic equation and outputs roots to the screen. Throws an exception is precision is lost during calculation.
*/
"""
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result

def x_solveQuadratic__mutmut_orig(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_1(a: float, b: float, c: float):
    discriminant = None

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_2(a: float, b: float, c: float):
    discriminant = b * b + 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_3(a: float, b: float, c: float):
    discriminant = b / b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_4(a: float, b: float, c: float):
    discriminant = b * b - 4 * a / c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_5(a: float, b: float, c: float):
    discriminant = b * b - 4 / a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_6(a: float, b: float, c: float):
    discriminant = b * b - 5 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_7(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) and discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_8(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(None) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_9(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant != b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_10(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b / b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_11(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException(None)

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_12(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("XXNot enough precision to processXX")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_13(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_14(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("NOT ENOUGH PRECISION TO PROCESS")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_15(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant <= 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_16(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 1:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_17(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = None
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_18(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(None)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_19(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 / discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_20(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(+1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_21(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-2 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_22(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = None
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_23(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble(None)
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_24(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) * (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_25(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 / b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_26(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((+1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_27(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-2 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_28(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 / a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_29(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (3 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_30(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = None
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_31(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(None)
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_32(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt * (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_33(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 / a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_34(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (3 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_35(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = None
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_36(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "XXx1 = XX"
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_37(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "X1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_38(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output = real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_39(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output -= real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_40(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real - " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_41(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + "XX + XX" if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_42(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if real == "0" else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_43(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real != "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_44(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "XX0XX") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_45(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else "XXXX"
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_46(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output = imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_47(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output -= imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_48(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if imaginary == "1" else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_49(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary != "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_50(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "XX1XX") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_51(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else "XXXX"
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_52(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output = "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_53(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output -= "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_54(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "XXj\nx2 = XX"
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_55(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "J\nX2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_56(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output = real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_57(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output -= real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_58(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real - " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_59(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + "XX - XX" if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_60(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if real == "0" else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_61(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real != "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_62(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "XX0XX") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_63(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "XX-XX"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_64(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output = imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_65(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output -= imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_66(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if imaginary == "1" else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_67(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary != "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_68(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "XX1XX") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_69(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else "XXXX"
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_70(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output = "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_71(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output -= "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_72(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "XXjXX"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_73(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "J"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_74(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(None)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_75(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = None
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_76(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(None)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_77(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = None
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_78(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) / (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_79(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (+0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_80(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-1.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_81(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b - sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_82(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) / sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_83(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(None) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_84(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = None
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_85(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(None)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_86(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q * a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_87(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = None
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_88(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(None)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_89(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c * q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_90(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = None
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_91(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " - x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_92(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "XXx1 = XX" + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_93(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "X1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_94(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output = "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_95(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output -= "\nx2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_96(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " - x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_97(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "XX\nx2 = XX" + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_98(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nX2 = " + x2 if (not x1 == x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_99(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if x1 == x2 else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_100(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 != x2) else ""
        print(output)
        return output

def x_solveQuadratic__mutmut_101(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else "XXXX"
        print(output)
        return output

def x_solveQuadratic__mutmut_102(a: float, b: float, c: float):
    discriminant = b * b - 4 * a * c

    # check for overflow and b^2 >> 4ac
    if math.isnan(discriminant) or discriminant == b * b:
        raise NotEnoughPrecisionException("Not enough precision to process")

    if discriminant < 0:  # complex roots
        sqrt = sqrtByNewton(-1 * discriminant)
        real = formatDouble((-1 * b) / (2 * a))
        imaginary = formatDouble(sqrt / (2 * a))
        # don't print redundant zeros and signs
        output = "x1 = "
        output += real + " + " if (not real == "0") else ""
        output += imaginary if (not imaginary == "1") else ""
        output += "j\nx2 = "
        output += real + " - " if (not real == "0") else "-"
        output += imaginary if (not imaginary == "1") else ""
        output += "j"
        print(output)
        return output
    else:  # real roots
        sqrt = sqrtByNewton(discriminant)
        # mixed approach to avoid subtractive cancellation
        q = (-0.5) * (b + sign(b) * sqrt)
        x1 = formatDouble(q / a)
        x2 = formatDouble(c / q)
        # don't print the same root twice
        output = "x1 = " + x1
        output += "\nx2 = " + x2 if (not x1 == x2) else ""
        print(None)
        return output

x_solveQuadratic__mutmut_mutants : ClassVar[MutantDict] = {
'x_solveQuadratic__mutmut_1': x_solveQuadratic__mutmut_1, 
    'x_solveQuadratic__mutmut_2': x_solveQuadratic__mutmut_2, 
    'x_solveQuadratic__mutmut_3': x_solveQuadratic__mutmut_3, 
    'x_solveQuadratic__mutmut_4': x_solveQuadratic__mutmut_4, 
    'x_solveQuadratic__mutmut_5': x_solveQuadratic__mutmut_5, 
    'x_solveQuadratic__mutmut_6': x_solveQuadratic__mutmut_6, 
    'x_solveQuadratic__mutmut_7': x_solveQuadratic__mutmut_7, 
    'x_solveQuadratic__mutmut_8': x_solveQuadratic__mutmut_8, 
    'x_solveQuadratic__mutmut_9': x_solveQuadratic__mutmut_9, 
    'x_solveQuadratic__mutmut_10': x_solveQuadratic__mutmut_10, 
    'x_solveQuadratic__mutmut_11': x_solveQuadratic__mutmut_11, 
    'x_solveQuadratic__mutmut_12': x_solveQuadratic__mutmut_12, 
    'x_solveQuadratic__mutmut_13': x_solveQuadratic__mutmut_13, 
    'x_solveQuadratic__mutmut_14': x_solveQuadratic__mutmut_14, 
    'x_solveQuadratic__mutmut_15': x_solveQuadratic__mutmut_15, 
    'x_solveQuadratic__mutmut_16': x_solveQuadratic__mutmut_16, 
    'x_solveQuadratic__mutmut_17': x_solveQuadratic__mutmut_17, 
    'x_solveQuadratic__mutmut_18': x_solveQuadratic__mutmut_18, 
    'x_solveQuadratic__mutmut_19': x_solveQuadratic__mutmut_19, 
    'x_solveQuadratic__mutmut_20': x_solveQuadratic__mutmut_20, 
    'x_solveQuadratic__mutmut_21': x_solveQuadratic__mutmut_21, 
    'x_solveQuadratic__mutmut_22': x_solveQuadratic__mutmut_22, 
    'x_solveQuadratic__mutmut_23': x_solveQuadratic__mutmut_23, 
    'x_solveQuadratic__mutmut_24': x_solveQuadratic__mutmut_24, 
    'x_solveQuadratic__mutmut_25': x_solveQuadratic__mutmut_25, 
    'x_solveQuadratic__mutmut_26': x_solveQuadratic__mutmut_26, 
    'x_solveQuadratic__mutmut_27': x_solveQuadratic__mutmut_27, 
    'x_solveQuadratic__mutmut_28': x_solveQuadratic__mutmut_28, 
    'x_solveQuadratic__mutmut_29': x_solveQuadratic__mutmut_29, 
    'x_solveQuadratic__mutmut_30': x_solveQuadratic__mutmut_30, 
    'x_solveQuadratic__mutmut_31': x_solveQuadratic__mutmut_31, 
    'x_solveQuadratic__mutmut_32': x_solveQuadratic__mutmut_32, 
    'x_solveQuadratic__mutmut_33': x_solveQuadratic__mutmut_33, 
    'x_solveQuadratic__mutmut_34': x_solveQuadratic__mutmut_34, 
    'x_solveQuadratic__mutmut_35': x_solveQuadratic__mutmut_35, 
    'x_solveQuadratic__mutmut_36': x_solveQuadratic__mutmut_36, 
    'x_solveQuadratic__mutmut_37': x_solveQuadratic__mutmut_37, 
    'x_solveQuadratic__mutmut_38': x_solveQuadratic__mutmut_38, 
    'x_solveQuadratic__mutmut_39': x_solveQuadratic__mutmut_39, 
    'x_solveQuadratic__mutmut_40': x_solveQuadratic__mutmut_40, 
    'x_solveQuadratic__mutmut_41': x_solveQuadratic__mutmut_41, 
    'x_solveQuadratic__mutmut_42': x_solveQuadratic__mutmut_42, 
    'x_solveQuadratic__mutmut_43': x_solveQuadratic__mutmut_43, 
    'x_solveQuadratic__mutmut_44': x_solveQuadratic__mutmut_44, 
    'x_solveQuadratic__mutmut_45': x_solveQuadratic__mutmut_45, 
    'x_solveQuadratic__mutmut_46': x_solveQuadratic__mutmut_46, 
    'x_solveQuadratic__mutmut_47': x_solveQuadratic__mutmut_47, 
    'x_solveQuadratic__mutmut_48': x_solveQuadratic__mutmut_48, 
    'x_solveQuadratic__mutmut_49': x_solveQuadratic__mutmut_49, 
    'x_solveQuadratic__mutmut_50': x_solveQuadratic__mutmut_50, 
    'x_solveQuadratic__mutmut_51': x_solveQuadratic__mutmut_51, 
    'x_solveQuadratic__mutmut_52': x_solveQuadratic__mutmut_52, 
    'x_solveQuadratic__mutmut_53': x_solveQuadratic__mutmut_53, 
    'x_solveQuadratic__mutmut_54': x_solveQuadratic__mutmut_54, 
    'x_solveQuadratic__mutmut_55': x_solveQuadratic__mutmut_55, 
    'x_solveQuadratic__mutmut_56': x_solveQuadratic__mutmut_56, 
    'x_solveQuadratic__mutmut_57': x_solveQuadratic__mutmut_57, 
    'x_solveQuadratic__mutmut_58': x_solveQuadratic__mutmut_58, 
    'x_solveQuadratic__mutmut_59': x_solveQuadratic__mutmut_59, 
    'x_solveQuadratic__mutmut_60': x_solveQuadratic__mutmut_60, 
    'x_solveQuadratic__mutmut_61': x_solveQuadratic__mutmut_61, 
    'x_solveQuadratic__mutmut_62': x_solveQuadratic__mutmut_62, 
    'x_solveQuadratic__mutmut_63': x_solveQuadratic__mutmut_63, 
    'x_solveQuadratic__mutmut_64': x_solveQuadratic__mutmut_64, 
    'x_solveQuadratic__mutmut_65': x_solveQuadratic__mutmut_65, 
    'x_solveQuadratic__mutmut_66': x_solveQuadratic__mutmut_66, 
    'x_solveQuadratic__mutmut_67': x_solveQuadratic__mutmut_67, 
    'x_solveQuadratic__mutmut_68': x_solveQuadratic__mutmut_68, 
    'x_solveQuadratic__mutmut_69': x_solveQuadratic__mutmut_69, 
    'x_solveQuadratic__mutmut_70': x_solveQuadratic__mutmut_70, 
    'x_solveQuadratic__mutmut_71': x_solveQuadratic__mutmut_71, 
    'x_solveQuadratic__mutmut_72': x_solveQuadratic__mutmut_72, 
    'x_solveQuadratic__mutmut_73': x_solveQuadratic__mutmut_73, 
    'x_solveQuadratic__mutmut_74': x_solveQuadratic__mutmut_74, 
    'x_solveQuadratic__mutmut_75': x_solveQuadratic__mutmut_75, 
    'x_solveQuadratic__mutmut_76': x_solveQuadratic__mutmut_76, 
    'x_solveQuadratic__mutmut_77': x_solveQuadratic__mutmut_77, 
    'x_solveQuadratic__mutmut_78': x_solveQuadratic__mutmut_78, 
    'x_solveQuadratic__mutmut_79': x_solveQuadratic__mutmut_79, 
    'x_solveQuadratic__mutmut_80': x_solveQuadratic__mutmut_80, 
    'x_solveQuadratic__mutmut_81': x_solveQuadratic__mutmut_81, 
    'x_solveQuadratic__mutmut_82': x_solveQuadratic__mutmut_82, 
    'x_solveQuadratic__mutmut_83': x_solveQuadratic__mutmut_83, 
    'x_solveQuadratic__mutmut_84': x_solveQuadratic__mutmut_84, 
    'x_solveQuadratic__mutmut_85': x_solveQuadratic__mutmut_85, 
    'x_solveQuadratic__mutmut_86': x_solveQuadratic__mutmut_86, 
    'x_solveQuadratic__mutmut_87': x_solveQuadratic__mutmut_87, 
    'x_solveQuadratic__mutmut_88': x_solveQuadratic__mutmut_88, 
    'x_solveQuadratic__mutmut_89': x_solveQuadratic__mutmut_89, 
    'x_solveQuadratic__mutmut_90': x_solveQuadratic__mutmut_90, 
    'x_solveQuadratic__mutmut_91': x_solveQuadratic__mutmut_91, 
    'x_solveQuadratic__mutmut_92': x_solveQuadratic__mutmut_92, 
    'x_solveQuadratic__mutmut_93': x_solveQuadratic__mutmut_93, 
    'x_solveQuadratic__mutmut_94': x_solveQuadratic__mutmut_94, 
    'x_solveQuadratic__mutmut_95': x_solveQuadratic__mutmut_95, 
    'x_solveQuadratic__mutmut_96': x_solveQuadratic__mutmut_96, 
    'x_solveQuadratic__mutmut_97': x_solveQuadratic__mutmut_97, 
    'x_solveQuadratic__mutmut_98': x_solveQuadratic__mutmut_98, 
    'x_solveQuadratic__mutmut_99': x_solveQuadratic__mutmut_99, 
    'x_solveQuadratic__mutmut_100': x_solveQuadratic__mutmut_100, 
    'x_solveQuadratic__mutmut_101': x_solveQuadratic__mutmut_101, 
    'x_solveQuadratic__mutmut_102': x_solveQuadratic__mutmut_102
}

def solveQuadratic(*args, **kwargs):
    result = _mutmut_trampoline(x_solveQuadratic__mutmut_orig, x_solveQuadratic__mutmut_mutants, args, kwargs)
    return result 

solveQuadratic.__signature__ = _mutmut_signature(x_solveQuadratic__mutmut_orig)
x_solveQuadratic__mutmut_orig.__name__ = 'x_solveQuadratic'

"""/*
* Extracts the sign of a double value.
*/"""

def x_sign__mutmut_orig(b: float) -> int:
    return 1 if (b > 0) else -1

def x_sign__mutmut_1(b: float) -> int:
    return 2 if (b > 0) else -1

def x_sign__mutmut_2(b: float) -> int:
    return 1 if (b >= 0) else -1

def x_sign__mutmut_3(b: float) -> int:
    return 1 if (b > 1) else -1

def x_sign__mutmut_4(b: float) -> int:
    return 1 if (b > 0) else +1

def x_sign__mutmut_5(b: float) -> int:
    return 1 if (b > 0) else -2

x_sign__mutmut_mutants : ClassVar[MutantDict] = {
'x_sign__mutmut_1': x_sign__mutmut_1, 
    'x_sign__mutmut_2': x_sign__mutmut_2, 
    'x_sign__mutmut_3': x_sign__mutmut_3, 
    'x_sign__mutmut_4': x_sign__mutmut_4, 
    'x_sign__mutmut_5': x_sign__mutmut_5
}

def sign(*args, **kwargs):
    result = _mutmut_trampoline(x_sign__mutmut_orig, x_sign__mutmut_mutants, args, kwargs)
    return result 

sign.__signature__ = _mutmut_signature(x_sign__mutmut_orig)
x_sign__mutmut_orig.__name__ = 'x_sign'

"""/*
* Computes the square root of a number using Newton's Method. Returns when the error threshold has been reached.
*/"""

def x_sqrtByNewton__mutmut_orig(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_1(value: float) -> float:
    # square root of zero is zero
    if value != 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_2(value: float) -> float:
    # square root of zero is zero
    if value == 1.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_3(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 1.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_4(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = None

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_5(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) * 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_6(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 - value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_7(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (2 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_8(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 3

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_9(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while False:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_10(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = None
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_11(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) * 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_12(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous - value / previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_13(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value * previous) / 2
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_14(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 3
        if previous - result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_15(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous + result < ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_16(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result <= ERROR:
            break
        previous = result

    return result

def x_sqrtByNewton__mutmut_17(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            return
        previous = result

    return result

def x_sqrtByNewton__mutmut_18(value: float) -> float:
    # square root of zero is zero
    if value == 0.0:
        return 0.0
    previous = (1 + value) / 2

    # iterate until error threshold is reached
    while True:
        result = (previous + value / previous) / 2
        if previous - result < ERROR:
            break
        previous = None

    return result

x_sqrtByNewton__mutmut_mutants : ClassVar[MutantDict] = {
'x_sqrtByNewton__mutmut_1': x_sqrtByNewton__mutmut_1, 
    'x_sqrtByNewton__mutmut_2': x_sqrtByNewton__mutmut_2, 
    'x_sqrtByNewton__mutmut_3': x_sqrtByNewton__mutmut_3, 
    'x_sqrtByNewton__mutmut_4': x_sqrtByNewton__mutmut_4, 
    'x_sqrtByNewton__mutmut_5': x_sqrtByNewton__mutmut_5, 
    'x_sqrtByNewton__mutmut_6': x_sqrtByNewton__mutmut_6, 
    'x_sqrtByNewton__mutmut_7': x_sqrtByNewton__mutmut_7, 
    'x_sqrtByNewton__mutmut_8': x_sqrtByNewton__mutmut_8, 
    'x_sqrtByNewton__mutmut_9': x_sqrtByNewton__mutmut_9, 
    'x_sqrtByNewton__mutmut_10': x_sqrtByNewton__mutmut_10, 
    'x_sqrtByNewton__mutmut_11': x_sqrtByNewton__mutmut_11, 
    'x_sqrtByNewton__mutmut_12': x_sqrtByNewton__mutmut_12, 
    'x_sqrtByNewton__mutmut_13': x_sqrtByNewton__mutmut_13, 
    'x_sqrtByNewton__mutmut_14': x_sqrtByNewton__mutmut_14, 
    'x_sqrtByNewton__mutmut_15': x_sqrtByNewton__mutmut_15, 
    'x_sqrtByNewton__mutmut_16': x_sqrtByNewton__mutmut_16, 
    'x_sqrtByNewton__mutmut_17': x_sqrtByNewton__mutmut_17, 
    'x_sqrtByNewton__mutmut_18': x_sqrtByNewton__mutmut_18
}

def sqrtByNewton(*args, **kwargs):
    result = _mutmut_trampoline(x_sqrtByNewton__mutmut_orig, x_sqrtByNewton__mutmut_mutants, args, kwargs)
    return result 

sqrtByNewton.__signature__ = _mutmut_signature(x_sqrtByNewton__mutmut_orig)
x_sqrtByNewton__mutmut_orig.__name__ = 'x_sqrtByNewton'

"""/* 
* Checks whether a double value actually represents an integer, and formats accordingly.
*/"""

def x_formatDouble__mutmut_orig(value: float) -> str:

    # check if value is actually an integer
    if math.floor(value) == value:
        intValue = int(value)
        return intValue.__str__()
    else:
        doubleValue = value
        return doubleValue.__str__()

def x_formatDouble__mutmut_1(value: float) -> str:

    # check if value is actually an integer
    if math.floor(None) == value:
        intValue = int(value)
        return intValue.__str__()
    else:
        doubleValue = value
        return doubleValue.__str__()

def x_formatDouble__mutmut_2(value: float) -> str:

    # check if value is actually an integer
    if math.floor(value) != value:
        intValue = int(value)
        return intValue.__str__()
    else:
        doubleValue = value
        return doubleValue.__str__()

def x_formatDouble__mutmut_3(value: float) -> str:

    # check if value is actually an integer
    if math.floor(value) == value:
        intValue = None
        return intValue.__str__()
    else:
        doubleValue = value
        return doubleValue.__str__()

def x_formatDouble__mutmut_4(value: float) -> str:

    # check if value is actually an integer
    if math.floor(value) == value:
        intValue = int(None)
        return intValue.__str__()
    else:
        doubleValue = value
        return doubleValue.__str__()

def x_formatDouble__mutmut_5(value: float) -> str:

    # check if value is actually an integer
    if math.floor(value) == value:
        intValue = int(value)
        return intValue.__str__()
    else:
        doubleValue = None
        return doubleValue.__str__()

x_formatDouble__mutmut_mutants : ClassVar[MutantDict] = {
'x_formatDouble__mutmut_1': x_formatDouble__mutmut_1, 
    'x_formatDouble__mutmut_2': x_formatDouble__mutmut_2, 
    'x_formatDouble__mutmut_3': x_formatDouble__mutmut_3, 
    'x_formatDouble__mutmut_4': x_formatDouble__mutmut_4, 
    'x_formatDouble__mutmut_5': x_formatDouble__mutmut_5
}

def formatDouble(*args, **kwargs):
    result = _mutmut_trampoline(x_formatDouble__mutmut_orig, x_formatDouble__mutmut_mutants, args, kwargs)
    return result 

formatDouble.__signature__ = _mutmut_signature(x_formatDouble__mutmut_orig)
x_formatDouble__mutmut_orig.__name__ = 'x_formatDouble'

"""/*
* Validates the input by converting to type double and inspecting for overflow. Throws an exception if overflow occurred.
*/"""

def x_validateInput__mutmut_orig(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_1(input: str) -> float:

    # parse the input
    value = None

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_2(input: str) -> float:

    # parse the input
    value = float(None)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_3(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = None
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_4(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(None) == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_5(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.rfind(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_6(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find("XX.XX") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_7(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") != -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_8(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == +1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_9(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -2:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_10(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted = ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_11(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted -= ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_12(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += "XX.0XX"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_13(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) or (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_14(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if f"{value}" == formatted and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_15(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" != formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_16(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (value.__str__() == input):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_17(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() != input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("Not enough precision to process")

    return value

def x_validateInput__mutmut_18(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException(None)

    return value

def x_validateInput__mutmut_19(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("XXNot enough precision to processXX")

    return value

def x_validateInput__mutmut_20(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("not enough precision to process")

    return value

def x_validateInput__mutmut_21(input: str) -> float:

    # parse the input
    value = float(input)

    # format value to decimal of (almost) arbitrary length 100.100

    # append .0 when input is integer
    formatted = input
    if input.find(".") == -1:
        formatted += ".0"

    # if new value is not equal to original, overflow has occurred
    if (not f"{value}" == formatted) and (
        not (value.__str__() == input)
    ):  # toString to validate e-notation
        raise NotEnoughPrecisionException("NOT ENOUGH PRECISION TO PROCESS")

    return value

x_validateInput__mutmut_mutants : ClassVar[MutantDict] = {
'x_validateInput__mutmut_1': x_validateInput__mutmut_1, 
    'x_validateInput__mutmut_2': x_validateInput__mutmut_2, 
    'x_validateInput__mutmut_3': x_validateInput__mutmut_3, 
    'x_validateInput__mutmut_4': x_validateInput__mutmut_4, 
    'x_validateInput__mutmut_5': x_validateInput__mutmut_5, 
    'x_validateInput__mutmut_6': x_validateInput__mutmut_6, 
    'x_validateInput__mutmut_7': x_validateInput__mutmut_7, 
    'x_validateInput__mutmut_8': x_validateInput__mutmut_8, 
    'x_validateInput__mutmut_9': x_validateInput__mutmut_9, 
    'x_validateInput__mutmut_10': x_validateInput__mutmut_10, 
    'x_validateInput__mutmut_11': x_validateInput__mutmut_11, 
    'x_validateInput__mutmut_12': x_validateInput__mutmut_12, 
    'x_validateInput__mutmut_13': x_validateInput__mutmut_13, 
    'x_validateInput__mutmut_14': x_validateInput__mutmut_14, 
    'x_validateInput__mutmut_15': x_validateInput__mutmut_15, 
    'x_validateInput__mutmut_16': x_validateInput__mutmut_16, 
    'x_validateInput__mutmut_17': x_validateInput__mutmut_17, 
    'x_validateInput__mutmut_18': x_validateInput__mutmut_18, 
    'x_validateInput__mutmut_19': x_validateInput__mutmut_19, 
    'x_validateInput__mutmut_20': x_validateInput__mutmut_20, 
    'x_validateInput__mutmut_21': x_validateInput__mutmut_21
}

def validateInput(*args, **kwargs):
    result = _mutmut_trampoline(x_validateInput__mutmut_orig, x_validateInput__mutmut_mutants, args, kwargs)
    return result 

validateInput.__signature__ = _mutmut_signature(x_validateInput__mutmut_orig)
x_validateInput__mutmut_orig.__name__ = 'x_validateInput'


if __name__ == "__main__":  # pragma: no cover

    a = b = c = 0

    prompt = ""

    # welcome message
    print(
        "Welcome to Quadratic Equation Solver.\n"
        + "A quadratic equation can be written in the form ax^2 + bx + c = 0, where x is an unknown, a, b, and c are constants, and a is not zero.\n"
        + "Given values for a, b, and c, this program will produce the two roots of the equation. Both real and complex roots are supported, but not complex coefficients.\n"
        + "Press Ctrl+C to quit at any time."
    )

    # repeat until the user quits
    while True:

        # collect input from user
        try:
            a = 5
            a = validateInput(
                input("Enter a value for 'a':")
            )  # validate before storing
            # make sure a is not zero
            if a == 0:
                print("'a' cannot be zero!")
                continue

            b = validateInput(input("Enter a value for 'b':"))
            c = validateInput(input("Enter a value for 'c':"))
        except NotEnoughPrecisionException as e:
            print(
                "The value you entered is too large or too small! Please enter a value between "
                + str(2**-1074)
                + " and "
                + str(1.7976931348623157 * 10**308)
                + "."
            )
            continue
        except ValueError as e:
            print(
                "The value you entered is not allowed! Please enter a number. E.g. 4, 0.3, -12"
            )
            continue

        # solve equation
        try:
            solveQuadratic(a, b, c)
        except NotEnoughPrecisionException as e:
            print(
                "Failed to find an accurate solution! This can happen when the values are too"
                + " big, a is too close to zero, or b^2 is much bigger than 4ac."
            )

        # prompt user
        prompt = input("Would you like to try again? [y/n]")

        # quit if no
        if not prompt == "y":
            break

        # goodbye
        print("Thank you for using Quadratic Equation Solver!")
