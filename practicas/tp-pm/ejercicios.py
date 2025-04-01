''' 
Ejercicio 1 (opcional) 
Implementar la función que responde a la siguiente especificación. 
def existChar(String, c): 
 Descripción: Confirma la existencia de un carácter específico en una 
cadena. 
Entrada: String en la cual se busca el carácter c.
Salida: True si el carácter c se encuentra en la cadena String, False en otro caso 
'''

def existChar(string, c): #Complejidad O(n): En el peor caso hay que recorrer toda la string y el caracter está al final
    for i in range(len(string)): 
        if string[i] == c: 
            return True 
    return False 

#print(existChar("abcde",'a')) 
#print(existChar("abcde",'g'))
#print(existChar("abcde",'c'))

'''
Ejercicio 2 (opcional) 
Implementar una función que detecte si una cadena es un Palíndromo. La implementación debe 
responder a la siguiente especificación: 
def isPalindrome(String): 
  Descripción: n que detecte si una cadena es un Palíndromo. 
  Entrada: String con la cadena a evaluar 
  Salida: Devuelve true si el palindromo o no 
'''

def esPalindromo(string): 
    k = len(string) 
    coincidencias = 0 
    for i in range(k): #O(n)
        if string[i] == string[k-i-1]: 
            coincidencias +=1
    if coincidencias == k: 
        return True 
    return False 

#print(esPalindromo("abababa")) 
#print(esPalindromo("abbbbasdal"))
#print(esPalindromo("a"))
#print(esPalindromo("aba")) 

''' 
Ejercicio 3 (opcional) 
Implementar la función que responde a la siguiente especificación. 
def mostRepeatedChar(String): 
  Descripción: Encuentra el carácter que más se repite en una cadena
  Entrada: String con la cadena a evaluar 
  Salida: Retorna el carácter que más se repite. En caso que haya más de un carácter con mayor ocurrencia devuelve el primero de ellos.
'''

def mostRepeated(string): 
    charsOcurrences = {} 
    for i in range(len(string)): #O(n)
        if string[i] in charsOcurrences: 
            charsOcurrences[string[i]] += 1 
        else: 
            charsOcurrences[string[i]] = 1
    mostRepeated = max(charsOcurrences, key=charsOcurrences.get) #O(n)
    return mostRepeated #Complejidad total : O(2n)


#print(mostRepeated("aabbcdabb")) devuelve b 


''' 
Implementar la función que dado un String S devuelve la longitud de la isla de mayor tamaño. Una isla es una secuencia consecutiva de un mismo carácter dentro de S. Por ejemplo S = “cdaaaaaasssbbb” su mayor isla es de tamaño 6 (aaaaaa) y además tiene dos islas de tamaño 3 (sss, bbb) el resto de las islas en s  son de tamaño 1.
def getBiggestIslandLen(String):
	Descripción: Determina el tamaño de la isla de mayor tamaño en una cadena.
Entrada: String con la cadena a ser evaluada.
Salida: Retorna un entero con la dimensión de la isla más grande dentro de la cadena
'''
def getBiggestIslandLen(string):
    currentIsland = 0 
    maxIsland = 0 
    currentChar = string[0]
    for i in range(len(string)): #O(n)
        if string[i] == currentChar: 
            currentIsland +=1 #aumentamos el contador de la isla con el caracter actual
        else: 
            if currentIsland > maxIsland: #si encontramos otro caracter, actualizamos el máximo hasta ahora 
                maxIsland = currentIsland
            currentIsland = 1 #currentIsland ahora es 1, puesto que ya visitamos el primer nuevo caracter 
            currentChar = string[i] #actualizamos el nuevo caracter encontrado 
    return maxIsland

#print(getBiggestIslandLen("cdaaaaaasssbbb")) #devuelve 6
#print(getBiggestIslandLen("bbbbbjjjjjjjjjjjjlll")) #devuelve 12

''' 
Implementar la función que responde a la siguiente especificación.

def isAnagram(String, String):
	Descripción: Determina si una cadena es un anagrama de otra.
Entrada: Un String con la cadena original, y otro String con el posible anagrama a evaluar.
Salida: Retorna un True si la segunda cadena es anagrama de la primera, en caso contrario devuelve False.

Nota: Una cadena s es anagrama de otra cadena p si existe alguna ordenación de los elementos de s con lo cual se obtenga la cadena p

'''

#Es un anagrama si encontramos todos los elementos s en p 

def isAnagrama(string1,string2): 
    #Convertirmos a un conjunto la string1
    set1= set(string1) #O(n)
    set2 = set(string2) #O(n)
    if set1 == set2: #(n)
        return True 
    return False
#O(3n)


''' 
def verifyBalancedParentheses(String):
	Descripción: Verifica si los paréntesis contenidos en una cadena se encuentran balanceados y en orden.
Entrada: Un String con la cadena a ser evaluada.
Salida: Retorna un True si la cadena posee sus paréntesis correctamente balanceados, en caso contrario devuelve False.
Ejemplo: “(ccc(ccc)cc((ccc(c))))” es correcto, pero “)ccc(ccc)cc((ccc(c)))(“ no lo es, aunque tenga el mismo número de paréntesis abiertos que cerrados.
'''

def verifyBalancedParentheses(String): #O(n)
    stack = []
    for char in String:
        if char == '(':
            stack.append(char)
        if char == ')': 
            if len(stack) == 0: 
                return False 
            stack.pop()
    if len(stack) == 0: 
        return True 
    return False 

#print(verifyBalancedParentheses("(())()"))

'''
Se tiene una cadena de caracteres y se quiere reducir a su longitud haciendo una serie de operaciones. En cada operación se selecciona un par de caracteres adyacentes que coinciden, y se los borra. Por ejemplo, la cadena “aab” puede ser acortada a “b” en una sola operación. Implementar una función que borre tantos caracteres como sea posible y devuelva la cadena resultante.

def reduceLen(String):
	Descripción: Reduce la longitud de una cadena removiendo iterativamente pares de caracteres repetidos.
Entrada: Un String con la cadena a ser reducida.
Salida: Retorna un String con la cadena resultante tras haber aplicado las remociones. 

Ejemplo: “aaabccddd” se puede reducir a “abd”  de la siguiente manera: 
“aaabccddd” → “abccddd” → “abddd” → “abd”

'''
def reduceLen(String):
    stack = []
    for char in String: 
        if stack and stack[-1] == char: 
            stack.pop()
        else: 
            stack.append(char)

    return "".join(stack) if stack else "Empty String"
    
        
print(reduceLen("aaabccddd"))
            
'''
Implementar una función que dadas dos palabras determine si la segunda está contenida dentro de la primera 
bajo la siguiente premisa. Una cadena s contiene la palabra “amarillo” si un subconjunto ordenado de sus caracteres 
deletrea la palabra amarillo. Por ejemplo, la cadena s = "aaafffmmmarillzzzllhooo" contiene amarillo, 
pero s = "aaafffmmmarrrilzzzhooo" no (debido a que le falta una l). Si ordenamos la primera cadena como 
s = "aaaaillllfffzzzhrmmmooo", ya no contiene la subsecuencia debido al ordenamiento.

def isContained(String,String):
	Descripción: Determina si los caracteres de una cadena se encuentran contenidos y en el mismo orden dentro de otra cadena.
Entrada: Un String con la cadena a evaluar, y otro String con la cadena posiblemente contenida en la primera.
Salida: Retorna un True si la segunda cadena se encuentra contenida en la primera, o False en caso contrario.
'''
def isContained(string1,string2):
    i = 0
    k = 0
    wantedChar = string2[k] 
    while i < len(string1):
        if string1[i] == wantedChar: 
            k+=1
            if k == len(string2): 
                return True 
            wantedChar = string2[k] 
        i +=1 
    return False 

#print(isContained("gggghskdfotttela","hola"))










def suffixFuncion(p,k):

    max = 0 
    m = len(p)
    for i in range(len(k)+1):
        print(k[0:i]) 

#suffixFuncion("abc", "abcde")

