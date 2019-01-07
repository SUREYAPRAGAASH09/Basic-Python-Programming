#string  = 'i LOve Solving Problems and iT is fUn'
#print string
#print (string).lower()
#S = string.split()
#print S
def getInt(s):
    return s




#s = [1,2,3,4,5]
#g = ['sureya','pragaash']
#print g[-1]
#g  = ' '.join(g)
#print g
#print type(g)
s = 'surey'
s = list(s)
#s = s.split()
#print s

#for i in range(1,len(s)-1):
 #   print s[i]
#N = input("Ente the numersdvibuh")
#if N > 0:
#    print "hello"
##else:
 #   print "bye"
import math
def check(N):
    flag = True
    if (N <= 0 or N == 2 or N == 1):
        return False
    for i in range(2,int(math.sqrt(N)-1)):
        if N%i==0:
            flag = False
    return flag

#print(check(-3))
#print math.sqrt(9)
#print abs(math.sqrt(9))     
#Printing the inbetween Prime Numbers
import math
#def Isprime(N):
#    Flag = True
#    if (N<=0 or N == 1):
#        return False
#    for i in range(2,int(math.sqrt(N)+1)):
#       if (N%i == 0):
 #           return False
#    return Flag

#def inbetween_Prime_Numbers(M,N):#

    #N = N + 1
    #for i in range(M,N):
    #    if Isprime(i):
    #        print i

#M = input("Enter the 1st Nuber")
#N = input("Enter the 2nd Number")
###if M<N :
 #   inbetween_Prime_Numbers(N,M)
#else:
 #   inbetween_Prime_Numbers(M,N)
#def stringcompares(fd):
 #   root = str("root")
 #   if ("root" == fd ):
 #       print("equal")
 #   else:
 #       print("noteaqual") #

#gives = (input("Enter the string to compares the srting "))
#stringcompares(gives)
def checkresult(intf):
    if (intf == 1):
        print("one")
    else:
        print("not one")
    if (intf == 2):
        print("two")
    else:
        print("not two")

#checkresult(2)
#give = givew
##N = list("hist")
#p#int(v,N)
#p = v[0]
#n  = N[0]
#
#p#rint(p+n)
#import os
#os.system("CLS")
#ls = ['sureya','hash',' ']
#inp = str(input("Enter the stimg"))
#if (inp in ls):
#    print("you have entered  valid input to the console")
#lse:
#3   print("sorry you have wrongly entered the input to the console")
#import random
#print (random.randint(0,2))
#d = str(1234)
# = d.split()
#f = list(d)
#print(f[-1])
f = "abc"
fe = "abc"
def equal():
    return f == fe 