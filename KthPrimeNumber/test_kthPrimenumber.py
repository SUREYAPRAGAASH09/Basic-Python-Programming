import kthprimenumber

def test_five_and_five():
    #rearrange
    number = 5
    position = 5
    excepted = 19
    #act
    actual = kthprimenumber.kthprimeNumber(number,position)
    #assert
    assert excepted == actual

def test_minusvalue_position_ten():
    #rearrange
    number = -4
    position = 10
    excepted = 29
    #act
    actual = kthprimenumber.kthprimeNumber(number,position)
    #assert
    assert excepted == actual