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
