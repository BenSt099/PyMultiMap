class BadParameterError(Exception):
    def __init__(self, salary, message="Second parameter has to be a list or a numpy-array !"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)