import networkx as nx

from model.model import Model

myModel = Model()
myModel.buildGraph(5)
myModel.printGraphDetails()

v0 = myModel.getAllNodes()[0]

connessa = list(nx.node_connected_component(myModel._grafo, v0))
v1 = connessa[10]

pathD = myModel.trovaCamminoD(v0, v1)
pathBFS = myModel.trovaCamminoBFS(v0, v1)
pathDFS = myModel.trovaCamminoDFS(v0, v1)

print("Metodo di Dijkstra")
print(*pathD, sep=" \n")
print("-------------------")
print("Metodo albero Breadth first")
print(*pathBFS, sep= "\n")
print("------------------")
print("Metodo albero Depth first")
print(*pathDFS, sep= "\n")