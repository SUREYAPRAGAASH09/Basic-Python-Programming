#function to find whether the given year is  leap year or not
#code 
def leap_year_1(year):
    if year%100==0:
        if year%400==0:
            return False
        return True
    return year%4==0
#testcase
def test_canAssertTrue():
    assert True

def  test_normal_leap_year():
    assert leap_year(1996)   

def test_normal_common_year():
    assert not leap_year(2001)

def test_atypical_common_year():
    assert not leap_year(1900)

def test_atypical_common_leap_year():
    assert leap_year(2000)

def leap_year_2(year):
    if (extra_conditions(year)):
        return True
    return year%4==0    

def extra_conditions(year):
    if year%100==0:
        if year%400==0:
            return True

def leap_year(year):
    if year%100==0 and not year%400==0: 
        return False
    return year%4==0

print(leap_year(1900))


