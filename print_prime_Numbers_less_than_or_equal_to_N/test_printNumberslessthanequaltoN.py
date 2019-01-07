import primeNumberslessthanorequaltoN

def testprimeNumberslessthanorequal1():
    #rearrange
    N = 1
    excepted = [2]
    #act
    actual = primeNumberslessthanorequaltoN.printNumberlessthanorequaltoN(N)
    #assert
    assert excepted == actual


def testprimeNumberslessthanorequal2():
    #rearrange
    N = 2
    excepted = [2,3]
    #act
    actual = primeNumberslessthanorequaltoN.printNumberlessthanorequaltoN(N)
    #assert
    assert excepted == actual


def testprimeNumberslessthanorequal5():
    #rearrange
    N = 5
    excepted = [2,3,5,7,11]
    #act
    actual = primeNumberslessthanorequaltoN.printNumberlessthanorequaltoN(N)
    #assert
    assert excepted == actual


def testprimeNumberslessthanorequal0():
    #rearrange
    N = 0
    excepted = []
    #act
    actual = primeNumberslessthanorequaltoN.printNumberlessthanorequaltoN(N)
    #assert
    assert excepted == actual


def testprimeNumberslessthanorequal20():
    #rearrange
    N = 20
    excepted = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    #act
    actual = primeNumberslessthanorequaltoN.printNumberlessthanorequaltoN(N)
    #assert
    assert excepted == actual