#recursive approarch using recurison and an array
#O(n) complexity 
def fiboPro(n,arrayAux): 
    
    if arrayAux[n] != None:
        return arrayAux[n] 

    if n == 0 or n == 1:
        result = 1 
    else: 
        result = fibo(n-1,arrayAux) + fibo(n-2,arrayAux) 
    arrayAux[n] = result 
    return result

#n = 10
#arrayAux = [None] * (n + 1)  #Create an array with length n + 1 before executing the function 
#print(len(arrayAux))
#print(fiboPro(n,arrayAux)) 


#dynamic approach using an array
#solved in O(n) time 

def fiboProMax(n):
    #create an array with length n + 1 
    fiboArray = [None] * (n+1)
    #Assing base cases to the fiboArray 
    fiboArray[0] = 0 
    fiboArray[1] = 1 
    for i in range(2,n +1): 
        fiboArray[i] = fiboArray[i-1] + fiboArray[i-2] 
    return fiboArray[n] 

#print(fiboProMax(8)) 

#Naive approach in O(2^n)  
def fiboNaive(n): 
    if n == 0: 
        return 0 
    if n == 1: 
        return 1 
    else: 
        return fiboNaive(n-1) + fiboNaive(n-2) 

#print(fiboNaive(8))




