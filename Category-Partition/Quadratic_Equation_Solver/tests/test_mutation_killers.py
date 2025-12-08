import pytest
from Quadratic_Equation_Solver.quadratic_equation_solver import Quadratic, NotEnoughPrecisionException

# ---------------------------------------------------------
# 1. Kill discriminant <=0 mutation by forcing D==0
# Original logic: D == 0 → one real root
# Mutant mistakenly treats it as complex or wrong branch
# ---------------------------------------------------------
def test_discriminant_equal_zero_behavior():
    # D = 2^2 - 4*1*1 = 0
    result = Quadratic.solveQuadratic(1,2,1)
    assert "x1" in result and "x2" not in result, \
           "D=0 should return one real root — mutant must be killed"

# ---------------------------------------------------------
# 2. Kill sign mutation: sign(b) for b==0 should be *negative* in original code
# Mutant treats b==0 as positive incorrectly
# ---------------------------------------------------------
def test_sign_zero_behavior():
    assert Quadratic.sign(0) == -1, \
           "sign(0) mutant incorrectly returns 1 — test should kill it"

# ---------------------------------------------------------
# 3. Kill overflow precision mutation
# Cause float precision breakdown intentionally to trigger exception
# ---------------------------------------------------------
def test_precision_overflow_mutation():
    with pytest.raises(NotEnoughPrecisionException):
        Quadratic.solveQuadratic(1e308, 1e308, 1e308)
