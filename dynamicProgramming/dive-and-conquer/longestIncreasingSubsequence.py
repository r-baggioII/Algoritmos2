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
    # Opción 1: La subsecuencia está completamente en left
    best_left = left
    
    # Opción 2: La subsecuencia está completamente en right
    best_right = right
    
    # Opción 3: La subsecuencia cruza entre left y right
    # Encontrar la secuencia más larga que termina en el último elemento de left
    # y la secuencia más larga que comienza en el primer elemento de right
    cross = []
    
    # Si las listas no están vacías, podemos intentar combinarlas
    if left and right:
        # Verificar si podemos conectar la última parte de left con la primera parte de right
        if left[-1] < right[0]:
            cross = left + right
        else:
            # Buscamos el prefijo más largo de left que puede conectarse con right
            i = len(left) - 1
            while i >= 0 and left[i] >= right[0]:
                i -= 1
                
            # Si encontramos un prefijo válido, lo combinamos con right
            if i >= 0:
                cross = left[:i+1] + right
    
    # Devolver la mejor opción entre las tres
    candidates = [best_left, best_right, cross]
    return max(candidates, key=len)

def subsecuenciaCrecienteWrapper(array):
    # Caso base
    if len(array) <= 1:
        return array
        
    # Dividir
    mid = len(array) // 2
    left = subsecuenciaCrecienteWrapper(array[:mid])
    right = subsecuenciaCrecienteWrapper(array[mid:])
    
    # Combinar
    combined = combine(left, right)
    
    # Devolver la subsecuencia más larga
    return len(combined)





