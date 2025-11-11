from quadratic_equation_solver import Quadratic, NotEnoughPrecisionException
import random
import math

'''
discriminant metamorphic relation tests
d = b**2-4ac
d > 0 => 2 roots
d = 0 => 1 root
d < 0 => 2 complex roots
'''
def disc_test_discriminant_check(a:int, b:int, c:int) -> bool:
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
def disc_test_vieta_check(a:int, b:int, c:int) -> bool:

    try:
        result = Quadratic.solveQuadratic(a, b, c)
        line2 = ""
        x2 = None

        if len(result.split("\n")) > 1:
            line1,line2 = result.split("\n")
        else:
            line1 = result
        #print(line1.replace("x1 = ","").replace(" ","").replace("\n",""))
        x1 = complex(line1.replace("x1 = ","").replace(" ","").replace("\n",""))

        if line2 != "":

            x2 = complex(line2.replace("x2 = ","").replace(" ","").replace("\n",""))
        
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

def run_and_generate_discriminant_tests():
    k = random.randint(2,1000)
    #negative d
    a = 5
    b = 5
    c = 5
    #seed test
    seedResult = disc_test_discriminant_check(a,b,c)
    #auto test (scale by k)
    genResult = disc_test_discriminant_check(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

    k = random.randint(2,1000)
    #positive d
    a = 1
    b = 5
    c = 1
    #seed test
    seedResult = disc_test_discriminant_check(a,b,c)
    #auto test (scale by k)
    genResult = disc_test_discriminant_check(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    
    k = random.randint(2,1000)
    #zero d
    a = 1
    b = 2
    c = 1
    #seed test
    seedResult = disc_test_discriminant_check(a,b,c)
    #auto test (scale by k)
    genResult = disc_test_discriminant_check(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

def run_and_generate_vieta_tests():
    k = random.randint(2,1000)
    #negative d
    a = 5
    b = 5
    c = 5
    #seed test
    seedResult = disc_test_vieta_check(a,b,c)
    #auto test (scale by k)
    genResult = disc_test_vieta_check(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (invert coefficients)
    genResult = disc_test_vieta_check(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (scale by -1)
    genResult = disc_test_vieta_check(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"

    k = random.randint(2,1000)
    #positive d
    a = 1
    b = 5
    c = 1
    #seed test
    seedResult = disc_test_vieta_check(a,b,c)
    #auto test (scale by k)
    genResult = disc_test_vieta_check(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (invert coefficients)
    genResult = disc_test_vieta_check(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (scale by -1)
    genResult = disc_test_vieta_check(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    
    k = random.randint(2,1000)
    #zero d
    a = 1
    b = 2
    c = 1
    #seed test
    seedResult = disc_test_vieta_check(a,b,c)
    #auto test (scale by k)
    genResult = disc_test_vieta_check(k*a,k*b,k*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (invert coefficients)
    genResult = disc_test_vieta_check(c,b,a)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"
    #auto test (scale by -1)
    genResult = disc_test_vieta_check(-1*a,-1*b,-1*c)
    assert (seedResult == genResult), f"seed test was: {seedResult}, generated test was: {genResult}"



if __name__ == "__main__":
    run_and_generate_discriminant_tests()
    run_and_generate_vieta_tests()