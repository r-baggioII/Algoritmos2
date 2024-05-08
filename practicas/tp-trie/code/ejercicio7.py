from trie import Trie, TrieNode,insert,search,delete,printTrie
from ejercicio4 import findPrefixRecursive

'''
Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol
Trie T y la cadena devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada
autoCompletar(T, "groen") devolvería “land”, ya que podemos tener “groenlandia” o
“groenlandés” (en este ejemplo la palabra groenlandia y groenlandés pertenecen al documento que
representa el Trie). Si hay varias formas o ninguna, devolvería la cadena vacía. Por ejemplo,
autoCompletar(T, "ma") devolvería “” (cadena vacia) si T presenta las cadenas “madera” y “mama”
'''

#1)Determinar si existe en prefijo en el Trie 
#2)Si no existe devolvemos "cadena vacía"

#3)Si existe y en el siguiente caracter hay una bifucarción, devolvemos "cadena vacía". 
#Pues esto significa que hay más de una forma de completar la palabra
#Si existe y luego del último caracter no hay una bifurcación devolvemos todos los caracteres siguientes hasta encontrar una bifurcación 


def autoCompletar(Trie,cadena): 
    if Trie.root is None: #El trie está vacío
        return "cadena vacía"
    
    current = findPrefixRecursive(Trie.root,cadena,cadena,foundChars ="") #Buscar la cadena (prefijo) en el trie 
    if current is None: #El prefijo no existe 
        return "cadena vacía"
    
    if len(current.children) > 1: #Hay una bifurcación (más de una forma de autocmpletarlo)
        return "cadena vacía"

    return autoCompletarRecursive(current,foundChars = "")

def autoCompletarRecursive(current,foundChars): 
    
    if current is None: 
        return 
    
    if len(current.children) > 1 or current.isEndOfWord: 
        return foundChars
    
    if current.children: 
        for child in current.children: 
            newChars = foundChars + child.key
            result = autoCompletarRecursive(child,newChars)
            if result: 
                return result       
    return foundChars


T = Trie() 
insert(T,"groenlandia")
insert(T,"groenlandes")
insert(T,"mamá")
insert(T,"madera")
print(autoCompletar(T,"groen"))

