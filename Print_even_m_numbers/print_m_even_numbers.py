def m_even_numbers(N):
    count = 0
    even = 2
    EvenNumbers = []
    
    

    while (count<N):
        if(even % 2 == 0):
            EvenNumbers.append(even)
        count = len(EvenNumbers)   
        even+=1
        #count += 1
    if (N == 0 or N < 0 or N==1):
        return "There is no Even Numbers found"
    return EvenNumbers

print(m_even_numbers(-1))