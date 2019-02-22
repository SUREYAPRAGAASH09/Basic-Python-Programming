#test file for Counting Even and odd Count 
import countevenodd

def test_CanAssertTrue(): #Environment Test
    assert True

def test_12345return23():
    #arrange
    n = 12345
    excepted = (2,3)
    #act
    actual = countevenodd.countevenodd(n)
    #assert
    assert excepted == actual


def test_12345678910return55():
    #arrange
    n = 12345678910
    excepted = (5,6)
    #act
    actual = countevenodd.countevenodd(n)
    #assert
    assert excepted == actual
