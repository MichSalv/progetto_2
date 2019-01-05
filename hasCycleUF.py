from unionfind import quickUnion
from graph.Graph_AdjacencyList import *
import random

def hasCycleUf():
    uf = quickUnion.QuickUnionBalanced()
    uf.makeSet(2)
    uf.makeSet(3)
    uf.union(uf.nodes[0],uf.nodes[1])
    uf.print()





def createGraph():
    graph = GraphAdjacencyList()
    graph.print()

    nodi = []
    for i in range(10):
        node = graph.addNode(i)
        print("Node inserted: ", node)
        nodi.append(node)


    graph.print()
    # num = random.randint(0, len(nodi))
    num = 4

    print("num: {}".format(num))

    # CONNETTO num NODI, non tutti --> creo un ciclo? 
    for i in range(num):
        for j in range(num):
            node_1 = nodi[i]
            node_2 = nodi[j]
            if node_1 != node_2:
                print("node_1: {};  node_2: {}; \nAdiacenti: {}".format(node_1.id, node_2.id, graph.isAdj(node_1.id, node_2.id)))
                graph.insertEdge(node_1.id, node_2.id)
                print("Aggiunto arco tra {} e {}\nAdiacenti: {}".format(node_1.id, node_2.id, graph.isAdj(node_1.id, node_2.id)))


            print("------")



    graph.print()


if __name__ == "__main__":
    createGraph()