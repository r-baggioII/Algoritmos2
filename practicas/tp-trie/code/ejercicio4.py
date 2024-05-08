from trie import Trie, TrieNode, insert,search,delete,printTrie

'''
Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, escriba todas
las palabras del árbol que empiezan por p y sean de longitud n.
'''

def commonPrefixWords(T,p,n): 
    #Find the prefix "p" in the trie 
    if T.root is None: 
        return None 
    foundCharsPrefix = "" #chars found from the string "p"
    lastPrefixNode = findPrefixRecursive(T.root,p,p,foundCharsPrefix)
    
    if not lastPrefixNode: return None #If the prefix was not found return None 

    words = [] 
    foundWord = p #All words start with the same prefix 
    return findWordsWithPrefix(lastPrefixNode,words,n,foundWord,p) 



def findPrefixRecursive(current,p,copyP,foundChars): 
    if current is None: 
        return None 

    if len(p) == 0: 
        if copyP == foundChars: 
            return current #Return the last node of the prefix 
        return None 
    
    nextNode = None 
    if current.children is not None: 
        for child in current.children: 
            if child.key == p[0]: 
                nextNode =child #Node whose key matches a char from our prefix 
                foundChars += child.key #Add the matching char to the "foundCahrs" string
        if nextNode:
            return findPrefixRecursive(nextNode,p[1:],copyP,foundChars)
        return None
    return None 

def findWordsWithPrefix(current,words,n,foundWord,p): 
    if current is None: 
        return words 

    if current.isEndOfWord: 
        if len(foundWord) == n: 
            words.append(foundWord) #append the word to the array with its prefix 

    if current.children is not None: 
        for child in current.children: 
            findWordsWithPrefix(child,words,n,foundWord + child.key,p)
    return words 

      
    
'''
T = Trie() 
insert(T,"ROBOT")
insert(T,"ROCIO")
insert(T,"ROSCA")
insert(T,"AUTO")
insert(T,"CASA") 
printTrie(T.root)
print("--------------") 
wordsArray = commonPrefixWords(T,"RO",5) 
print(wordsArray)
'''
