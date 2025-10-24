import unittest
from quadratic_equation_solver import Quadratic

class TestQES(unittest.TestCase):

    '''
    Value allowed should be greater than 5e-324 and less than 1.79e+308
    '''
    def validateInput_Test(self):
        assert Quadratic.validateInput(5e-324), "too low"
        assert Quadratic.validateInput(1.79e+308), "too high"