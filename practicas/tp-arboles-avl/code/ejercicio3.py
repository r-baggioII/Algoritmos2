
from ejercicio1 import rotateLeft, rotateRight
from ejercicio2 import calculateBalance


#Ejercicio 3 ---------------------------------------------------------------------------
#Calculates balance factor for each node (calculateBalance())
def reBalance(Tree):
  if Tree is None:
    return

  calculateBalance(Tree)  
  reBalance_R(Tree,Tree.root)  

#Recursive function for reBalance 
def reBalance_R(Tree,node): 
  performRebalancing(Tree,node) 
  
  reBalance_R(Tree,node.leftnode)
  reBalance_R(Tree,node.rightnode)

#Performs necessary rotations to keep the tree balanced 
def performRebalancing(Tree, node):
  if node is None:
    return
  if node.bf == -2:
    if node.rightnode.bf == 2:
      rotateRight(Tree, node.rightnode)
      rotateLeft(Tree, node)
    else:
      rotateLeft(Tree, node)
  elif node.bf == 2:
    if node.leftnode.bf == -2:
      rotateLeft(Tree, node.leftnode)
      rotateRight(Tree, node)
    else:
      rotateRight(Tree, node)
  return 
