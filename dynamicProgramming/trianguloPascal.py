
def crearMatriz(indexRow): 
    matriz= []
    for row in range(indexRow+1):
         matriz.append([1] + [0] * (indexRow))  # Primer fila: 1 y luego 0's
    return matriz


def trianguloPascal(indexRow):
    pascal = crearMatriz(indexRow) 
    for i in range(1,indexRow+1): 
        for j in range(1,indexRow+1): 
            if j <= i:
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1] 
            else: 
                pascal[i][j] = 0 
    return pascal[-1] #return the last row 

'''


'''
print(trianguloPascal(3))
print(trianguloPascal(4))
print(trianguloPascal(5))
print(trianguloPascal(6))