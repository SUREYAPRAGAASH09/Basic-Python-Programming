import palindrome

# def eveoddlenghtpalindrome(N):
#     lenght = palindrome.palindrome(N)
#     flag = False
#     if (lenght%2==0):
#         flag = True
#     return flag

# print(eveoddlenghtpalindrome(121))


def list_of_palindrome_numbers(N):
    flag = False
    for i in range(1,N):
        if palindrome.palindrome(i):
            if i%2==0:
                print("")


list_of_palindrome_numbers(10000)