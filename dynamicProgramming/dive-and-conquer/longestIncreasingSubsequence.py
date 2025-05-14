'''
def subsecuenciaCreciente(numeros): 
Descripción: Implementa la función SubsecuenciaCreciente 
Entrada: numeros array de números naturales.
Salida: retorna array de números con la mayor subsecuencia creciente en el array de entrada números.
'''

'''
1) Divido el array a la mitad, y para cada mitad calculo recursivamente la mayor subsecuencia creciente
left = subsecuenciaCreciente(numeros)
right = subsecuenciaCreciente(numeros) 
2) nuestro caso base es cuando llegamos a una lista de longitud = 1, aquí devolvemos la lista compuesta por un único elemento como
la mayor subsecuencia creciente
3) luego de calcular left y right, las combinamos 
    3.1) Para combinar ambas listas debemos comparar el último elemento de la lista left con el primero de la lista right 
        si ultimoElemento > primerElemento entonces descartamos ese ultimo elemento y concatenamos ambas listas 
        sino, simplemente concatenamos las dos listas 
'''

def combine(left, right): 
    if left[-1] >= right[0]:  # Enforce strictly increasing
        return []
    else: 
        return left + right 

def subsecuenciaCreciente(array):
    if len(array) == 1: 
        return array 
    
    mid = len(array) // 2 
    leftLongest = subsecuenciaCreciente(array[:mid]) 
    rightLongest = subsecuenciaCreciente(array[mid:])
    
    combined = combine(leftLongest, rightLongest)

    # Return the longest of the three
    if len(combined) >= len(leftLongest) and len(combined) >= len(rightLongest):
        return combined
    elif len(leftLongest) >= len(rightLongest):
        return leftLongest
    else:
        return rightLongest



#print(subsecuenciaCreciente([5,1,2,3,100,20,17,8,19,21])) 
#rint(subsecuenciaCreciente([5, 4, 3, 2, 1]))
#print(subsecuenciaCreciente([1, 3, 5, 4, 6, 7, 8, 2, 3]))
print(subsecuenciaCreciente([10, 9, 8, 1, 2, 3, 4]))
# Expected: [1, 2, 3, 4]
print(subsecuenciaCreciente([100, 1, 2, 3, 4, 2, 1]))
# Expected: [1, 2, 3, 4]
print(subsecuenciaCreciente([7, 7, 7, 7, 8, 9, 1]))
# Expected: [7, 8, 9]
