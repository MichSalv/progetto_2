from hasCycleUF import *



def graph_Utility(graph):


if __name__ == "__main__":

        for i in range(100):
            g = createGraph(1)
            x = len(g.dfs(g.nodes[0].id))
            print("GRAFO NUMERO: ", i)
            print("len: {}\t#nodes: {}\n".format(x, len(g.nodes)))
            if x < len(g.nodes):
                print("ERRORE")
                g.print()
                break