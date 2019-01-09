from graphUtility import *
from datastruct.Stack import PilaArrayList as Stack

def hasCycleDFS(graph):
    '''

    :param graph
    :return: 1 if cycle detected, 0 otherwise
    '''
    rootId = graph.nodes[0].id          # poichè connesso e non orientato va bene partire da qualsiasi nodo

    if rootId not in graph.nodes:
        return None

    # DFS nodes initialization
    dfs_nodes = []

    # queue initialization
    s = Stack()
    s.push(rootId)
    stack_Copy = []
    explored = []       # nodes already explored
    stack_Copy.append(rootId)

    while not s.isEmpty():
        node = s.pop()
        stack_Copy.remove(node)
        explored.append(node)

        for adj_node in graph.getAdj(node):

            if adj_node in stack_Copy and adj_node not in explored:
                return 1

            if adj_node not in explored:
                s.push(adj_node)
                stack_Copy.append(adj_node)

        dfs_nodes.append(node)
    return 0


def test():

    for i in range(100):
        g = createGraph(10, True)
        if isConnected(g):
            if not hasCycleDFS(g):
                print("Grafo numero: ", i, "errore \n", g.print())
                return


if __name__ == "__main__":
    # test()
    # g = createGraph(10, 9, True)
    # g.print()
    g = GraphAdjacencyList()
    g.addNode(0)
    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode(4)
    g.insertEdge(0,2)
    g.insertEdge(2,0)
    g.insertEdge(0,1)
    g.insertEdge(1,0)
    g.insertEdge(1,3)
    g.insertEdge(3,1)
    g.insertEdge(3,4)
    g.insertEdge(4,3)
    g.insertEdge(4,1)
    g.insertEdge(1,4)
    hasCycleDFS(g)