import signal
import os

class Set:

    def __init__(self, nGlobalSetSize:int =0, nSubSets:int = 0, originalOrder:list[int] = [], nSubSetSizes:list[int] = [], subsets:list[list[int]] = [], subSetsSizesSum:list[list[int]] = []):
        self.nGlobalSetSize = nGlobalSetSize
        self.nSubSets = nSubSets
        self.originalOrder = originalOrder
        self.nSubSetSizes = nSubSetSizes
        self.subsets = subsets
        self.subSetSizesSum = subSetsSizesSum


class Solution:

    def __init__(self, probSet:Set, nSolutionSize:int=0):
        self.nSolutionSize = nSolutionSize
            
        self.subSets = []
        for i in range(probSet.nSubSets):
            self.subSets.append(-1)

        self.boolIncluded = []
        for i in range(probSet.nGlobalSetSize):
            self.boolIncluded.append(0)



class SetCoverProblem:


    def __init__(self, mainSet:Set, aSolution:Solution, bestSolution:Solution, depth:int):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.depth = depth

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

    def numberOfUncoveredElements(self, subSetIndex:int):
        count = 0
        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            if (self.bestSolution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] == 0):
                count += 1
        
        return count

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

    def copySolutionToBest(self, solution:Solution):
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        for i in range(solution.nSolutionSize):
            self.bestSolution.subSets[i] = solution.subSets[i]
        for i in range(self.mainSet.nGlobalSetSize):
            self.bestSolution.boolIncluded[i] = solution.boolIncluded[i]

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

    def backTrack4(self, solution:Solution, last:int, sum:int):
        if solution.nSolutionSize >= self.bestSolution.nSolutionSize:
            return
        
        if (self.checkSolution(solution)):
            if solution.nSolutionSize < self.bestSolution.nSolutionSize:
                self.copySolutionToBest(solution)
                print(f"New Solution Size: {self.bestSolution.nSolutionSize}\n")

            return
        
        for i in range(last, self.mainSet.nSubSets):
            if (sum + self.mainSet.subSetSizesSum[i][(self.bestSolution.nSolutionSize-1)-solution.nSolutionSize] < self.mainSet.nGlobalSetSize):
                return
            
            self.addSubSet(solution, i)
            sum += self.mainSet.nSubSetSizes[i]

            self.backTrack4(solution, i+1, sum)
            sum -= self.mainSet.nSubSetSizes[i]

            self.removeSubSet(solution, i)

    def addSubSet(self, solution:Solution, subSetIndex:int):
        solution.nSolutionSize += 1
        solution.subSets[solution.nSolutionSize-1] = subSetIndex

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i]-1] += 1


    def removeSubSet(self, solution:Solution, subSetIndex:int):
        solution.subSets[solution.nSolutionSize-1] = -1
        solution.nSolutionSize -= 1

        for i in range(self.mainSet.nSubSetSizes[subSetIndex]):
            solution.boolIncluded[self.mainSet.subsets[subSetIndex][i] - 1] -= 1

    def containsSubSet(self, solution:Solution, subSetIndex:int) -> bool:
        for i in range(solution.nSolutionSize):
            if solution.subSets[i] == subSetIndex:
                return True
            
        return False

    def checkSolution(self, solution:Solution) -> bool:
        allDone = True
        for i in range(self.mainSet.nGlobalSetSize):
            boolInc = solution.boolIncluded[i]
            if boolInc == 0:
                return False
            
        return allDone

    def printSolution(self, solution:Solution):
        print(solution.nSolutionSize)
        for i in range(solution.nSolutionSize):
            print(self.mainSet.originalOrder[solution.subSets[i]])
            self.printSubSet(solution.subSets[i])

    def echoInit(self):
        print(f"Universal Set 1-{self.mainSet.nGlobalSetSize}\n")
        print(f"Number of subsets {self.mainSet.nSubSets}\n")
        for i in range(self.mainSet.nSubSets):
            self.printSubSet(i)

    def printSubSet(self, nSubSetIndex:int):
        for i in range(self.mainSet.nSubSetSizes[nSubSetIndex]):
            print(self.mainSet.subsets[nSubSetIndex][i])
        print("\n")

def inthandler(signum, frame, setCover:SetCoverProblem):
        setCover.printSolution(setCover.bestSolution)
        exit(0)

if __name__ == "__main__":

    cwd = os.getcwd()

    if cwd.endswith("ATCG"):
        os.chdir("CaseStudies/Set_Problem_Solver")
    elif cwd.endswith("Studies"):
        os.chdir("Set_Problem_Solver")
    
    cwd = os.getcwd()
    print(cwd)

    filename = input("Enter your filename: ")

    timerUsed = input("Enter y for a 60s timer: ")

    if timerUsed == 'y':
        signal.signal(signal.SIGALRM, inthandler)
        signal.alarm(60)
    
    mainSet = Set()
    try:
        lineno = 0
        with open("tests/original_problem_files/"+filename+".txt", 'r') as gameFile:
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
                        int_nums.append(int(num.replace("\n","")))
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
    
