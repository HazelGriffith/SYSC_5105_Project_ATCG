from source.quadratic_equation_solver import solveQuadratic, validateInput
from source.quadratic_equation_problem import Quadratic_Equation_Problem
from source.notEnoughPrecisionException import NotEnoughPrecisionException
import random, math, os, pytest

disc_tests = {}
eval_tests = {}
vieta_mult_tests = {}
vieta_invert_tests = {}
vieta_negate_tests = {}

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

def load_tests(filename:str):
    with open(f"tests/test_cases/tests_used/{filename}.txt", "r") as tests_file:
        line = tests_file.readline()
        lineNo = 1
        tests = {}
        while line != "":
            coeffs = line.split(";")
            a = int(coeffs[0].replace("a = ",""))
            b = int(coeffs[1].replace("b = ",""))
            c = int(coeffs[2].replace("c = ",""))

            if filename == "disc_tests" or filename == "eval_tests" or filename == "vieta_mult_tests":
                k = int(coeffs[3].replace("k = ",""))
                gen_prob = Quadratic_Equation_Problem(a,b,c,k)
                seed_prob = Quadratic_Equation_Problem(a,b,c,None)
            elif filename == "vieta_invert_tests":
                gen_prob = Quadratic_Equation_Problem(a,b,c,None)
                seed_prob = Quadratic_Equation_Problem(c,b,a,None)
            elif filename == "vieta_negate_tests":
                gen_prob = Quadratic_Equation_Problem(a,b,c,None)
                seed_prob = Quadratic_Equation_Problem(-1*a,-1*b,-1*c,None)
            
            tests.update({f"Trial {filename} {lineNo}" : {"seed_prob" : seed_prob, "gen_prob" : gen_prob}})
            line = tests_file.readline()
            lineNo += 1
    return tests

cwd = os.getcwd()
print(cwd)
if cwd.endswith("ATCG"):
    os.chdir("CaseStudies/Quadratic_Equation_Solver")
elif cwd.endswith("Studies"):
    os.chdir("Quadratic_Equation_Solver")

disc_tests = load_tests("disc_tests")
eval_tests = load_tests("eval_tests")
vieta_tests = load_tests("vieta_invert_tests")
vieta_tests.update(load_tests("vieta_mult_tests"))
vieta_tests.update(load_tests("vieta_negate_tests"))

def pytest_generate_tests(metafunc):

    if "get_discrim_tests" in metafunc.fixturenames:
        test_ids = list(disc_tests.keys())
        test_values = list(disc_tests.values())

        metafunc.parametrize("get_discrim_tests", test_values, ids=test_ids)

    if "get_vieta_tests" in metafunc.fixturenames:
        test_ids = list(vieta_tests.keys())
        test_values = list(vieta_tests.values())

        metafunc.parametrize("get_vieta_tests", test_values, ids=test_ids)

    if "get_eval_tests" in metafunc.fixturenames:
        test_ids = list(eval_tests.keys())
        test_values = list(eval_tests.values())

        metafunc.parametrize("get_eval_tests", test_values, ids=test_ids)

def test_discriminants(get_discrim_tests):
    seed_problem = get_discrim_tests["seed_prob"]

    seed_prop_holds = discriminant_property_check(validateInput(str(seed_problem.a)), validateInput(str(seed_problem.b)), validateInput(str(seed_problem.c)))

    gen_problem = get_discrim_tests["gen_prob"]

    gen_prop_holds = discriminant_property_check(validateInput(str(gen_problem.a)), validateInput(str(gen_problem.b)), validateInput(str(gen_problem.c)))

    assert(seed_prop_holds and gen_prop_holds)

def test_vieta(get_vieta_tests):
    seed_problem = get_vieta_tests["seed_prob"]

    seed_prop_holds = vieta_property_check(validateInput(str(seed_problem.a)), validateInput(str(seed_problem.b)), validateInput(str(seed_problem.c)))

    gen_problem = get_vieta_tests["gen_prob"]

    gen_prop_holds = vieta_property_check(validateInput(str(gen_problem.a)), validateInput(str(gen_problem.b)), validateInput(str(gen_problem.c)))

    assert(seed_prop_holds and gen_prop_holds)

def test_eval(get_eval_tests):
    seed_problem = get_eval_tests["seed_prob"]

    seed_prop_holds = evaluation_property_check(validateInput(str(seed_problem.a)), validateInput(str(seed_problem.b)), validateInput(str(seed_problem.c)))

    gen_problem = get_eval_tests["gen_prob"]

    gen_prop_holds = evaluation_property_check(validateInput(str(gen_problem.a)), validateInput(str(gen_problem.b)), validateInput(str(gen_problem.c)))

    assert(seed_prop_holds and gen_prop_holds)

'''
discriminant metamorphic relation tests
d = b**2-4ac
d > 0 => 2 roots
d = 0 => 1 root
d < 0 => 2 complex roots
'''
def discriminant_property_check(a:int, b:int, c:int) -> bool:

    d = (b**2)-(4*a*c)
    if d > 0:
        expRoots = "2 simple"
    elif d == 0:
        expRoots = "1 simple"
    else:
        expRoots = "2 complex"

    try:
        result = solveQuadratic(a, b, c)
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

        return actualRoots == expRoots
        
    except NotEnoughPrecisionException as e:
        print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")

'''
Checks if the Vieta sum and product relations between the roots and the coefficients hold
Vieta's product: x1 * x2 = c/a
Vieta's sum: x1 + x2 = -b/a
'''
def vieta_property_check(a:int, b:int, c:int) -> bool:

    try:
        result = solveQuadratic(a, b, c)
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

        vieta_prop_1 = math.isclose(product.real,c/a)
        vieta_prop_2 = math.isclose(sum.real,-b/a)
        return vieta_prop_1 and vieta_prop_2
    
    except NotEnoughPrecisionException as e:
        print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")
    return False

'''
Checks if the roots found, substituted into the quadratic formula equal zero
ax**2 + bx**2 + c = 0
'''
def evaluation_property_check(a:int, b:int, c:int) -> bool:
    try:
        result = solveQuadratic(a, b, c)
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

        evalx1_prop = math.isclose(evalx1.real,0.0,abs_tol=1e-9)
        evalx2_prop = math.isclose(evalx2.real,0.0,abs_tol=1e-9)

        return evalx1_prop and evalx2_prop
    
    except NotEnoughPrecisionException as e:
        print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")
    return False