import factors_of_N
def test_factors():
    #rearrange
    n = 100
    excepted = [2,4,5,10,20,25,50]
    #act
    actual = factors_of_N.factor(n)
    #assert
    assert excepted == actual

def test_negativenumbers():
    #rearrange
    n = -100
    excepted = [2,4,5,10,20,25,50]
    #act
    actual = factors_of_N.factor(n)
    #assert
    assert excepted == actual