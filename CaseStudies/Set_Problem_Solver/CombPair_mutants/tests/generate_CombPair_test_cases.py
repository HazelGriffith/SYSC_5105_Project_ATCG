# cpt_frames_set_cover.py
from dataclasses import dataclass
from pathlib import Path
from typing import List
import random

@dataclass
class SetCoverTestCase:
    """
    Represents a combinatorial pair-wise test case for the Set Cover problem.
    """
    name: str
    n_global: int
    subsets: List[List[int]]
    description: str = ""

    def to_file_content(self) -> str:
        """
        Convert this case into the text format expected by set_cover_problem.py:
        line 1: nGlobalSetSize
        line 2: nSubSets
        lines 3+: each subset (space-separated indices in 1..nGlobalSetSize)
        """
        lines = [
            str(self.n_global),
            str(len(self.subsets)),
        ]
        for subset in self.subsets:
            if subset:
                lines.append(" ".join(str(x) for x in subset))
            else:
                # allow empty subset line if needed
                lines.append("")
        return "\n".join(lines) + "\n"


# ---------- Category-Partition Test Frames ----------
'''
input parameters identified: n = gobal set size, m = number of subsets, t = subset size trend
n and m independently do not influence the problem behaviour much, but relative to each other they are important
CATEGORIES: n < m | n = m | n > m
            t = big to low | t = low to big | t = uniform small | t = uniform large
COMBINATIONS: 
    (n < m & t = big to low)
    (n < m & t = low to big)
    (n < m & t = uniform small)
    (n < m & t = uniform big)

    (n = m & t = big to low)
    (n = m & t = low to big)
    (n = m & t = uniform small)
    (n = m & t = uniform big)

    (n > m & t = big to low)
    (n > m & t = low to big)
    (n > m & t = uniform small)
    (n > m & t = uniform big)

CONSTRAINTS:
    0 < n < 30 (max 30 is used to avoid timeout)
    0 < m < 30 (same as above)
    0 < size of any subset < n
'''
def generate_test_case(filename:str, n:int, m:int, firstHalfSizes:int, secondHalfSizes:int) ->SetCoverTestCase:
    try:

        assert (int(m/2)*firstHalfSizes+int(m/2)*secondHalfSizes) >= n
        list_of_subsets = []
        global_set = list(range(1,n+1))
        for i in range(int(m/2)):
            subset = []
            for j in range(firstHalfSizes):
                if len(global_set) > 0:
                    element_index = random.randint(0,len(global_set)-1)
                    subset.append(global_set.pop(element_index))
                else:
                    random_element = random.randint(1,n)
                    while random_element in subset:
                        random_element = random.randint(1,n)
                    subset.append(random_element)
            list_of_subsets.append(subset)
        
        for i in range(int(m/2)):
            subset = []
            for j in range(secondHalfSizes):
                if len(global_set) > 0:
                    element_index = random.randint(0,len(global_set)-1)
                    subset.append(global_set.pop(element_index))
                else:
                    random_element = random.randint(1,n)
                    while random_element in subset:
                        random_element = random.randint(1,n)
                    subset.append(random_element)
            list_of_subsets.append(subset)
        assert len(global_set) == 0
        return SetCoverTestCase(filename,n,list_of_subsets)
    except AssertionError as e:
        print(f"the generated problem cannot be solved")
        return None


def setup_param_1(max_value:int, category:int):
    if category == 1:
        # n < m
        n_global = random.randint(2,max_value-3) # 1 < n_global < max_value-5
        n_subsets = random.randint(n_global, max_value) # n_global < n_subsets < max_value
    elif category == 2:
        # n = m
        n_global = random.randint(2,max_value) # 1 < n_global < max_value-5
        n_subsets = n_global # n_global = n_subsets
    else:
        # n > m
        n_global = random.randint(5,max_value) # 1 < n_global < max_value-5
        n_subsets = random.randint(2, n_global-1) # n_global < n_subsets < max_value
    return n_global, n_subsets

def setup_param_2(n_global:int, category:int):
    big_subset_size = random.randint(int(n_global*(2/3)),n_global) # 2*n_global/3 < big_subset_size < n_global
    if (n_global >= 6):
        small_subset_size = random.randint(1,int(n_global/3)) # 1 < small_subset_size < n_global/3
    else:
        small_subset_size = 1
    if category == 1:
        # t = big to low
        return big_subset_size, small_subset_size
    elif category == 2:
        # t = low to big
        return small_subset_size, big_subset_size
    elif category == 3:
        # t = uniform small
        return small_subset_size, small_subset_size
    else:
        # t = uniform big
        return big_subset_size, big_subset_size
'''

'''
def generate_test_cases(max_value:int, num_tests_per_frame:int):
    tests = []
    param1_categories = [1,2,3]
    param2_categories = [1,2,3,4]
    for i in range(num_tests_per_frame):
        for param1_category in param1_categories:
            for param2_category in param2_categories:
                n_global, n_subsets = setup_param_1(max_value,param1_category)
                firstHalfSize,secondHalfSize = setup_param_2(n_global,param2_category)
                tests.append(generate_test_case(f"frame1_{i}_p1_{param1_category}_p2_{param2_category}", n_global, n_subsets, firstHalfSize, secondHalfSize))
    return tests

def write_test_cases_as_files(output_dir: Path, tests) -> List[Path]:
    """
    Write each FRAMES instance as a .txt file in output_dir and
    return the list of paths.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: List[Path] = []
    for test in tests:
        if test is not None:
            path = output_dir / f"{test.name}.txt"
            path.write_text(test.to_file_content(), encoding="utf-8")
            paths.append(path)
    return paths

if __name__ == "__main__":
    tests = generate_test_cases(15,3)
    cwd = Path.cwd()
    comb_pair_tests_dir = cwd / f"tests/test_cases/comb_pair_tests/"

    print(write_test_cases_as_files(comb_pair_tests_dir, tests))