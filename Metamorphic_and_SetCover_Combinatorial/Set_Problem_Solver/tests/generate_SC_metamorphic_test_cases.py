from source.setCover import Set
from pathlib import Path
import random, os, shutil


'''
Reads a problem file and obtains the mainSet object needed to represent and process it
args: filename = string
returns: mainSet = Set 
'''
def setup_problem(filename:str) -> Set:
    mainSet = Set()
    try:
        lineno = 0
        cwd = Path.cwd()
        filePath = cwd/f"tests/test_cases/"
        with open(filePath/f"{filename}.txt", 'r') as gameFile:
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
Given a new Set problem this function saves that Set as a text file with the given filename
args: filename = str, newSet = Set
'''
def save(filename:str, newSet:Set):
    cwd = Path.cwd()
    filePath = cwd/f"tests/test_cases/"
    try:
        with open(filePath/f"{filename}.txt", "x") as newFile:
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
        os.remove(filePath/f"{filename}.txt")
        save(filename,newSet)

'''
accepts a filename as a string that is used to load the problem, transform it in a random way, 
save it as a new problem file, and repeat this "num" times for each metamorphic relation
args: filename = string, num = int
'''
def create_and_transform_problem(filename:str, num_of_tests_to_generate:int, num_of_redundant_subsets:int):
    mainSet = setup_problem("MR_tests_used/"+filename)

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

        newSet.originalOrder.append(len(newSet.subsets)+1)
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

'''
loads the tests in the MR_tests_used folder, creates transformations according to the metamorphic relations, and saves the transformations
'''
def main():
    # Number of tests per metamorphic relation
    num_of_tests_to_generate = 5
    
    #Number of redundant subsets to add to test-cases for this metamorphic relation
    num_of_redundant_subsets = 1

    #First, we take all problem files in the "MR_tests_used" folder and prepare directories to contain
    #all of the transformed auto generated test problem files
    cwd = Path.cwd()

    testFilePath = cwd/"tests/test_cases/"
    testEntries = os.listdir(testFilePath/"MR_tests_used")

    #Prepare new folders in the directory
    for pos, entry in enumerate(testEntries):
        foldername = entry.replace(".txt","")
        if os.path.exists(testFilePath/f"transformed_problem_files/{foldername}_transformations"):
            shutil.rmtree(testFilePath/f"transformed_problem_files/{foldername}_transformations")
        os.makedirs(testFilePath/f"transformed_problem_files/{foldername}_transformations/relabeling/", exist_ok=True)
        os.makedirs(testFilePath/f"transformed_problem_files/{foldername}_transformations/add_redundant_sets/", exist_ok=True)
    
    #here we generate the transformations of each problem file
    for entry in testEntries:
        create_and_transform_problem(entry.replace(".txt",""),num_of_tests_to_generate,num_of_redundant_subsets)

if __name__ == "__main__":
    main()
    