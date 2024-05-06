#Ejercicio 4 
def sortList(L):

    L.sort()
    print()
    L[2], L[len(L) // 2] = L[len(L) // 2], L[2]
    L[0], L[len(L) - 1] = L[len(L) - 1], L[0]

    return L


L = [1, 3, 5, 2, 4, 6, 9, 8, 7, 10,11]

#Ejercicio 5 
def contieneSuma(A,n): 
    i = 0
    j = len(A) - 1 
    while i != j: 
        suma = A[i] + A[j]
        if suma == n: 
            return True    

        if suma < n: 
            i += 1 
        else: 
            j -= 1 
    
    return False 

L = [1, 3, 5, 2, 4, 6, 9, 8, 7, 10,11]
print(contieneSuma(L))

