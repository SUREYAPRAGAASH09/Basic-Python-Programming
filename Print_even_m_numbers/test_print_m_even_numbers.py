import print_m_even_numbers

def test_negative_numbers():
    #rearrange
    n = -1
    excepted = "There is no Even Numbers found"
    #act
    actual = print_m_even_numbers.m_even_numbers(n)
    #assert
    assert excepted == actual

def test_positive_numbers():
    #rearrange
    n = 1
    excepted = [2]
     #act
    actual = print_m_even_numbers.m_even_numbers(n)
    #assert
    assert excepted == actual


def test_with_zero():
    #rearrange
    n = 0
    excepted = "There is no Even Numbers found"
     #act
    actual = print_m_even_numbers.m_even_numbers(n)
    #assert
    assert excepted == actual