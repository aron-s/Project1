"""Testing the Calculator"""
from calculator import Calculator, Calculation, Addition, Subtraction


def tuple_list():
    """Arranging Data for AAA Testing"""
    return 1.0, 2


def test_calculator_is_instance():
    """Testing the Calculator"""
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculation_is_instance():
    """Testing the Calculator"""
    calculate = Calculation((1, 2))
    assert isinstance(calculate, Calculation)


def test_calculation_addition_instance():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)


def test_calculator_add_method():
    """Testing the Calculator"""
    result = Calculator.add(tuple_list())
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert Calculator.subtract(tuple_list()) == -1
