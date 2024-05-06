from AVLTree import AVLTree, insert, printTree

'''
Si n es la cantidad de nodos en un árbol AVL, implemente la operación height() en el módulo
avltree.py que determine su altura en O(log n). Justifique el por qué de dicho orden.
'''
'''
La complejidad del algoritmo propuesto es log n, puesto que no recorremos todo el árbol, sino que por cada nodo chqueamos su bf
y así decidimos si hay que ir a la derecha o a la izquierda.
'''

def height(Tree):
    return heightR(Tree.root,0)


def heightR(node,h): 
    if node is None: #Base case 
        return h - 1 
    
    if node.bf > 0: #Traverse left subtree only
        leftHeight = heightR(node.leftnode,h+1)
        return leftHeight 
    elif node.bf < 0: 
        #Traverse rightsubtree only
        rightHeight = heightR(node.rightnode,h+1) 
        return rightHeight
    else:
        #We can traverse right or left subtree 
        leftHeight = heightR(node.leftnode,h+1) 
        return leftHeight 


'''
Otra implementación con una pequeña modificación

def height(Tree):
    return heightR(Tree.root)


def heightR(node): 
    if node is None: #Base case 
        return -1
    
    if node.bf > 0: #Traverse left subtree only
        leftHeight = heightR(node.leftnode)
        return leftHeight + 1 
    elif node.bf < 0: 
        #Traverse rightsubtree only
        rightHeight = heightR(node.rightnode) 
        return rightHeight + 1 
    else:
        #We can traverse right or left subtree 
        leftHeight = heightR(node.leftnode) 
        return heightR(node.leftnode) + 1 

'''



test = AVLTree()
insert(test,12,12)
insert(test,10,10)
insert(test,14,14)
insert(test,8,8)
insert(test,11,11)

printTree(test)

print("height -->>")
print(height(test))
