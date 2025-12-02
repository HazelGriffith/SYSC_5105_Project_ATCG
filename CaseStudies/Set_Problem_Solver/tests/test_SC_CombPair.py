from source.setCover import SetCoverProblem, Solution, Set
from pathlib import Path
import os, signal, pytest, pulp

tests = {}

'''
Reads a problem file and obtains the mainSet object needed to represent and process it
args: filename = string
returns: mainSet = Set 
'''
def setup_problem(filename:str) -> Set:
    mainSet = Set()
    directory = Path.cwd() / "tests/test_cases/comb_pair_tests"
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

def time_out_handler(signum, frame):
    raise Exception("Timed out")

def solve_problem(mainSet:Set):
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet, mainSet.nSubSets-1)
    setCover = SetCoverProblem(mainSet, aSolution, bestSolution, 0)
    setCover.sortSubSets()
    signal.signal(signal.SIGALRM, time_out_handler)
    signal.alarm(20)

    try:
        setCover.greedy()
        setCover.backTrack4(setCover.aSolution, 0, 0)
        signal.alarm(0)
        timedOut = False
    except Exception as e:
        print(e)
        timedOut = True

    return setCover.bestSolution, timedOut

cwd = Path.cwd()

testEntries = os.listdir(cwd / "tests/test_cases/comb_pair_tests/")

for entry in testEntries:
    filename = entry.replace(".txt","")
    mainSet = setup_problem(filename)
    tests.update({filename : {"set" : mainSet}})

def pytest_generate_tests(metafunc):

    if "get_tests" in metafunc.fixturenames:
        test_ids = list(tests.keys())
        test_values = list(tests.values())

        metafunc.parametrize("get_tests", test_values, ids=test_ids)

def test_set_cover_solver(get_tests):
    mainSet = get_tests["set"]

    solution, timedout = solve_problem(mainSet)

    