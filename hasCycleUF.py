from unionfind import quickUnion
from graph.Graph_AdjacencyList import *
import random
from time import time
from graph.ITERATORE import edgeIterator

def hasCycleUf(graph):

    # print("--------------UNION-------------------")
    uf = quickUnion.QuickUnionBalanced()

    # per ogni nodo una union find
    for node in graph.getNodes():
        uf.makeSet(node.id)

    # uf.print()
    # print(uf.nodes)

    iterator = edgeIterator(graph.getEdges())

    while True:
        try:
            edge = next(iterator)
            ufHead = uf.nodes[edge.head]
            # markedNodes += ufHead
            ufTail = uf.nodes[edge.tail]
            # markedNodes += ufTail


            # print("edge: {}\tufTail: {}\tufHead: {}".format(edge, ufTail, ufHead))

            if uf.find(ufTail) == uf.find(ufHead):
                return 1

            else:
                uf.union(ufTail, ufHead)

            # uf.print()
        except StopIteration:
            break;


    #
    # # for edge in graph.getEdges():
    # #     print("Head root of node {}: {} Tail root of node {}: {}".format(edge.tail, uf.find(uf.nodes[edge.tail]) ,edge.head,uf.find(uf.nodes[edge.head])))  # uf.nodes[i] per come è creata la find serve
    # #
    # #     if uf.find(uf.nodes[edge.tail]) == uf.find(uf.nodes[edge.head]):        # uf.nodes[i] per come è creata la find serve
    # #         print("IF")
    # #         return 1
    # #     else:
    # #         uf.union(uf.nodes[edge.tail],uf.nodes[edge.head])           # TODO RICONTROLLARE SE E' CORRETTO L'INSERIMENTO DEGLI ARCHI (testa e coda sono invertiti!?)
    # #
    # # uf.print()
    # # return 0                                ## Sembra funzionare


def createGraph(cycle = False):
    graph = GraphAdjacencyList()
    # numNodes = random.randint(0,100)
    numNodes = 3000
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


if __name__ == "__main__":
    start = time()
    g = createGraph(False)
    print("Grafo creato in ",time()-start, "secondi")
    start = time()
    if hasCycleUf(g):
        print("Graph has cycles")
    else:
        print("Graph hasn't cycles")

    print(time()-start)
        # ERRORE: in caso di grafi senza cicli stampa solo i primi due elementi della singola union find rimanente  # TODO Giusto perchè c'è il return