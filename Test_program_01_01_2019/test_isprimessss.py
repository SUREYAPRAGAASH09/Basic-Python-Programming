#test cases for isprime 
import validate_prime

def test_isprimes():
    #rearrange
    n = 1
    excepted = False
    #act
    actual = validate_prime.isprime(n)
    #assert
    assert excepted == actual

def test_negativenumbers():
    #rearrange
    n = -1
    excepted = False
    #act
    actual = validate_prime.isprime(n)
    #assert
    assert excepted == actual

def test_primenumbers():
    #rearrange
    n = 1001
    expected = False # because 1001 is divisible by 7 = 143
    #act
    actual = validate_prime.isprime(n)
    #assert
    assert expected == actual 


def test_even_primenumbers():
    #rearrange
    n = 2
    expected = True 
        #act
    actual = validate_prime.isprime(n)
    #assert
    assert expected == actual 
        
def test_Zero_primenumbers():
    #rearrange
    n = 0
    expected = False 
    #act
    actual = validate_prime.isprime(n)
    #assert
    assert expected == actual 

def test_some_larger_numbers():
    #rearrange
    n = 123457
    expected = True 
    #act
    actual = validate_prime.isprime(n)
    #assert
    assert expected == actual 

