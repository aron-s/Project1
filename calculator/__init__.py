""" This is the Calculator Class"""

class Calculation:

    def __init__(self, tuple_list: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    """Addition class inherits calculation"""
    def calculate(self):
        result = 0.0
        for value in self.values:
            result = result + value
        return result


class Subtraction(Calculation):
    """ Subtraction class inherits calculation"""
    def calculate(self):
        if len(self.values) != 0:
            result = self.values[0]
        else:
            return 0.0
        for value in self.values:
            result = result - value
        result = result + self.values[0]
        return result


class Calculator:

    @staticmethod
    def add(tuple_list):
        """ This is the add method"""
        calculation = Addition.create(tuple_list)
        return calculation.calculate()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method"""
        calculation = Subtraction.create(tuple_list)
        return calculation.calculate()
