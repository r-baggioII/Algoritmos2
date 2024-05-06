from dictionary import insert,delete,search,printHashTable,hashFunction

'''
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. 
Por ejemplo, la cadena 'aabcccccaaa' se convertiría en 'a2blc5a3'. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). 
Justificar el costo en tiempo de la solución propuesta.
'''

def compressString(str): 
    #Create a hash table to store the chars from str 
    hash = [[] for i in range(10)] #dict size 10 
    for char in str:
        index = hashFunction(ord(char)) #Determine at which index the char will be stored using the ascii code 
        if hash[index] is not None: 
            for key,count in hash[index]: 
                if key == char: 
                    #remove the current tuple 
                    hash[index].remove((key,count))
                    #append a new tuple with the value updated 
                    hash[index].append((key,count+1))
                else: 
                    hash[index].append((char,1))
        else: 
            hash[index].append((char,1)) #
    return hash


hash = compressString("aabcccccaaa")
printHashTable(hash)
