from trie import Trie, TrieNode,insert,search,delete,printTrie

'''
Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas
invertidas. Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos
caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y
asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un
carácter.
'''

#Traverse the whole Trie "T"
#For each word found search for its reversed in Trie 

def reversedString(T): 
    if T.root is None: 
        return False 
    
    return reversedStringRecursive(T,T.root,wordArray= [])

def reversedStringRecursive(T,current,wordArray): 
    
    if current is None: 
        return False 
    
    if current.isEndOfWord: 
        word = ''.join(wordArray) 
        if not search(T,word): 
            return False 
        return True 
    
    if current.children is not None: 
        for child in current.children: 
            newWordArray = wordArray[:]  
            newWordArray.insert(0, child.key)
            if reversedStringRecursive(T,child,newWordArray): 
                return True # If any child returns True, return True
    return False 


'''
T = Trie()
insert(T,"ROLYAT")
insert(T,"ROCIO")
insert(T,"CASA")
insert(T,"TAYLOR")
insert(T,"FEARLESS")
print("Trie 1 -->")
printTrie(T.root) 
print("--------------------")
print(reversedString(T)) 
'''

