from hasCycleDFS import *
from hasCycleUF import *
from graphUtility import *
from demo.writeOnCsv import *
from time import time

def timer(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)  # chiamata alla funzione da decorare
        elapsed = time() - start
        print(f'Function {func.__name__} with Graph: n:{args[0]}  m:{args[1]}  cycle:{args[2]}  \ntook {elapsed} seconds')

        if(func.__name__=="detectCycleDFS"):
            write("../results/detectCycleDFS_"+str(args[0])+"_"+str(args[2])+".csv", [[args[1], elapsed]])
        if (func.__name__ == "detectCycleUF"):
            write("../results/detectCycleUF_"+str(args[0])+"_"+str(+args[2])+".csv", [[args[1], elapsed]])
        print("-----------")
        return value
    return wrapping_function


@timer
def detectCycleDFS(num_nodes,_num_edges,cycle):
        print("-----------")
        if(hasCycleDFS(g)):
            print("grafo con ciclo")
        else:
            print("senza ciclo")


@timer
def detectCycleUF(num_nodes,_num_edges,cycle):
        print("-----------")
        if(hasCycleUf(g)):
            print("grafo con ciclo")
        else:
            print("senza ciclo")


if __name__ == "__main__":



    numNodes = 50
    maxEdges = (numNodes*(numNodes-1))//2
    cycle = False
    steps = 50

    if not cycle:
        numEdges = numNodes -1
        g = createGraph(numNodes, numEdges, cycle)
        detectCycleUF(numNodes, numEdges, cycle)
        detectCycleDFS(numNodes, numEdges, cycle)


    else:
        for numEdges in range(numNodes, maxEdges, steps):
            g = createGraph(numNodes, numEdges, cycle)
            if isConnected(g):
                detectCycleDFS(numNodes, numEdges, cycle)
                detectCycleUF(numNodes, numEdges, cycle)
