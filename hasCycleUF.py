from unionfind import quickUnion
from graph.Graph_AdjacencyList import *
import random
from time import time

def hasCycleUf(graph):
    uf = quickUnion.QuickUnionBalanced()

    # per ogni nodo una union find
    for node in graph.getNodes():
        uf.makeSet(node.id)

    uf.print()

    for edge in graph.getEdges():
        print("Head root of node {}: {} Tail root of node {}: {}".format(edge.tail, uf.find(uf.nodes[edge.tail]) ,edge.head,uf.find(uf.nodes[edge.head])))  # uf.nodes[i] per come è creata la find serve

        if uf.find(uf.nodes[edge.tail]) == uf.find(uf.nodes[edge.head]):        # uf.nodes[i] per come è creata la find serve
            print("IF")
            return 1
        else:
            uf.union(uf.nodes[edge.tail],uf.nodes[edge.head])           # TODO RICONTROLLARE SE E' CORRETTO L'INSERIMENTO DEGLI ARCHI (testa e coda sono invertiti!?)

    uf.print()
    return 0                                ## Sembra funzionare


def createGraph(cycle = None):
    graph = GraphAdjacencyList()
    # numNodes = random.randint(0,100)
    numNodes = 10
    nodes = []
    for i in range(numNodes):
        node = graph.addNode(i)
        nodes.append(node)
        # print("Node(id) inserted: ", node.id)
    i = 0
    while(i<len(nodes) and i<numNodes-1):                    ## SERVIREBBE UN ITERATOR PER EVITARE DI COLLEGARE PIU' ARCHI ALLO STESSO NODO ?? oppure while con condizione i<len

            node_1 = nodes[i]
            node_2 = nodes[i+1]
            if node_1 != node_2:
                # print("Node_1: {}\nNode_2: {}\n{}".format(node_1.id, node_2.id, graph.getAdj(node_1.id)))
                if graph.getAdj(node_1.id) == []:
                    # print("Nodo {} non ha adiacenti".format(node_1.id))
                    graph.insertEdge(node_1.id, node_2.id)
                    # print("Inserito arco\n-----")
            i += 1
    if cycle:
        numCycles = 1

        while numCycles>0:
            nodeH_pos = random.randint(0,len(nodes)-1)
            print(nodeH_pos)
            nodeH = nodes[nodeH_pos]
            print(nodeH)
            nodeT_pos = random.randint(0, len(nodes) - 1)
            print(nodeT_pos)
            nodeT = nodes[nodeT_pos]
            print(nodeT)
            print("Head {} Tail {}".format(nodeH, nodeT))
            if (nodeH == nodeT) or graph.isAdj(nodeT.id, nodeH.id):
                print("Già adiacenti o uguali")
                pass
            else:
                graph.insertEdge(nodeT.id, nodeH.id)
                numCycles-=1

    graph.print()
    return graph


if __name__ == "__main__":
    g = createGraph()
    if hasCycleUf(g):
        print("Graph has cycles")
    else:
        print("Graph hasn't cycles")


        # ERRORE: in caso di grafi senza cicli stampa solo i primi due elementi della singola union find rimanente 