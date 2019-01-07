import fizzbuzz_P

def checkfizzbuzz(value,excepted):
    actual = fizzbuzz_P.fizzBizz(value)
    assert excepted == actual

def test_canAssertTrue():
    assert True

def test_return1for1():
    checkfizzbuzz(1,"1")

def test_return2for2():
    checkfizzbuzz(2,"2")

def test_return3forfizz():
    checkfizzbuzz(3,"fizz")

def test_return5forbuzz():
    checkfizzbuzz(5,"buzz")

def test_return6forfizz():
    checkfizzbuzz(6,"fizz")

def test_return10forbuzz():
    checkfizzbuzz(10,"buzz")

def test_return15forfizzbuzz():
    checkfizzbuzz(15,"fizzbuzz")

def test_return7forwhoops():
    checkfizzbuzz(7,"whoops")

def test_return21forfizzwhoops():
    checkfizzbuzz(21,"fizzwhoops")

def test_return35forbuzzwhoops():
    checkfizzbuzz(35,"buzzwhoops")

def test_return42forfizzwhoops():
    checkfizzbuzz(42,"fizzwhoops")

def test_return49forwhoops():
    checkfizzbuzz(49,"whoops")

def test_return105forfizzbuzzwhoops():
    checkfizzbuzz(105,"fizzbuzzwhoops")
