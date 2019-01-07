import printPrimeNumbersFrom2

def test_print_Prime_Numbers_from_2():
    #rearrange
    n = 2
    excepted = "Sorry,There is no Prime Numbers"
    #act
    actual =  str(printPrimeNumbersFrom2.primeNumbersfrom2(n))
    #assert
    assert excepted == actual

def test_print_Prime_Numbers_from_negative_Numbers():
    #rearrange
    n = 2
    excepted = "Sorry,There is no Prime Numbers"
    #act
    actual =  str(printPrimeNumbersFrom2.primeNumbersfrom2(n))
    #assert
    assert excepted == actual

def test_print_Prime_Numbers_from_0():
    #rearrange
    n = 20
    excepted = [2, 3, 5, 7, 11, 13, 17, 19]
    #act
    actual =  (printPrimeNumbersFrom2.primeNumbersfrom2(n))
    #assert
    assert excepted == actual


