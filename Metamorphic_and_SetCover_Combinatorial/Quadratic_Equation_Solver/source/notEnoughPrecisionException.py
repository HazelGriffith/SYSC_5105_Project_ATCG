'''
This class creates a sub class of the Exception class to indicate that a value is too large or too small
That is to say the computer is not precise enough to store and compute this value
'''
class NotEnoughPrecisionException(Exception): # pragma: no cover
	
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)