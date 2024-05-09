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

def existPath(graph, v1, v2): 
    
    #traverse adjacency list of v1, if v2 is there then return True, else, return False 
    for vertex in graph[v1]: 
        if vertex == v2: 
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
def isConnected(graph):
    for vertex in graph: 
        if len(graph[vertex]) == 0: 
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

#Usar algoritmo BFS of DFS para determinar si el grafo tiene o no ciclos 
#Si no tiene es ciclos, es un árbol, luego, devuelve True, sino devuelve False 

#Para determinar si hay un ciclo: 
#Recorremos el grafo usando bfs, y vamos marcando los nodos que visitamos, si en la lista de adayancencia de un vertice u
#encontramos un vertice q ya fue visitado este debe ser si o sí el padre del u, sino, estamos en presencial de un ciclo 
def isTree(grafo):
    s = next(iter(grafo)) 
    parents = {}
    visited = set() 
    visited.add(s) 
    queue = deque() 
    queue.append(s) 
    parents[s] = None 
    while queue: 
        u = queue.popleft() 
        for vertex in grafo[u]: 
            if vertex not in visited: 
                visited.add(vertex)
                parents[vertex] = u 
                queue.append(vertex)
            elif parents[u] != vertex:
                return False 
    return True 
'''
#Test 
vertices = [1,2,3,4,5,6] 
edges = [(1,2),(1,3),(1,4),(2,6),(6,5)]
tree = createGraph(vertices,edges)
print(isTree(tree))
edges = [(1,2),(1,3),(1,4),(2,6),(6,5),(2,3)]
graph = createGraph(vertices,edges)
print(isTree(graph))
'''

# I dont understand why the time complexity should be O( V + E) but okay, at least it works 
#Apparently my implementation is O(E)
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
    
'''
#Test 
vertices = [1,2,3,4,5,6] 
edges = [(1,2),(1,3),(1,4),(2,3),(2,6),(6,5)]

graph = createGraph(vertices,edges)
print("graph --->>")
print(graph)

print("Traversal -->") 
traversal = BFS(graph,1) #start from vertex 1 
print(traversal)
'''      

#Ejercicio 5
'''
def isComplete(Grafo):
Descripción: Implementa la operación es completo
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo
'''
#En todo grafo completo hay n(n-1) / 2 cantidad de aristas, donde n es la cantidad de vertices 
def isComplete(grafo): 
    
    #Recorrer la lista de adyacencia de cada vertice 
    for vertice in grafo: 
        if len(grafo[vertice]) != len(grafo)-1:  #cada lista de adyancencia contiene n -1 vertices 
            return False
        #Comprobar que cada vertice contenga a los demás vertices (excepto a sí mismo) 
        expectedVertices = set(grafo) - {vertice}
        actualvertices = set(grafo[vertice])
        if expectedVertices != actualvertices: 
            return False 
    return True 
'''
#Test 
vertices = [1,2,3,4] 
edges = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]

graph = createGraph(vertices,edges)
print("graph --->>")
print(graph)

print(isComplete(graph))
'''
