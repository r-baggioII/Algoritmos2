from binarytree import BinaryTree, BinaryTreeNode
from linkedlist import LinkedList,addAtTheEnd

class AVLTree:
  root = None


class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None


#Print the elements of a binary tree
def printTree(Tree):
  printTreeR(Tree.root, 0)


def printTreeR(node, level):
  if node is not None:
    printTreeR(node.rightnode, level + 1)
    print('  ' * level + str(node.key))
    printTreeR(node.leftnode, level + 1)

def printBf(Tree): 
 printBfR(Tree.root, 0)

def printBfR(node, level): 
   if node is not None:
    printBfR(node.rightnode, level + 1)
    print('  ' * level + str(node.bf))
    printBfR(node.leftnode, level + 1)


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
        

def access(Tree,key): 
    if Tree.root is None: 
        return None 
    node = access_R(Tree.root, key) 
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



#Ejercicio 1 ---------------------------------------------------------------------------
def rotateRight(Tree, node):
  #El hijo izquierdo de la antigua raiz pasa a ser la nueva raiz
  newRoot = node.leftnode
  #Si la nueva raiz tiene un hijo derecho, este
  #pasa a ser el hijo izquierdo de la antigua raíz
  node.leftnode = newRoot.rightnode

  #Actualizar el parent del hijo derecho de la nueva raiz
  if newRoot.rightnode is not None:
    newRoot.rightnode.parent = node

  #Actualizar el parent de la nueva raiz
  newRoot.parent = node.parent

  #Si parent es None, designamos
  #a ese nodo como la raíz del árbol
  if node.parent is None:
    Tree.root = newRoot
  else:
    if node.parent.rightnode == node:  #Es un hijo derecho
      node.parent.rightnode = newRoot
    else:
      node.parent.leftnode = newRoot  #Es un hijo izquierdo

  #La antigua raiz pasa a ser el hijo derecho de la nueva raíz
  newRoot.rightnode = node

  #Actualizamos el nuevo parent del nodo
  node.parent = newRoot

  return newRoot


def rotateLeft(Tree, node):
  #El hijo derecho del nodo pasa a ser la nueva raíz
  newRoot = node.rightnode
  #Si la nueva raíz tiene un hijo izquierdo pasa a ser el hijo derecho de la antigua raíz
  node.rightnode = newRoot.leftnode

  #Actulizar el parent del hijo izquierdo de la antigua raiz
  if newRoot.leftnode is not None:
    newRoot.leftnode.parent = node

  #Actualizar el parent de la nueva raíz
  newRoot.parent = node.parent

  #Si el parent es None, designamos al nodo como la raíz del árbol
  if node.parent is None:
    Tree.root = newRoot
  else:
    if node.parent.leftnode == node:  #Es un hijo izquierdo
      node.parent.leftnode = newRoot
    else:
      node.parent.rightnode = newRoot  #Es un hijo derecho

  #La antigua raiz es ahora el hijo izquierdo de la nueva raíz
  newRoot.leftnode = node
  #Actulizar el parent
  node.parent = newRoot

  return newRoot


#Ejercicio 2 ---------------------------------------------------------------------------
#Calculates balance factor for an AVL 
def calculateBalance(Tree):
  if Tree.root is None:
    return

  calculateBalance_R(Tree.root)

  return Tree


def calculateBalance_R(node):
  if node is None:
    return

  #Calculates difference between left subtree and right subtree 
  node.bf = getHeight_R(node.leftnode) - getHeight_R(node.rightnode)

  #Repeat recursivly for each node
  calculateBalance_R(node.leftnode)
  calculateBalance_R(node.rightnode)


def getHeight_R(node):
  if node is None:
    return 0
  return max(getHeight_R(node.leftnode), getHeight_R(node.rightnode)) + 1


#Ejercicio 3 ---------------------------------------------------------------------------
#Calculates balance factor for each node (calculateBalance())
def reBalance(Tree):
  if Tree is None:
    return

  calculateBalance(Tree)  
  reBalance_R(Tree,Tree.root)  

#Recursive function for reBalance 
def reBalance_R(Tree,node): 
  if node is None: 
    return
  performRebalancing(Tree,node) 
  calculateBalance(Tree)  
  
  reBalance_R(Tree,node.leftnode)
  reBalance_R(Tree,node.rightnode)

#Performs necessary rotations to keep the tree balanced 
def performRebalancing(Tree, node):
  if node is None:
    return
  if node.bf == -2:
    if node.rightnode.bf > 0:
      rotateRight(Tree, node.rightnode)
      rotateLeft(Tree, node)
    else:
      rotateLeft(Tree, node)
  elif node.bf == 2:
    if node.leftnode.bf < 0:
      rotateLeft(Tree, node.leftnode)
      rotateRight(Tree, node)
    else:
      rotateRight(Tree, node)
  return 


#Ejercicio 4 ---------------------------------------------------------------------------
#Función recursiva para insert 
def insert_R(newNode, currentNode):
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

def insert(Tree, element, key):
  newNode = AVLNode()
  newNode.value = element
  newNode.key = key

  if Tree.root is None:
    Tree.root = newNode
    return Tree.root.key

  node = insert_R(newNode, Tree.root)

  reBalanceNodeToRootR(Tree,node)

  if node is not None:
    return node.key


def reBalanceNodeToRoot(Tree,node): 
  calculateBalance(Tree)
  reBalanceNodeToRootR(Tree,node)  

def reBalanceNodeToRootR(Tree,node): 
  
  if node is None: 
    return
   
  performRebalancing(Tree,node)
  calculateBalance(Tree)
  reBalanceNodeToRootR(Tree,node.parent) 

#Ejercicio 5 ---------------------------------------------------------------------------
def lesser_of(node): 
    while node.leftnode is not None: 
        node = node.leftnode 
    return node 

def delete(Tree,element): 
  if search(Tree,element) is None: 
      return None 
  
  node = search_R(Tree.root,element)
  key = deleteNode(node)

  if key is not None: 
    reBalance(Tree)
  return key 

   
def deleteNode(node): 
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
    















