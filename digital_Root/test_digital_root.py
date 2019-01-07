import digital_root

def test_postive_number():
    #rearrange
    n = 1234
    excepted = 1
    #act
    actual = digital_root.digital_root(n)
    #assert
    assert excepted == actual

    
def test_postive_number_():
    #rearrange
    n = 12345
    excepted = 6
    #act
    actual = digital_root.digital_root(n)
    #assert
    assert excepted == actual


def test_negative_number():
    #rearrange
    n = -1234
    excepted = 0
    #act
    actual = digital_root.digital_root(n)
    #assert
    assert excepted == actual