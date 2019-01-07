import print_all_prime_factors_of_N

def test_prime_Numbers():
    #rearrange
    N = 23
    excepted = [23]
    #act
    actual = print_all_prime_factors_of_N.prime_factors(N)
    #assert
    assert excepted == actual


def test_composite_Numbers():
    #rearrange
    N = 18
    excepted = [2,3,3]
    #act
    actual = print_all_prime_factors_of_N.prime_factors(N)
    #assert
    assert excepted == actual


def test_zero():
    #rearrange
    N = 0
    excepted = "sorry prime Numbers can't be found"
    #act
    actual = print_all_prime_factors_of_N.prime_factors(N)
    #assert
    assert excepted == actual


def test_negative_number():
    #rearrange
    N = 0
    excepted = "sorry prime Numbers can't be found"
    #act
    actual = print_all_prime_factors_of_N.prime_factors(N)
    #assert
    assert excepted == actual