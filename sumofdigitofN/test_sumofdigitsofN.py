import sumofdigitsofN

def test_negative_number():
    #rearrange
    n = -10003
    excepted = " Sorry,sum of digits of N can't be found"
    #act
    actual = sumofdigitsofN.sumofdigits(n)
    #assert
    assert excepted == actual


def test_with_Zero():
    #rearrange
    n = 0
    excepted = 0
    #act
    actual = sumofdigitsofN.sumofdigits(n)
    #assert
    assert excepted == actual


def test_some_number():
    #rearrange
    n = 10003
    excepted = 4
    #act
    actual = sumofdigitsofN.sumofdigits(n)
    #assert
    assert excepted == actual