from graph.Graph_AdjacencyList import *

class edgeIterator(GraphAdjacencyList):

    def __init__(self, listEdge):
        self.curr = 0
        self.listEdge = listEdge
        self.markedList = []


    def __iter__(self):
        return self

    def __next__(self):

        while self.curr < len(self.listEdge):
            edge = self.listEdge[self.curr]
            # print("preso in considerazione", edge)

            if (edge.tail, edge.head) in self.markedList or (edge.head, edge.tail) in self.markedList:
                self.curr += 1
                continue


            self.markedList.append((edge.tail, edge.head))
            self.markedList.append((edge.head, edge.tail))
            self.curr += 1

            break

        else:
            raise StopIteration()

        # print(self.markedList)
        return edge






if __name__ == "__main__":

    graph = GraphAdjacencyList()

    nodes = []
    for i in range(5):
        node = graph.addNode(i)
        nodes.append(node)

    for node_src in nodes:
        for node_dst in nodes:
            if node_src != node_dst:
                graph.insertEdge(node_src.id, node_dst.id,
                                 node_src.id + node_dst.id)

    graph.print()

    iterator = edgeIterator(graph.getEdges())
    print([str(i) for i in graph.getEdges()])
    for i in range(100):
        print("---------")
        print(next(iterator))


