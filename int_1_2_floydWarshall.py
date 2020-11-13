from int_1_2_display import printAdjacencyMatrix

def floydWarshall(graph):
	print("")
	print("******************** Floyd Warshall ********************")
	dist = graph.adjMatrix.copy()
	path = [[None for x in range(graph.nb_vertex)] for y in range(graph.nb_vertex)] #matrice path n x n

#Initialization of Path
	for i in range(graph.nb_vertex):
		for j in range(graph.nb_vertex):
			if(i == j and dist[i][j] == 0):
				path[i][j] = 0
			elif(dist[i][j] != float('inf')): 
				path[i][j] = i
			else:
				path[i][j] = -1
	
	for k in range(graph.nb_vertex):
		for i in range(graph.nb_vertex):
			for j in range(graph.nb_vertex):
				if(dist[i][j] > dist[i][k] + dist[k][j]):
					dist[i][j] = dist[i][k] + dist[k][j]
					path[i][j] = path[k][j]
		print("")
		print("A" + str(k))
		if (dist[k][k] < 0):
				print("Absorbent cycle found")
				return
		printAdjacencyMatrix(dist)
		print("")
		
		
	print("")
	print("********************************************************")
	print("")
	print("The Shortest paths: ")
	printSolution(path, dist, graph.nb_vertex)


def printSolution(path, matrix, nb_vertex):

	for i in range(nb_vertex):
		for j in range(nb_vertex):
			if (i != j and path[i][j] != -1):
				print(f"Shortest Path from {i} -> {j} is ({i}", end=' ')
				printPath(path, i, j)
				print(f"{j})", end = ' ')
				print("the final weight is: ", matrix[i][j])
			if (i == j and matrix[i][j] != 0):
				print(f"Shortest Path from {i} -> {j} is ({i}", end=' ')
				printPath(path, i, j)
				print(f"{j})", end = ' ')
				print("the final weight is: ", matrix[i][j])

def printPath(path, i, j):

	if (path[i][j] == i):
		return

	printPath(path, i, path[i][j])
	print(path[i][j], end=' ')
