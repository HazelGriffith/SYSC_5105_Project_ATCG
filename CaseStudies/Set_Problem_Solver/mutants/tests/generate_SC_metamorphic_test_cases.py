from source.setCover import SetCoverProblem, Solution, Set
import random, os, signal, shutil


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

def save(filename:str, newSet:Set):
    try:
        with open(f"tests/{filename}.txt", "x") as newFile:
            newFile.write(str(newSet.nGlobalSetSize)+"\n")
            newFile.write(str(newSet.nSubSets)+"\n")
            for setNum in newSet.originalOrder:
                for numInSet, pos in enumerate(range(len(newSet.subsets[setNum-1]))):
                    newFile.write(str(newSet.subsets[setNum-1][numInSet]))
                    if pos == len(newSet.subsets[setNum-1])-1:
                        newFile.write("\n")
                    else:
                        newFile.write(" ")
    except Exception as e:
        os.remove(f"tests/{filename}.txt")
        save(filename,newSet)

'''
accepts a filename as a string that is used to load the problem, transform it in a random way, 
save it as a new problem file, and repeat this "num" times for each metamorphic relation
args: filename = string, num = int
'''
def create_and_transform_problem(filename:str, num_of_tests_to_generate:int, num_of_redundant_subsets:int):
    mainSet = setup_problem("tests_used/"+filename)

    for i in range(num_of_tests_to_generate):
        new_relabeling_transformations(filename,mainSet.copy(),i)
        new_added_redundant_sets_transformations(filename,mainSet.copy(),i,num_of_redundant_subsets)

    new_add_new_element_transformations(filename,mainSet.copy())

'''
Given the original filename, the lines of the file, and the current transformation made,
this function transforms the original problem by reordering the problem's sets,
thereby relabeling the sets. This should not change any solution found.
args: filename = str, lines = list[str], i = int
'''
def new_relabeling_transformations(filename:str, mainSet:Set, i:int):
    newSet = mainSet.copy()
    originalOrder = newSet.originalOrder.copy()
    newOrder = []
    while len(originalOrder) > 0:
        randomIndex = random.randint(0,len(originalOrder)-1)
        newOrder.append(originalOrder.pop(randomIndex))

    newSet.originalOrder = newOrder
    save(f"transformed_problem_files/{filename}_transformations/relabeling/{i}", newSet)

'''
Given the original filename, the lines of the file, and the current transformation made,
this function transforms the original problem by adding redundant sets to the original problem.
The resulting transformed problem should have the same size solution or better
args: filename = str, lines = list[str], i = int, numOfNewSets = int
'''
def new_added_redundant_sets_transformations(filename:str, mainSet:Set, i:int, numOfNewSets:int):
    newSet = mainSet.copy()

    for j in range(numOfNewSets):
        randomIndex = random.randint(0,newSet.nSubSets-1)
        subSet1 = newSet.subsets[randomIndex].copy()
        randomIndex = random.randint(0,newSet.nSubSets-1)
        subSet2 = newSet.subsets[randomIndex].copy()
        for num in subSet2:
            if subSet1.count(num) == 0:
                subSet1.append(num)

        newSet.originalOrder.append(len(newSet.subsets))
        newSet.subsets.append(subSet1)   

    newSet.nSubSets += numOfNewSets

    save(f"transformed_problem_files/{filename}_transformations/add_redundant_sets/{i}", newSet)

'''
Given the original filename, the lines of the file, and the current transformation made,
this function transforms the original problem by adding a single set with a new element.
The metamorphic relation is that the solution to the new problem will require exactly one more subset
args: filename = str, lines = list[str], i = int
'''
def new_add_new_element_transformations(filename:str, mainSet):
    newSet = mainSet.copy()

    newSet.nGlobalSetSize += 1
    newSet.nSubSets += 1

    newSubSet = [newSet.nGlobalSetSize]

    newSet.originalOrder.append(len(newSet.subsets)+1)

    newSet.subsets.append(newSubSet)

    save(f"transformed_problem_files/{filename}_transformations/add_new_element", newSet)

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

def test_add_one_element(seed_solution, seed_timedOut:bool, gen_solution, gen_timedOut:bool, filename:str):
    seed_solution_size = seed_solution.nSolutionSize
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        try:
            assert(gen_solution_size >= seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {filename}, add_one_element"
        except AssertionError as e:
            print(f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {filename}, add_one_element")
    else:
        try:
            assert(gen_solution_size == seed_solution_size+1), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {filename}, add_one_element"
        except AssertionError as e:
            print(f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {filename}, add_one_element")

def test_relabeling(seed_solution, seed_timedOut:bool, gen_solution, gen_timedOut:bool, filename:str, i:int):
    seed_solution_size = seed_solution.nSolutionSize
    gen_solution_size = gen_solution.nSolutionSize

    if not(seed_timedOut or gen_timedOut):
        try:
            assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {filename}, relabeling {str(i)}"
        except AssertionError as e:
            print(f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {filename}, relabeling {str(i)}")

def test_add_redundant_set(seed_solution, seed_timedOut:bool, gen_solution, gen_timedOut:bool, filename:str, i:int):
    seed_solution_size = seed_solution.nSolutionSize
    gen_solution_size = gen_solution.nSolutionSize

    if (seed_timedOut or gen_timedOut):
        try:
            assert(gen_solution_size <= seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {filename}, add_redundant_sets {str(i)}"
        except AssertionError as e:
            print(f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, timed out, in {filename}, add_redundant_sets {str(i)}")
    else:
        try:
            assert(gen_solution_size == seed_solution_size), f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {filename}, add_redundant_sets {str(i)}"
        except AssertionError as e:
            print(f"gen_solution_size = {gen_solution_size}, and seed_solution_size = {seed_solution_size}, in {filename}, add_redundant_sets {str(i)}")

def run_tests(filename:str, num_of_tests_to_generate:int, num_of_redundant_subsets:int):
    #Run original problem and get result
    seed_solution, seed_timedOut = solve_problem("tests_used/"+filename)
    gen_solution, gen_timedOut = solve_problem("transformed_problem_files/"+filename+"_transformations/add_new_element")
    
    test_add_one_element(seed_solution, seed_timedOut, gen_solution, gen_timedOut, filename)

    for i in range(num_of_tests_to_generate):
        #tests add redundant subsets MR
        gen_solution, gen_timedOut = solve_problem("transformed_problem_files/"+filename+"_transformations/add_redundant_sets/"+str(i))
        
        test_relabeling(seed_solution, seed_timedOut, gen_solution, gen_timedOut, filename, i)

        #tests relabeling MR
        gen_solution, gen_timedOut = solve_problem("transformed_problem_files/"+filename+"_transformations/relabeling/"+str(i))
        
        test_add_redundant_set(seed_solution, seed_timedOut, gen_solution, gen_timedOut, filename, i)


def main():
    num_of_tests_to_generate = 2
    num_of_redundant_subsets = 3

    #First, we take all problem files in the "tests_used" folder and prepare directories to contain
    #all of the transformed auto generated test problem files
    cwd = os.getcwd()
    if cwd.endswith("ATCG"):
        os.chdir("CaseStudies/Set_Problem_Solver")
    elif cwd.endswith("Studies"):
        os.chdir("Set_Problem_Solver")

    generate = input("Generate new tests? (y/n): ")

    testEntries = os.listdir("tests/tests_used/")

    if (generate.casefold() == "y"):
        for pos, entry in enumerate(testEntries):
            foldername = entry.replace(".txt","")
            if os.path.exists(os.path.join(cwd,f"tests/transformed_problem_files/{foldername}_transformations")):
                shutil.rmtree(f"tests/transformed_problem_files/{foldername}_transformations")
            os.makedirs(f"tests/transformed_problem_files/{foldername}_transformations/relabeling/", exist_ok=True)
            os.makedirs(f"tests/transformed_problem_files/{foldername}_transformations/add_redundant_sets/", exist_ok=True)
    
    #here we generate the transformations of each problem file
    for entry in testEntries:
        if (generate.casefold() == "y"):
            create_and_transform_problem(entry.replace(".txt",""),num_of_tests_to_generate,num_of_redundant_subsets)
        run_tests(entry.replace(".txt",""),num_of_tests_to_generate, num_of_redundant_subsets)

if __name__ == "__main__":
    main()
    