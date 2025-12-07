import random, os

'''
creates seed tests for automatically generating test cases based on the
metamorphic relations of discriminant properties
returns: tests_generated = list[str]
'''
def generate_discriminant_tests():
    tests_generated = []


    k = random.randint(2,1000)
    #negative discriminant
    a = 5*k
    b = 5
    c = 5*k
    k = random.randint(2,1000)
    tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    k = random.randint(2,1000)
    #positive discriminant
    a = 1
    b = 5*k
    c = 1
    k = random.randint(2,1000)
    tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    k = random.randint(2,1000)
    #zero discriminant
    a = 1*k
    b = 2*k
    c = 1*k
    k = random.randint(2,1000)
    tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")

    return tests_generated
'''
creates seed tests for automatically generating test cases based on the
metamorphic relations of the Vieta formulas for quadratic equations
returns: mult_tests_generated = list[str], invert_tests_generated = list[str], negate_tests_generated = list[str]
'''
def generate_vieta_tests():
    mult_tests_generated = []
    invert_tests_generated= []
    negate_tests_generated = []

    k = random.randint(2,1000)
    #negative discriminant
    a = 5*k
    b = 5
    c = 5*k
    k = random.randint(2,1000)
    #(scale by k)
    mult_tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    #(invert coefficients)
    invert_tests_generated.append(f"a = {str(c)};b = {str(b)};c = {str(a)}")
    #(scale by -1)
    negate_tests_generated.append(f"a = {str(-1*a)};b = {str(-1*b)};c = {str(-1*c)}")

    k = random.randint(2,1000)
    #positive discriminant
    a = 1
    b = 5*k
    c = 1
    k = random.randint(2,1000)
    #(scale by k)
    mult_tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    #(invert coefficients)
    invert_tests_generated.append(f"a = {str(c)};b = {str(b)};c = {str(a)}")
    #(scale by -1)
    negate_tests_generated.append(f"a = {str(-1*a)};b = {str(-1*b)};c = {str(-1*c)}")
    
    k = random.randint(2,1000)
    #zero discriminant
    a = 1*k
    b = 2*k
    c = 1*k
    k = random.randint(2,1000)
    #(scale by k)
    mult_tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    #(invert coefficients)
    invert_tests_generated.append(f"a = {str(c)};b = {str(b)};c = {str(a)}")
    #(scale by -1)
    negate_tests_generated.append(f"a = {str(-1*a)};b = {str(-1*b)};c = {str(-1*c)}")

    return mult_tests_generated, invert_tests_generated, negate_tests_generated

'''
Will generate 1 random quadratic equation
low is the smallest possible number to be generated for coefficients, whereas high is the greatest
args: low = int, high = int, trials = int
return: tests_generated = list[str]
'''
def generate_evaluation_tests(low:int, high:int, trials:int):
    tests_generated = []
    for i in range(trials):
        
        a = random.randint(low,high)
        b = random.randint(low,high)
        c = random.randint(low,high)
        k = random.randint(low,high)
        trial = f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}"
        tests_generated.append(trial)
    return tests_generated

'''
Given a list of test-cases it saves them in a .txt file with the given filename in the "new_tests" folder
args: tests = list[str], filename = str
'''
def save(tests:list[str], filename:str):
    try:
        with open(f"tests/test_cases/new_tests/{filename}.txt", "x") as newFile:
            for trial in tests:
                newFile.write(trial+"\n")
    except Exception as e:
        os.remove(f"tests/test_cases/new_tests/{filename}.txt")
        save(tests, filename)

if __name__ == "__main__":
    '''
    Generates test-cases
    '''
    cwd = os.getcwd()

    if cwd.endswith("ATCG"):
        os.chdir("CaseStudies/Quadratic_Equation_Solver")
    elif cwd.endswith("Studies"):
        os.chdir("Quadratic_Equation_Solver")

    disc_tests = generate_discriminant_tests()
    vieta_tests = generate_vieta_tests()
    eval_tests = generate_evaluation_tests(-1000,1000,5)
    save(disc_tests, "disc_tests")
    save(vieta_tests[0], "vieta_mult_tests")
    save(vieta_tests[1], "vieta_invert_tests")
    save(vieta_tests[2], "vieta_negate_tests")
    save(eval_tests, "eval_tests")