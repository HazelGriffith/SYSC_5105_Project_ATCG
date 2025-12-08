# ========================================================================
# FINAL PASSING VERSION – Compatible with test_set_cover_cpt.py
# ========================================================================

class Set:
    def __init__(self):
        self.nGlobalSetSize = 0
        self.nSubSets = 0
        self.subsets = []
        self.nSubSetSizes = []
        self.subSetSizesSum = []
        self.originalOrder = []


class Solution:
    def __init__(self, mainSet, preset_size=0):
        self.mainSet = mainSet
        self.subSets = []
        self.nSolutionSize = preset_size
        self.boolIncluded = [0] * mainSet.nGlobalSetSize


class SetCoverProblem:
    def __init__(self, mainSet, aSolution, bestSolution, bestSize):
        self.mainSet = mainSet
        self.aSolution = aSolution
        self.bestSolution = bestSolution
        self.bestSize = bestSize

        # New flag used by pytest to detect “no cover possible”
        self.no_cover_possible = False

    # ============================================================
    def addSubSet(self, solution: Solution, subSetIndex: int):
        solution.subSets.append(subSetIndex)
        solution.nSolutionSize = len(solution.subSets)
        for v in self.mainSet.subsets[subSetIndex]:
            solution.boolIncluded[v - 1] += 1

    def removeSubSet(self, solution: Solution, subSetIndex: int):
        if subSetIndex in solution.subSets:
            solution.subSets.remove(subSetIndex)
            solution.nSolutionSize = len(solution.subSets)
            for v in self.mainSet.subsets[subSetIndex]:
                solution.boolIncluded[v - 1] -= 1

    def copySolutionToBest(self, solution: Solution):
        self.bestSolution.subSets = list(solution.subSets)
        self.bestSolution.nSolutionSize = solution.nSolutionSize
        self.bestSolution.boolIncluded = list(solution.boolIncluded)

    def checkSolution(self, solution: Solution):
        for i in range(self.mainSet.nGlobalSetSize):
            if solution.boolIncluded[i] == 0:
                return False
        return True

    def containsSubSet(self, solution: Solution, idx: int):
        return idx in solution.subSets

    def sortSubSets(self):
        zipped = list(zip(self.mainSet.nSubSetSizes,
                          self.mainSet.subsets,
                          self.mainSet.originalOrder))
        zipped.sort(reverse=True, key=lambda x: x[0])
        self.mainSet.nSubSetSizes, \
            self.mainSet.subsets, \
            self.mainSet.originalOrder = map(list, zip(*zipped))

    # ============================================================
    # GREEDY (populates aSolution only)
    # ============================================================
    def greedy(self):
        while True:
            maxCover = 0
            addIndex = -1

            for i in range(self.mainSet.nSubSets):
                c = 0
                for elem in self.mainSet.subsets[i]:
                    if self.aSolution.boolIncluded[elem - 1] == 0:
                        c += 1
                if c > maxCover:
                    maxCover = c
                    addIndex = i

            if addIndex == -1 or maxCover == 0:
                return

            self.addSubSet(self.aSolution, addIndex)

    # ============================================================
    # BACKTRACK 4 – MAIN SOLVER
    # ============================================================
    def backTrack4(self, solution: Solution, depth: int, lastAdded: int):
        # full coverage?
        if self.checkSolution(solution):
            if (self.bestSolution.nSolutionSize == 0 or
                solution.nSolutionSize < self.bestSolution.nSolutionSize):
                self.copySolutionToBest(solution)
            return

        # prune
        if (self.bestSolution.nSolutionSize != 0 and
                solution.nSolutionSize >= self.bestSolution.nSolutionSize):
            return

        # explore
        for i in range(lastAdded, self.mainSet.nSubSets):
            if i in solution.subSets:
                continue
            self.addSubSet(solution, i)
            self.backTrack4(solution, depth + 1, i)
            self.removeSubSet(solution, i)


# ========================================================================
# Helper for pytest
# ========================================================================
def solve_set_cover(mainSet: Set) -> SetCoverProblem:
    aSolution = Solution(mainSet)
    bestSolution = Solution(mainSet)
    problem = SetCoverProblem(mainSet, aSolution, bestSolution, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    # If no solution covers universe → mark flag
    if bestSolution.nSolutionSize == 0:
        problem.no_cover_possible = True

    return problem


# ========================================================================
# Main program (unchanged)
# ========================================================================
def main():
    print("This program solves the set cover problem.")
    x = input("File name: ")
    fileName = "tests/" + x + ".txt"

    mainSet = Set()

    try:
        with open(fileName, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        mainSet.nGlobalSetSize = int(lines[0])
        mainSet.nSubSets = int(lines[1])

        for i in range(mainSet.nSubSets):
            mainSet.originalOrder.append(i + 1)
            subset = list(map(int, lines[2 + i].split()))
            mainSet.subsets.append(subset)
            mainSet.nSubSetSizes.append(len(subset))

    except FileNotFoundError:
        print("File not found.")
        return

    a = Solution(mainSet)
    b = Solution(mainSet)
    problem = SetCoverProblem(mainSet, a, b, 9999)

    problem.sortSubSets()
    problem.greedy()
    problem.backTrack4(problem.aSolution, 0, 0)

    print("\nBest Solution Size:", b.nSolutionSize)
    print("Subsets chosen:", [mainSet.originalOrder[i] for i in b.subSets])


if __name__ == "__main__":
    main()
