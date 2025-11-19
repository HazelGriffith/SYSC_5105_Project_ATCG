from setCover import SetCoverProblem, Solution, Set
import random, os


'''
Reads a problem file and obtains the mainSet object needed to represent and process it
args: filename = string
returns: mainSet = Set 
'''
def setup(filename:str) -> Set:
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

'''
accepts a filename as a string that is used to load the problem, transform it in a random way, 
save it as a new problem file, and repeat this "num" times for each metamorphic relation
args: filename = string, num = int
'''
def create_and_transform_problem(filename:str, num_of_tests_to_generate:int, num_of_redundant_subsets:int):
    origLines = []
    with open("tests/original_problem_files/"+filename+".txt", 'r') as gameFile:
        line = gameFile.readline()
        while line != "":
            origLines.append(line)
            line = gameFile.readline()

    for i in range(num_of_tests_to_generate):
        new_relabeling_transformations(filename,origLines.copy(),i)
        new_added_redundant_sets_transformations(filename,origLines.copy(),i,num_of_redundant_subsets)

    new_add_new_element_transformations(filename,origLines.copy())

'''
Given the original filename, the lines of the file, and the current transformation made,
this function transforms the original problem by reordering the problem's sets,
thereby relabeling the sets. This should not change any solution found.
args: filename = str, lines = list[str], i = int
'''
def new_relabeling_transformations(filename:str, origLines:list[str], i:int):
    newLines = origLines.copy()
    try:
        with open(f"tests/transformed_problem_files/{filename}_transformations/relabeling/{i}.txt", 'x') as newFile:
            newFile.write(newLines.pop(0))
            newFile.write(newLines.pop(0))
            while len(newLines) > 0:
                randomIndex = random.randint(0,len(newLines)-1)
                newFile.write(newLines.pop(randomIndex))

    except Exception as e:
        os.remove(f"tests/transformed_problem_files/{filename}_transformations/relabeling/{i}.txt")
        new_relabeling_transformations(filename,origLines.copy(),i)

'''
Given the original filename, the lines of the file, and the current transformation made,
this function transforms the original problem by adding redundant sets to the original problem.
The resulting transformed problem should have the same size solution or better
args: filename = str, lines = list[str], i = int, numOfNewSets = int
'''
def new_added_redundant_sets_transformations(filename:str, origLines:list[str], i:int, numOfNewSets:int):
    newLines = origLines.copy()

    try:
        with open(f"tests/transformed_problem_files/{filename}_transformations/add_redundant_sets/{i}.txt", 'x') as newFile:
            newFile.write(newLines.pop(0))
            numberOfTotalSets = int(newLines.pop(0)) + numOfNewSets
            newFile.write(str(numberOfTotalSets) + "\n")
            problemSets = newLines.copy()
            while len(newLines) > 0:
                newFile.write(newLines.pop(0).replace(" ",""))
            for i in range(numOfNewSets):
                randomIndex = random.randint(0,len(problemSets)-1)
                newline = problemSets[randomIndex].replace("\n","")
                randomIndex = random.randint(0,len(problemSets)-1)
                line = problemSets[randomIndex].replace("\n","")
                numsInLine = line.split(" ")
                for pos, num in enumerate(numsInLine):
                    if not newline.endswith(" "):
                        newline += " "
                    if newline.find(num) == -1:
                        newline += num
                    if pos == len(numsInLine)-1:
                        newline += "\n"
                newFile.write(newline)


    except Exception as e:
        os.remove(f"tests/transformed_problem_files/{filename}_transformations/add_redundant_sets/{i}.txt")
        new_added_redundant_sets_transformations(filename,origLines.copy(),i,numOfNewSets)

'''
Given the original filename, the lines of the file, and the current transformation made,
this function transforms the original problem by adding a single set with a new element.
The metamorphic relation is that the solution to the new problem will require exactly one more subset
args: filename = str, lines = list[str], i = int
'''
def new_add_new_element_transformations(filename:str, origLines:list[str]):
    newLines = origLines.copy()

    try:
        with open(f"tests/transformed_problem_files/{filename}_transformations/add_new_element.txt", 'x') as newFile:
            maxElement = int(newLines.pop(0)) + 1
            newFile.write(str(maxElement) + "\n")
            newFile.write(newLines.pop(0))
            while len(newLines) > 0:
                newFile.write(newLines.pop(0))
            newFile.write(str(maxElement) + "\n")

    except Exception as e:
        os.remove(f"tests/transformed_problem_files/{filename}_transformations/add_new_element.txt")
        new_add_new_element_transformations(filename,origLines.copy())

def solve_problem(filename:str) -> Solution:
    mainSet = setup(filename)
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet, mainSet.nSubSets-1)
    setCover = SetCoverProblem(mainSet, aSolution, bestSolution, 0)
    setCover.sortSubSets()

    setCover.greedy()
    setCover.backTrack4(setCover.aSolution, 0, 0)
    return setCover.bestSolution

def run_tests(filename:str, num_of_tests_to_generate:int):
    #Run original problem and get result
    seed_solution = solve_problem("original_problem_files/"+filename)
    seed_solution_size = seed_solution.nSolutionSize

    gen_solution = solve_problem("transformed_problem_files/"+filename+"_transformations/add_new_element")
    gen_solution_size = gen_solution.nSolutionSize
    assert(gen_solution_size == seed_solution_size+1)

    for i in range(num_of_tests_to_generate):
        #tests add redundant subsets MR
        gen_solution = solve_problem("transformed_problem_files/"+filename+"_transformations/add_redundant_sets/"+str(i))
        gen_solution_size = gen_solution.nSolutionSize
        assert(gen_solution_size <= seed_solution_size)

        #tests relabeling MR
        gen_solution = solve_problem("transformed_problem_files/"+filename+"_transformations/relabeling/"+str(i))
        gen_solution_size = gen_solution.nSolutionSize
        assert(gen_solution_size == seed_solution_size)

if __name__ == "__main__":

    num_of_tests_to_generate = 5
    num_of_redundant_subsets = 3

    #First, we take all problem files in the "original_problem_files" folder and prepare directories to contain
    #all of the transformed auto generated test problem files
    cwd = os.getcwd()
    if cwd.endswith("ATCG"):
        os.chdir("CaseStudies/Set_Problem_Solver")
    elif cwd.endswith("Studies"):
        os.chdir("Set_Problem_Solver")

    testEntries = os.listdir("tests/original_problem_files/")
    for pos, entry in enumerate(testEntries):
        foldername = entry.replace(".txt","")
        os.makedirs(f"tests/transformed_problem_files/{foldername}_transformations/relabeling/", exist_ok=True)
        os.makedirs(f"tests/transformed_problem_files/{foldername}_transformations/add_redundant_sets/", exist_ok=True)
    
    #here we generate the transformations of each problem file
    for entry in testEntries:
        create_and_transform_problem(entry.replace(".txt",""),num_of_tests_to_generate,num_of_redundant_subsets)
        run_tests(entry.replace(".txt",""),num_of_tests_to_generate)

