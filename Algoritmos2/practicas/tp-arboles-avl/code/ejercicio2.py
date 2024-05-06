


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
