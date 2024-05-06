from dictionary import insert,delete,search,printHashTable,hashFunction

def hashFunctionZipCode(code): 
    for element in code: 
        if element.isdigit(): 
            index = int(element) % 9 #Hash function 
        else: 
            index = ord(element) % 9 #if it's a non numeric char use the ascii code 
        return index 