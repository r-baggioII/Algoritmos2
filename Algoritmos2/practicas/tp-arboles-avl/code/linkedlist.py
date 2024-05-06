
class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None
L = LinkedList()

#Adds elements at the end of a linkedlist 
def addAtTheEnd(L,element): 
  newNode = Node()
  newNode.value = element     
  if L.head is None: 
    L.head = newNode 
  else: 
    currentNode = L.head 
    while currentNode.nextNode is not None: 
      currentNode = currentNode.nextNode 
    currentNode.nextNode = newNode 

def printList(L): 
  currentNode = L.head 
  while currentNode is not None: 
    print(currentNode.value) 
    currentNode = currentNode.nextNode 


#Agrega un elemento al comienzo de L, siendo L una LinkedList que representa el TAD secuencia.
def add(L,element): 
  newNode = Node()
  newNode.value = element
  if L.head is None: 
    L.head = newNode 
  else: 
    newNode.nextNode = L.head 
    L.head = newNode 


#Busca un elemento de la lista que representa el TAD secuencia.
def search(L,element): 
  currentNode = L.head 
  position = 0  
  while currentNode is not None: 
    if currentNode.value == element: 
      return position 
    position +=1 
    currentNode = currentNode.nextNode 
  #Si el elemento no se encunetra devolvemos None 
  return None 

def length(L): 
  currentNode = L.head
  size = 0 
  while currentNode is not None: 
    size +=1 
    currentNode= currentNode.nextNode 
  return size 

#Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
def insertList(L,element,position): 
  newNode = Node()
  newNode.value = element
  #Si la posición es mayor al número de elementos devolvemos None 
  listLength = length(L)
  if position > listLength: 
    return None 
  #Si la lista está vacía 
  if L.head is None or position == 0: 
    newNode.nextNode = L.head
    L.head = newNode 
    return position 
  currentNode = L.head
  currentPos= 0 
    #Recorremos la lista hasta  encontrar el nodo donde debemos insertar 
  while currentNode is not None : 
      if currentPos == position- 1: 
        #Insertamos el nodo 
        newNode.nextNode = currentNode.nextNode 
        currentNode.nextNode = newNode 
      currentNode = currentNode.nextNode 
      currentPos += 1 
  return position 

#Elimina un elemento de la lista que representa el TAD secuencia.
def delete(L,element): 
  position = search(L,element) 
  #Devuelve None si el elemento no se encuentra 
  if position is None: 
    return None 
  currentNode = L.head 
  #El nodo a eliminar está al principio 
  if position == 0: 
    L.head = currentNode.nextNode 
    currentNode = None 
  currentPos = 0 
  while currentNode is not None: 
    if  currentPos == position - 1: 
      currentNode.nextNode = currentNode.nextNode.nextNode 

    currentNode = currentNode.nextNode 
    currentPos += 1 
  return position


#Permite acceder a un elemento de la lista en una posición determinada.
def access(L,position): 
  listLength = length(L)
  if position < 0 or position > listLength: 
    return None 
  currentNode = L.head 
  currentPos = 0 
  while currentNode is not None: 
    if position == currentPos: 
      return currentNode.value 
    currentNode = currentNode.nextNode 
    currentPos += 1 
  return None   

#Permite cambiar el valor de un elemento de la lista en una posición determinada
def update(L,element,position): 
  currentNode = L.head 
  currentPos = 0 
  while currentNode is not None and currentPos < position: 
    currentNode = currentNode.nextNode 
    currentPos += 1 
  if currentNode is not None: 
    currentNode.value = element
    return position 
  return None 
