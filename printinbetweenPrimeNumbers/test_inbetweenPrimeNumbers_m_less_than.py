import printinbetweenPrimeNumbers_m_less_than

def test_two_even_numbers():
    #rearrange
    m = 8
    n = 10
    excepted = "There is no Prime Numbers exsist"
    #act
    actual = printinbetweenPrimeNumbers_m_less_than.inbetweenPrimeNumbers(m,n)
    #assert
    assert excepted == actual

def test_one_and_two():
    #rearrange
    m = 1
    n = 2
    excepted = [2]
    #act
    actual = printinbetweenPrimeNumbers_m_less_than.inbetweenPrimeNumbers(m,n)
    #assert
    assert excepted == actual

def test_with_two_and_three():
    #rearrange
    m = 2
    n = 3
    excepted = [2,3]
    #act
    actual = printinbetweenPrimeNumbers_m_less_than.inbetweenPrimeNumbers(m,n)
    #assert
    assert excepted == actual


def test_with_seven_and_three():
    #rearrange
    m = 3
    n = 7
    excepted = [3,5,7]
    #act
    actual = printinbetweenPrimeNumbers_m_less_than.inbetweenPrimeNumbers(m,n)
    #assert
    assert excepted == actual


def test_with_seven_and_eleven():
    #rearrange
    m = 7
    n = 11
    excepted = [7,11]
    #act
    actual = printinbetweenPrimeNumbers_m_less_than.inbetweenPrimeNumbers(m,n)
    #assert
    assert excepted == actual    


def test_with_three_and_two():
    #rearrange
    m = 3
    n = 2
    excepted = "Provide always M less than N"
    #act
    actual = printinbetweenPrimeNumbers_m_less_than.inbetweenPrimeNumbers(m,n)
    #assert
    assert excepted == actual