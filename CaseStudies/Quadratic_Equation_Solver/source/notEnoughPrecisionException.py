class NotEnoughPrecisionException(Exception): # pragma: no mutate
	
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)