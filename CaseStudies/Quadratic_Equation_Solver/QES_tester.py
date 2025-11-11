from quadratic_equation_solver import Quadratic, NotEnoughPrecisionException
import random
import math

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
    k = random.randint(2,1000)
    #negative d
    a = 5
    b = 5
    c = 5
    #seed test
    seedResult = test_discriminant(a,b,c)
    #auto test (scale by k)
    genResult = test_discriminant(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

    k = random.randint(2,1000)
    #positive d
    a = 1
    b = 5
    c = 1
    #seed test
    seedResult = test_discriminant(a,b,c)
    #auto test (scale by k)
    genResult = test_discriminant(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    
    k = random.randint(2,1000)
    #zero d
    a = 1
    b = 2
    c = 1
    #seed test
    seedResult = test_discriminant(a,b,c)
    #auto test (scale by k)
    genResult = test_discriminant(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

'''
creates/runs seed tests for automatically generating/running test cases based on the
metamorphic relations of the Vieta formulas for quadratic equations
'''
def run_and_generate_vieta_tests():
    k = random.randint(2,1000)
    #negative d
    a = 5
    b = 5
    c = 5
    #seed test
    seedResult = test_vieta(a,b,c)
    #auto test (scale by k)
    genResult = test_vieta(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (invert coefficients)
    genResult = test_vieta(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (scale by -1)
    genResult = test_vieta(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

    k = random.randint(2,1000)
    #positive d
    a = 1
    b = 5
    c = 1
    #seed test
    seedResult = test_vieta(a,b,c)
    #auto test (scale by k)
    genResult = test_vieta(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (invert coefficients)
    genResult = test_vieta(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (scale by -1)
    genResult = test_vieta(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    
    k = random.randint(2,1000)
    #zero d
    a = 1
    b = 2
    c = 1
    #seed test
    seedResult = test_vieta(a,b,c)
    #auto test (scale by k)
    genResult = test_vieta(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (invert coefficients)
    genResult = test_vieta(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (scale by -1)
    genResult = test_vieta(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

'''
Will generate 1 random quadratic equation and check if the 
roots found for both it and its random transformations evaluate to zero
It will repeat this for as many trials as provided
low is the smallest possible number to be generated for coefficients, whereas high is the greatest
args: low = int, high = int, trials = int
'''
def run_and_generate_evaluation_tests(low:int, high:int, trials:int):
    for i in range(trials):
        a = random.randint(low,high)
        b = random.randint(low,high)
        c = random.randint(low,high)
        k = random.randint(low,high)
        seedResult = test_evaluation(a,b,c)
        genResult = test_evaluation(k*a,k*b,k*c)
        assert(seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

if __name__ == "__main__":
    run_and_generate_discriminant_tests()
    run_and_generate_vieta_tests()
    run_and_generate_evaluation_tests(-1000,1000,5)