from quadratic_equation_solver import Quadratic, NotEnoughPrecisionException
import random, math, os

'''
accepts a string containing a complex number and removes negative signs from complex portion
by changing the operator as appropriate to be compatible with the complex() python function
args: string with form "a (+/-) (-)bj"
returns: string with form "a (+/-) bj"
'''
def simplify_complex_num(number:str) -> str:
    numberparts = number.split(" ")
    if (len(numberparts) > 1):
        if numberparts[2].startswith("-"):
            numberparts[2] = numberparts[2].replace("-","").replace("\n","")
            if numberparts[1] == "+":
                numberparts[1] = "-"
            else:
                numberparts[1] = "+"
        
        return f"{numberparts[0]}{numberparts[1]}{numberparts[2]}"
    else:
        return number

'''
discriminant metamorphic relation tests
d = b**2-4ac
d > 0 => 2 roots
d = 0 => 1 root
d < 0 => 2 complex roots
'''
def test_discriminant(a:int, b:int, c:int) -> bool:
    d = (b**2)-(4*a*c)
    if d > 0:
        expRoots = "2 simple"
    elif d == 0:
        expRoots = "1 simple"
    else:
        expRoots = "2 complex"

    try:
        result = Quadratic.solveQuadratic(a, b, c)
        if len(result.split("\n")) > 1:
            actualRoots = "2"
            x1,x2 = result.split("\n")
        else:
            actualRoots = "1"
            x1 = result
        parts = x1.split(" ")
        if len(parts) > 3:
            actualRoots += " complex"
        else:
            actualRoots += " simple"

        assert (actualRoots == expRoots), f"Expected Roots are: {expRoots}, but Actual Roots are: {actualRoots}"
        print(f"Expected Roots are: {expRoots}")
        print(f"Actual Roots are: {actualRoots}")
        return actualRoots == expRoots
        
    except NotEnoughPrecisionException as e:
        print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")

'''
Checks if the Vieta sum and product relations between the roots and the coefficients hold
Vieta's product: x1 * x2 = c/a
Vieta's sum: x1 + x2 = -b/a
'''
def test_vieta(a:int, b:int, c:int) -> bool:

    try:
        result = Quadratic.solveQuadratic(a, b, c)
        line2 = ""
        x2 = None

        if len(result.split("\n")) > 1:
            line1,line2 = result.split("\n")
            line2 = simplify_complex_num(line2.replace("x2 = ",""))
        else:
            line1 = result

        line1 = simplify_complex_num(line1.replace("x1 = ",""))

        x1 = complex(line1)

        if line2 != "":
            x2 = complex(line2)
        
        if x2 is None:
            x2 = x1

        product = x1*x2
        sum = x1+x2

        assert(math.isclose(product.real,c/a)), "Vieta's product did not hold"
        assert(math.isclose(sum.real,-b/a)), "Vieta's sum did not hold"
        return True
    
    except NotEnoughPrecisionException as e:
        print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")
    return False

'''
Checks if the roots found, substituted into the quadratic formula equal zero
ax**2 + bx**2 + c = 0
'''
def test_evaluation(a:int, b:int, c:int) -> bool:
    try:
        result = Quadratic.solveQuadratic(a, b, c)
        line2 = ""
        x2 = None

        if len(result.split("\n")) > 1:
            line1,line2 = result.split("\n")
            line2 = simplify_complex_num(line2.replace("x2 = ",""))
        else:
            line1 = result

        line1 = simplify_complex_num(line1.replace("x1 = ",""))

        x1 = complex(line1)

        if line2 != "":
            x2 = complex(line2)
        
        if x2 is None:
            x2 = x1

        evalx1 = a*(x1**2)+b*x1+c
        evalx2 = a*(x2**2)+b*x2+c

        assert(math.isclose(evalx1.real,0,abs_tol=1e-9)), f"x1: {x1} is not a root of equation {a}x^2 + {b}x + {c}"
        assert(math.isclose(evalx2.real,0,abs_tol=1e-9)), f"x2: {x2} is not a root of equation {a}x^2 + {b}x + {c}"

        return True
    
    except NotEnoughPrecisionException as e:
        print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")
    return False

'''
creates/runs seed tests for automatically generating/running test cases based on the
metamorphic relations of discriminant properties
'''
def run_and_generate_discriminant_tests():
    tests_generated = []


    k = random.randint(2,1000)
    #negative d
    a = 5*k
    b = 5
    c = 5*k
    k = random.randint(2,1000)
    #seed test
    seedResult = test_discriminant(a,b,c)
    #auto test (scale by k)
    genResult = test_discriminant(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    k = random.randint(2,1000)
    #positive d
    a = 1
    b = 5*k
    c = 1
    k = random.randint(2,1000)
    #seed test
    seedResult = test_discriminant(a,b,c)
    #auto test (scale by k)
    genResult = test_discriminant(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    k = random.randint(2,1000)
    #zero d
    a = 1*k
    b = 2*k
    c = 1*k
    k = random.randint(2,1000)
    #seed test
    seedResult = test_discriminant(a,b,c)
    #auto test (scale by k)
    genResult = test_discriminant(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")

    return tests_generated
'''
creates/runs seed tests for automatically generating/running test cases based on the
metamorphic relations of the Vieta formulas for quadratic equations
'''
def run_and_generate_vieta_tests():
    mult_tests_generated = []
    invert_tests_generated= []
    negate_tests_generated = []

    k = random.randint(2,1000)
    #negative d
    a = 5*k
    b = 5
    c = 5*k
    k = random.randint(2,1000)
    #seed test
    seedResult = test_vieta(a,b,c)
    #auto test (scale by k)
    genResult = test_vieta(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    mult_tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    #auto test (invert coefficients)
    genResult = test_vieta(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    invert_tests_generated.append(f"a = {str(c)};b = {str(b)};c = {str(a)}")
    #auto test (scale by -1)
    genResult = test_vieta(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    negate_tests_generated.append(f"a = {str(-1*a)};b = {str(-1*b)};c = {str(-1*c)}")

    k = random.randint(2,1000)
    #positive d
    a = 1
    b = 5*k
    c = 1
    k = random.randint(2,1000)
    #seed test
    seedResult = test_vieta(a,b,c)
    #auto test (scale by k)
    genResult = test_vieta(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    mult_tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    #auto test (invert coefficients)
    genResult = test_vieta(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    invert_tests_generated.append(f"a = {str(c)};b = {str(b)};c = {str(a)}")
    #auto test (scale by -1)
    genResult = test_vieta(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    negate_tests_generated.append(f"a = {str(-1*a)};b = {str(-1*b)};c = {str(-1*c)}")
    
    k = random.randint(2,1000)
    #zero d
    a = 1*k
    b = 2*k
    c = 1*k
    k = random.randint(2,1000)
    #seed test
    seedResult = test_vieta(a,b,c)
    #auto test (scale by k)
    genResult = test_vieta(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    mult_tests_generated.append(f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}")
    #auto test (invert coefficients)
    genResult = test_vieta(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    invert_tests_generated.append(f"a = {str(c)};b = {str(b)};c = {str(a)}")
    #auto test (scale by -1)
    genResult = test_vieta(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    negate_tests_generated.append(f"a = {str(-1*a)};b = {str(-1*b)};c = {str(-1*c)}")

    return mult_tests_generated, invert_tests_generated, negate_tests_generated

'''
Will generate 1 random quadratic equation and check if the 
roots found for both it and its random transformations evaluate to zero
It will repeat this for as many trials as provided
low is the smallest possible number to be generated for coefficients, whereas high is the greatest
args: low = int, high = int, trials = int
'''
def run_and_generate_evaluation_tests(low:int, high:int, trials:int):
    tests_generated = []
    for i in range(trials):
        
        a = random.randint(low,high)
        b = random.randint(low,high)
        c = random.randint(low,high)
        k = random.randint(low,high)
        seedResult = test_evaluation(a,b,c)
        genResult = test_evaluation(k*a,k*b,k*c)
        assert(seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
        trial = f"a = {str(a)};b = {str(b)};c = {str(c)};k = {str(k)}"
        tests_generated.append(trial)
    return tests_generated

def save(tests:list[str], filename:str):
    try:
        with open(f"tests/new_tests/{filename}.txt", "x") as newFile:
            for trial in tests:
                newFile.write(trial+"\n")
    except Exception as e:
        os.remove(f"tests/new_tests/{filename}.txt")
        save(tests, filename)

if __name__ == "__main__":
    cwd = os.getcwd()
    if cwd.endswith("ATCG"):
        os.chdir("CaseStudies/Quadratic_Equation_Solver")
    elif cwd.endswith("Studies"):
        os.chdir("Quadratic_Equation_Solver")

    disc_tests = run_and_generate_discriminant_tests()
    vieta_tests = run_and_generate_vieta_tests()
    eval_tests = run_and_generate_evaluation_tests(-1000,1000,5)
    save(disc_tests, "disc_tests")
    save(vieta_tests[0], "vieta_mult_tests")
    save(vieta_tests[1], "vieta_invert_tests")
    save(vieta_tests[2], "vieta_negate_tests")
    save(eval_tests, "eval_tests")