import armstrong

def test_CanAssertTrue():
    assert True 

def test_153returnTrue(): #Environment test
    #arrange
    n = 153
    excepted = True
    #act
    actual = armstrong.armstrongs(n)
    #assert
    assert excepted == actual


def test_1533returnFalse():
    #arrange
    n = 1533
    excepted = False
    #act
    actual = armstrong.armstrongs(n)
    #assert
    assert excepted == actual
