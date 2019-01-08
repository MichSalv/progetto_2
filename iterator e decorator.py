from graph.Graph_AdjacencyList import *

class Iteratore(GraphAdjacencyList):

    def __init__(self):
        self.currEdge = None
        self.prevEdge = None
        self.curr = 0

    def __iter__(self):
        return  self

    def __next__(self):
        self.prevEdge = self.currEdge
        self.currEdge = GraphAdjacencyList.getEdges()

        edge = self.currEdge[self.curr]
        self.curr += 1
        return edge





if __name__ == "__main__":

    g = GraphAdjacencyList()
    nodi = []
    for i in range(10):
        node = g.addNode(i)
        nodi.append(node)
    for node_1 in nodi:
        for node_2 in nodi:
            if node_1 != node_2:


                g.insertEdge(node_1.id, node_2.id,
                                 node_1.id + node_2.id)

    g.print()

    print("\n\nARCHI: ", g.getEdges())
    print("Edges: ", [str(i) for i in g.getEdges()])
    my_iterator=iter(g.getEdges())
    print(next(my_iterator))
    print(next(my_iterator))

    f = Iteratore()
