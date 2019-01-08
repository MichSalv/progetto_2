import random
from graph.Graph_AdjacencyList import *

def createGraph(cycle = False):
    graph = GraphAdjacencyList()
    # numNodes = random.randint(0,100)
    numNodes = 10
    nodes = []
    for i in range(numNodes):
        node = graph.addNode(i)
        nodes.append(node)



    minEdge = numNodes -1
    maxEdge = (numNodes*(numNodes-1))/2                     # PER AVERE UN ARCO SENZA CICLI DEVE AVERE ESATTAMENTE N-1 ARCHI (per essere anche connesso)
    if cycle:
        numEdges = random.randint(numNodes, maxEdge)          # numNodes al posto di numEdges per non ricadere sul grafo aciclico
    else:
        numEdges = minEdge

    while(numEdges>0):

            node_1 = random.choice(nodes)
            node_2 = random.choice(nodes)
            # print(node_1, node_2)

            if node_1 != node_2:
                if not cycle:
                    bfsList = graph.bfs(node_1.id)
                    # print("bfs: ",bfsList)
                    if node_2.id not in bfsList:
                        new_node = graph.insertEdge(node_1.id, node_2.id)          # condizione che verifica se sono adiacenti inserita nel metodo insertEdge
                        if new_node is not None:
                            graph.insertEdge(node_2.id, node_1.id)
                            numEdges -= 1
                else:
                    new_node = graph.insertEdge(node_1.id,node_2.id)  # condizione che verifica se sono adiacenti inserita nel metodo insertEdge
                    if new_node is not None:
                        graph.insertEdge(node_2.id, node_1.id)
                        numEdges -= 1

    # graph.print()
    return graph

def isConnected(graph):
    '''

    :param graph
    :return: 1 if graph is connected, 0 otherwise
    '''
    x = graph.dfs(graph.nodes[0].id)
    for node in graph.nodes:
        if node not in x:
            return 0
    return 1



if __name__ == "__main__":
    g = createGraph(1)
    g.print()
    # print(isConnected(g))
    a = isConnected(g)
    print(a)