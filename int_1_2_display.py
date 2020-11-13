
def printAdjacencyMatrix(matrix):
    print(" ", end = ' ')
    for i in range(len(matrix)):
        print(" " * (7 - len(str(i))) + (str(i)), end=" ")
    print('')
    for i in range(len(matrix)):
        print(i, end = ' ')
        for j in range(len(matrix)):
            print(" " * (7 - len(str(matrix[i][j]))) + str(matrix[i][j]), end=" ")
        print('')

