# cpt_frames_set_cover.py
# Complete Category-Partition Test Frames for Set Cover Solver

from dataclasses import dataclass
from typing import List


@dataclass
class SetCoverTestFrame:
    """Represents one CPT test frame."""
    name: str
    n_global: int
    subsets: List[List[int]]
    description: str

    def to_file_content(self) -> str:
        """
        Produces the .txt format expected by the SetCover solver:
        First line: number of universal elements
        Second line: number of subsets
        Following lines: subsets (space-separated element IDs)
        """
        lines = [str(self.n_global), str(len(self.subsets))]
        for subset in self.subsets:
            lines.append(" ".join(str(x) for x in subset))
        return "\n".join(lines) + "\n"



# Base CPT Frames 


FRAMES = [

    SetCoverTestFrame(
        name="single_subset_covers_all",
        n_global=5,
        subsets=[[1, 2, 3, 4, 5]],
        description="One subset covers the entire universe."
    ),

    SetCoverTestFrame(
        name="each_element_own_subset",
        n_global=4,
        subsets=[[1], [2], [3], [4]],
        description="Every element isolated; solution requires all subsets."
    ),

    SetCoverTestFrame(
        name="overlap_with_redundant_subset",
        n_global=4,
        subsets=[[1, 2], [2, 3, 4], [1, 2, 3, 4]],
        description="Redundant superset present; solver should still cover all elements."
    ),

    SetCoverTestFrame(
        name="element_in_many_subsets",
        n_global=5,
        subsets=[[1, 2], [2, 3], [2, 4, 5], [3, 4]],
        description="Element 2 appears frequently."
    ),

    SetCoverTestFrame(
        name="dense_overlap_large",
        n_global=7,
        subsets=[
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [4, 5, 6],
            [5, 6, 7],
            [1, 7]
        ],
        description="High overlap chain structure."
    ),

    SetCoverTestFrame(
        name="highly_redundant_large",
        n_global=8,
        subsets=[
            [1, 2, 3, 4],
            [3, 4, 5, 6],
            [1, 2, 5, 6],
            [7, 8],
            [1, 2, 3, 4, 5, 6]
        ],
        description="One large superset plus many overlap subsets."
    ),

    SetCoverTestFrame(
        name="multi_optimal_solutions",
        n_global=8,
        subsets=[
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [1, 5],
            [2, 6],
            [3, 7],
            [4, 8]
        ],
        description="Multiple different minimal solutions possible."
    ),

    SetCoverTestFrame(
        name="scale_20_elements",
        n_global=20,
        subsets=[
            list(range(1, 11)),
            list(range(11, 21)),
            [1, 5, 10, 15, 20],
            [2, 4, 6, 8, 18],
            [3, 7, 11, 14]
        ],
        description="Larger problem for stress-testing."
    ),

]


# NEW COVERAGE-BOOSTING CPT FRAMES


# 1. Greedy Tie-Breaker Branch
FRAMES.append(SetCoverTestFrame(
    name="greedy_tie_break",
    n_global=6,
    subsets=[
        [1, 2, 3],   # equal-size subset
        [4, 5, 6],   # equal-size subset
        [1, 6]       # distractor
    ],
    description="Greedy encounters subsets with equal coverage → tie-break branch."
))

# 2. Subset Adds Zero New Elements
FRAMES.append(SetCoverTestFrame(
    name="subset_adds_zero_new",
    n_global=5,
    subsets=[
        [1, 2, 3],
        [1],      # adds no new elements
        [2],      # adds no new elements
        [3, 4, 5]
    ],
    description="Tests greedy ignore-branch and backtracking zero-benefit branch."
))

# 3. Greedy Early Termination
FRAMES.append(SetCoverTestFrame(
    name="greedy_early_termination",
    n_global=7,
    subsets=[
        [1,2],
        [3],
        [4,5,6,7]  # completes universe
    ],
    description="Greedy should terminate early when full cover is achieved."
))

# 4. backTrack4() Pruning Branch
FRAMES.append(SetCoverTestFrame(
    name="backtrack_prune_branch",
    n_global=6,
    subsets=[
        [1,2,3,4,5,6],   # greedy finds perfect cover → UB=1
        [1], [2], [3], [4], [5], [6]
    ],
    description="Triggers prune branch in backtracking."
))

# 5. Backtracking No-Benefit Branch
FRAMES.append(SetCoverTestFrame(
    name="backtrack_no_benefit",
    n_global=5,
    subsets=[
        [1,2,3],
        [1], [2],      # provide zero benefit
        [3,4,5]
    ],
    description="Forces backtracking to explore no-benefit branches."
))

# 6. Sort Equal-Length Subsets Branch
FRAMES.append(SetCoverTestFrame(
    name="sorting_equal_length",
    n_global=6,
    subsets=[
        [1,2], [3,4], [5,6],  # equal sizes
        [1,3,5]
    ],
    description="Tests equal-size branch in sortSubSets()."
))

# 7. Deep Backtracking Case
FRAMES.append(SetCoverTestFrame(
    name="deep_backtracking_case",
    n_global=8,
    subsets=[
        [1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,8]
    ],
    description="Forces deep recursion in backtracking."
))

# 8. Impossible Coverage
FRAMES.append(SetCoverTestFrame(
    name="no_possible_cover",
    n_global=5,
    subsets=[
        [1,2],
        [3,4]   # cannot cover 5
    ],
    description="Tests branch where universe cannot be fully covered."
))

# 9. Redundant Superset
FRAMES.append(SetCoverTestFrame(
    name="redundant_superset",
    n_global=5,
    subsets=[
        [1,2,3,4,5],   # superset
        [1,2],
        [2,3],
        [3,4],
        [4,5]
    ],
    description="Tests redundant superset logic."
))

