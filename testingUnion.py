from time import time
from hasCycleUF import *
from unionfind import quickUnion


def hasCycleUfTest(graph, type):
    '''

    :param graph
    :return: 0 if no cycle detect, 1 otherwise
    '''

    if type == "QU":
        uf = quickUnion.QuickUnionBalanced()
    elif type == "QUPS":
        uf = quickUnion.QuickUnionBalancedPathSplitting()
    elif type == "QF":
        uf = quickFind.QuickFindBalanced()

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
            break

    return 0

if __name__ == "__main__":

    g = createGraph(200,400,1)
    # g.print()
    print("QUICKUNIONBALANCED")
    start = time()
    print("RESULT: ", hasCycleUfTest(g, "QU"))
    print(time()-start)
    print("QUICKFIND")
    start = time()
    print("RESULT: ",hasCycleUfTest(g, "QF"))
    print(time() - start)
    print("QUICKUNIONBALANCEDPATHSPLITTING")
    start = time()
    print("RESULT: ",hasCycleUfTest(g, "QUPS"))
    print(time() - start)


