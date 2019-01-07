import sum_of_two_numbers 

def test_true():
    #rearrange
    a=10
    b=20
    Excepted = 30
    #act
    actual = sum_of_two_numbers.sum(a,b)
       #assert
    assert actual == Excepted 

def test_false():
    #rearrange
    a=10
    b=20
    Expected = 32
    #act 
    actual = sum_of_two_numbers.sum(a,b)
    #assert
    assert actual != Expected
