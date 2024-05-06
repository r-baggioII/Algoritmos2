from dictionary import insert,delete,search,printHashTable,hashFunction

'''
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. 
Por ejemplo, la cadena 'aabcccccaaa' se convertiría en 'a2blc5a3'. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). 
Justificar el costo en tiempo de la solución propuesta.
'''
#Time complexity --> O(n), since you need to traverse the whole string 

def compressString(string):
    previousChar = string[0]
    currentChar = string[0]
    compressedStr = ""
    count = 0

    for i in range(len(string)):
        currentChar = string[i]
        if previousChar == currentChar:
            count += 1
        else:
            compressedStr += str(count) + previousChar
            count = 1  # reset count to 1 for the new different char
        previousChar = currentChar

    compressedStr += str(count) + currentChar  # Adding the count of the last character

    if len(string) <= len(compressedStr):
        return string
    return compressedStr

'''
test = "aabcccccaaa"
comp = compressString(test)
print(comp)
'''

