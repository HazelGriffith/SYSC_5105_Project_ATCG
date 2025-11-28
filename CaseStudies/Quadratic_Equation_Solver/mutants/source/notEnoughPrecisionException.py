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
class NotEnoughPrecisionException(Exception): # pragma: no mutate
	
    def xǁNotEnoughPrecisionExceptionǁ__init____mutmut_orig(self, message):
        self.message = message
        super().__init__(self.message)
	
    def xǁNotEnoughPrecisionExceptionǁ__init____mutmut_1(self, message):
        self.message = None
        super().__init__(self.message)
	
    def xǁNotEnoughPrecisionExceptionǁ__init____mutmut_2(self, message):
        self.message = message
        super().__init__(None)
    
    xǁNotEnoughPrecisionExceptionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁNotEnoughPrecisionExceptionǁ__init____mutmut_1': xǁNotEnoughPrecisionExceptionǁ__init____mutmut_1, 
        'xǁNotEnoughPrecisionExceptionǁ__init____mutmut_2': xǁNotEnoughPrecisionExceptionǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNotEnoughPrecisionExceptionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁNotEnoughPrecisionExceptionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁNotEnoughPrecisionExceptionǁ__init____mutmut_orig)
    xǁNotEnoughPrecisionExceptionǁ__init____mutmut_orig.__name__ = 'xǁNotEnoughPrecisionExceptionǁ__init__'