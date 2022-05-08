class NegativeNumberException(Exception):
    def __init__(self, number):
        self.number = number
        self.message = "The number can't be negative!"
        super().__init__(self.message)



class BigNumberException(Exception):
    def __init__(self, number, bound):
        self.number = number
        self.message = f"Invalid input! The number can't be bigger than {bound}."
        super().__init__(self.message)


class NotNumericException(Exception):
    def __init__(self):
        self.message = "A string is not a valid input!"
        super().__init__(self.message)

class OverheatException(Exception):
    def __init__(self):
        super().__init__()

class RustException(Exception):
    def __init__(self):
        super().__init__()

