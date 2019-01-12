from unionfind import quickFind
from unionfind import quickUnion
from graphIterator import edgeIterator
from graphUtility import *


def hasCycleUf(graph):
    '''

    :param graph
    :return: 0 if no cycle detect, 1 otherwise
    '''

    uf = quickFind.QuickFindBalanced()                              # scelto quickFind bilanciato, effettuiamo 2 find,ed 1 union per ogni arco

    for node in graph.getNodes():
        uf.makeSet(node.id)

    iterator = edgeIterator(graph.getEdges())                       # Scandisco tutti gli archi non ancora visitati implementando un iteratore

    while True:
        try:
            edge = next(iterator)
            ufHead = uf.nodes[edge.head]
            ufTail = uf.nodes[edge.tail]

            findRootTail = uf.findRoot(ufTail)
            findRootHead = uf.findRoot(ufHead)


            if findRootTail == findRootHead:
                return 1

            else:
                uf.union(findRootTail, findRootHead)


        except StopIteration:
            break;
    return 0



def test():
    for i in range(100):
        g = createGraph()
        if isConnected(g):
            # g.print()
            if  hasCycleUf(g):
                print("Grafo numero: ", i, "errore ")
                # g.print()
                return


if __name__ == "__main__":
    test()
