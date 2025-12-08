from source.setCover import SetCoverProblem, Solution, Set
from pathlib import Path
import os, signal, pytest



relabeling_transforms_per_problem = {}
add_one_element_transforms_per_problem = {}
add_redundant_sets_transforms_per_problem = {}
seed_solutions = {}

'''
Reads a problem file and obtains the mainSet object needed to represent and process it
args: filename = string
returns: mainSet = Set 
'''
def setup_problem(filename:str) -> Set:
    mainSet = Set()
    directory = Path.cwd()/"tests/test_cases/"
    try:
        lineno = 0
        with open(directory/f"{filename}.txt", 'r') as gameFile:
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

    return mainSet

def time_out_handler(signum, frame):
    raise Exception("Timed out")

def solve_problem(mainSet:Set, backTrackVersion:int):
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet, mainSet.nSubSets-1)
    setCover = SetCoverProblem(mainSet, aSolution, bestSolution, 0)
    setCover.sortSubSets()
    signal.signal(signal.SIGALRM, time_out_handler)
    signal.alarm(20)
    try:
        setCover.greedy()
        if (backTrackVersion == 1):
            setCover.backTrack(setCover.aSolution)
        elif (backTrackVersion == 2):
            setCover.backTrack2(setCover.aSolution)
        elif (backTrackVersion == 3):
            setCover.backTrack3(setCover.aSolution, 0)
        elif (backTrackVersion == 4):
            setCover.backTrack4(setCover.aSolution, 0, 0)
        else:
            assert False, "Unsupported Back Track Function Version"
        signal.alarm(0)
        timedOut = False
    except Exception as e:
        print(e)
        timedOut = True

    ResultingSolution = setCover.bestSolution
    aSolution = None
    bestSolution = None
    setCover = None
    return ResultingSolution, timedOut

cwd = Path.cwd()
print(cwd)
testEntries = os.listdir(cwd/"tests/test_cases/tests_used/")

for entry in testEntries:
    filename = entry.replace(".txt","")
    mainSet = setup_problem(f"tests_used/{filename}")
    seed_solution_1, seed_timedOut_1 = solve_problem(mainSet,1)
    seed_solution_2, seed_timedOut_2 = solve_problem(mainSet,2)
    seed_solution_3, seed_timedOut_3 = solve_problem(mainSet,3)
    seed_solution_4, seed_timedOut_4 = solve_problem(mainSet,4)

    relabeling_problem_folder = f"transformed_problem_files/{filename}_transformations/relabeling/"
    relabeling_problem_files = os.listdir(cwd/f"tests/test_cases/{relabeling_problem_folder}")

    for num, prob in enumerate(relabeling_problem_files):
        relabeling_transforms_per_problem.update({f"{filename} {str(num)}" : {"seed_solution_1" : seed_solution_1, "seed_timedOut_1" : seed_timedOut_1, 
                                                                              "seed_solution_2" : seed_solution_2, "seed_timedOut_2" : seed_timedOut_2, 
                                                                              "seed_solution_3" : seed_solution_3, "seed_timedOut_3" : seed_timedOut_3, 
                                                                              "seed_solution_4" : seed_solution_4, "seed_timedOut_4" : seed_timedOut_4, 
                                                                              "gen_prob_filename" : relabeling_problem_folder + prob.replace(".txt",""), "seed_prob_filename" : filename}})

    add_one_element_transforms_per_problem.update({filename : {"seed_solution_1" : seed_solution_1, "seed_timedOut_1" : seed_timedOut_1,
                                                               "seed_solution_2" : seed_solution_2, "seed_timedOut_2" : seed_timedOut_2, 
                                                               "seed_solution_3" : seed_solution_3, "seed_timedOut_3" : seed_timedOut_3, 
                                                               "seed_solution_4" : seed_solution_4, "seed_timedOut_4" : seed_timedOut_4, 
                                                               "gen_prob_filename" : f"transformed_problem_files/{filename}_transformations/add_new_element", "seed_prob_filename" : filename}})

    add_redundant_sets_problem_folder = f"transformed_problem_files/{filename}_transformations/add_redundant_sets/"
    add_redundant_sets_problem_files = os.listdir("tests/test_cases/"+add_redundant_sets_problem_folder)

    for num, prob in enumerate(add_redundant_sets_problem_files):
        add_redundant_sets_transforms_per_problem.update({f"{filename} {str(num)}" : {"seed_solution_1" : seed_solution_1, "seed_timedOut_1" : seed_timedOut_1,
                                                                                      "seed_solution_2" : seed_solution_2, "seed_timedOut_2" : seed_timedOut_2, 
                                                                                      "seed_solution_3" : seed_solution_3, "seed_timedOut_3" : seed_timedOut_3, 
                                                                                      "seed_solution_4" : seed_solution_4, "seed_timedOut_4" : seed_timedOut_4,  
                                                                                      "gen_prob_filename" : add_redundant_sets_problem_folder + prob.replace(".txt",""), "seed_prob_filename" : filename}})


def pytest_generate_tests(metafunc):

    if "get_add_one_element" in metafunc.fixturenames:
        test_ids = list(add_one_element_transforms_per_problem.keys())
        test_values = list(add_one_element_transforms_per_problem.values())

        metafunc.parametrize("get_add_one_element", test_values, ids=test_ids)

    if "get_relabeling" in metafunc.fixturenames:
        test_ids = list(relabeling_transforms_per_problem.keys())
        test_values = list(relabeling_transforms_per_problem.values())

        metafunc.parametrize("get_relabeling", test_values, ids=test_ids)

    if "get_add_redundant_sets" in metafunc.fixturenames:
        test_ids = list(add_redundant_sets_transforms_per_problem.keys())
        test_values = list(add_redundant_sets_transforms_per_problem.values())

        metafunc.parametrize("get_add_redundant_sets", test_values, ids=test_ids)

def test_add_one_element_v1(get_add_one_element):
    transformed_problem_file = get_add_one_element["gen_prob_filename"]
    original_problem_file = get_add_one_element["seed_prob_filename"]
    
    
    seed_solution_size = get_add_one_element["seed_solution_1"].nSolutionSize
    seed_timedOut = get_add_one_element["seed_timedOut_1"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 1)
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        assert(gen_solution_size >= seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {original_problem_file}, add_one_element"
    else:
        assert(gen_solution_size == seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_one_element"
    
    seed_solution = get_add_one_element["seed_solution_1"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"


def test_add_one_element_v2(get_add_one_element):
    transformed_problem_file = get_add_one_element["gen_prob_filename"]
    original_problem_file = get_add_one_element["seed_prob_filename"]
    
    seed_solution_size = get_add_one_element["seed_solution_2"].nSolutionSize
    seed_timedOut = get_add_one_element["seed_timedOut_2"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 2)
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        assert(gen_solution_size >= seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {original_problem_file}, add_one_element"
    else:
        assert(gen_solution_size == seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_one_element"

    seed_solution = get_add_one_element["seed_solution_2"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_add_one_element_v3(get_add_one_element):
    transformed_problem_file = get_add_one_element["gen_prob_filename"]
    original_problem_file = get_add_one_element["seed_prob_filename"]
    
    seed_solution_size = get_add_one_element["seed_solution_3"].nSolutionSize
    seed_timedOut = get_add_one_element["seed_timedOut_3"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 3)
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        assert(gen_solution_size >= seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {original_problem_file}, add_one_element"
    else:
        assert(gen_solution_size == seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_one_element"

    seed_solution = get_add_one_element["seed_solution_3"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_add_one_element_v4(get_add_one_element):
    transformed_problem_file = get_add_one_element["gen_prob_filename"]
    original_problem_file = get_add_one_element["seed_prob_filename"]
    
    seed_solution_size = get_add_one_element["seed_solution_4"].nSolutionSize
    seed_timedOut = get_add_one_element["seed_timedOut_4"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 4)
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        assert(gen_solution_size >= seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {original_problem_file}, add_one_element"
    else:
        assert(gen_solution_size == seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_one_element"

    seed_solution = get_add_one_element["seed_solution_4"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_relabeling_v1(get_relabeling):
    transformed_problem_file = get_relabeling["gen_prob_filename"]
    original_problem_file = get_relabeling["seed_prob_filename"]
    
    seed_solution_size = get_relabeling["seed_solution_1"].nSolutionSize
    seed_timedOut = get_relabeling["seed_timedOut_1"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 1)
    gen_solution_size = gen_solution.nSolutionSize

    if not(seed_timedOut or gen_timedOut):
        assert(gen_solution_size == seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, relabeling {transformed_problem_file}"

    seed_solution = get_relabeling["seed_solution_1"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_relabeling_v2(get_relabeling):
    transformed_problem_file = get_relabeling["gen_prob_filename"]
    original_problem_file = get_relabeling["seed_prob_filename"]
    
    seed_solution_size = get_relabeling["seed_solution_2"].nSolutionSize
    seed_timedOut = get_relabeling["seed_timedOut_2"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 2)
    gen_solution_size = gen_solution.nSolutionSize

    if not(seed_timedOut or gen_timedOut):
        assert(gen_solution_size == seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, relabeling {transformed_problem_file}"

    seed_solution = get_relabeling["seed_solution_2"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_relabeling_v3(get_relabeling):
    transformed_problem_file = get_relabeling["gen_prob_filename"]
    original_problem_file = get_relabeling["seed_prob_filename"]
    
    seed_solution_size = get_relabeling["seed_solution_3"].nSolutionSize
    seed_timedOut = get_relabeling["seed_timedOut_3"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 3)
    gen_solution_size = gen_solution.nSolutionSize

    if not(seed_timedOut or gen_timedOut):
        assert(gen_solution_size == seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, relabeling {transformed_problem_file}"

    seed_solution = get_relabeling["seed_solution_3"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_relabeling_v4(get_relabeling):
    transformed_problem_file = get_relabeling["gen_prob_filename"]
    original_problem_file = get_relabeling["seed_prob_filename"]
    
    seed_solution_size = get_relabeling["seed_solution_4"].nSolutionSize
    seed_timedOut = get_relabeling["seed_timedOut_4"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 4)
    gen_solution_size = gen_solution.nSolutionSize

    if not(seed_timedOut or gen_timedOut):
        assert(gen_solution_size == seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, relabeling {transformed_problem_file}"

    seed_solution = get_relabeling["seed_solution_4"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_add_redundant_set_v1(get_add_redundant_sets):
    transformed_problem_file = get_add_redundant_sets["gen_prob_filename"]
    original_problem_file = get_add_redundant_sets["seed_prob_filename"]
    
    seed_solution_size = get_add_redundant_sets["seed_solution_1"].nSolutionSize
    seed_timedOut = get_add_redundant_sets["seed_timedOut_1"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 1)
    gen_solution_size = gen_solution.nSolutionSize

    assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_redundant_sets {transformed_problem_file}"

    seed_solution = get_add_redundant_sets["seed_solution_1"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_add_redundant_set_v2(get_add_redundant_sets):
    transformed_problem_file = get_add_redundant_sets["gen_prob_filename"]
    original_problem_file = get_add_redundant_sets["seed_prob_filename"]
    
    seed_solution_size = get_add_redundant_sets["seed_solution_2"].nSolutionSize
    seed_timedOut = get_add_redundant_sets["seed_timedOut_2"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 2)
    gen_solution_size = gen_solution.nSolutionSize

    assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_redundant_sets {transformed_problem_file}"

    seed_solution = get_add_redundant_sets["seed_solution_2"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_add_redundant_set_v3(get_add_redundant_sets):
    transformed_problem_file = get_add_redundant_sets["gen_prob_filename"]
    original_problem_file = get_add_redundant_sets["seed_prob_filename"]
    
    seed_solution_size = get_add_redundant_sets["seed_solution_3"].nSolutionSize
    seed_timedOut = get_add_redundant_sets["seed_timedOut_3"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 3)
    gen_solution_size = gen_solution.nSolutionSize

    assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_redundant_sets {transformed_problem_file}"

    seed_solution = get_add_redundant_sets["seed_solution_3"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_add_redundant_set_v4(get_add_redundant_sets):
    transformed_problem_file = get_add_redundant_sets["gen_prob_filename"]
    original_problem_file = get_add_redundant_sets["seed_prob_filename"]
    
    seed_solution_size = get_add_redundant_sets["seed_solution_4"].nSolutionSize
    seed_timedOut = get_add_redundant_sets["seed_timedOut_4"]
    
    gen_solution, gen_timedOut = solve_problem(setup_problem(transformed_problem_file), 4)
    gen_solution_size = gen_solution.nSolutionSize

    assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_redundant_sets {transformed_problem_file}"

    seed_solution = get_add_redundant_sets["seed_solution_4"]
    solutions = [seed_solution, gen_solution]
    for solution in solutions:
        toRemove = []
        for i in solution.subSets:
            if i == -1:
                toRemove.append(i)
        for j in toRemove:
            solution.subSets.remove(j)
        assert (len(solution.subSets) == solution.nSolutionSize), f"solution subsets: {solution.subSets}"
        count = 0
        for i in solution.boolIncluded:
            if i == 1:
                count += 1
        assert (count >= 1), "BoolIncluded is not incrementing by ones"