def write(fileName, data):
    with open(fileName,'a') as writeFile:
        for row in data:
            writeFile.write('{0},'.format(row[0]))
            writeFile.write('{0}'.format(row[1]))
            writeFile.write('\n')
    writeFile.close()