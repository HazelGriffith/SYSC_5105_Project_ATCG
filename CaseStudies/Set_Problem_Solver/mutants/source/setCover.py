import signal
import os
from pathlib import Path
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

class Set:

    def xǁSetǁ__init____mutmut_orig(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_1(self, nGlobalSetSize:int = 1, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_2(self, nGlobalSetSize:int = 0, nSubSets:int = 1, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_3(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = None
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_4(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = None
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_5(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is not None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_6(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = None
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_7(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = None

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_8(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is not None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_9(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = None
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_10(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = None

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_11(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is not None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_12(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = None
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_13(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = None

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_14(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is not None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_15(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = None
        else:
            self.subSetSizesSum = subSetsSizesSum

    def xǁSetǁ__init____mutmut_16(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = None
    
    xǁSetǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetǁ__init____mutmut_1': xǁSetǁ__init____mutmut_1, 
        'xǁSetǁ__init____mutmut_2': xǁSetǁ__init____mutmut_2, 
        'xǁSetǁ__init____mutmut_3': xǁSetǁ__init____mutmut_3, 
        'xǁSetǁ__init____mutmut_4': xǁSetǁ__init____mutmut_4, 
        'xǁSetǁ__init____mutmut_5': xǁSetǁ__init____mutmut_5, 
        'xǁSetǁ__init____mutmut_6': xǁSetǁ__init____mutmut_6, 
        'xǁSetǁ__init____mutmut_7': xǁSetǁ__init____mutmut_7, 
        'xǁSetǁ__init____mutmut_8': xǁSetǁ__init____mutmut_8, 
        'xǁSetǁ__init____mutmut_9': xǁSetǁ__init____mutmut_9, 
        'xǁSetǁ__init____mutmut_10': xǁSetǁ__init____mutmut_10, 
        'xǁSetǁ__init____mutmut_11': xǁSetǁ__init____mutmut_11, 
        'xǁSetǁ__init____mutmut_12': xǁSetǁ__init____mutmut_12, 
        'xǁSetǁ__init____mutmut_13': xǁSetǁ__init____mutmut_13, 
        'xǁSetǁ__init____mutmut_14': xǁSetǁ__init____mutmut_14, 
        'xǁSetǁ__init____mutmut_15': xǁSetǁ__init____mutmut_15, 
        'xǁSetǁ__init____mutmut_16': xǁSetǁ__init____mutmut_16
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSetǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSetǁ__init____mutmut_orig)
    xǁSetǁ__init____mutmut_orig.__name__ = 'xǁSetǁ__init__'

    def xǁSetǁcopy__mutmut_orig(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_1(self):
        newSet = None
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_2(self):
        newSet = Set()
        newSet.nGlobalSetSize = None
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_3(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = None
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_4(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = None
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_5(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = None
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_6(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = None
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

    def xǁSetǁcopy__mutmut_7(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = None
        return newSet
    
    xǁSetǁcopy__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetǁcopy__mutmut_1': xǁSetǁcopy__mutmut_1, 
        'xǁSetǁcopy__mutmut_2': xǁSetǁcopy__mutmut_2, 
        'xǁSetǁcopy__mutmut_3': xǁSetǁcopy__mutmut_3, 
        'xǁSetǁcopy__mutmut_4': xǁSetǁcopy__mutmut_4, 
        'xǁSetǁcopy__mutmut_5': xǁSetǁcopy__mutmut_5, 
        'xǁSetǁcopy__mutmut_6': xǁSetǁcopy__mutmut_6, 
        'xǁSetǁcopy__mutmut_7': xǁSetǁcopy__mutmut_7
    }
    
    def copy(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetǁcopy__mutmut_orig"), object.__getattribute__(self, "xǁSetǁcopy__mutmut_mutants"), args, kwargs, self)
        return result 
    
    copy.__signature__ = _mutmut_signature(xǁSetǁcopy__mutmut_orig)
    xǁSetǁcopy__mutmut_orig.__name__ = 'xǁSetǁcopy'

class Solution:

    def xǁSolutionǁ__init____mutmut_orig(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_1(self, probSet:Set, nSolutionSize:int=1):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_2(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = None
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_3(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = None
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_4(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(None):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_5(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(None)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_6(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(+1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_7(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-2)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_8(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = None
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_9(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(None):
            self.boolIncluded.append(0)

    def xǁSolutionǁ__init____mutmut_10(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(None)

    def xǁSolutionǁ__init____mutmut_11(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(1)
    
    xǁSolutionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSolutionǁ__init____mutmut_1': xǁSolutionǁ__init____mutmut_1, 
        'xǁSolutionǁ__init____mutmut_2': xǁSolutionǁ__init____mutmut_2, 
        'xǁSolutionǁ__init____mutmut_3': xǁSolutionǁ__init____mutmut_3, 
        'xǁSolutionǁ__init____mutmut_4': xǁSolutionǁ__init____mutmut_4, 
        'xǁSolutionǁ__init____mutmut_5': xǁSolutionǁ__init____mutmut_5, 
        'xǁSolutionǁ__init____mutmut_6': xǁSolutionǁ__init____mutmut_6, 
        'xǁSolutionǁ__init____mutmut_7': xǁSolutionǁ__init____mutmut_7, 
        'xǁSolutionǁ__init____mutmut_8': xǁSolutionǁ__init____mutmut_8, 
        'xǁSolutionǁ__init____mutmut_9': xǁSolutionǁ__init____mutmut_9, 
        'xǁSolutionǁ__init____mutmut_10': xǁSolutionǁ__init____mutmut_10, 
        'xǁSolutionǁ__init____mutmut_11': xǁSolutionǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSolutionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSolutionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSolutionǁ__init____mutmut_orig)
    xǁSolutionǁ__init____mutmut_orig.__name__ = 'xǁSolutionǁ__init__'



class SetCoverProblem:


    def xǁSetCoverProblemǁ__init____mutmut_orig(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.depth = depth


    def xǁSetCoverProblemǁ__init____mutmut_1(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = None
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.depth = depth


    def xǁSetCoverProblemǁ__init____mutmut_2(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = mainSet
        self.aSolution = None
        self.bestSolution = bestSolution
        self.depth = depth


    def xǁSetCoverProblemǁ__init____mutmut_3(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = None
        self.depth = depth


    def xǁSetCoverProblemǁ__init____mutmut_4(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.depth = None
    
    xǁSetCoverProblemǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁ__init____mutmut_1': xǁSetCoverProblemǁ__init____mutmut_1, 
        'xǁSetCoverProblemǁ__init____mutmut_2': xǁSetCoverProblemǁ__init____mutmut_2, 
        'xǁSetCoverProblemǁ__init____mutmut_3': xǁSetCoverProblemǁ__init____mutmut_3, 
        'xǁSetCoverProblemǁ__init____mutmut_4': xǁSetCoverProblemǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSetCoverProblemǁ__init____mutmut_orig)
    xǁSetCoverProblemǁ__init____mutmut_orig.__name__ = 'xǁSetCoverProblemǁ__init__'

    def xǁSetCoverProblemǁgreedy__mutmut_orig(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_1(self):
        self.bestSolution.nSolutionSize = None
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_2(self):
        self.bestSolution.nSolutionSize = 1
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_3(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(None, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_4(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, None)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_5(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_6(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, )
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_7(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 1)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_8(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = None
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_9(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 1
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_10(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = None

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_11(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 1

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_12(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(None) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_13(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) != False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_14(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == True:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_15(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = None
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_16(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 1
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_17(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = None
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_18(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 1
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_19(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(None):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_20(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(None, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_21(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, None) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_22(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_23(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, ) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_24(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) != False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_25(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == True:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_26(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = None
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_27(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(None)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_28(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp >= addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_29(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = None
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_30(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = None
            self.addSubSet(self.bestSolution, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_31(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(None, addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_32(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, None)

    def xǁSetCoverProblemǁgreedy__mutmut_33(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(addIndex)

    def xǁSetCoverProblemǁgreedy__mutmut_34(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, )
    
    xǁSetCoverProblemǁgreedy__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁgreedy__mutmut_1': xǁSetCoverProblemǁgreedy__mutmut_1, 
        'xǁSetCoverProblemǁgreedy__mutmut_2': xǁSetCoverProblemǁgreedy__mutmut_2, 
        'xǁSetCoverProblemǁgreedy__mutmut_3': xǁSetCoverProblemǁgreedy__mutmut_3, 
        'xǁSetCoverProblemǁgreedy__mutmut_4': xǁSetCoverProblemǁgreedy__mutmut_4, 
        'xǁSetCoverProblemǁgreedy__mutmut_5': xǁSetCoverProblemǁgreedy__mutmut_5, 
        'xǁSetCoverProblemǁgreedy__mutmut_6': xǁSetCoverProblemǁgreedy__mutmut_6, 
        'xǁSetCoverProblemǁgreedy__mutmut_7': xǁSetCoverProblemǁgreedy__mutmut_7, 
        'xǁSetCoverProblemǁgreedy__mutmut_8': xǁSetCoverProblemǁgreedy__mutmut_8, 
        'xǁSetCoverProblemǁgreedy__mutmut_9': xǁSetCoverProblemǁgreedy__mutmut_9, 
        'xǁSetCoverProblemǁgreedy__mutmut_10': xǁSetCoverProblemǁgreedy__mutmut_10, 
        'xǁSetCoverProblemǁgreedy__mutmut_11': xǁSetCoverProblemǁgreedy__mutmut_11, 
        'xǁSetCoverProblemǁgreedy__mutmut_12': xǁSetCoverProblemǁgreedy__mutmut_12, 
        'xǁSetCoverProblemǁgreedy__mutmut_13': xǁSetCoverProblemǁgreedy__mutmut_13, 
        'xǁSetCoverProblemǁgreedy__mutmut_14': xǁSetCoverProblemǁgreedy__mutmut_14, 
        'xǁSetCoverProblemǁgreedy__mutmut_15': xǁSetCoverProblemǁgreedy__mutmut_15, 
        'xǁSetCoverProblemǁgreedy__mutmut_16': xǁSetCoverProblemǁgreedy__mutmut_16, 
        'xǁSetCoverProblemǁgreedy__mutmut_17': xǁSetCoverProblemǁgreedy__mutmut_17, 
        'xǁSetCoverProblemǁgreedy__mutmut_18': xǁSetCoverProblemǁgreedy__mutmut_18, 
        'xǁSetCoverProblemǁgreedy__mutmut_19': xǁSetCoverProblemǁgreedy__mutmut_19, 
        'xǁSetCoverProblemǁgreedy__mutmut_20': xǁSetCoverProblemǁgreedy__mutmut_20, 
        'xǁSetCoverProblemǁgreedy__mutmut_21': xǁSetCoverProblemǁgreedy__mutmut_21, 
        'xǁSetCoverProblemǁgreedy__mutmut_22': xǁSetCoverProblemǁgreedy__mutmut_22, 
        'xǁSetCoverProblemǁgreedy__mutmut_23': xǁSetCoverProblemǁgreedy__mutmut_23, 
        'xǁSetCoverProblemǁgreedy__mutmut_24': xǁSetCoverProblemǁgreedy__mutmut_24, 
        'xǁSetCoverProblemǁgreedy__mutmut_25': xǁSetCoverProblemǁgreedy__mutmut_25, 
        'xǁSetCoverProblemǁgreedy__mutmut_26': xǁSetCoverProblemǁgreedy__mutmut_26, 
        'xǁSetCoverProblemǁgreedy__mutmut_27': xǁSetCoverProblemǁgreedy__mutmut_27, 
        'xǁSetCoverProblemǁgreedy__mutmut_28': xǁSetCoverProblemǁgreedy__mutmut_28, 
        'xǁSetCoverProblemǁgreedy__mutmut_29': xǁSetCoverProblemǁgreedy__mutmut_29, 
        'xǁSetCoverProblemǁgreedy__mutmut_30': xǁSetCoverProblemǁgreedy__mutmut_30, 
        'xǁSetCoverProblemǁgreedy__mutmut_31': xǁSetCoverProblemǁgreedy__mutmut_31, 
        'xǁSetCoverProblemǁgreedy__mutmut_32': xǁSetCoverProblemǁgreedy__mutmut_32, 
        'xǁSetCoverProblemǁgreedy__mutmut_33': xǁSetCoverProblemǁgreedy__mutmut_33, 
        'xǁSetCoverProblemǁgreedy__mutmut_34': xǁSetCoverProblemǁgreedy__mutmut_34
    }
    
    def greedy(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁgreedy__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁgreedy__mutmut_mutants"), args, kwargs, self)
        return result 
    
    greedy.__signature__ = _mutmut_signature(xǁSetCoverProblemǁgreedy__mutmut_orig)
    xǁSetCoverProblemǁgreedy__mutmut_orig.__name__ = 'xǁSetCoverProblemǁgreedy'

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_orig(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_1(self, subSetIndex:int):
        count = None
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_2(self, subSetIndex:int):
        count = 1
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_3(self, subSetIndex:int):
        count = 0
        for i in range(None):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_4(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] + 1] == 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_5(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 2] == 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_6(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] != 0):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_7(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 1):
                count += 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_8(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count = 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_9(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count -= 1
        
        return count

    def xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_10(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 2
        
        return count
    
    xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_1': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_1, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_2': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_2, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_3': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_3, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_4': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_4, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_5': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_5, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_6': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_6, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_7': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_7, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_8': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_8, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_9': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_9, 
        'xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_10': xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_10
    }
    
    def numberOfUncoveredElements(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_mutants"), args, kwargs, self)
        return result 
    
    numberOfUncoveredElements.__signature__ = _mutmut_signature(xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_orig)
    xǁSetCoverProblemǁnumberOfUncoveredElements__mutmut_orig.__name__ = 'xǁSetCoverProblemǁnumberOfUncoveredElements'

    def xǁSetCoverProblemǁsortSubSets__mutmut_orig(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_1(self):
        for i in range(None):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_2(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(None):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_3(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] <= self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_4(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = None
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_5(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = None
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_6(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = None
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_7(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = None
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_8(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = None
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_9(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = None
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_10(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = None
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_11(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = None
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_12(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = None
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_13(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(None):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_14(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append(None)
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_15(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(None):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_16(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(None)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_17(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(1)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_18(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(None):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_19(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = None
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_20(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 1
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_21(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(None, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_22(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, None):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_23(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_24(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, ):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_25(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt = self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_26(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt -= self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    def xǁSetCoverProblemǁsortSubSets__mutmut_27(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = None

    def xǁSetCoverProblemǁsortSubSets__mutmut_28(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j + i] = tempInt
    
    xǁSetCoverProblemǁsortSubSets__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁsortSubSets__mutmut_1': xǁSetCoverProblemǁsortSubSets__mutmut_1, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_2': xǁSetCoverProblemǁsortSubSets__mutmut_2, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_3': xǁSetCoverProblemǁsortSubSets__mutmut_3, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_4': xǁSetCoverProblemǁsortSubSets__mutmut_4, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_5': xǁSetCoverProblemǁsortSubSets__mutmut_5, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_6': xǁSetCoverProblemǁsortSubSets__mutmut_6, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_7': xǁSetCoverProblemǁsortSubSets__mutmut_7, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_8': xǁSetCoverProblemǁsortSubSets__mutmut_8, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_9': xǁSetCoverProblemǁsortSubSets__mutmut_9, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_10': xǁSetCoverProblemǁsortSubSets__mutmut_10, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_11': xǁSetCoverProblemǁsortSubSets__mutmut_11, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_12': xǁSetCoverProblemǁsortSubSets__mutmut_12, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_13': xǁSetCoverProblemǁsortSubSets__mutmut_13, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_14': xǁSetCoverProblemǁsortSubSets__mutmut_14, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_15': xǁSetCoverProblemǁsortSubSets__mutmut_15, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_16': xǁSetCoverProblemǁsortSubSets__mutmut_16, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_17': xǁSetCoverProblemǁsortSubSets__mutmut_17, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_18': xǁSetCoverProblemǁsortSubSets__mutmut_18, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_19': xǁSetCoverProblemǁsortSubSets__mutmut_19, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_20': xǁSetCoverProblemǁsortSubSets__mutmut_20, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_21': xǁSetCoverProblemǁsortSubSets__mutmut_21, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_22': xǁSetCoverProblemǁsortSubSets__mutmut_22, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_23': xǁSetCoverProblemǁsortSubSets__mutmut_23, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_24': xǁSetCoverProblemǁsortSubSets__mutmut_24, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_25': xǁSetCoverProblemǁsortSubSets__mutmut_25, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_26': xǁSetCoverProblemǁsortSubSets__mutmut_26, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_27': xǁSetCoverProblemǁsortSubSets__mutmut_27, 
        'xǁSetCoverProblemǁsortSubSets__mutmut_28': xǁSetCoverProblemǁsortSubSets__mutmut_28
    }
    
    def sortSubSets(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁsortSubSets__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁsortSubSets__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sortSubSets.__signature__ = _mutmut_signature(xǁSetCoverProblemǁsortSubSets__mutmut_orig)
    xǁSetCoverProblemǁsortSubSets__mutmut_orig.__name__ = 'xǁSetCoverProblemǁsortSubSets'

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_orig(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(len(solution.subSets)):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_1(self, solution:Solution):
        self.bestSolution.nSolutionSize = None
        for i in range(len(solution.subSets)):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_2(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(None):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_3(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(len(solution.subSets)):
            self.bestSolution.subSets[i] = None
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_4(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(len(solution.subSets)):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(None):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_5(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(len(solution.subSets)):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = None
    
    xǁSetCoverProblemǁcopySolutionToBest__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁcopySolutionToBest__mutmut_1': xǁSetCoverProblemǁcopySolutionToBest__mutmut_1, 
        'xǁSetCoverProblemǁcopySolutionToBest__mutmut_2': xǁSetCoverProblemǁcopySolutionToBest__mutmut_2, 
        'xǁSetCoverProblemǁcopySolutionToBest__mutmut_3': xǁSetCoverProblemǁcopySolutionToBest__mutmut_3, 
        'xǁSetCoverProblemǁcopySolutionToBest__mutmut_4': xǁSetCoverProblemǁcopySolutionToBest__mutmut_4, 
        'xǁSetCoverProblemǁcopySolutionToBest__mutmut_5': xǁSetCoverProblemǁcopySolutionToBest__mutmut_5
    }
    
    def copySolutionToBest(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁcopySolutionToBest__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁcopySolutionToBest__mutmut_mutants"), args, kwargs, self)
        return result 
    
    copySolutionToBest.__signature__ = _mutmut_signature(xǁSetCoverProblemǁcopySolutionToBest__mutmut_orig)
    xǁSetCoverProblemǁcopySolutionToBest__mutmut_orig.__name__ = 'xǁSetCoverProblemǁcopySolutionToBest'

    def xǁSetCoverProblemǁbackTrack__mutmut_orig(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_1(self, solution:Solution):
        if solution.nSolutionSize > self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_2(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(None):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_3(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize <= self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_4(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(None)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_5(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(None):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_6(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(None, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_7(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, None) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_8(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_9(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, ) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_10(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) != False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_11(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == True):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_12(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(None, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_13(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, None)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_14(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_15(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, )
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_16(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth = 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_17(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth -= 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_18(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 2
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_19(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(None)
                self.depth -= 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_20(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth = 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_21(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth += 1
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_22(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 2
                self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_23(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(None, i)

    def xǁSetCoverProblemǁbackTrack__mutmut_24(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, None)

    def xǁSetCoverProblemǁbackTrack__mutmut_25(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(i)

    def xǁSetCoverProblemǁbackTrack__mutmut_26(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, )
    
    xǁSetCoverProblemǁbackTrack__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁbackTrack__mutmut_1': xǁSetCoverProblemǁbackTrack__mutmut_1, 
        'xǁSetCoverProblemǁbackTrack__mutmut_2': xǁSetCoverProblemǁbackTrack__mutmut_2, 
        'xǁSetCoverProblemǁbackTrack__mutmut_3': xǁSetCoverProblemǁbackTrack__mutmut_3, 
        'xǁSetCoverProblemǁbackTrack__mutmut_4': xǁSetCoverProblemǁbackTrack__mutmut_4, 
        'xǁSetCoverProblemǁbackTrack__mutmut_5': xǁSetCoverProblemǁbackTrack__mutmut_5, 
        'xǁSetCoverProblemǁbackTrack__mutmut_6': xǁSetCoverProblemǁbackTrack__mutmut_6, 
        'xǁSetCoverProblemǁbackTrack__mutmut_7': xǁSetCoverProblemǁbackTrack__mutmut_7, 
        'xǁSetCoverProblemǁbackTrack__mutmut_8': xǁSetCoverProblemǁbackTrack__mutmut_8, 
        'xǁSetCoverProblemǁbackTrack__mutmut_9': xǁSetCoverProblemǁbackTrack__mutmut_9, 
        'xǁSetCoverProblemǁbackTrack__mutmut_10': xǁSetCoverProblemǁbackTrack__mutmut_10, 
        'xǁSetCoverProblemǁbackTrack__mutmut_11': xǁSetCoverProblemǁbackTrack__mutmut_11, 
        'xǁSetCoverProblemǁbackTrack__mutmut_12': xǁSetCoverProblemǁbackTrack__mutmut_12, 
        'xǁSetCoverProblemǁbackTrack__mutmut_13': xǁSetCoverProblemǁbackTrack__mutmut_13, 
        'xǁSetCoverProblemǁbackTrack__mutmut_14': xǁSetCoverProblemǁbackTrack__mutmut_14, 
        'xǁSetCoverProblemǁbackTrack__mutmut_15': xǁSetCoverProblemǁbackTrack__mutmut_15, 
        'xǁSetCoverProblemǁbackTrack__mutmut_16': xǁSetCoverProblemǁbackTrack__mutmut_16, 
        'xǁSetCoverProblemǁbackTrack__mutmut_17': xǁSetCoverProblemǁbackTrack__mutmut_17, 
        'xǁSetCoverProblemǁbackTrack__mutmut_18': xǁSetCoverProblemǁbackTrack__mutmut_18, 
        'xǁSetCoverProblemǁbackTrack__mutmut_19': xǁSetCoverProblemǁbackTrack__mutmut_19, 
        'xǁSetCoverProblemǁbackTrack__mutmut_20': xǁSetCoverProblemǁbackTrack__mutmut_20, 
        'xǁSetCoverProblemǁbackTrack__mutmut_21': xǁSetCoverProblemǁbackTrack__mutmut_21, 
        'xǁSetCoverProblemǁbackTrack__mutmut_22': xǁSetCoverProblemǁbackTrack__mutmut_22, 
        'xǁSetCoverProblemǁbackTrack__mutmut_23': xǁSetCoverProblemǁbackTrack__mutmut_23, 
        'xǁSetCoverProblemǁbackTrack__mutmut_24': xǁSetCoverProblemǁbackTrack__mutmut_24, 
        'xǁSetCoverProblemǁbackTrack__mutmut_25': xǁSetCoverProblemǁbackTrack__mutmut_25, 
        'xǁSetCoverProblemǁbackTrack__mutmut_26': xǁSetCoverProblemǁbackTrack__mutmut_26
    }
    
    def backTrack(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack__mutmut_mutants"), args, kwargs, self)
        return result 
    
    backTrack.__signature__ = _mutmut_signature(xǁSetCoverProblemǁbackTrack__mutmut_orig)
    xǁSetCoverProblemǁbackTrack__mutmut_orig.__name__ = 'xǁSetCoverProblemǁbackTrack'

    def xǁSetCoverProblemǁbackTrack2__mutmut_orig(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_1(self, solution:Solution):

        if solution.nSolutionSize > self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_2(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(None)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_3(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize <= self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_4(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(None)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_5(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(None, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_6(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, None):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_7(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_8(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, ):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_9(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(None, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_10(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, None)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_11(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_12(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, )
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_13(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth = 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_14(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth -= 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_15(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 2
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_16(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(None)
            self.depth -= 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_17(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth = 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_18(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth += 1
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_19(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 2
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_20(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(None, i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_21(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, None)

    def xǁSetCoverProblemǁbackTrack2__mutmut_22(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(i)

    def xǁSetCoverProblemǁbackTrack2__mutmut_23(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, )
    
    xǁSetCoverProblemǁbackTrack2__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁbackTrack2__mutmut_1': xǁSetCoverProblemǁbackTrack2__mutmut_1, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_2': xǁSetCoverProblemǁbackTrack2__mutmut_2, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_3': xǁSetCoverProblemǁbackTrack2__mutmut_3, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_4': xǁSetCoverProblemǁbackTrack2__mutmut_4, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_5': xǁSetCoverProblemǁbackTrack2__mutmut_5, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_6': xǁSetCoverProblemǁbackTrack2__mutmut_6, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_7': xǁSetCoverProblemǁbackTrack2__mutmut_7, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_8': xǁSetCoverProblemǁbackTrack2__mutmut_8, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_9': xǁSetCoverProblemǁbackTrack2__mutmut_9, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_10': xǁSetCoverProblemǁbackTrack2__mutmut_10, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_11': xǁSetCoverProblemǁbackTrack2__mutmut_11, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_12': xǁSetCoverProblemǁbackTrack2__mutmut_12, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_13': xǁSetCoverProblemǁbackTrack2__mutmut_13, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_14': xǁSetCoverProblemǁbackTrack2__mutmut_14, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_15': xǁSetCoverProblemǁbackTrack2__mutmut_15, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_16': xǁSetCoverProblemǁbackTrack2__mutmut_16, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_17': xǁSetCoverProblemǁbackTrack2__mutmut_17, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_18': xǁSetCoverProblemǁbackTrack2__mutmut_18, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_19': xǁSetCoverProblemǁbackTrack2__mutmut_19, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_20': xǁSetCoverProblemǁbackTrack2__mutmut_20, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_21': xǁSetCoverProblemǁbackTrack2__mutmut_21, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_22': xǁSetCoverProblemǁbackTrack2__mutmut_22, 
        'xǁSetCoverProblemǁbackTrack2__mutmut_23': xǁSetCoverProblemǁbackTrack2__mutmut_23
    }
    
    def backTrack2(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack2__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack2__mutmut_mutants"), args, kwargs, self)
        return result 
    
    backTrack2.__signature__ = _mutmut_signature(xǁSetCoverProblemǁbackTrack2__mutmut_orig)
    xǁSetCoverProblemǁbackTrack2__mutmut_orig.__name__ = 'xǁSetCoverProblemǁbackTrack2'

    def xǁSetCoverProblemǁbackTrack3__mutmut_orig(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_1(self, solution:Solution, last:int):
        if solution.nSolutionSize > self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_2(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(None)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_3(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize <= self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_4(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(None)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_5(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(None, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_6(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, None):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_7(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_8(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, ):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_9(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(None, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_10(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, None)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_11(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_12(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, )
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_13(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(None, i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_14(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, None)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_15(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(i + 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_16(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, )
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_17(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i - 1)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_18(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 2)
            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_19(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(None, i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_20(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, None)

    def xǁSetCoverProblemǁbackTrack3__mutmut_21(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(i)

    def xǁSetCoverProblemǁbackTrack3__mutmut_22(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, )
    
    xǁSetCoverProblemǁbackTrack3__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁbackTrack3__mutmut_1': xǁSetCoverProblemǁbackTrack3__mutmut_1, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_2': xǁSetCoverProblemǁbackTrack3__mutmut_2, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_3': xǁSetCoverProblemǁbackTrack3__mutmut_3, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_4': xǁSetCoverProblemǁbackTrack3__mutmut_4, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_5': xǁSetCoverProblemǁbackTrack3__mutmut_5, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_6': xǁSetCoverProblemǁbackTrack3__mutmut_6, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_7': xǁSetCoverProblemǁbackTrack3__mutmut_7, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_8': xǁSetCoverProblemǁbackTrack3__mutmut_8, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_9': xǁSetCoverProblemǁbackTrack3__mutmut_9, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_10': xǁSetCoverProblemǁbackTrack3__mutmut_10, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_11': xǁSetCoverProblemǁbackTrack3__mutmut_11, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_12': xǁSetCoverProblemǁbackTrack3__mutmut_12, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_13': xǁSetCoverProblemǁbackTrack3__mutmut_13, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_14': xǁSetCoverProblemǁbackTrack3__mutmut_14, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_15': xǁSetCoverProblemǁbackTrack3__mutmut_15, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_16': xǁSetCoverProblemǁbackTrack3__mutmut_16, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_17': xǁSetCoverProblemǁbackTrack3__mutmut_17, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_18': xǁSetCoverProblemǁbackTrack3__mutmut_18, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_19': xǁSetCoverProblemǁbackTrack3__mutmut_19, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_20': xǁSetCoverProblemǁbackTrack3__mutmut_20, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_21': xǁSetCoverProblemǁbackTrack3__mutmut_21, 
        'xǁSetCoverProblemǁbackTrack3__mutmut_22': xǁSetCoverProblemǁbackTrack3__mutmut_22
    }
    
    def backTrack3(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack3__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack3__mutmut_mutants"), args, kwargs, self)
        return result 
    
    backTrack3.__signature__ = _mutmut_signature(xǁSetCoverProblemǁbackTrack3__mutmut_orig)
    xǁSetCoverProblemǁbackTrack3__mutmut_orig.__name__ = 'xǁSetCoverProblemǁbackTrack3'

    def xǁSetCoverProblemǁbackTrack4__mutmut_orig(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_1(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize > self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_2(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(None)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_3(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize <= self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_4(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(None)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_5(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(None, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_6(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, None):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_7(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_8(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, ):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_9(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum - self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_10(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1) + solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_11(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize + 1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_12(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-2)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_13(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] <= self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_14(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(None, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_15(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, None)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_16(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_17(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, )
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_18(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum = self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_19(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum -= self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_20(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(None, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_21(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, None, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_22(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, None)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_23(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_24(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_25(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, )
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_26(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i - 1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_27(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+2, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_28(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum = self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_29(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum += self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_30(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(None, i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_31(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, None)

    def xǁSetCoverProblemǁbackTrack4__mutmut_32(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(i)

    def xǁSetCoverProblemǁbackTrack4__mutmut_33(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, )
    
    xǁSetCoverProblemǁbackTrack4__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁbackTrack4__mutmut_1': xǁSetCoverProblemǁbackTrack4__mutmut_1, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_2': xǁSetCoverProblemǁbackTrack4__mutmut_2, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_3': xǁSetCoverProblemǁbackTrack4__mutmut_3, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_4': xǁSetCoverProblemǁbackTrack4__mutmut_4, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_5': xǁSetCoverProblemǁbackTrack4__mutmut_5, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_6': xǁSetCoverProblemǁbackTrack4__mutmut_6, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_7': xǁSetCoverProblemǁbackTrack4__mutmut_7, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_8': xǁSetCoverProblemǁbackTrack4__mutmut_8, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_9': xǁSetCoverProblemǁbackTrack4__mutmut_9, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_10': xǁSetCoverProblemǁbackTrack4__mutmut_10, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_11': xǁSetCoverProblemǁbackTrack4__mutmut_11, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_12': xǁSetCoverProblemǁbackTrack4__mutmut_12, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_13': xǁSetCoverProblemǁbackTrack4__mutmut_13, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_14': xǁSetCoverProblemǁbackTrack4__mutmut_14, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_15': xǁSetCoverProblemǁbackTrack4__mutmut_15, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_16': xǁSetCoverProblemǁbackTrack4__mutmut_16, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_17': xǁSetCoverProblemǁbackTrack4__mutmut_17, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_18': xǁSetCoverProblemǁbackTrack4__mutmut_18, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_19': xǁSetCoverProblemǁbackTrack4__mutmut_19, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_20': xǁSetCoverProblemǁbackTrack4__mutmut_20, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_21': xǁSetCoverProblemǁbackTrack4__mutmut_21, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_22': xǁSetCoverProblemǁbackTrack4__mutmut_22, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_23': xǁSetCoverProblemǁbackTrack4__mutmut_23, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_24': xǁSetCoverProblemǁbackTrack4__mutmut_24, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_25': xǁSetCoverProblemǁbackTrack4__mutmut_25, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_26': xǁSetCoverProblemǁbackTrack4__mutmut_26, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_27': xǁSetCoverProblemǁbackTrack4__mutmut_27, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_28': xǁSetCoverProblemǁbackTrack4__mutmut_28, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_29': xǁSetCoverProblemǁbackTrack4__mutmut_29, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_30': xǁSetCoverProblemǁbackTrack4__mutmut_30, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_31': xǁSetCoverProblemǁbackTrack4__mutmut_31, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_32': xǁSetCoverProblemǁbackTrack4__mutmut_32, 
        'xǁSetCoverProblemǁbackTrack4__mutmut_33': xǁSetCoverProblemǁbackTrack4__mutmut_33
    }
    
    def backTrack4(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack4__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack4__mutmut_mutants"), args, kwargs, self)
        return result 
    
    backTrack4.__signature__ = _mutmut_signature(xǁSetCoverProblemǁbackTrack4__mutmut_orig)
    xǁSetCoverProblemǁbackTrack4__mutmut_orig.__name__ = 'xǁSetCoverProblemǁbackTrack4'

    def xǁSetCoverProblemǁaddSubSet__mutmut_orig(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_1(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize = 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_2(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize -= 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_3(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 2
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_4(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = None

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_5(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize + 1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_6(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-2] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_7(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(None):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_8(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] = 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_9(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] -= 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_10(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] + 1] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_11(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-2] += 1

    def xǁSetCoverProblemǁaddSubSet__mutmut_12(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 2
    
    xǁSetCoverProblemǁaddSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁaddSubSet__mutmut_1': xǁSetCoverProblemǁaddSubSet__mutmut_1, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_2': xǁSetCoverProblemǁaddSubSet__mutmut_2, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_3': xǁSetCoverProblemǁaddSubSet__mutmut_3, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_4': xǁSetCoverProblemǁaddSubSet__mutmut_4, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_5': xǁSetCoverProblemǁaddSubSet__mutmut_5, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_6': xǁSetCoverProblemǁaddSubSet__mutmut_6, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_7': xǁSetCoverProblemǁaddSubSet__mutmut_7, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_8': xǁSetCoverProblemǁaddSubSet__mutmut_8, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_9': xǁSetCoverProblemǁaddSubSet__mutmut_9, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_10': xǁSetCoverProblemǁaddSubSet__mutmut_10, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_11': xǁSetCoverProblemǁaddSubSet__mutmut_11, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_12': xǁSetCoverProblemǁaddSubSet__mutmut_12
    }
    
    def addSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁaddSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁaddSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    addSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁaddSubSet__mutmut_orig)
    xǁSetCoverProblemǁaddSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁaddSubSet'


    def xǁSetCoverProblemǁremoveSubSet__mutmut_orig(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_1(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = None
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_2(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize + 1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_3(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-2] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_4(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = +1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_5(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -2
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_6(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize = 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_7(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize += 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_8(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 2

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_9(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(None):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_10(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] = 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_11(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] += 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_12(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] + 1] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_13(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 2] -= 1


    def xǁSetCoverProblemǁremoveSubSet__mutmut_14(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 2
    
    xǁSetCoverProblemǁremoveSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁremoveSubSet__mutmut_1': xǁSetCoverProblemǁremoveSubSet__mutmut_1, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_2': xǁSetCoverProblemǁremoveSubSet__mutmut_2, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_3': xǁSetCoverProblemǁremoveSubSet__mutmut_3, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_4': xǁSetCoverProblemǁremoveSubSet__mutmut_4, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_5': xǁSetCoverProblemǁremoveSubSet__mutmut_5, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_6': xǁSetCoverProblemǁremoveSubSet__mutmut_6, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_7': xǁSetCoverProblemǁremoveSubSet__mutmut_7, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_8': xǁSetCoverProblemǁremoveSubSet__mutmut_8, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_9': xǁSetCoverProblemǁremoveSubSet__mutmut_9, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_10': xǁSetCoverProblemǁremoveSubSet__mutmut_10, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_11': xǁSetCoverProblemǁremoveSubSet__mutmut_11, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_12': xǁSetCoverProblemǁremoveSubSet__mutmut_12, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_13': xǁSetCoverProblemǁremoveSubSet__mutmut_13, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_14': xǁSetCoverProblemǁremoveSubSet__mutmut_14
    }
    
    def removeSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁremoveSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁremoveSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    removeSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁremoveSubSet__mutmut_orig)
    xǁSetCoverProblemǁremoveSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁremoveSubSet'

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_orig(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(len(solution.subSets)):
            if solution.subSets[i] == subSetIndex:
                return True
            
        return False

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_1(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(None):
            if solution.subSets[i] == subSetIndex:
                return True
            
        return False

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_2(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(len(solution.subSets)):
            if solution.subSets[i] != subSetIndex:
                return True
            
        return False

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_3(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(len(solution.subSets)):
            if solution.subSets[i] == subSetIndex:
                return False
            
        return False

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_4(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(len(solution.subSets)):
            if solution.subSets[i] == subSetIndex:
                return True
            
        return True
    
    xǁSetCoverProblemǁcontainsSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁcontainsSubSet__mutmut_1': xǁSetCoverProblemǁcontainsSubSet__mutmut_1, 
        'xǁSetCoverProblemǁcontainsSubSet__mutmut_2': xǁSetCoverProblemǁcontainsSubSet__mutmut_2, 
        'xǁSetCoverProblemǁcontainsSubSet__mutmut_3': xǁSetCoverProblemǁcontainsSubSet__mutmut_3, 
        'xǁSetCoverProblemǁcontainsSubSet__mutmut_4': xǁSetCoverProblemǁcontainsSubSet__mutmut_4
    }
    
    def containsSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁcontainsSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁcontainsSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    containsSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁcontainsSubSet__mutmut_orig)
    xǁSetCoverProblemǁcontainsSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁcontainsSubSet'

    def xǁSetCoverProblemǁcheckSolution__mutmut_orig(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_1(self, solution:Solution) -> bool:
        allDone = None
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_2(self, solution:Solution) -> bool:
        allDone = False
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_3(self, solution:Solution) -> bool:
        allDone = True
        for i in range(None):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_4(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = None
            if boolInc == 0:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_5(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc != 0:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_6(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 1:
                return False
            
        return allDone

    def xǁSetCoverProblemǁcheckSolution__mutmut_7(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return True
            
        return allDone
    
    xǁSetCoverProblemǁcheckSolution__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁcheckSolution__mutmut_1': xǁSetCoverProblemǁcheckSolution__mutmut_1, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_2': xǁSetCoverProblemǁcheckSolution__mutmut_2, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_3': xǁSetCoverProblemǁcheckSolution__mutmut_3, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_4': xǁSetCoverProblemǁcheckSolution__mutmut_4, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_5': xǁSetCoverProblemǁcheckSolution__mutmut_5, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_6': xǁSetCoverProblemǁcheckSolution__mutmut_6, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_7': xǁSetCoverProblemǁcheckSolution__mutmut_7
    }
    
    def checkSolution(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁcheckSolution__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁcheckSolution__mutmut_mutants"), args, kwargs, self)
        return result 
    
    checkSolution.__signature__ = _mutmut_signature(xǁSetCoverProblemǁcheckSolution__mutmut_orig)
    xǁSetCoverProblemǁcheckSolution__mutmut_orig.__name__ = 'xǁSetCoverProblemǁcheckSolution'

    def xǁSetCoverProblemǁprintSolution__mutmut_orig(self, solution:Solution): # pragma: no cover
        print(solution.nSolutionSize)
        for i in range(solution.nSolutionSize):
            print(self.mainSet.originalOrder[solution.subSets[i]])
            self.printSubSet(solution.subSets[i])

    def xǁSetCoverProblemǁprintSolution__mutmut_1(self, solution:Solution): # pragma: no cover
        print(None)
        for i in range(solution.nSolutionSize):
            print(self.mainSet.originalOrder[solution.subSets[i]])
            self.printSubSet(solution.subSets[i])

    def xǁSetCoverProblemǁprintSolution__mutmut_2(self, solution:Solution): # pragma: no cover
        print(solution.nSolutionSize)
        for i in range(None):
            print(self.mainSet.originalOrder[solution.subSets[i]])
            self.printSubSet(solution.subSets[i])

    def xǁSetCoverProblemǁprintSolution__mutmut_3(self, solution:Solution): # pragma: no cover
        print(solution.nSolutionSize)
        for i in range(solution.nSolutionSize):
            print(None)
            self.printSubSet(solution.subSets[i])

    def xǁSetCoverProblemǁprintSolution__mutmut_4(self, solution:Solution): # pragma: no cover
        print(solution.nSolutionSize)
        for i in range(solution.nSolutionSize):
            print(self.mainSet.originalOrder[solution.subSets[i]])
            self.printSubSet(None)
    
    xǁSetCoverProblemǁprintSolution__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁprintSolution__mutmut_1': xǁSetCoverProblemǁprintSolution__mutmut_1, 
        'xǁSetCoverProblemǁprintSolution__mutmut_2': xǁSetCoverProblemǁprintSolution__mutmut_2, 
        'xǁSetCoverProblemǁprintSolution__mutmut_3': xǁSetCoverProblemǁprintSolution__mutmut_3, 
        'xǁSetCoverProblemǁprintSolution__mutmut_4': xǁSetCoverProblemǁprintSolution__mutmut_4
    }
    
    def printSolution(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁprintSolution__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁprintSolution__mutmut_mutants"), args, kwargs, self)
        return result 
    
    printSolution.__signature__ = _mutmut_signature(xǁSetCoverProblemǁprintSolution__mutmut_orig)
    xǁSetCoverProblemǁprintSolution__mutmut_orig.__name__ = 'xǁSetCoverProblemǁprintSolution'

    def xǁSetCoverProblemǁechoInit__mutmut_orig(self): # pragma: no cover
        print(f"Universal Set 1-{self.mainSet.nGlobalSetSize}\n")
        print(f"Number of subsets {self.mainSet.nSubSets}\n")
        for i in range(self.mainSet.nSubSets):
            self.printSubSet(i)

    def xǁSetCoverProblemǁechoInit__mutmut_1(self): # pragma: no cover
        print(None)
        print(f"Number of subsets {self.mainSet.nSubSets}\n")
        for i in range(self.mainSet.nSubSets):
            self.printSubSet(i)

    def xǁSetCoverProblemǁechoInit__mutmut_2(self): # pragma: no cover
        print(f"Universal Set 1-{self.mainSet.nGlobalSetSize}\n")
        print(None)
        for i in range(self.mainSet.nSubSets):
            self.printSubSet(i)

    def xǁSetCoverProblemǁechoInit__mutmut_3(self): # pragma: no cover
        print(f"Universal Set 1-{self.mainSet.nGlobalSetSize}\n")
        print(f"Number of subsets {self.mainSet.nSubSets}\n")
        for i in range(None):
            self.printSubSet(i)

    def xǁSetCoverProblemǁechoInit__mutmut_4(self): # pragma: no cover
        print(f"Universal Set 1-{self.mainSet.nGlobalSetSize}\n")
        print(f"Number of subsets {self.mainSet.nSubSets}\n")
        for i in range(self.mainSet.nSubSets):
            self.printSubSet(None)
    
    xǁSetCoverProblemǁechoInit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁechoInit__mutmut_1': xǁSetCoverProblemǁechoInit__mutmut_1, 
        'xǁSetCoverProblemǁechoInit__mutmut_2': xǁSetCoverProblemǁechoInit__mutmut_2, 
        'xǁSetCoverProblemǁechoInit__mutmut_3': xǁSetCoverProblemǁechoInit__mutmut_3, 
        'xǁSetCoverProblemǁechoInit__mutmut_4': xǁSetCoverProblemǁechoInit__mutmut_4
    }
    
    def echoInit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁechoInit__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁechoInit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    echoInit.__signature__ = _mutmut_signature(xǁSetCoverProblemǁechoInit__mutmut_orig)
    xǁSetCoverProblemǁechoInit__mutmut_orig.__name__ = 'xǁSetCoverProblemǁechoInit'

    def xǁSetCoverProblemǁprintSubSet__mutmut_orig(self, nSubSetIndex:int): # pragma: no cover
        for i in range(self.mainSet.nSubSetSizes[nSubSetIndex]):
            print(self.mainSet.subsets[nSubSetIndex][i])
        print("\n")

    def xǁSetCoverProblemǁprintSubSet__mutmut_1(self, nSubSetIndex:int): # pragma: no cover
        for i in range(None):
            print(self.mainSet.subsets[nSubSetIndex][i])
        print("\n")

    def xǁSetCoverProblemǁprintSubSet__mutmut_2(self, nSubSetIndex:int): # pragma: no cover
        for i in range(self.mainSet.nSubSetSizes[nSubSetIndex]):
            print(None)
        print("\n")

    def xǁSetCoverProblemǁprintSubSet__mutmut_3(self, nSubSetIndex:int): # pragma: no cover
        for i in range(self.mainSet.nSubSetSizes[nSubSetIndex]):
            print(self.mainSet.subsets[nSubSetIndex][i])
        print(None)

    def xǁSetCoverProblemǁprintSubSet__mutmut_4(self, nSubSetIndex:int): # pragma: no cover
        for i in range(self.mainSet.nSubSetSizes[nSubSetIndex]):
            print(self.mainSet.subsets[nSubSetIndex][i])
        print("XX\nXX")
    
    xǁSetCoverProblemǁprintSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁprintSubSet__mutmut_1': xǁSetCoverProblemǁprintSubSet__mutmut_1, 
        'xǁSetCoverProblemǁprintSubSet__mutmut_2': xǁSetCoverProblemǁprintSubSet__mutmut_2, 
        'xǁSetCoverProblemǁprintSubSet__mutmut_3': xǁSetCoverProblemǁprintSubSet__mutmut_3, 
        'xǁSetCoverProblemǁprintSubSet__mutmut_4': xǁSetCoverProblemǁprintSubSet__mutmut_4
    }
    
    def printSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁprintSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁprintSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    printSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁprintSubSet__mutmut_orig)
    xǁSetCoverProblemǁprintSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁprintSubSet'

def x_inthandler__mutmut_orig(signum, frame, setCover:SetCoverProblem): # pragma: no cover
        setCover.printSolution(setCover.bestSolution)
        exit(0)

def x_inthandler__mutmut_1(signum, frame, setCover:SetCoverProblem): # pragma: no cover
        setCover.printSolution(None)
        exit(0)

def x_inthandler__mutmut_2(signum, frame, setCover:SetCoverProblem): # pragma: no cover
        setCover.printSolution(setCover.bestSolution)
        exit(None)

def x_inthandler__mutmut_3(signum, frame, setCover:SetCoverProblem): # pragma: no cover
        setCover.printSolution(setCover.bestSolution)
        exit(1)

x_inthandler__mutmut_mutants : ClassVar[MutantDict] = {
'x_inthandler__mutmut_1': x_inthandler__mutmut_1, 
    'x_inthandler__mutmut_2': x_inthandler__mutmut_2, 
    'x_inthandler__mutmut_3': x_inthandler__mutmut_3
}

def inthandler(*args, **kwargs):
    result = _mutmut_trampoline(x_inthandler__mutmut_orig, x_inthandler__mutmut_mutants, args, kwargs)
    return result 

inthandler.__signature__ = _mutmut_signature(x_inthandler__mutmut_orig)
x_inthandler__mutmut_orig.__name__ = 'x_inthandler'

if __name__ == "__main__": # pragma: no cover

    cwd = Path.cwd()
    
    cwd = cwd

    filename = input("Enter your filename: ")

    timerUsed = input("Enter y for a 60s timer: ")

    if timerUsed == 'y':
        signal.signal(signal.SIGALRM, inthandler)
        signal.alarm(60)
    
    mainSet = Set()
    try:
        lineno = 0
        with open(cwd/f"tests/test_cases/{filename}.txt", 'r') as gameFile:
            line = gameFile.readline()
            while line != "":
                if lineno == 0:
                    mainSet.nGlobalSetSize = int(line)
                elif lineno == 1:
                    mainSet.nSubSets = int(line)
                    for i in range(mainSet.nSubSets):
                        mainSet.originalOrder.append(i + 1)
                else:
                    nums = line.split(" ")
                    int_nums = []
                    for num in nums: 
                        if num.replace("\n","") != "":
                            int_nums.append(int(num.replace("\n","")))
                        else:
                            nums.remove(num)    
                    subsetSize = len(nums)
                    mainSet.nSubSetSizes.append(subsetSize)
                    mainSet.subsets.append(int_nums)

                lineno += 1
                line = gameFile.readline()


    except Exception as e:
        print(e)
        print("Invalid Filename")
        exit(0)

    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet, mainSet.nSubSets-1)
    setCover = SetCoverProblem(mainSet, aSolution, bestSolution, 0)
    setCover.sortSubSets()

    setCover.greedy()
    setCover.backTrack4(setCover.aSolution, 0, 0)
    
    setCover.printSolution(setCover.bestSolution)
    print("\n")
    
