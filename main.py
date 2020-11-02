class Graph:
    nb_vertix = 0
    nb_edge = 0
    edges = [[]]
    
# #Set Graph from a file
# def setGraph(index):
#     f = open(index + ".txt", "r")
#     graph = Graph()
#     graph.nb_vertix = int(f.readline())
#     graph.nb_edge = int(f.readline())
#     newTable = dict() {"key": "valeur", "key": "valeur"}
#     for i in range(graph.nb_edge):
#         temp = int(f.readline(1))
#         tempArray = [int(f.readline(3)), int(f.readline(5))]
#         if graph.edges.get(temp) != None:
#             graph.edges.get(temp).append(tempArray)
#         else:
#             graph.edges.update({temp: [tempArray]})
#     return graph

def setGraph(index):
    f = open(index + ".txt", "r")
    graph = Graph()
    graph.nb_vertix = int(f.readline())
    graph.nb_edge = int(f.readline())
    graph.edges = [['∞' for i in range(graph.nb_vertix)] for j in range(graph.nb_vertix)]
    for x in range(graph.nb_edge):
        i = int(f.readline(1))
        j = int(f.readline(3))
        graph.edges[i][j] = int(f.readline(5))
    for i in range(graph.nb_vertix):
        for j in range(graph.nb_vertix):
            if(i == j):
                graph.edges[i][j] = 0
    return graph

def printAdjacencyMatrix(graph):
    print('', end = '\t')
    for i in range(graph.nb_vertix):
        print(i, end = '\t')
    print('')
    for i in range(graph.nb_vertix):
        print(i, end = '\t')
        for j in range(graph.nb_vertix):
            print(graph.edges[i][j], end = '\t')
        print('')
    
def main():
    newGraph = setGraph("1")
    print(newGraph.edges)
    printAdjacencyMatrix(newGraph)

if __name__ == "__main__":
    main()