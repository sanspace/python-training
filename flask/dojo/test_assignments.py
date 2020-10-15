import pytest

def factor(fact):
    """returns factorial for a number"""
    factorial =  1
    if fact == 0:
        print('hello')
    else:
        for i in range(1,fact+1):
            factorial = factorial * i
        
    return(factorial)

# def test_factorial(inputs):
#      return factor(inputs)

@pytest.mark.parametrize(" test_input, expected",[(3,6),(4,8)])
def test_function(test_input, expected):
    assert factor(test_input) == expected 