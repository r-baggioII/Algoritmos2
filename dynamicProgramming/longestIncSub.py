def mayorSubsecuenciaCreciente(numeros):
    n = len(numeros)
    LIS = [1] * n # Inicializamos la lista LIS con 1 para cada elemento
    for i in range(n-1,-1,-1): #comenzamos desde el penúltimo índice ya que LIS[j] = 1 siempre 
        for j in range(i+1,n): #chequeamos el resto de secuencias crecientes después del indice i 

            if numeros[i] < numeros[i+1]: #verificamos la secuencia sea creciente 
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS) if numeros else 0 #caso lista vacía 
            

# Casos de prueba
if __name__ == "__main__":
    print(mayorSubsecuenciaCreciente([10, 9, 2, 5, 3, 7, 101, 18]))  # Esperado: 4 ([2,3,7,101])
    print(mayorSubsecuenciaCreciente([0, 1, 0, 3, 2, 3]))            # Esperado: 4 ([0,1,2,3])
    print(mayorSubsecuenciaCreciente([7, 7, 7, 7, 7, 7, 7]))         # Esperado: 1 ([7])
    print(mayorSubsecuenciaCreciente([]))                            # Esperado: 0 (lista vacía)
    print(mayorSubsecuenciaCreciente([1, 3, 2, 4, 3, 5]))            # Esperado: 4 ([1,2,3,5])

