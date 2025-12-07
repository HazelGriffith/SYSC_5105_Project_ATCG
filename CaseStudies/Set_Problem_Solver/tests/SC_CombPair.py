from source.setCover import SetCoverProblem, Solution, Set
from pathlib import Path
import os, signal, pytest

tests = {}

'''
Reads a problem file and obtains the mainSet object needed to represent and process it
args: filename = string
returns: mainSet = Set 
'''
def setup_problem(filename:str) -> Set:
    mainSet = Set()
    directory = Path.cwd()/"tests/test_cases/comb_pair_tests/"
    try:
        lineno = 0
        with open(directory / f"{filename}.txt", 'r') as gameFile:
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

'''
Raises a 'timed out' exception when an alarm rings from the signal class
'''
def time_out_handler(signum, frame):
    raise Exception("Timed out")

'''
Solves the given minimal set cover problem using the given back track algorithm version
Returns the solution object and a boolean that is true if it timed out, and false otherwise
args: mainSet = Set, backTrackVersion = int
returns: solution, timedOut = bool
'''
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

'''
This section loads the dictionary of tests for PyTest along with the correct answers for each test
'''
cwd = Path.cwd()
testEntries = os.listdir(cwd / "tests/test_cases/comb_pair_tests/")

for entry in testEntries:
    filename = entry.replace(".txt","")
    mainSet = setup_problem(filename)
    answer_list = []
    with open(cwd / f"tests/test_cases/answers/{filename}.txt", 'r') as answerFile:
        line = answerFile.readline()
        while line != "":
            answer_list.append(int(line.replace("\n","")))
            line = answerFile.readline()
    tests.update({filename : {"set" : mainSet, "answer" : answer_list}})

'''
This PyTest function collects all of the tests stored in the tests dictionary and parametrizes each test for each entry of the dictionary
'''
def pytest_generate_tests(metafunc):

    if "get_tests" in metafunc.fixturenames:
        test_ids = list(tests.keys())
        test_values = list(tests.values())

        metafunc.parametrize("get_tests", test_values, ids=test_ids)

'''
These functions run the source code with each back track version on the given test-case and compare the solution received with the correct solution
args: get_tests tells PyTest to pass the parametrized tests dictionary 
'''
def test_set_cover_solver_v1(get_tests):
    mainSet = get_tests["set"]
    answer = get_tests["answer"]
    solution, timedout = solve_problem(mainSet.copy(), 1)
    #checks if the solution size matches the correct solution size
    assert (solution.nSolutionSize == len(answer)), f"solution subsets: {solution.subSets}"
    toRemove = []
    for i in solution.subSets:
        if i == -1:
            toRemove.append(i)
    for j in toRemove:
        solution.subSets.remove(j)
    #checks if the solution's list of subsets has the same size as the correct answer
    assert (len(solution.subSets) == len(answer)), f"solution subsets: {solution.subSets}"
    count = 0
    for i in range(len(solution.boolIncluded)):
        if i == 1:
            count += 1
    #Checks that at least one entry in Boolincluded is equal to 1
    #otherwise it is not incrementing by or it is not the optimal solution
    assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_set_cover_solver_v2(get_tests):
    mainSet = get_tests["set"]
    answer = get_tests["answer"]
    solution, timedout = solve_problem(mainSet.copy(), 2)
    #checks if the solution size matches the correct solution size
    assert (solution.nSolutionSize == len(answer)), f"solution subsets: {solution.subSets}"
    toRemove = []
    for i in solution.subSets:
        if i == -1:
            toRemove.append(i)
    for j in toRemove:
        solution.subSets.remove(j)
    #checks if the solution's list of subsets has the same size as the correct answer
    assert (len(solution.subSets) == len(answer)), f"solution subsets: {solution.subSets}"
    count = 0
    for i in range(len(solution.boolIncluded)):
        if i == 1:
            count += 1
    #Checks that at least one entry in Boolincluded is equal to 1
    #otherwise it is not incrementing by or it is not the optimal solution
    assert (count >= 1), "BoolIncluded is not incrementing by ones"

def test_set_cover_solver_v3(get_tests):
    mainSet = get_tests["set"]
    answer = get_tests["answer"]
    solution, timedout = solve_problem(mainSet.copy(), 3)
    #checks if the solution size matches the correct solution size
    assert (solution.nSolutionSize == len(answer)), f"solution subsets: {solution.subSets}"
    toRemove = []
    for i in solution.subSets:
        if i == -1:
            toRemove.append(i)
    for j in toRemove:
        solution.subSets.remove(j)
    #checks if the solution's list of subsets has the same size as the correct answer
    assert (len(solution.subSets) == len(answer)), f"solution subsets: {solution.subSets}"
    count = 0
    for i in range(len(solution.boolIncluded)):
        if i == 1:
            count += 1
    #Checks that at least one entry in Boolincluded is equal to 1
    #otherwise it is not incrementing by or it is not the optimal solution
    assert (count >= 1), "BoolIncluded is not incrementing by ones"
    
def test_set_cover_solver_v4(get_tests):
    mainSet = get_tests["set"]
    answer = get_tests["answer"]
    solution, timedout = solve_problem(mainSet.copy(), 4)
    #checks if the solution size matches the correct solution size
    assert (solution.nSolutionSize == len(answer)), f"solution subsets: {solution.subSets}"
    toRemove = []
    for i in solution.subSets:
        if i == -1:
            toRemove.append(i)
    for j in toRemove:
        solution.subSets.remove(j)
    #checks if the solution's list of subsets has the same size as the correct answer
    assert (len(solution.subSets) == len(answer)), f"solution subsets: {solution.subSets}"
    count = 0
    for i in range(len(solution.boolIncluded)):
        if i == 1:
            count += 1
    #Checks that at least one entry in Boolincluded is equal to 1
    #otherwise it is not incrementing by or it is not the optimal solution
    assert (count >= 1), "BoolIncluded is not incrementing by ones"