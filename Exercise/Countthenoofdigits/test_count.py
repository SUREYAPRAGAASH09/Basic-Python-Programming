import count
def test_CanAssertTrue():
    assert True

def test_1234return4():
    #arrange
    n = 12344
    excepted = 5
    #act
    actual = count.countnumbers(n)
    #assert
    assert excepted == actual 