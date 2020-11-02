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
    f = open("Graph/" + index + ".txt", "r")
    graph = Graph()
    graph.nb_vertix = int(f.readline())
    graph.nb_edge = int(f.readline())
    graph.edges = [[float('inf') for i in range(graph.nb_vertix)] for j in range(graph.nb_vertix)]
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
    
def floydWarshall(adjMatrix, N):

	# cost and parent matrix stores shortest-path
	# (shortest-cost/shortest route) information

	# initially cost would be same as weight of the edge
	cost = adjMatrix.copy()
	path = [[None for x in range(N)] for y in range(N)]

	# initialize cost and parent
	for v in range(N):
		for u in range(N):
			if v == u:
				path[v][u] = 0
			elif cost[v][u] != float('inf'):
				path[v][u] = v
			else:
				path[v][u] = -1

	# run Floyd-Warshall
	for k in range(N):
		for v in range(N):
			for u in range(N):
				# If vertex k is on the shortest path from v to u,
				# then update the value of cost[v][u], path[v][u]
				if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
						and (cost[v][k] + cost[k][u] < cost[v][u]):
					cost[v][u] = cost[v][k] + cost[k][u]
					path[v][u] = path[k][u]

			# if diagonal elements become negative, the
			# graph contains a negative weight cycle
			if cost[v][v] < 0:
				print("Negative Weight Cycle Found")
				return

	# Print the shortest path between all pairs of vertices
	printSolution(path, N)

def printSolution(path, N):

	for v in range(N):
		for u in range(N):
			if u != v and path[v][u] != -1:
				print(f"Shortest Path from {v} -> {u} is ({v}", end=' ')
				printPath(path, v, u)
				print(f"{u})")

def printPath(path, v, u):

	if path[v][u] == v:
		return

	printPath(path, v, path[v][u])
	print(path[v][u], end=' ')

def main():
    newGraph = setGraph("1")
    print(newGraph.edges)
    printAdjacencyMatrix(newGraph)
    floydWarshall(newGraph.edges, newGraph.nb_vertix)

if __name__ == "__main__":
    main()