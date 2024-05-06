class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


def insert(T, element):
    if T.root is None:
        newNode = TrieNode()
        newNode.key = None
        T.root = newNode
        T.root.parent = None
    insert_R(T.root, element)


def insert_R(current, element):

    if current is None:
        return
    if len(element) < 1:
        current.isEndOfWord = True
        return

    if current.children is None:
        current.children = []

    newChar = element[0]
    childNode = None

  # Check if a child node with the current character already exists
    for child in current.children:
        if child.key == newChar:
            childNode = child
            break

  # If no child node exists with the current character, create a new one
    if childNode is None:
        newNode = TrieNode()
        newNode.key = newChar
        newNode.parent = current
        current.children.append(newNode)
    else:
        newNode = childNode  #Assing childNode to newNode (for words containing other words)

    insert_R(newNode, element[1:])


def search(T, element):
    if T.root is None:
        return False

    foundChars = ""  #store the chars found in a string
    return search_R(T.root, element, element, foundChars)


def search_R(current, element, elementCopy, foundChars):

    if current is None:
        return False

    if len(element) < 1:
        if elementCopy != foundChars:
            return False
        return current.isEndOfWord

    newChar = element[0]

    if current.children is not None:

        #Traverse the list on children and determine if there exist a child with a key iqual to the char
        for child in current.children:
            if child.key == newChar:
                foundChars = foundChars + child.key
                return search_R(child, element[1:], elementCopy, foundChars)  #pass as a parameter the child whose key is equal to the char we're looking for
        return False


def delete(T, element):
    
    if T.root is None: 
        return False 

    foundChars = "" #Store the chars found 
    return delete_R(T.root, element,element,foundChars) 
    

def delete_R(current, element, copyElement,foundChars):

    if len(element) <= 1:
        if foundChars == copyElement:
            current.isEndOfWord = False
        while current.parent is not None and current.isEndOfWord == False: 
            if len(current.parent.children) == 1 : 
                current.parent.children.remove(current)
                current = current.parent
            else:
                current.parent.children.remove(current)
                current = current.parent
                break
        return True 

    nextNode = None 
    if current.children is not None:
        for child in current.children:
            if child is not None and child.key == element[0]:
                foundChars = foundChars + child.key
                nextNode = child
        if not nextNode: 
            return False 
        return delete_R(nextNode, element[1:],copyElement,foundChars)  #pass the child whose key matches our char
    return False 



def printTrie(node, level=0):
  
    if node is None:
        return

  # Print the current node's key (or "root" if it's the root node)
    if level == 0:  # Check if it's the root node
        print("root")
    else:
        print(" " * level + node.key +("*" if node.isEndOfWord else ""))  # Add '*' if it's the end of a word

  # Recursively print children with proper indentation
    if node.children:
        for child_node in node.children:
            printTrie(child_node,level + 4)  # Increase indentation level for children



def printKeyNodes(L):
    index = 0 
    for node in L:
        print(node.key, "at index", index) 
        index +=1 

'''
T = Trie()
insert(T, "Hola")
insert(T, "Diego")
insert(T, "Rocio")
insert(T,"Raton")
insert(T,"Holanda")
insert(T, "Rosca")
print("-------------------")
printTrie(T.root)
print("-------------------")
print(search(T,"Hola"))
printTrie(T.root)
'''





