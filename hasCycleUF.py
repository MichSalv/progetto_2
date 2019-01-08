from unionfind import quickUnion, quickFind
from graph.ITERATORE import edgeIterator
from graphUtility import *


def hasCycleUf(graph):
    '''

    :param graph
    :return: 0 if no cycle detect, 1 otherwise
    '''

    uf = quickFind.QuickFindBalanced()                                            ## meglio con pathSplitting
                                                                    ## quickUnion meglio di quickFind, facciamo molte più union che find???
    for node in graph.getNodes():
        uf.makeSet(node.id)

    iterator = edgeIterator(graph.getEdges())

    while True:                              # Scandisco tutti gli archi non ancora visitati implementando un iteratore
        try:
            edge = next(iterator)
            ufHead = uf.nodes[edge.head]
            ufTail = uf.nodes[edge.tail]

            if uf.find(ufTail) == uf.find(ufHead):
                return 1

            else:
                uf.union(uf.findRoot(ufTail), uf.findRoot(ufHead))


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
