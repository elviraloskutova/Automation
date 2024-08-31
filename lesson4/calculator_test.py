from calculator import Calculator


calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0
