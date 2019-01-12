from hasCycleDFS import *
from hasCycleUF import *
from graphUtility import *
from demo.writeOnCsv import *
from time import time

def timer(func):
    def wrapping_function(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)  # chiamata alla funzione da decorare

        elapsed = time() - start
        n= args[0]
        m= args[1]
        hasCycle = args[2]

        print(f'Function {func.__name__} with Graph: n:{str(n)}  m:{str(m)}  cycle:{str(hasCycle)}  \ntook {elapsed} seconds')

        if hasCycle == True:
            if(func.__name__=="detectCycleDFS"):
                write("../results/detectCycleDFS_"+str(n)+"_"+str(hasCycle)+".csv", [[m, elapsed]])
            if (func.__name__ == "detectCycleUF"):
                write("../results/detectCycleUF_"+str(n)+"_"+str(hasCycle)+".csv", [[m, elapsed]])
        else:
            if (func.__name__ == "detectCycleDFS"):
                write("../results/detectCycleDFS_" + str(hasCycle) + ".csv", [[m, elapsed]])
            if (func.__name__ == "detectCycleUF"):
                write("../results/detectCycleUF_" + str(hasCycle) + ".csv", [[m, elapsed]])

        return value
    return wrapping_function


@timer
def detectCycleDFS(num_nodes,_num_edges,cycle):
        if (hasCycleDFS(g) == False and cycle == True  ):
            print("ERROR-CYCLE NOT DETECTED")
            print("n:", num_nodes, "m:", numEdges)


@timer
def detectCycleUF(num_nodes,_num_edges,cycle):
        if(hasCycleUf(g)==False and cycle==True ):
            print("ERROR-CYCLE NOT DETECTED")
            print("n:",num_nodes,"m:",numEdges)
            exit(0)




if __name__ == "__main__":
    cycle = True

    numNodes = 20
    maxNodes = 1500
    stepNodes = 50

    maxEdges = (numNodes*(numNodes-1))//2
    stepsEdges = 3

    # test con grafi senza ciclo
    if not cycle:
        for n in range(numNodes,maxNodes, stepNodes):
            numEdges = n -1
            g = createGraph(n, numEdges, cycle)
            detectCycleUF(n, numEdges, cycle)
            detectCycleDFS(n, numEdges, cycle)


    # test con grafi con ciclo
    else:
        for numEdges in range(numNodes, maxEdges, stepsEdges):
            g = createGraph(numNodes, numEdges, cycle)
            if isConnected(g):
                detectCycleDFS(numNodes, numEdges, cycle)
                detectCycleUF(numNodes, numEdges, cycle)
    print("DONE!")
