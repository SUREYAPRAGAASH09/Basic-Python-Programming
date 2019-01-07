import palindrome

def test_CanAssertTrue():
    assert True

def test_121returnTrue():
    #arrange
    n = 121
    excepted = True
    #act
    actual = palindrome.palindrome(n)
    #assert
    assert excepted == actual