from collections import deque

#Ejercicio 1 
'''
def createGraph(List, List)
    Descripción: Implementa la operación crear grafo
    Entrada: LinkedList con la lista de vértices y LinkedList con la lista
    de aristas donde por cada par de elementos representa una conexión
    entre dos vértices.
    Salida: retorna el nuevo grafo
'''

#Time complexity --> O(|V| * |E|) --> se puede mejorar 
def createGraph(vertices,edges): 
    graph = {}
    i = 0 
    for vertex in vertices: 
        graph[vertex] = []
        for edge in edges: 
            if vertex == edge[0]: 
                graph[vertex].append(edge[1]) 
            if vertex == edge[1]: 
                graph[vertex].append(edge[0]) 
        i+= 1 
    return graph

'''
vertices = [1, 2,3,4,5,6] 
edges = [(1,2),(1,3),(1,4),(2,3),(2,6)]

print(createGraph(vertices,edges))
'''

#Ejercicio 2 

'''
def existPath(Grafo, v1, v2): 
    Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
    Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
    Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
'''

#Time complexity ---> O(|V| * Gr(v1)) o O(|V| * Gr(v2)) -- > se puede mejorar 
def existPath(Grafo, v1, v2): 
    
    for vertexTuple in Grafo: 
        if vertexTuple[0]== v1: 
            if v2 in vertexTuple[1]: 
                return True 
        if vertexTuple[0] == v2: 
            if v1 in vertexTuple[1]: 
                return True 
    return False 

'''
vertices = ["v1", "v2","v3","v4","v5","v6"] 
edges = [("v1","v2"),("v1","v3"),("v1","v4"),("v2","v3"),("v2","v6")]

graph = createGraph(vertices,edges)

print(existPath(graph,"v1","v2")) 
print(existPath(graph,"v1","v5")) 
'''

#Ejercicio 3 

'''
def isConnected(Grafo):
    Descripción: Implementa la operación es conexo
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si existe camino entre todo par de vértices,
    False en caso contrario
'''
#Time complexity ---> O(|V|) 
def isConnected(Grafo):
    for vertexTuple in Grafo: 
        if len(vertexTuple[1]) == 0: 
            return False 
    return True 

''''
test1 --> returns False 
vertices = ["v1", "v2","v3","v4","v5","v6"] 
edges = [("v1","v2"),("v1","v3"),("v1","v4"),("v2","v3"),("v2","v6")]
graph = createGraph(vertices,edges)

print(isConnected(graph)) 

test2 --> returns True
vertices = ["v1", "v2","v3","v4","v5","v6"] 
edges = [("v1","v2"),("v1","v3"),("v1","v4"),("v2","v3"),("v2","v6"),("v5","v6")]
graph = createGraph(vertices,edges)
'''

#Ejercicio 4 
'''
def isTree(Grafo):
    Descripción: Implementa la operación es árbol
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si el grafo es un árbol.
'''

def isTree(Grafo):
    #Usar algoritmo BFS of DFS para determinar si el grafo tiene o no ciclos 
    #Si no tiene es ciclos, es un árbol, luego, devuelve True, sino devuelve False 
    pass 

# I dont understand why the time complexity should be O( V + E) but okay, at least it works 
def BFS(graph,s): 
    visited = set()
    traversal = []
    queue = deque() #queue  
    queue.append(s) #start from vertex s 
    
    visited.add(s) #mark vertex s as visited 
    
    while queue: 
        u = queue.popleft() #dequeue vertex u 
        traversal.append(u) #add it to the traversal list 
        for vertex in graph[u]:  # graph[u] gives the adjacency list for vertex u
            if vertex not in visited: 
                visited.add(vertex) #mark vertex as visited 
                queue.append(vertex) #Enqueue vertex to continue traversing the graph 
    return traversal
    
         
#Test 
vertices = [1,2,3,4,5,6] 
edges = [(1,2),(1,3),(1,4),(2,3),(2,6),(6,5)]

graph = createGraph(vertices,edges)
print("graph --->>")
print(graph)

print("Traversal -->") 
traversal = BFS(graph,1) #start from vertex 1 
print(traversal)
