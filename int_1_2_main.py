from os import system, name 

class Graph:
    nb_vertix = 0
    nb_edge = 0
    adjMatrix = [[]]
    index = 1

    
def setGraph(index):
    f = open("Graph/" + index + ".txt", "r")
    graph = Graph()
    graph.nb_vertix = int(f.readline())
    graph.nb_edge = int(f.readline())
    graph.adjMatrix = [[float('inf') for i in range(graph.nb_vertix)] for j in range(graph.nb_vertix)]

    for x in range(graph.nb_edge):
        i = int(f.readline(1))
        j = int(f.readline(3))
        graph.adjMatrix[i][j] = int(f.readline(5))
    for i in range(graph.nb_vertix):
        for j in range(graph.nb_vertix):
            if(i == j):
                graph.adjMatrix[i][j] = 0
    f.close()
    return graph

def printAdjacencyMatrix(graph):
    print('', end = '\t')
    for i in range(graph.nb_vertix):
        print(i, end = '\t')
    print('')
    for i in range(graph.nb_vertix):
        print(i, end = '\t')
        for j in range(graph.nb_vertix):
            print(graph.adjMatrix[i][j], end = '\t')
        print('')
    
def floydWarshall(graph):

	# cost and parent matrix stores shortest-path
	# (shortest-cost/shortest route) information

	# initially cost would be same as weight of the edge
	cost = graph.adjMatrix.copy()
	path = [[None for x in range(graph.nb_vertix)] for y in range(graph.nb_vertix)]

	# initialize cost and parent
	for i in range(graph.nb_vertix):
		for j in range(graph.nb_vertix):
			if i == j:
				path[i][j] = 0
			elif cost[i][j] != float('inf'):
				path[i][j] = i
			else:
				path[i][j] = -1

	# run Floyd-Warshall
	for k in range(graph.nb_vertix):
		for v in range(graph.nb_vertix):
			for u in range(graph.nb_vertix):
				# If vertex k is on the shortest path from v to u,
				# then update the value of cost[v][u], path[v][u]
				if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
						and (cost[v][k] + cost[k][u] < cost[v][u]):
					cost[v][u] = cost[v][k] + cost[k][u]
					path[v][u] = path[k][u]

			# if diagonal elements become negative, the
			# graph contains a negative weight cycle
			if cost[v][v] < 0:
				print("Absorbent cycle found")
				return

	# Print the shortest path between all pairs of vertices
	print("")
	printSolution(path, graph.nb_vertix)

def printSolution(path, nb_vertex):

	for i in range(nb_vertex):
		for j in range(nb_vertex):
			if i != j and path[i][j] != -1:
				print(f"Shortest Path from {i} -> {j} is ({i}", end=' ')
				printPath(path, i, j)
				print(f"{j})")

def printPath(path, i, j):

	if path[i][j] == i:
		return

	printPath(path, i, path[i][j])
	print(path[i][j], end=' ')

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main():

	clear()
	validity = 1

	while(validity):
		print("")
		print("")
		print("          ***********************************************")
		print("          ***             - Graph Theory -            ***")
		print("          ***               GROUP 2 INT 1             ***")
		print("          **VictorGARNIER * WilliamLI * VictorineRICHARD*")
		print("          ***********************************************")
		print("")
		
		while True:
			try:
				index = int(input("Choose the graph: "))
			except ValueError:
				print("The number must be between 1 and 13")
				continue
			if index < 1 or index > 13:
				print("The number must be between 1 and 13")
				continue
			else:
				break
		print("")
		print("")

		newGraph = setGraph(str(index))
		print(newGraph.adjMatrix)
		printAdjacencyMatrix(newGraph)
		floydWarshall(newGraph)

		test = input("Do you want to test another graph ? Y/N: ")
		while((test.upper() != 'Y') and (test.upper() != 'N')):
			test = input("Please enter the letter Y or N: ")

		if(test == 'N' or test == 'n'):
			validity = 0
	

if __name__ == "__main__":
    main()

print("")
print("")