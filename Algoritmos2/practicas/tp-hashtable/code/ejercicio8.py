from dictionary import * 

def findSubStringIndex(S,P):
    hash = hashFunction(P) 
    for i in range(len(S)): 
        if hashFunction(S[i:len(P)+i]) == hash: 
            return i 
    return None 


def hashFunction(string): 
    hash = 0 
    for i in range(len(string)): 
        hash += i * ord(string[i]) 
    return hash 


s = "abracadabra" 
p = "cada"
print(findSubStringIndex(s,p))

