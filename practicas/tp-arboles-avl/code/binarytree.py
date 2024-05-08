from linkedlist import LinkedList,Node,addAtTheEnd,printList

class BinaryTree:
    root=None
class BinaryTreeNode:
    key=None
    value=None
    leftnode=None
    rightnode=None
    parent=None


#Print the elements of a binary tree 
def print_tree(B):
  _print_tree(B.root, 0)

def _print_tree(node, level):
  if node is not None:
      _print_tree(node.rightnode, level + 1)
      print('  ' * level + str(node.key))
      _print_tree(node.leftnode, level + 1)



def search_R(currentNode,element): 
    
    if currentNode is None: 
        return 
    
    if currentNode.value == element: 
        return currentNode
    
    leftNode = search_R(currentNode.leftnode, element) 
    if leftNode is not None: 
        return leftNode 
    
    rightNode = search_R(currentNode.rightnode, element)
    if rightNode is not None: 
        return rightNode 


def search(B,element): 
    node = search_R(B.root,element)
    if node is not None: 
        return node.key 
    

def insert_R(newNode,currentNode): 
    if newNode.key > currentNode.key: 
        if currentNode.rightnode is None: 
            currentNode.rightnode = newNode 
            newNode.parent = currentNode 
            return newNode
        else: 
            right = insert_R(newNode, currentNode.rightnode)
            if right is not None: 
                return right 
    else: 
        if currentNode.leftnode is None: 
            currentNode.leftnode = newNode 
            newNode.parent = currentNode 
            return newNode 
        else: 
            left = insert_R(newNode, currentNode.leftnode) 
            if left is not None: 
                return left 
    

def insert(B,element,key): 
    
    newNode = BinaryTreeNode() 
    newNode.value = element
    newNode.key = key 
    
    if B.root is None: 
        B.root = newNode 
        return B.root.key 
    
    node = insert_R(newNode, B.root) 
    
    if node is not None: 
        return node.key 
    

def access_R(currentNode, key): 
    if currentNode is None: 
        return 
    if currentNode.key == key: 
        return currentNode 
    if key > currentNode.key: 
        right = access_R(currentNode.rightnode,key) 
        if right is not None: 
            return right 
    else: 
        left = access_R(currentNode.leftnode,key)
        if left is not None: 
            return left 
        

def access(B,key): 
    if B.root is None: 
        return None 
    node = access_R(B.root, key) 
    if node is not None: 
        return node.value 



def searchKey_R(currentNode,key):
    if currentNode is None: 
        return 
    if currentNode.key == key: 
        return currentNode
    if key > currentNode.key: 
        right = searchKey_R(currentNode.rightnode,key)
        if right is not None: 
            return right 
    else: 
        left = searchKey_R(currentNode.leftnode,key) 
        if left is not None: 
            return left 
    

def update(B,element,key): 
    
    node = searchKey_R(B.root,key)
    
    if node is not None: 
        node.value = element
        return key 
    return None 



def lesser_of(node): 
    while node.leftnode is not None: 
        node = node.leftnode 
    return node 



def delete(B,element): 
    
    if search(B,element) is None: 
        return None 
    
    node = search_R(B.root,element)
    key = node.key  

    #Case 1: the node is a leaf 
    if node.rightnode is None and node.leftnode is None: 
        #The node is the right child 
        if node.parent.rightnode == node: 
            node.parent.rightnode = None
            return key 
        #The node is the left child 
        if node.parent.leftnode == node: 
            node.parent.leftnode = None
            return key 
    
    #Case 2: the node has only one child 
    #The node has a right child 
    if node.rightnode is not None and node.leftnode is None: 
        if node.parent.rightnode == node: 
            node.parent.rightnode = node.parent.rightnode.rightnode
        else: 
            node.parent.leftnode = node.parent.leftnode.rightnode
        return key 
    
    
    #The node has a left child 
    if node.leftnode is not None and node.rightnode is None: 
        if node.parent.rightnode == node: 
            node.parent.rightnode = node.parent.rightnode.leftnode
        else: 
            node.parent.leftnode = node.parent.leftnode.leftnode
        return key 


    #Case 3: The node has two children 
    if node.rightnode is not None and node.leftnode is not None: 
        #Look for the lesser of its ancestors
        nodeToChange = lesser_of(node.rightnode) 
        #Rep node
        node.key = nodeToChange.key 
        node.value = nodeToChange.value 
        #Delete nodeToChange from the BST 
        if nodeToChange.parent.rightnode == nodeToChange: 
            nodeToChange.parent.rightnode = nodeToChange.parent.rightnode.rightnode
        else: 
            nodeToChange.parent.leftnode = nodeToChange.parent.leftnode.leftnode
        return key 

def deleteKey(B,key): 
    if searchKey_R(B.root,key) is None: 
        return None 
    node = searchKey_R(B.root,key) 
    
    #Case 1: the node is a leaf 
    if node.rightnode is None and node.leftnode is None: 
        #The node is the right child 
        if node.parent.rightnode == node: 
            node.parent.rightnode = None
            return key 
        #The node is the left child 
        if node.parent.leftnode == node: 
            node.parent.leftnode = None
            return key 
    
    #Case 2: the node has only one child 
    #The node has a right child 
    if node.rightnode is not None and node.leftnode is None: 
        if node.parent.rightnode == node: 
            node.parent.rightnode = node.parent.rightnode.rightnode
        else: 
            node.parent.leftnode = node.parent.leftnode.rightnode
        return key 
    
    
    #The node has a left child 
    if node.leftnode is not None and node.rightnode is None: 
        if node.parent.rightnode == node: 
            node.parent.rightnode = node.parent.rightnode.leftnode
        else: 
            node.parent.leftnode = node.parent.leftnode.leftnode
        return key 


    #Case 3: The node has two children 
    if node.rightnode is not None and node.leftnode is not None: 
        #Look for the lesser of its ancestors
        nodeToChange = lesser_of(node.rightnode) 
        #Rep node
        node.key = nodeToChange.key 
        node.value = nodeToChange.value 
        #Delete nodeToChange from the BST 
        if nodeToChange.parent.rightnode == nodeToChange: 
            nodeToChange.parent.rightnode = nodeToChange.parent.rightnode.rightnode
        else: 
            nodeToChange.parent.leftnode = nodeToChange.parent.leftnode.leftnode
        return key 


def traverseInPreOrder(B): 
    L = LinkedList() 
    traverseInPreOrder_R(B.root,L) 
    return L 

def traverseInPreOrder_R(root,L): 
    if root is None: 
        return 
    addAtTheEnd(L,root.key)
    traverseInPreOrder_R(root.leftnode,L)
    traverseInPreOrder_R(root.rightnode,L)


def traverseInOrder(B): 
    L = LinkedList() 
    traverseInOrder_R(B.root,L)
    return L 


def traverseInOrder_R(root,L): 
    if root is None: 
        return 
    traverseInOrder_R(root.leftnode, L)
    addAtTheEnd(L,root.key)
    traverseInOrder_R(root.rightnode,L)

def traverseInPostOrder(B): 
    L = LinkedList() 
    traverseInPostOrder_R(B.root,L)
    return L 

def traverseInPostOrder_R(root,L): 
    if root is None: 
        return 
    traverseInPostOrder_R(root.leftnode,L)
    traverseInPostOrder_R(root.rightnode,L)
    addAtTheEnd(L,root.key)

