class Quadratic_Equation_Problem: # pragma: no cover
     
    def __init__(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k