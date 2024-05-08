from dictionary import insert,delete,search,printHashTable,hashFunction
'''
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. 
Justificar el costo en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición

'''
#Time complexity -->> O(n²)
def uniqueElements(L): 
    #Create a hash table with the elements of L 
    hash = [[] for i in range(10)] #dict size 10

    for element in L: 
        index = hashFunction(element) #Determine at which index the element will be inserted 
        if (element,element) in hash[index]: #Search for the key-value pair before inserting 
            return False 
        else: 
            insert(hash,element,element) 
    return True 

L = [10,5,12,1,2]
print(uniqueElements(L))


