import divisibiity_of_all_numbers

def test_CanAssertTrue():
    assert True

def test_3699returntheNumbercanbedivisiblealltheintegers():
    actual = divisibiity_of_all_numbers.divisibleofallNumbers(123)
    Excepted = "the Number can't be divided"
    assert Excepted == actual

def test_36returntheNumbercanbedivisiblealltheintegers():
    actual = divisibiity_of_all_numbers.divisibleofallNumbers(36)
    Excepted = "the Number can be divisible all the integers"
    assert Excepted == actual

