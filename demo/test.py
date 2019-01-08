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
            write("../results/detectCycleDFS.csv", [[args[0], elapsed]])
        if (func.__name__ == "detectCycleUF"):
            write("../results/detectCycleUF.csv", [[args[0], elapsed]])
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
    num_times = 1
    num_nodes = 200
    max_nodes = 210
    step=10
    cycle = True

    for n in range(num_nodes,max_nodes,step):
        for x in range(num_times):
            g = createGraph(n, cycle)

            num_edges = g.numEdges()/2

            detectCycleDFS(n,num_edges,cycle)
            detectCycleUF(n,num_edges,cycle)

