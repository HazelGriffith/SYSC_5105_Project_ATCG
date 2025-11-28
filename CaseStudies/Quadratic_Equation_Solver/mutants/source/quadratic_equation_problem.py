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
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
class Quadratic_Equation_Problem: # pragma: no cover
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_orig(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_1(self, a, b, c, k = None):
        if k is not None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_2(self, a, b, c, k = None):
        if k is None:
            self.a = None
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_3(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = None
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_4(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = None
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_5(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = None
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_6(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a / k
            self.b = b*k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_7(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = None
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_8(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b / k
            self.c = c*k
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_9(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = None
     
    def xǁQuadratic_Equation_Problemǁ__init____mutmut_10(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c / k
    
    xǁQuadratic_Equation_Problemǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁQuadratic_Equation_Problemǁ__init____mutmut_1': xǁQuadratic_Equation_Problemǁ__init____mutmut_1, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_2': xǁQuadratic_Equation_Problemǁ__init____mutmut_2, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_3': xǁQuadratic_Equation_Problemǁ__init____mutmut_3, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_4': xǁQuadratic_Equation_Problemǁ__init____mutmut_4, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_5': xǁQuadratic_Equation_Problemǁ__init____mutmut_5, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_6': xǁQuadratic_Equation_Problemǁ__init____mutmut_6, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_7': xǁQuadratic_Equation_Problemǁ__init____mutmut_7, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_8': xǁQuadratic_Equation_Problemǁ__init____mutmut_8, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_9': xǁQuadratic_Equation_Problemǁ__init____mutmut_9, 
        'xǁQuadratic_Equation_Problemǁ__init____mutmut_10': xǁQuadratic_Equation_Problemǁ__init____mutmut_10
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁQuadratic_Equation_Problemǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁQuadratic_Equation_Problemǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁQuadratic_Equation_Problemǁ__init____mutmut_orig)
    xǁQuadratic_Equation_Problemǁ__init____mutmut_orig.__name__ = 'xǁQuadratic_Equation_Problemǁ__init__'