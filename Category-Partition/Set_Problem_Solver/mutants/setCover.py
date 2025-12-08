# ========================================================================
# FINAL PASSING VERSION – Compatible with test_set_cover_cpt.py
# ========================================================================

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
class Set:
    def xǁSetǁ__init____mutmut_orig(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_1(self):
        self.nGlobalSetSize = None
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_2(self):
        self.nGlobalSetSize = 1
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_3(self):
        self.nGlobalSetSize = 0
        self.nSubSets = None
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_4(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 1
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_5(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 0
        self.subsets = None
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_6(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = None
        self.subSetSizesSum = []
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_7(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = None
        self.originalOrder = []
    def xǁSetǁ__init____mutmut_8(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = None
    
    xǁSetǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetǁ__init____mutmut_1': xǁSetǁ__init____mutmut_1, 
        'xǁSetǁ__init____mutmut_2': xǁSetǁ__init____mutmut_2, 
        'xǁSetǁ__init____mutmut_3': xǁSetǁ__init____mutmut_3, 
        'xǁSetǁ__init____mutmut_4': xǁSetǁ__init____mutmut_4, 
        'xǁSetǁ__init____mutmut_5': xǁSetǁ__init____mutmut_5, 
        'xǁSetǁ__init____mutmut_6': xǁSetǁ__init____mutmut_6, 
        'xǁSetǁ__init____mutmut_7': xǁSetǁ__init____mutmut_7, 
        'xǁSetǁ__init____mutmut_8': xǁSetǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSetǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSetǁ__init____mutmut_orig)
    xǁSetǁ__init____mutmut_orig.__name__ = 'xǁSetǁ__init__'


class Solution:
    def xǁSolutionǁ__init____mutmut_orig(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = [0] * mainSet.nGlobalSetSize
    def xǁSolutionǁ__init____mutmut_1(self, mainSet, preset_size=1):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = [0] * mainSet.nGlobalSetSize
    def xǁSolutionǁ__init____mutmut_2(self, mainSet, preset_size=0):
        self.mainSet = None
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = [0] * mainSet.nGlobalSetSize
    def xǁSolutionǁ__init____mutmut_3(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = None
        self.nSolutionSize = preset_size
        self.boolIncluded = [0] * mainSet.nGlobalSetSize
    def xǁSolutionǁ__init____mutmut_4(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = None
        self.boolIncluded = [0] * mainSet.nGlobalSetSize
    def xǁSolutionǁ__init____mutmut_5(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = None
    def xǁSolutionǁ__init____mutmut_6(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = [0] / mainSet.nGlobalSetSize
    def xǁSolutionǁ__init____mutmut_7(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = [1] * mainSet.nGlobalSetSize
    
    xǁSolutionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSolutionǁ__init____mutmut_1': xǁSolutionǁ__init____mutmut_1, 
        'xǁSolutionǁ__init____mutmut_2': xǁSolutionǁ__init____mutmut_2, 
        'xǁSolutionǁ__init____mutmut_3': xǁSolutionǁ__init____mutmut_3, 
        'xǁSolutionǁ__init____mutmut_4': xǁSolutionǁ__init____mutmut_4, 
        'xǁSolutionǁ__init____mutmut_5': xǁSolutionǁ__init____mutmut_5, 
        'xǁSolutionǁ__init____mutmut_6': xǁSolutionǁ__init____mutmut_6, 
        'xǁSolutionǁ__init____mutmut_7': xǁSolutionǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSolutionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSolutionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSolutionǁ__init____mutmut_orig)
    xǁSolutionǁ__init____mutmut_orig.__name__ = 'xǁSolutionǁ__init__'


class SetCoverProblem:
    def xǁSetCoverProblemǁ__init____mutmut_orig(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = False
    def xǁSetCoverProblemǁ__init____mutmut_1(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = None
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = False
    def xǁSetCoverProblemǁ__init____mutmut_2(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = None
        self.bestSolution = bestSolution
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = False
    def xǁSetCoverProblemǁ__init____mutmut_3(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = None
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = False
    def xǁSetCoverProblemǁ__init____mutmut_4(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.bestSize = None

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = False
    def xǁSetCoverProblemǁ__init____mutmut_5(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = None
    def xǁSetCoverProblemǁ__init____mutmut_6(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = True
    
    xǁSetCoverProblemǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁ__init____mutmut_1': xǁSetCoverProblemǁ__init____mutmut_1, 
        'xǁSetCoverProblemǁ__init____mutmut_2': xǁSetCoverProblemǁ__init____mutmut_2, 
        'xǁSetCoverProblemǁ__init____mutmut_3': xǁSetCoverProblemǁ__init____mutmut_3, 
        'xǁSetCoverProblemǁ__init____mutmut_4': xǁSetCoverProblemǁ__init____mutmut_4, 
        'xǁSetCoverProblemǁ__init____mutmut_5': xǁSetCoverProblemǁ__init____mutmut_5, 
        'xǁSetCoverProblemǁ__init____mutmut_6': xǁSetCoverProblemǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSetCoverProblemǁ__init____mutmut_orig)
    xǁSetCoverProblemǁ__init____mutmut_orig.__name__ = 'xǁSetCoverProblemǁ__init__'

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_orig(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] += 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_1(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(None)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] += 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_2(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = None
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] += 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_3(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] = 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_4(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] -= 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_5(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v + 1] += 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_6(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 2] += 1

    # ============================================================
    def xǁSetCoverProblemǁaddSubSet__mutmut_7(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] += 2
    
    xǁSetCoverProblemǁaddSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁaddSubSet__mutmut_1': xǁSetCoverProblemǁaddSubSet__mutmut_1, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_2': xǁSetCoverProblemǁaddSubSet__mutmut_2, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_3': xǁSetCoverProblemǁaddSubSet__mutmut_3, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_4': xǁSetCoverProblemǁaddSubSet__mutmut_4, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_5': xǁSetCoverProblemǁaddSubSet__mutmut_5, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_6': xǁSetCoverProblemǁaddSubSet__mutmut_6, 
        'xǁSetCoverProblemǁaddSubSet__mutmut_7': xǁSetCoverProblemǁaddSubSet__mutmut_7
    }
    
    def addSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁaddSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁaddSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    addSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁaddSubSet__mutmut_orig)
    xǁSetCoverProblemǁaddSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁaddSubSet'

    def xǁSetCoverProblemǁremoveSubSet__mutmut_orig(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] -= 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_1(self, solution: Solution, subSetIndex: int):
        if subSetIndex not in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] -= 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_2(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(None)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] -= 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_3(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = None
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] -= 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_4(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] = 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_5(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] += 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_6(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v + 1] -= 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_7(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 2] -= 1

    def xǁSetCoverProblemǁremoveSubSet__mutmut_8(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] -= 2
    
    xǁSetCoverProblemǁremoveSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁremoveSubSet__mutmut_1': xǁSetCoverProblemǁremoveSubSet__mutmut_1, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_2': xǁSetCoverProblemǁremoveSubSet__mutmut_2, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_3': xǁSetCoverProblemǁremoveSubSet__mutmut_3, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_4': xǁSetCoverProblemǁremoveSubSet__mutmut_4, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_5': xǁSetCoverProblemǁremoveSubSet__mutmut_5, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_6': xǁSetCoverProblemǁremoveSubSet__mutmut_6, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_7': xǁSetCoverProblemǁremoveSubSet__mutmut_7, 
        'xǁSetCoverProblemǁremoveSubSet__mutmut_8': xǁSetCoverProblemǁremoveSubSet__mutmut_8
    }
    
    def removeSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁremoveSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁremoveSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    removeSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁremoveSubSet__mutmut_orig)
    xǁSetCoverProblemǁremoveSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁremoveSubSet'

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_orig(self, solution: Solution):
        self.bestSolution.subSets = list(solution.subSets)
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        self.bestSolution.boolIncluded = list(solution.boolIncluded)

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_1(self, solution: Solution):
        self.bestSolution.subSets = None
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        self.bestSolution.boolIncluded = list(solution.boolIncluded)

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_2(self, solution: Solution):
        self.bestSolution.subSets = list(None)
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        self.bestSolution.boolIncluded = list(solution.boolIncluded)

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_3(self, solution: Solution):
        self.bestSolution.subSets = list(solution.subSets)
        self.bestSolution.nSolutionSize = None
        self.bestSolution.boolIncluded = list(solution.boolIncluded)

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_4(self, solution: Solution):
        self.bestSolution.subSets = list(solution.subSets)
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        self.bestSolution.boolIncluded = None

    def xǁSetCoverProblemǁcopySolutionToBest__mutmut_5(self, solution: Solution):
        self.bestSolution.subSets = list(solution.subSets)
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        self.bestSolution.boolIncluded = list(None)
    
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

    def xǁSetCoverProblemǁcheckSolution__mutmut_orig(self, solution: Solution):
        for i in range(self.mainSet.nGlobalSetSize):
            if solution.boolIncluded[i] == 0:
                return False
        return True

    def xǁSetCoverProblemǁcheckSolution__mutmut_1(self, solution: Solution):
        for i in range(None):
            if solution.boolIncluded[i] == 0:
                return False
        return True

    def xǁSetCoverProblemǁcheckSolution__mutmut_2(self, solution: Solution):
        for i in range(self.mainSet.nGlobalSetSize):
            if solution.boolIncluded[i] != 0:
                return False
        return True

    def xǁSetCoverProblemǁcheckSolution__mutmut_3(self, solution: Solution):
        for i in range(self.mainSet.nGlobalSetSize):
            if solution.boolIncluded[i] == 1:
                return False
        return True

    def xǁSetCoverProblemǁcheckSolution__mutmut_4(self, solution: Solution):
        for i in range(self.mainSet.nGlobalSetSize):
            if solution.boolIncluded[i] == 0:
                return True
        return True

    def xǁSetCoverProblemǁcheckSolution__mutmut_5(self, solution: Solution):
        for i in range(self.mainSet.nGlobalSetSize):
            if solution.boolIncluded[i] == 0:
                return False
        return False
    
    xǁSetCoverProblemǁcheckSolution__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁcheckSolution__mutmut_1': xǁSetCoverProblemǁcheckSolution__mutmut_1, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_2': xǁSetCoverProblemǁcheckSolution__mutmut_2, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_3': xǁSetCoverProblemǁcheckSolution__mutmut_3, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_4': xǁSetCoverProblemǁcheckSolution__mutmut_4, 
        'xǁSetCoverProblemǁcheckSolution__mutmut_5': xǁSetCoverProblemǁcheckSolution__mutmut_5
    }
    
    def checkSolution(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁcheckSolution__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁcheckSolution__mutmut_mutants"), args, kwargs, self)
        return result 
    
    checkSolution.__signature__ = _mutmut_signature(xǁSetCoverProblemǁcheckSolution__mutmut_orig)
    xǁSetCoverProblemǁcheckSolution__mutmut_orig.__name__ = 'xǁSetCoverProblemǁcheckSolution'

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_orig(self, solution: Solution, idx: int):
        return idx in solution.subSets

    def xǁSetCoverProblemǁcontainsSubSet__mutmut_1(self, solution: Solution, idx: int):
        return idx not in solution.subSets
    
    xǁSetCoverProblemǁcontainsSubSet__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSetCoverProblemǁcontainsSubSet__mutmut_1': xǁSetCoverProblemǁcontainsSubSet__mutmut_1
    }
    
    def containsSubSet(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁcontainsSubSet__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁcontainsSubSet__mutmut_mutants"), args, kwargs, self)
        return result 
    
    containsSubSet.__signature__ = _mutmut_signature(xǁSetCoverProblemǁcontainsSubSet__mutmut_orig)
    xǁSetCoverProblemǁcontainsSubSet__mutmut_orig.__name__ = 'xǁSetCoverProblemǁcontainsSubSet'

    def xǁSetCoverProblemǁsortSubSets__mutmut_orig(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_1(self):
        zipped = None
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_2(self):
        zipped = list(None)
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_3(self):
        zipped = list(zip(None,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_4(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          None,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_5(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          None))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_6(self):
        zipped = list(zip(self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_7(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_8(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          ))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_9(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=None, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_10(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=None)
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_11(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_12(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, )
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_13(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=False, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_14(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: None)
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_15(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[1])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_16(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = None

    def xǁSetCoverProblemǁsortSubSets__mutmut_17(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(None, zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_18(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, None)

    def xǁSetCoverProblemǁsortSubSets__mutmut_19(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(zip(*zipped))

    def xǁSetCoverProblemǁsortSubSets__mutmut_20(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, )
    
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
        'xǁSetCoverProblemǁsortSubSets__mutmut_20': xǁSetCoverProblemǁsortSubSets__mutmut_20
    }
    
    def sortSubSets(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁsortSubSets__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁsortSubSets__mutmut_mutants"), args, kwargs, self)
        return result 
    
    sortSubSets.__signature__ = _mutmut_signature(xǁSetCoverProblemǁsortSubSets__mutmut_orig)
    xǁSetCoverProblemǁsortSubSets__mutmut_orig.__name__ = 'xǁSetCoverProblemǁsortSubSets'

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_orig(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_1(self):
        while False:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_2(self):
        while True:
            maxCover = None
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_3(self):
        while True:
            maxCover = 1
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_4(self):
        while True:
            maxCover = 0
            addIndex = None

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_5(self):
        while True:
            maxCover = 0
            addIndex = +1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_6(self):
        while True:
            maxCover = 0
            addIndex = -2

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_7(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(None):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_8(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = None
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_9(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 1
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_10(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem + 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_11(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 2] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_12(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] != 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_13(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 1:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_14(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c = 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_15(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c -= 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_16(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 2
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_17(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c >= maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_18(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = None
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_19(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = None

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_20(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 and maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_21(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex != -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_22(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == +1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_23(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -2 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_24(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover != 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_25(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 1:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_26(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(None, addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_27(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, None)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_28(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(addIndex)

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def xǁSetCoverProblemǁgreedy__mutmut_29(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, )
    
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
        'xǁSetCoverProblemǁgreedy__mutmut_29': xǁSetCoverProblemǁgreedy__mutmut_29
    }
    
    def greedy(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁgreedy__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁgreedy__mutmut_mutants"), args, kwargs, self)
        return result 
    
    greedy.__signature__ = _mutmut_signature(xǁSetCoverProblemǁgreedy__mutmut_orig)
    xǁSetCoverProblemǁgreedy__mutmut_orig.__name__ = 'xǁSetCoverProblemǁgreedy'

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_orig(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_1(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(None):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_2(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 and solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_3(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize != 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_4(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 1 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_5(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize <= self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_6(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(None)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_7(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 or solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_8(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize == 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_9(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 1 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_10(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize > self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_11(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(None, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_12(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, None):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_13(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_14(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, ):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_15(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i not in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_16(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                break
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_17(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(None, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_18(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, None)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_19(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_20(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, )
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_21(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(None, depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_22(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, None, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_23(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, None)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_24(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(depth + 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_25(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_26(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, )
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_27(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth - 1, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_28(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 2, i)
            self.removeSubSet(solution, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_29(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(None, i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_30(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, None)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_31(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(i)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def xǁSetCoverProblemǁbackTrack4__mutmut_32(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
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
        'xǁSetCoverProblemǁbackTrack4__mutmut_32': xǁSetCoverProblemǁbackTrack4__mutmut_32
    }
    
    def backTrack4(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack4__mutmut_orig"), object.__getattribute__(self, "xǁSetCoverProblemǁbackTrack4__mutmut_mutants"), args, kwargs, self)
        return result 
    
    backTrack4.__signature__ = _mutmut_signature(xǁSetCoverProblemǁbackTrack4__mutmut_orig)
    xǁSetCoverProblemǁbackTrack4__mutmut_orig.__name__ = 'xǁSetCoverProblemǁbackTrack4'


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_orig(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_1(mainSet: Set) -> SetCoverProblem:
    aSolution = None
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_2(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(None)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_3(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = None
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_4(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(None)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_5(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = None

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_6(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(None, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_7(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, None, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_8(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, None, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_9(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, None)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_10(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_11(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_12(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_13(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, )

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_14(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 10000)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_15(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(None, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_16(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, None, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_17(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, None)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_18(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_19(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_20(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, )

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_21(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 1, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_22(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 1)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_23(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize != 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_24(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 1:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_25(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = None

    return problem


# ========================================================================
# Helper for pytest
# ========================================================================
def x_solve_set_cover__mutmut_26(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = False

    return problem

x_solve_set_cover__mutmut_mutants : ClassVar[MutantDict] = {
'x_solve_set_cover__mutmut_1': x_solve_set_cover__mutmut_1, 
    'x_solve_set_cover__mutmut_2': x_solve_set_cover__mutmut_2, 
    'x_solve_set_cover__mutmut_3': x_solve_set_cover__mutmut_3, 
    'x_solve_set_cover__mutmut_4': x_solve_set_cover__mutmut_4, 
    'x_solve_set_cover__mutmut_5': x_solve_set_cover__mutmut_5, 
    'x_solve_set_cover__mutmut_6': x_solve_set_cover__mutmut_6, 
    'x_solve_set_cover__mutmut_7': x_solve_set_cover__mutmut_7, 
    'x_solve_set_cover__mutmut_8': x_solve_set_cover__mutmut_8, 
    'x_solve_set_cover__mutmut_9': x_solve_set_cover__mutmut_9, 
    'x_solve_set_cover__mutmut_10': x_solve_set_cover__mutmut_10, 
    'x_solve_set_cover__mutmut_11': x_solve_set_cover__mutmut_11, 
    'x_solve_set_cover__mutmut_12': x_solve_set_cover__mutmut_12, 
    'x_solve_set_cover__mutmut_13': x_solve_set_cover__mutmut_13, 
    'x_solve_set_cover__mutmut_14': x_solve_set_cover__mutmut_14, 
    'x_solve_set_cover__mutmut_15': x_solve_set_cover__mutmut_15, 
    'x_solve_set_cover__mutmut_16': x_solve_set_cover__mutmut_16, 
    'x_solve_set_cover__mutmut_17': x_solve_set_cover__mutmut_17, 
    'x_solve_set_cover__mutmut_18': x_solve_set_cover__mutmut_18, 
    'x_solve_set_cover__mutmut_19': x_solve_set_cover__mutmut_19, 
    'x_solve_set_cover__mutmut_20': x_solve_set_cover__mutmut_20, 
    'x_solve_set_cover__mutmut_21': x_solve_set_cover__mutmut_21, 
    'x_solve_set_cover__mutmut_22': x_solve_set_cover__mutmut_22, 
    'x_solve_set_cover__mutmut_23': x_solve_set_cover__mutmut_23, 
    'x_solve_set_cover__mutmut_24': x_solve_set_cover__mutmut_24, 
    'x_solve_set_cover__mutmut_25': x_solve_set_cover__mutmut_25, 
    'x_solve_set_cover__mutmut_26': x_solve_set_cover__mutmut_26
}

def solve_set_cover(*args, **kwargs):
    result = _mutmut_trampoline(x_solve_set_cover__mutmut_orig, x_solve_set_cover__mutmut_mutants, args, kwargs)
    return result 

solve_set_cover.__signature__ = _mutmut_signature(x_solve_set_cover__mutmut_orig)
x_solve_set_cover__mutmut_orig.__name__ = 'x_solve_set_cover'


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_orig():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_1():
    print(None)
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_2():
    print("XXThis program solves the set cover problem.XX")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_3():
    print("this program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_4():
    print("THIS PROGRAM SOLVES THE SET COVER PROBLEM.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_5():
    print("This program solves the set cover problem.")
    x = None
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_6():
    print("This program solves the set cover problem.")
    x = input(None)
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_7():
    print("This program solves the set cover problem.")
    x = input("XXFile name: XX")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_8():
    print("This program solves the set cover problem.")
    x = input("file name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_9():
    print("This program solves the set cover problem.")
    x = input("FILE NAME: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_10():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = None

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_11():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x - ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_12():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" - x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_13():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "XXtests/XX" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_14():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "TESTS/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_15():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + "XX.txtXX"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_16():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".TXT"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_17():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = None

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_18():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(None, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_19():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, None) as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_20():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open("r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_21():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, ) as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_22():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "XXrXX") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_23():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "R") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_24():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = None

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_25():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = None
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_26():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(None)
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_27():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[1])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_28():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = None

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_29():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(None)

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_30():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[2])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_31():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(None):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_32():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(None)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_33():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i - 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_34():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 2)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_35():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = None
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_36():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(None)
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_37():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(None, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_38():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, None))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_39():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_40():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, ))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_41():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 - i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_42():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[3 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_43():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(None)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_44():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(None)

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_45():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print(None)
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_46():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("XXFile not found.XX")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_47():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("file not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_48():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("FILE NOT FOUND.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_49():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = None
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_50():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(None)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_51():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = None
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_52():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(None)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_53():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = None

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_54():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(None, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_55():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, None, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_56():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, None, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_57():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, None)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_58():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_59():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_60():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_61():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, )

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_62():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 10000)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_63():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(None, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_64():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, None, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_65():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, None)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_66():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_67():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_68():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, )

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_69():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 1, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_70():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 1)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_71():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print(None, b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_72():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", None)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_73():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print(b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_74():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", )
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_75():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("XX\nBest Solution Size:XX", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_76():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nbest solution size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_77():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBEST SOLUTION SIZE:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_78():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print(None, [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_79():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", None)


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_80():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print([mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_81():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", )


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_82():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("XXSubsets chosen:XX", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_83():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


# ========================================================================
# Main program (unchanged)
# ========================================================================
def x_main__mutmut_84():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("SUBSETS CHOSEN:", [mainSet.originalOrder[i] for i in b.subSets])

x_main__mutmut_mutants : ClassVar[MutantDict] = {
'x_main__mutmut_1': x_main__mutmut_1, 
    'x_main__mutmut_2': x_main__mutmut_2, 
    'x_main__mutmut_3': x_main__mutmut_3, 
    'x_main__mutmut_4': x_main__mutmut_4, 
    'x_main__mutmut_5': x_main__mutmut_5, 
    'x_main__mutmut_6': x_main__mutmut_6, 
    'x_main__mutmut_7': x_main__mutmut_7, 
    'x_main__mutmut_8': x_main__mutmut_8, 
    'x_main__mutmut_9': x_main__mutmut_9, 
    'x_main__mutmut_10': x_main__mutmut_10, 
    'x_main__mutmut_11': x_main__mutmut_11, 
    'x_main__mutmut_12': x_main__mutmut_12, 
    'x_main__mutmut_13': x_main__mutmut_13, 
    'x_main__mutmut_14': x_main__mutmut_14, 
    'x_main__mutmut_15': x_main__mutmut_15, 
    'x_main__mutmut_16': x_main__mutmut_16, 
    'x_main__mutmut_17': x_main__mutmut_17, 
    'x_main__mutmut_18': x_main__mutmut_18, 
    'x_main__mutmut_19': x_main__mutmut_19, 
    'x_main__mutmut_20': x_main__mutmut_20, 
    'x_main__mutmut_21': x_main__mutmut_21, 
    'x_main__mutmut_22': x_main__mutmut_22, 
    'x_main__mutmut_23': x_main__mutmut_23, 
    'x_main__mutmut_24': x_main__mutmut_24, 
    'x_main__mutmut_25': x_main__mutmut_25, 
    'x_main__mutmut_26': x_main__mutmut_26, 
    'x_main__mutmut_27': x_main__mutmut_27, 
    'x_main__mutmut_28': x_main__mutmut_28, 
    'x_main__mutmut_29': x_main__mutmut_29, 
    'x_main__mutmut_30': x_main__mutmut_30, 
    'x_main__mutmut_31': x_main__mutmut_31, 
    'x_main__mutmut_32': x_main__mutmut_32, 
    'x_main__mutmut_33': x_main__mutmut_33, 
    'x_main__mutmut_34': x_main__mutmut_34, 
    'x_main__mutmut_35': x_main__mutmut_35, 
    'x_main__mutmut_36': x_main__mutmut_36, 
    'x_main__mutmut_37': x_main__mutmut_37, 
    'x_main__mutmut_38': x_main__mutmut_38, 
    'x_main__mutmut_39': x_main__mutmut_39, 
    'x_main__mutmut_40': x_main__mutmut_40, 
    'x_main__mutmut_41': x_main__mutmut_41, 
    'x_main__mutmut_42': x_main__mutmut_42, 
    'x_main__mutmut_43': x_main__mutmut_43, 
    'x_main__mutmut_44': x_main__mutmut_44, 
    'x_main__mutmut_45': x_main__mutmut_45, 
    'x_main__mutmut_46': x_main__mutmut_46, 
    'x_main__mutmut_47': x_main__mutmut_47, 
    'x_main__mutmut_48': x_main__mutmut_48, 
    'x_main__mutmut_49': x_main__mutmut_49, 
    'x_main__mutmut_50': x_main__mutmut_50, 
    'x_main__mutmut_51': x_main__mutmut_51, 
    'x_main__mutmut_52': x_main__mutmut_52, 
    'x_main__mutmut_53': x_main__mutmut_53, 
    'x_main__mutmut_54': x_main__mutmut_54, 
    'x_main__mutmut_55': x_main__mutmut_55, 
    'x_main__mutmut_56': x_main__mutmut_56, 
    'x_main__mutmut_57': x_main__mutmut_57, 
    'x_main__mutmut_58': x_main__mutmut_58, 
    'x_main__mutmut_59': x_main__mutmut_59, 
    'x_main__mutmut_60': x_main__mutmut_60, 
    'x_main__mutmut_61': x_main__mutmut_61, 
    'x_main__mutmut_62': x_main__mutmut_62, 
    'x_main__mutmut_63': x_main__mutmut_63, 
    'x_main__mutmut_64': x_main__mutmut_64, 
    'x_main__mutmut_65': x_main__mutmut_65, 
    'x_main__mutmut_66': x_main__mutmut_66, 
    'x_main__mutmut_67': x_main__mutmut_67, 
    'x_main__mutmut_68': x_main__mutmut_68, 
    'x_main__mutmut_69': x_main__mutmut_69, 
    'x_main__mutmut_70': x_main__mutmut_70, 
    'x_main__mutmut_71': x_main__mutmut_71, 
    'x_main__mutmut_72': x_main__mutmut_72, 
    'x_main__mutmut_73': x_main__mutmut_73, 
    'x_main__mutmut_74': x_main__mutmut_74, 
    'x_main__mutmut_75': x_main__mutmut_75, 
    'x_main__mutmut_76': x_main__mutmut_76, 
    'x_main__mutmut_77': x_main__mutmut_77, 
    'x_main__mutmut_78': x_main__mutmut_78, 
    'x_main__mutmut_79': x_main__mutmut_79, 
    'x_main__mutmut_80': x_main__mutmut_80, 
    'x_main__mutmut_81': x_main__mutmut_81, 
    'x_main__mutmut_82': x_main__mutmut_82, 
    'x_main__mutmut_83': x_main__mutmut_83, 
    'x_main__mutmut_84': x_main__mutmut_84
}

def main(*args, **kwargs):
    result = _mutmut_trampoline(x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs)
    return result 

main.__signature__ = _mutmut_signature(x_main__mutmut_orig)
x_main__mutmut_orig.__name__ = 'x_main'


if __name__ == "__main__":
    main()
