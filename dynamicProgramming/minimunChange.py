'''
def darCambio(Cambio, Monedas)
Descripción: Implementa la operación devolver cambio
Entrada: Cambio número que representa el monto del cambio, Monedas, un Array con las monedas que se dispone para dar ese cambio.
Salida: retorna el número mínimo de monedas que son utilizadas para devolver el cambio.

Nota: Asuma que en la lista de monedas siempre está la moneda con valor 1. Y que las monedas no se agotan.
Ejemplos: 
monedas = [1, 2, 6, 8, 10],  cambio = 14,  solución: 2 (una moneda con denominación 6 y otra con 8) 
monedas = [1, 3, 11, 7, 12],  cambio = 20,  solución: 3 (utilizando la combinación de monedas 12,7,1)

'''

def coinChanges(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    table = [
        [col if row == 0 else None for col in range(amount + 1)]
        for row in range(len(coins))
    ]
    
    for row in range(1,len(coins)):
        #print("???")
        for column in range(amount+1): 
            if column < coins[row]: 
                table[row][column] = column
            else: 
                previousAmount = table[row-1][column]
                aux = column - coins[row]
                calculatedAmount = 1 + table[row][aux]

                if previousAmount > calculatedAmount:
                    table[row][column] = calculatedAmount
                else: 
                    table[row][column] = previousAmount
    lastRow = len(coins) -1
    lastColumn = amount
    return table[lastRow][lastColumn]



def coinChange(coins, amount):
    # Inicializamos la tabla: fila 0 es base, columnas de 0 a amount
    table = [
        [0 if column == 0 else float('inf') for column in range(amount + 1)]
        for row in range(len(coins) + 1)
    ]

    for row in range(1, len(coins) + 1):
        for column in range(amount + 1): 
            if column < coins[row - 1]:
                table[row][column] = table[row - 1][column] #si el valor de la moneda es demasiado grande para usarse nunca usamos esa monead (nos quedamos con el valor anterior)
            else:
                previousAmount = table[row - 1][column] #decidimos entre usar la moneda o no usarla
                aux = 1 + table[row][column - coins[row - 1]]
                table[row][column] = min(previousAmount, aux)

    lastRow = len(coins)
    lastColumn = amount
    result = table[lastRow][lastColumn]
    return result if result != float('inf') else -1, table




coins = [1,2,6,8,10] 
amount =14
#for row in table: 
    #print(row[6]) 

a,table = coinChange(coins,amount) 
for row in table: 
    print(row )
