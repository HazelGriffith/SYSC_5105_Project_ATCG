import signal
import os
from pathlib import Path

'''
This class stores the global set and all its subsets
'''
class Set:

    '''
    Constructor for the global set
    nGlobalSetSize is the global set size
    nSubSets is the number of subsets
    originalOrder is the subset order as they were ordered in the file
    nSubSetSizes is the size of each subset in the original order
    subsets is a list of the subsets
    subSetSizesSum is a matrix of sums of subset sizes used by BackTrack4 to determine if the sum of subset sizes of the current solution is bigger than the global set size
    '''
    def __init__(self, nGlobalSetSize:int = 0, nSubSets:int = 0, originalOrder:list[int] = None, nSubSetSizes:list[int] = None, subsets:list[list[int]] = None, subSetsSizesSum:list[list[int]] = None):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        if originalOrder is None:
            self.originalOrder = []
        else:
            self.originalOrder = originalOrder

        if nSubSetSizes is None:
            self.nSubSetSizes = []
        else:
            self.nSubSetSizes = nSubSetSizes

        if subsets is None:
            self.subsets = []
        else:
            self.subsets = subsets

        if subSetsSizesSum is None:
            self.subSetSizesSum = []
        else:
            self.subSetSizesSum = subSetsSizesSum

    '''
    returns a copy of the set object to avoid altering the original
    '''
    def copy(self):
        newSet = Set()
        newSet.nGlobalSetSize = self.nGlobalSetSize
        newSet.nSubSets = self.nSubSets
        newSet.originalOrder = self.originalOrder.copy()
        newSet.nSubSetSizes = self.nSubSetSizes.copy()
        newSet.subsets = self.subsets.copy()
        newSet.subSetSizesSum = self.subSetSizesSum.copy()
        return newSet

'''
The Solution class creates objects that could be valid solutions to a given minimal set cover problem
'''
class Solution:

    '''
    This constructor accepts the global set and the solution's current number of subsets
    '''
    def __init__(self, probSet:Set, nSolutionSize:int=0):
        #Number of subsets in the solution
        self.nSolutionSize = nSolutionSize
            
        #Initializes list of subsets selected for this solution
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        #initializes list of integers where the index is the element from the global set, and the value stored there is the number of occurences in this solution's subsets
        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)


'''
This class creates and solves minimal set cover problems
Step 1) Sort the subsets from smallest to largest in size
Step 2) Run the greedy algorithm where the next subset with the largest number of uncovered elements is selected
Step 3) Take the solution found by the greedy algorithm and compare it to the result of 1 of 4 back tracking algorithms
Step 4) print the solution found
'''
class SetCoverProblem:


    '''
    Constructor for SetCoverProblem class
    args: mainSet is the global set
          aSolution is temporary storage for a possible solution
          bestSolution is the current best solution created
          depth is used by BackTrack 1 & 2 to track the number of recursive executions 
    '''
    def __init__(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.depth = depth

    '''
    This greedy algorithm finds a valid solution that is not often optimal by following these steps
    Step 1) Add first subset to bestSolution
    Step 2) measure number of uncovered elements in all subsets NOT in bestSolution
    Step 3) add subset with largest number of uncovered elements
    Step 4) Loop steps 2 & 3 until a valid solution is found
    '''
    def greedy(self):
        self.bestSolution.nSolutionSize = 0
        self.addSubSet(self.bestSolution, 0)
        addIndex = 0
        addNumber = 0

        while self.checkSolution(self.bestSolution) == False:
            addIndex = 0
            addNumber = 0
            for i in range(self.mainSet.nSubSets):
                if self.containsSubSet(self.bestSolution, i) == False:
                    temp = self.numberOfUncoveredElements(i)
                    if temp > addNumber:
                        addNumber = temp
                        addIndex = i
            self.addSubSet(self.bestSolution, addIndex)

    '''
    Calculates the number of elements in the given subset that are uncovered by the current bestSolution
    args: subSetIndex = int
    returns: count = int
    '''
    def numberOfUncoveredElements(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 1
        
        return count

    '''
    Sorts the subsets from smallest to largest in size, then calculates the subSetSizesSum matrix
    '''
    def sortSubSets(self):
        for i in range(self.mainSet.nSubSets):
            for j in range(self.mainSet.nSubSets):
                if self.mainSet.nSubSetSizes[i] < self.mainSet.nSubSetSizes[j]:
                    tempInt = self.mainSet.nSubSetSizes[i]
                    tempIntP = self.mainSet.subsets[i]
                    self.mainSet.subsets[i] = self.mainSet.subsets[j]
                    self.mainSet.subsets[j] = tempIntP
                    self.mainSet.nSubSetSizes[i] = self.mainSet.nSubSetSizes[j]
                    self.mainSet.nSubSetSizes[j] = tempInt
                    tempInt = self.mainSet.originalOrder[i]
                    self.mainSet.originalOrder[i] = self.mainSet.originalOrder[j]
                    self.mainSet.originalOrder[j] = tempInt
        
        for i in range(self.mainSet.nSubSets):
            self.mainSet.subSetSizesSum.append([])
            for j in range(self.mainSet.nSubSets):
                self.mainSet.subSetSizesSum[i].append(0)


        for i in range(self.mainSet.nSubSets):
            tempInt = 0
            for j in range(i, self.mainSet.nSubSets):
                tempInt += self.mainSet.nSubSetSizes[j]
                self.mainSet.subSetSizesSum[i][j-i] = tempInt

    '''
    Receives a Solution object and copies it to the bestSolution object
    args: solution is any given Solution object
    '''
    def copySolutionToBest(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(len(solution.subSets)):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

    '''
    Recursive Back track algorithm version 1
    base case: solution size is larger than or equal to the bestSolution size
    otherwise: if solution size is smaller, copy it to bestSolution
    Then sequentially add the first subset not contained in solution and make a recursive call
    After returning remove the subset from solution and loop with next missing subset
    '''
    def backTrack(self, solution:Solution):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if self.checkSolution(solution):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.mainSet.nSubSets):
            if (self.containsSubSet(solution, i) == False):
                self.addSubSet(solution, i)
                self.depth += 1
                self.backTrack(solution)
                self.depth -= 1
                self.removeSubSet(solution, i)

    '''
    Same as version 1, except we no longer check if the next subset is contained by the current solution
    '''
    def backTrack2(self, solution:Solution):

        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

        for i in range(self.depth, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.depth += 1
            self.backTrack2(solution)
            self.depth -= 1
            self.removeSubSet(solution, i)

    '''
    Same as version 2, except we treat finding a solution better than bestSolution to be a second base case
    '''
    def backTrack3(self, solution:Solution, last:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
            return
        
        for i in range(last, self.mainSet.nSubSets):
            self.addSubSet(solution, i)
            self.backTrack3(solution, i + 1)
            self.removeSubSet(solution, i)

    '''
    Same as version 3, except when we loop we check if the current solution's subset sizes sum + the next subset's subsetSizesSum in relation to the bestSoluton size minus the current
    solution's size, is less than the global set size.
    If this is true we treat it as a third base case and end early
    '''
    def backTrack4(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)

            return

        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    '''
    Given a solution and a subset's index from the global set, that subset is added to the given solution
    All the elements covered by the added subset have their entry in the boolIncluded list incremented
    args: solution, subSetIndex = int
    '''
    def addSubSet(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1

    '''
    The same as addSubSet except the subset at the given index is removed from the given solution
    The boolIncluded entries are decremented if they were covered by the subset being removed
    args: solution, subSetIndex = int
    '''
    def removeSubSet(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1

    '''
    Given a solution and a subSetIndex this function returns true if the index is found within
    the solution's subsets list
    args: solution, subSetIndex = int
    returns: Bool
    '''
    def containsSubSet(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(len(solution.subSets)):
            if solution.subSets[i] == subSetIndex:
                return True
            
        return False

    '''
    Given a solution, this function checks if each entry in the boolIncluded list has at least a value of 1
    It returns true if this is the case, and false otherwise
    args: solution
    returns: Bool
    '''
    def checkSolution(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return False
            
        return allDone

    '''
    Given a solution it prints it's size and subsets
    args: solution
    '''
    def printSolution(self, solution:Solution): # pragma: no cover
        print(solution.nSolutionSize)
        for i in range(solution.nSolutionSize):
            print(self.mainSet.originalOrder[solution.subSets[i]])
            self.printSubSet(solution.subSets[i])

    '''
    Used to print the parameters of the loaded problem set
    '''
    def echoInit(self): # pragma: no cover
        print(f"Universal Set 1-{self.mainSet.nGlobalSetSize}\n")
        print(f"Number of subsets {self.mainSet.nSubSets}\n")
        for i in range(self.mainSet.nSubSets):
            self.printSubSet(i)

    '''
    Given a subset index of the global set this function prints the values of that subset
    '''
    def printSubSet(self, nSubSetIndex:int): # pragma: no cover
        for i in range(self.mainSet.nSubSetSizes[nSubSetIndex]):
            print(self.mainSet.subsets[nSubSetIndex][i])
        print("\n")

'''
Using the Signal library function handles any timeOut signals by printing the current solution and exitng the program
'''
def inthandler(signum, frame, setCover:SetCoverProblem): # pragma: no cover
        setCover.printSolution(setCover.bestSolution)
        exit(0)

'''
This section controls normal execution of loading a problem set, solving it according to Back tracking algorithm version 4, and printing the solution
'''
if __name__ == "__main__": # pragma: no cover

    cwd = Path.cwd()
    
    cwd = cwd

    filename = input("Enter your filename: ")

    timerUsed = input("Enter y for a 60s timer: ")

    if timerUsed == 'y':
        signal.signal(signal.SIGALRM, inthandler)
        signal.alarm(60)
    
    mainSet = Set()
    try:
        lineno = 0
        with open(cwd/f"tests/test_cases/{filename}.txt", 'r') as gameFile:
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

    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet, mainSet.nSubSets-1)
    setCover = SetCoverProblem(mainSet, aSolution, bestSolution, 0)
    setCover.sortSubSets()

    setCover.greedy()
    setCover.backTrack4(setCover.aSolution, 0, 0)
    
    setCover.printSolution(setCover.bestSolution)
    print("\n")
    
