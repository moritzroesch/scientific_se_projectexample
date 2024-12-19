from scientific_se_projectexample import calculator

def test_add():
    assert calculator.add(2,5) == 7
def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 3) == -3
def test_multiply():
    assert calculator.multiply(2,5) == 10
    
# add more tests here 
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
