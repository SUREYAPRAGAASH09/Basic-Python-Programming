import IsPrime

def test_Isprimenumbers():
    #rearrange
    a = 2
    excepted = True
    #act
    actual = IsPrime.Isprime(a)
    #assert
    assert excepted == actual

def test_Isprimenumbersy():
    #rearrange
    a = 13
    excepted = True
    #act
    actual = IsPrime.Isprime(a)
    #assert
    assert excepted == actual  