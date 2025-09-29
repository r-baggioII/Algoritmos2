def maxProfit(prices):
    profit = 0
    next_accion = "comprar"  # para saber si compro o vendo
    for i in range(len(prices) - 1):
        if next_accion == "comprar":
            if prices[i] < prices[i + 1]:
                #comprar la acción, es más barata 
                precio_compra = prices[i] 
                next_accion = "vender" 
        else: 
            if prices[i] > prices[i+1]: #El precio actual es mayor, conviene vender 
                precio_venta = prices[i] 
                profit = profit + (precio_venta - precio_compra) 
                next_accion = "comprar" #La siguiente accion posible es comprar
    if next_accion == "vender": #llego al final pero nunca encuentro un precio ideal
        profit += prices[-1] - precio_compra #vender al ultimo precio

    return max(profit, 0) 

print(maxProfit([3,3,3]))