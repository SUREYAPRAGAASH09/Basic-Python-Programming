import print_prime_numbers_from_1_to_N
def test_primeNumbersfrom1to20():
    #rearrange
    n = 20
    excepted = [1, 2, 3, 5, 7, 11, 13, 17]
    #act
    actual  = print_prime_numbers_from_1_to_N.prime_numbers_from_1_to_N(n)
    #assert
    assert excepted == actual 

def test_primeNumbersfrom1to2():
    #rearrange
    n = 2
    excepted = [1]
    #act
    actual  = print_prime_numbers_from_1_to_N.prime_numbers_from_1_to_N(n)
    #assert
    assert excepted == actual 

def test_primeNumbersfrom1tominus20():
    #rearrange
    n = 20
    excepted = [1, 2, 3, 5, 7, 11, 13, 17]
    #act
    actual  = print_prime_numbers_from_1_to_N.prime_numbers_from_1_to_N(n)
    #assert
    assert excepted == actual 


