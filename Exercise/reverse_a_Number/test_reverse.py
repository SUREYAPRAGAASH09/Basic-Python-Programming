import reverse
def test_CanAssertTrue():
    assert True

def test_1234to4321():
    actual = reverse.reversess(1234)
    excepted = 4321
    assert excepted == actual

