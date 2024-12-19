from scientific_se_projectexample import calculator

def test_add():
    assert calculator.add(2,5) == 7
def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 3) == -3
