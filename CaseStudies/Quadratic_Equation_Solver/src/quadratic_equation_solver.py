import math


class Quadratic_Equation_Problem: # pragma: no cover
     
    def __init__(self, a, b, c, k = None):
        if k is None:
            self.a = a
            self.b = b
            self.c = c
        else:
            self.a = a*k
            self.b = b*k
            self.c = c*k
          

class NotEnoughPrecisionException(Exception): # pragma: no cover
	
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)




class Quadratic:

    ERROR = 0.00000001 # acceptable error for Newton's Method
    '''
	* Solves the quadratic equation and outputs roots to the screen. Throws an exception is precision is lost during calculation.
	*/
	'''
    @staticmethod
    def solveQuadratic(a:float, b:float, c:float):
        sqrt = 0
        q = 0
        discriminant = b*b - 4 * a * c
        real = "" 
        imaginary = ""
        output = ""
        x1 = "" 
        x2 = ""
		
		# check for overflow and b^2 >> 4ac
        if (math.isnan(discriminant) or discriminant == b*b):
            raise NotEnoughPrecisionException("Not enough precision to process")
		
        if (discriminant < 0): # complex roots
            sqrt = Quadratic.sqrtByNewton(-1*discriminant)
            real = Quadratic.formatDouble((-1*b)/(2*a))
            imaginary = Quadratic.formatDouble(sqrt/(2*a))
			# don't print redundant zeros and signs
            output = "x1 = "
            output += real + " + " if (not real == "0") else ""
            output += imaginary if (not imaginary == "1") else ""
            output += "j\nx2 = "
            output += real + " - " if (not real == "0") else "-"
            output += imaginary if (not imaginary == "1") else ""
            output += "j"
            print(output)
            return output
        else: # real roots
            sqrt = Quadratic.sqrtByNewton(discriminant)
			# mixed approach to avoid subtractive cancellation
            q = (-0.5) * (b + Quadratic.sign(b)*sqrt)
            x1 = Quadratic.formatDouble(q/a)
            x2 = Quadratic.formatDouble(c/q)
			# don't print the same root twice
            output = "x1 = " + x1
            output += "\nx2 = " + x2 if (not x1 == x2) else ""
            print(output)
            return output
	
    '''/*
	* Extracts the sign of a double value.
	*/'''
    @staticmethod
    def sign(b:float) -> int:
        return 1 if (b > 0) else -1
	
    '''/*
    * Computes the square root of a number using Newton's Method. Returns when the error threshold has been reached.
	*/'''
    @staticmethod
    def sqrtByNewton(value:float) -> float:
		# square root of zero is zero
        if (value == 0.0): 
            return 0.0
        previous = (1 + value)/2
		
		# iterate until error threshold is reached
        while(True):
            result = (previous + value/previous) / 2
            if (previous - result < Quadratic.ERROR):
                break
            previous = result
		
        return result
		
	
    '''/* 
	* Checks whether a double value actually represents an integer, and formats accordingly.
	*/'''
    @staticmethod
    def formatDouble(value:float) -> str:
		
		# check if value is actually an integer
        if (math.floor(value) == value):
            intValue = int(value)
            return intValue.__str__()
        else:
            doubleValue = value
            return doubleValue.__str__()
		
		

	
    '''/*
	* Validates the input by converting to type double and inspecting for overflow. Throws an exception if overflow occurred.
	*/'''
    @staticmethod
    def validateInput(input:str) -> float:
		
		# parse the input
        value = float(input)
		
		# format value to decimal of (almost) arbitrary length 100.100
		
		# append .0 when input is integer
        formatted = input
        if (input.find('.') == -1): 
            formatted += ".0"

		# if new value is not equal to original, overflow has occurred
        if (not f"{value}" == formatted) and (not (value.__str__() == input) ): # toString to validate e-notation
            raise NotEnoughPrecisionException("Not enough precision to process")
		
        return value
	

if __name__ == "__main__": # pragma: no cover
		
	a = b = c = 0 
		
	prompt = ""
		
	# welcome message
	print("Welcome to Quadratic Equation Solver.\n" +
				"A quadratic equation can be written in the form ax^2 + bx + c = 0, where x is an unknown, a, b, and c are constants, and a is not zero.\n" +
				"Given values for a, b, and c, this program will produce the two roots of the equation. Both real and complex roots are supported, but not complex coefficients.\n" +
				"Press Ctrl+C to quit at any time.")
		
	# repeat until the user quits
	while (True):
		
		# collect input from user
		try:
			a = 5
			a = Quadratic.validateInput(input("Enter a value for 'a':")) # validate before storing
			# make sure a is not zero
			if (a == 0):
				print("'a' cannot be zero!")
				continue
                    
			b = Quadratic.validateInput(input("Enter a value for 'b':"))
			c = Quadratic.validateInput(input("Enter a value for 'c':"))
		except NotEnoughPrecisionException as e :
			print("The value you entered is too large or too small! Please enter a value between " + str(2**-1074) +
					" and " + str(1.7976931348623157*10**308) + ".")
			continue
		except ValueError as e:
			print("The value you entered is not allowed! Please enter a number. E.g. 4, 0.3, -12")
			continue
			
		      
		# solve equation
		try :
			Quadratic.solveQuadratic(a, b, c)
		except NotEnoughPrecisionException as e:
			print("Failed to find an accurate solution! This can happen when the values are too" +
					" big, a is too close to zero, or b^2 is much bigger than 4ac.")
			
		# prompt user
		prompt = input("Would you like to try again? [y/n]")
			
		# quit if no
		if (not prompt == "y"):
			break
		
		# goodbye
		print("Thank you for using Quadratic Equation Solver!")