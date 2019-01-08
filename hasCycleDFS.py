from hasCycleUF import *
from unionfind.quickUnion import *
from graphUtility import *
from datastruct.Stack import PilaArrayList as Stack

def hasCycleDFS(graph):
    rootId = graph.nodes[0].id          # poichè connesso e non orientato va bene partire da qualsiasi nodo
    if rootId not in graph.nodes:
        return None

    # DFS nodes initialization
    dfs_nodes = []

    # queue initialization
    s = Stack()
    s.push(rootId)

    explored = [] # nodes already explored

    while not s.isEmpty():  # while there are nodes to explore ...
        node = s.pop()  # get the node from the stack
        # print("node: ", node)
        # # print("adj_node: ", adj_node)
        # print("explored: ", explored)
        # print("-------")
        if node in explored:
            return 1

        explored.append(node)

        for adj_node in graph.getAdj(node):
            if adj_node not in explored:
                s.push(adj_node)
        dfs_nodes.append(node)

        # for adj_node in graph.getAdj(node):
        #     print("node: ", node)
        #     print("adj_node: ", adj_node)
        #     print("explored: ", explored)
        #     print("prevVisited: ", prevVisited)
        #     print("-------")
        #
        #     if adj_node != prevVisited and adj_node in explored:
        #
        #         print("ciclo")
        #         return 1

        # s.push(adj_node)
        # prevVisited = node

        # dfs_nodes.append(node)

    return 0


def test():

    for i in range(100):
        g = createGraph(1)
        if isConnected(g):
            if not hasCycleDFS(g):
                print("Grafo numero: ", i, "errore \n", g.print())
                return




if __name__ == "__main__":
    test()