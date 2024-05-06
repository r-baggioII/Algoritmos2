from binarytree import BinaryTree, BinaryTreeNode, update
from ejercicio2 import calculateBalance
from ejercicio3 import performRebalancing 

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
def print_tree(B):
  _print_tree(B.root, 0)


def _print_tree(node, level):
  if node is not None:
    _print_tree(node.rightnode, level + 1)
    print('  ' * level + str(node.key))
    _print_tree(node.leftnode, level + 1)



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

  reBalanceNodeToRoot(Tree,node) 

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


