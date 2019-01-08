import matplotlib.pyplot as plt
import xlsxwriter
import pandas as pd
import numpy as np


def plot():
    names = ["detectCycleDFS","detectCycleUF"]

    c = 0       #color
    for alg in names:
        d = pd.read_csv("../results/" + alg + ".csv", sep=',', header=None)  # read file
        #d e' un dataframe: in pratica è una matrice. In d[i] c'è l'i-esima colonna

        # crea tabella excel
        createExcelTable(alg, d)

        x = d[0].values
        y = d[1].values
        plt.plot(x, y, color="C" + str(c), label=alg)
        plt.legend(loc="best")
        # plt.savefig
        c += 1

    plt.savefig("../results/result.png")
    plt.show()

def histogram():
    data = pd.read_csv("filename.csv", sep=',', header=None)  # read file
    data = data[0]

    binNumber = max(int(round(np.log(max(data) - min(data)))), 25)

    # plt.hist(data, bins=range(min(data), max(data) + 10, (max(data) - min(data)) / binNumber), color='red')
    plt.hist(data, bins=binNumber, color='red')

    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title('Put here a title')

    plt.savefig('hist.png')

    plt.show()


def createExcelTable(alg, d):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('../results/' + alg + '.xlsx')
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    worksheet.write(row,col, alg)
    row = row + 1
    for index, riga in d.iterrows():
        worksheet.write(row, col, riga[0])
        worksheet.write(row, col + 1, riga[1])
        row = row + 1


    workbook.close()



if(__name__ == "__main__"):
    plot()
    # histogram()