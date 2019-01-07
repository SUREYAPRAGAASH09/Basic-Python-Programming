def fizzBizz(value):
    if (value%3 == 0) and  (value%7 == 0) and (value%5==0):
        return "fizzbuzzwhoops"
    elif (value%3 == 0) and  (value%7 == 0):
        return "fizzwhoops"
    elif (value%5==0) and (value%3==0):
            return "fizzbuzz"
    elif (value%7==0) and (value%5==0):
            return "buzzwhoops"
    elif (value%7==0):
        return "whoops"
    elif (value%3==0):
        return "fizz"
    elif(value%5==0):
        return "buzz"
    else:
        return str(value)

