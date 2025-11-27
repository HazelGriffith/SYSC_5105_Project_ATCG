from ..src.setCover import SetCoverProblem, Solution, Set
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
    try:
        lineno = 0
        with open("tests/"+filename+".txt", 'r') as gameFile:
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

def solve_problem(filename:str):
    mainSet = setup_problem(filename)
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet, mainSet.nSubSets-1)
    setCover = SetCoverProblem(mainSet, aSolution, bestSolution, 0)
    setCover.sortSubSets()
    signal.signal(signal.SIGALRM, time_out_handler)
    signal.alarm(20)

    try:
        setCover.greedy()
        setCover.backTrack4(setCover.aSolution, 0, 0)
        timedOut = False
    except Exception as e:
        print(e)
        timedOut = True

    return setCover.bestSolution, timedOut

cwd = os.getcwd()
if cwd.endswith("ATCG"):
    os.chdir("CaseStudies/Set_Problem_Solver")
elif cwd.endswith("Studies"):
    os.chdir("Set_Problem_Solver")

testEntries = os.listdir("tests/tests_used/")

for entry in testEntries:
    filename = entry.replace(".txt","")
    seed_solution, seed_timedOut = solve_problem(f"tests_used/{filename}")

    relabeling_problem_folder = f"transformed_problem_files/{filename}_transformations/relabeling/"
    relabeling_problem_files = os.listdir("tests/"+relabeling_problem_folder)

    for num, prob in enumerate(relabeling_problem_files):
        relabeling_transforms_per_problem.update({f"{filename} {str(num)}" : {"seed_solution" : seed_solution, "seed_timedOut" : seed_timedOut, "gen_prob_filename" : relabeling_problem_folder + prob.replace(".txt",""), "seed_prob_filename" : filename}})

    add_one_element_transforms_per_problem.update({filename : {"seed_solution" : seed_solution, "seed_timedOut" : seed_timedOut, "gen_prob_filename" : f"transformed_problem_files/{filename}_transformations/add_new_element", "seed_prob_filename" : filename}})

    add_redundant_sets_problem_folder = f"transformed_problem_files/{filename}_transformations/add_redundant_sets/"
    add_redundant_sets_problem_files = os.listdir("tests/"+add_redundant_sets_problem_folder)

    for num, prob in enumerate(add_redundant_sets_problem_files):
        add_redundant_sets_transforms_per_problem.update({f"{filename} {str(num)}" : {"seed_solution" : seed_solution, "seed_timedOut" : seed_timedOut, "gen_prob_filename" : add_redundant_sets_problem_folder + prob.replace(".txt",""), "seed_prob_filename" : filename}})


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

def test_add_one_element(get_add_one_element):
    transformed_problem_file = get_add_one_element["gen_prob_filename"]
    original_problem_file = get_add_one_element["seed_prob_filename"]
    
    seed_solution_size = get_add_one_element["seed_solution"].nSolutionSize
    seed_timedOut = get_add_one_element["seed_timedOut"]
    
    gen_solution, gen_timedOut = solve_problem(transformed_problem_file)
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        assert(gen_solution_size >= seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {original_problem_file}, add_one_element"
    else:
        assert(gen_solution_size == seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, add_one_element"

def test_relabeling(get_relabeling):
    transformed_problem_file = get_relabeling["gen_prob_filename"]
    original_problem_file = get_relabeling["seed_prob_filename"]
    
    seed_solution_size = get_relabeling["seed_solution"].nSolutionSize
    seed_timedOut = get_relabeling["seed_timedOut"]
    
    gen_solution, gen_timedOut = solve_problem(transformed_problem_file)
    gen_solution_size = gen_solution.nSolutionSize

    if not(seed_timedOut or gen_timedOut):
        assert(gen_solution_size == seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {original_problem_file}, relabeling {transformed_problem_file[-1]}"

def test_add_redundant_set(get_add_redundant_sets):
    transformed_problem_file = get_add_redundant_sets["gen_prob_filename"]
    original_problem_file = get_add_redundant_sets["seed_prob_filename"]
    
    seed_solution_size = get_add_redundant_sets["seed_solution"].nSolutionSize
    seed_timedOut = get_add_redundant_sets["seed_timedOut"]
    
    gen_solution, gen_timedOut = solve_problem(transformed_problem_file)
    gen_solution_size = gen_solution.nSolutionSize

    assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {original_problem_file}, add_redundant_sets {transformed_problem_file[-1]}"