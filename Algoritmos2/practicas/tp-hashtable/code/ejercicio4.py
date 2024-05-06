from dictionary import printHashTable,delete,search,hashFunction,insert


def isPermutation(str1,str2): 
    #If the strings are diffents lengths return False
    if len(str1) != len(str2): #len() function is O(1)
        return False 
    
    #Create a hash table and insert chars from str1 
    hashStr1 = [[] for _ in range(15)] #dictionary size 10 
    for char in str1: 
        insert(hashStr1,ord(char),char) 

    #Search all elements from str2 in hashStr1 
    for char in str2: 
        if not search(hashStr1,ord(char)): #Search the corresponding ascii code for the char (key) in the hash table 
            return False 
    return True  

print(isPermutation("hola","laoh"))



