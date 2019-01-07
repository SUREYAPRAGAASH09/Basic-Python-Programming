#To change the Title to correct format  
def Core_Function(string):
    letters = list(string)
    letters[0] = letters[0].upper()
    letters = ''.join(letters)
    return letters

#Check whether the string is used connecting words 
def Special_words(string):
    flag = False
    Special_words = ['a','the','is','to','at','in','with','and','but','or']
    if (string in Special_words):
        flag = True
    
    return flag    

#Title Captialization
def captialize(Title):
    Title = Title.lower() #converting the string to lower case String 
    Title_List = Title.split()#converting the sentence to words and stored in a List (Data Structure)
    Title_List[0] = Core_Function(Title_List[0])
    Title_List[-1] = Core_Function(Title_List[-1])
    for i in range(1,len(Title_List)-1):
        if (Special_words(Title_List[i])):
            Title_List[i] = Title_List[i]
        else:
            Title_List[i] = Core_Function(Title_List[i])
    Title_List = ' '.join(Title_List)
    return Title_List



print ("Precaution:")
print("\tBefore Entering Your Title ")
print("Place Quotation Mark Before and After Entering Your Title")
Title = input("Please Enter Your Title")
#s  = []
#s = captialize(Title)
print(captialize(Title))

