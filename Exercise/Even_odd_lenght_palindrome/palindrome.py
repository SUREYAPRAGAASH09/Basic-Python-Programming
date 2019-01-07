#To check whether the given number is palindrome or not 
import reverse
def palindrome(N):
    Num  = N
    N = reverse.reversess(N) 
    flag = False
    if Num == N:
        flag = True
    return flag

#print(palindrome(343))
