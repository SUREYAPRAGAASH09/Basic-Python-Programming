import print_m_odd_numbers

def test_negative_numbers():
    #rearrange
    n = -1
    excepted = "There is no odd Numbers found"
    #act
    actual = print_m_odd_numbers.m_even_numbers(n)
    #assert
    assert excepted == actual

def test_positive_numbers():
    #rearrange
    n = 1
    excepted = [3]
     #act
    actual = print_m_odd_numbers.m_even_numbers(n)
    #assert
    assert excepted == actual

def test_with_Zero():
    #rearrange
    n = 0
    excepted = "There is no odd Numbers found"
    #act
    actual = print_m_odd_numbers.m_even_numbers(n)
    #assert
    assert excepted == actual



