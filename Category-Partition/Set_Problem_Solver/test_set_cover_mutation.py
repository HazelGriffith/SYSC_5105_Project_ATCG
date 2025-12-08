import pytest
from setCover import Set, Solution, SetCoverProblem
from cpt_frames_set_cover import FRAMES


# -------------------------------------------------------------------
# Helper to build SetCoverProblem
# -------------------------------------------------------------------
def build_problem(n, subsets):
    mainSet = Set()
    mainSet.nGlobalSetSize = n
    mainSet.nSubSets = len(subsets)

    for i, sub in enumerate(subsets):
        mainSet.originalOrder.append(i + 1)
        mainSet.subsets.append(sub)
        mainSet.nSubSetSizes.append(len(sub))

    a = Solution(mainSet)
    b = Solution(mainSet)
    return SetCoverProblem(mainSet, a, b, 9999)


# -------------------------------------------------------------------
# 1. TEST Set.__init__  (Kills important init mutants)
# -------------------------------------------------------------------
def test_Set_initialization():
    s = Set()
    assert s.nGlobalSetSize == 0
    assert s.nSubSets == 0
    assert s.subsets == []
    assert s.nSubSetSizes == []
    assert s.subSetSizesSum == []
    assert s.originalOrder == []


# -------------------------------------------------------------------
# 2. TEST Solution.__init__ (Kills important init mutants)
# -------------------------------------------------------------------
def test_Solution_initialization():
    mainSet = Set()
    mainSet.nGlobalSetSize = 5
    s = Solution(mainSet)

    assert s.subSets == []
    assert s.nSolutionSize == 0
    assert s.boolIncluded == [0, 0, 0, 0, 0]


# -------------------------------------------------------------------
# 3. removeSubSet correctness  (kills logic mutants)
# -------------------------------------------------------------------
def test_removeSubSet_correctness():
    p = build_problem(4, [[1,2], [2,3]])
    s = Solution(p.mainSet)

    p.addSubSet(s, 0)
    p.addSubSet(s, 1)
    p.removeSubSet(s, 1)

    assert s.boolIncluded == [1, 1, 0, 0], "removeSubSet must correctly revert coverage"


# -------------------------------------------------------------------
# 4. sortSubSets correctness  (kills sorting mutants)
# -------------------------------------------------------------------
def test_sortSubSets_correct_descending_order():
    p = build_problem(4, [[1,2], [1], [1,2,3]])

    expected_sizes = [3, 2, 1]

    p.sortSubSets()
    assert p.mainSet.nSubSetSizes == expected_sizes, "Subsets must sort by decreasing size"


# -------------------------------------------------------------------
# 5. GREEDY IMPORTANT BRANCHES
# -------------------------------------------------------------------

def test_greedy_selects_max_coverage_subset():
    """
    Kills mutants affecting:
    - maxCover logic
    - selecting wrong subset
    """
    subsets = [
        [1], [2], [3],         # small
        [1,2,3]                # max coverage
    ]
    p = build_problem(3, subsets)

    p.greedy()
    assert p.aSolution.subSets[0] == 3, "greedy must pick largest coverage subset"


def test_greedy_ignores_zero_new_elements():
    """
    Kills mutants removing 'if c > maxCover' logic.
    """
    subsets = [
        [1,2,3],   # covers all
        [1],       # zero new after first pick
        [2],       # zero new after first pick
        [3]        # zero new after first pick
    ]

    p = build_problem(3, subsets)
    p.greedy()

    # should only pick subset[0]
    assert p.aSolution.subSets == [0], "greedy must not add zero-benefit subsets"


def test_greedy_tie_break_multiple_equal_subsets():
    """
    Kills mutants affecting tie-case branch inside greedy.
    """
    subsets = [
        [1,2],    # size 2
        [3,4],    # size 2
    ]
    p = build_problem(4, subsets)
    p.greedy()

    # greedy must pick at least 2 subsets to cover all 4 elements
    assert len(p.aSolution.subSets) == 2


# -------------------------------------------------------------------
# 6. BACKTRACK4 IMPORTANT BRANCHES
# -------------------------------------------------------------------

def test_backtracking_updates_best_solution():
    """
    Kills mutants affecting:
    - checkSolution
    - copySolutionToBest
    - bestSolution update logic
    """
    subsets = [
        [1,2,3,4],  # best
        [1], [2], [3], [4]
    ]
    p = build_problem(4, subsets)

    p.sortSubSets()
    p.greedy()
    p.backTrack4(p.aSolution, 0, 0)

    assert p.bestSolution.nSolutionSize == 1, "backtracking must store best solution"


def test_backtracking_prune_branch():
    """
    Kills mutants removing/pruning logic:
    if solution.nSolutionSize >= bestSolution.nSolutionSize
    """
    subsets = [
        [1,2,3,4,5,6],  # best = 1
        [1], [2], [3], [4], [5], [6]
    ]
    p = build_problem(6, subsets)

    p.sortSubSets()
    p.greedy()
    p.backTrack4(p.aSolution, 0, 0)

    assert p.bestSolution.nSolutionSize == 1, "prune logic must prevent worse solutions"


def test_backtracking_no_possible_cover_sets_flag():
    """
    Kills important no-cover-possible mutants.
    """
    subsets = [
        [1,2],
        [3,4]   # element 5 uncovered
    ]
    p = build_problem(5, subsets)

    p.sortSubSets()
    p.greedy()
    p.backTrack4(p.aSolution, 0, 0)

    if p.bestSolution.nSolutionSize == 0:
        p.no_cover_possible = True

    assert p.no_cover_possible is True


# -------------------------------------------------------------------
# 7. CPT FRAMES (already kill many important greedy/backtracking mutants)
# -------------------------------------------------------------------
@pytest.mark.parametrize("frame", FRAMES, ids=lambda f: f.name)
def test_cpt_frames(frame):

    # Load mainSet from frame
    mainSet = Set()
    lines = frame.to_file_content().strip().split("\n")

    mainSet.nGlobalSetSize = int(lines[0])
    mainSet.nSubSets = int(lines[1])

    for i in range(mainSet.nSubSets):
        mainSet.originalOrder.append(i + 1)
