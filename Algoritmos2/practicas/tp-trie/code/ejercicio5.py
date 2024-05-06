from trie import Trie, TrieNode,insert,search,delete,printTrie

'''
Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo
documento y False en caso contrario.
Determinar si todas las palabras de T1 están en T2
'''
#check all words from T1 are in T2 
def equalTries(T1,T2): 
    #Traverse T1 complete. For each word on T1 check it also exists on T2
    
    if T1.root is None or T2.root is None: #Consider false the case in which one or both of the tries are empty  
        return False 

    return equalTriesRecursive(T1.root,T2,word="") 

def equalTriesRecursive(currentT1,T2,word=""): 
    
    if currentT1 is None: 
        return True 
    
    if currentT1.isEndOfWord: 
        #For every word found search that word on T2 
        if not search(T2,word): 
            return False  
     
    
    if currentT1.children is not None: 
        for child in currentT1.children:
            newWord = word + child.key 
            #Repeat recursivly 
            if not equalTriesRecursive(child,T2,newWord): return False 
    return True 

'''
T1 = Trie() 
T2 = Trie() 

insert(T1,"ROCIO")
insert(T1,"CASA")
insert(T1,"TAYLOR")
insert(T1,"FEARLESS")
insert(T1,"PHONE")
print("Trie 1 -->")
printTrie(T1.root) 
print("--------------------")
insert(T2,"CASA")
insert(T2,"FEARLESS")
insert(T2,"ROCIO")
insert(T2,"TAYLOR")
print("Trie 2 -->")
printTrie(T2.root) 

print(equalTries(T1,T2))
'''


