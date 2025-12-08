# Automated Test Case Generation Project for SYSC 5105
Authors: Hazel Grifith and Ghinwa Yassin

## Description
In this project we demonstrate two techniques for automatically generating test cases for software. We use the techniques known as category partition/combinatorial pair-wise and metamorphic to automatically generate test cases for two case studies.
Case study 1 is a program that uses a version of Newton's method to solve quadratic equations for their roots.
Case study 2 is a program that uses a greedy algorithm followed by one of four back tracking algorithms to find a solution to minimal set cover problems

## Methods
After generating the test-cases for each technique we measure their statement coverage, branch coverage, and execution times. If any tests fail we determine what fault(s) was/were detected.
Then mutation testing is completed with the mutmut library where we demonstrate how to increase your test-suite's mutation score.

## Libraries Used
- pytest
- mutmut
- coverage
- pytest-cov
- signal (requires Linux based OS)

## Categroy Partition Testing
Access the "CategoryPartition" folder for the software that generates and runs tests with this technique

## Combinatorial Testing for Quadratic Equation Solver
Access the "QuadraticEquationSolver_Combinatorial" folder for the software that generates and runs tests with this technique

## How to run Quadratic Equation Solver Metamorphic Testing
first, ensure your terminal has navigated to the Quadratic_Equation_Solver directory. 
From the root directory enter: 
"cd Metamorphic_and_SetCover_Combinatorial/Quadratic_Equation_Solver"

### Run Source Code
To run the code enter: 
"python -m source.quadratic_equation_solver"
You will be asked for values of all coefficients, then after receiving an answer enter "n" to exit the program, or "y" to use it again.

### Run Tests
To generate new metamorphic test cases in the tests/test_cases/new_tests folder enter: 
"python -m tests.generate_QES_metamorphic_test_cases"

To run the metamorphic tests in the tests/test_cases/tests_used folder enter: 
"pthon -m pytest --cov=source --cov-branch --cov-report=html --durations=0 tests/test_QES_MR.py"

This command above will generate a folder called htmlcover that contains an html file called "index" that can be loaded to see your coverage report.
Ensure the .coverage file has been deleted before running if you want to start over.
Test execution times will be displayed in the terminal. 

For mutation testing, ensure that the current "mutants" folder has been renamed or deleted, and that only the test driver you want to run has a name that starts with "test_"
mutmut automatically uses test drivers with that name in its mutation testing.
To generate and test mutants enter the command, "mutmut run"
Once it is complete the results will be displayed in the terminal.
To view the results in greater detail enter the command, "mutmut browse"
For more details on how to use mutmut read this article, https://mutmut.readthedocs.io/en/latest/

## How to run Set Problem Solver Metamorphic and Combinatorial Testing
first, ensure your terminal has navigated to the Set_Problem_Solver directory. 
From the root directory enter: 
"cd Metamorphic_and_SetCover_Combinatorial/Set_Problem_Solver"

### Run Source Code
To run the code enter: 
"python -m source.setCover"
You will be asked for the filename of the problem file you want to run.
It will automatically look for your filename in the "tests/test_cases" folder, so enter the "folder name" + "/" + "file name" without the .txt
Press enter and you will be asked if you want to use a 60 second timer. Enter "y" if you do, and "n" if you do not.
The printed result will start with the size of the solution, then immediately below that is the first subset in the solution's original index from the set. This is followed by the next subset with its index.
An example can be seen below.
<img width="677" height="493" alt="image" src="https://github.com/user-attachments/assets/75c4bcc4-515c-44c4-a102-35463166d810" />


### Run Tests
To generate new combinatorial pair-wise test cases in the tests/test_cases/comb_pair_tests folder enter: 
!!!EVERY TIME YOU GENERATE NEW CASES, NEW ANSWERS NEED TO BE WRITTEN IN THE tests/test_cases/answers FOLDER!!!
"python -m tests.generate_CombPair_test_cases"

To run the combinatorial pair-wise tests in the tests/test_cases/comb_pair_tests folder enter: 
"pthon -m pytest tests/test_SC_CombPair.py --cov=source --cov-branch --cov-report=html --durations=0 "

To generate new metamorphic test cases in the tests/test_cases/transformed_problem_files based upon the tests/test_cases/MR_tests_used folder enter: 
"python -m tests.generate_MR_test_cases"

To run the metamorphic tests with the seed tests stored in the tests/test_cases/MR_tests_used folder and the transformed tests stored in the tests/test_cases/transformed_problem_files folder enter:
"python -m pytest tests/test_SC_MR.py --cov=source --cov-branch --cov-report=html --durations=0 "

The test driver executions above will generate a folder called htmlcover that contains an html file called "index" that can be loaded to see your coverage report.
Ensure the .coverage file has been deleted before running if you want to start over.
Test execution times will be displayed in the terminal. 

For mutation testing, ensure that the current "mutants" folder has been renamed or deleted, and that only the test driver you want to run has a name that starts with "test_"
mutmut automatically uses test drivers with that name in its mutation testing.
To generate and test mutants enter the command, "mutmut run"
Once it is complete the results will be displayed in the terminal.
To view the results in greater detail enter the command, "mutmut browse"
For more details on how to use mutmut read this article, https://mutmut.readthedocs.io/en/latest/
