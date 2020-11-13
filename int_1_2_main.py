from os import system, name 
import sys

class Graph:
    nb_vertex = 0
    nb_edge = 0
    adjMatrix = [[]]

    
def setGraph(index):
    f = open("Graph/" + index + ".txt", "r")
    graph = Graph()
    graph.nb_vertex = int(f.readline())
    graph.nb_edge = int(f.readline())
    graph.adjMatrix = [[float('inf') for i in range(graph.nb_vertex)] for j in range(graph.nb_vertex)]

    for x in range(graph.nb_edge):
        i = int(f.readline(1))
        j = int(f.readline(3))
        graph.adjMatrix[i][j] = int(f.readline(5))
    for i in range(graph.nb_vertex):
        for j in range(graph.nb_vertex):
            if(i == j and graph.adjMatrix[i][j] == float('inf')):
                graph.adjMatrix[i][j] = 0
    f.close()
    return graph

def printAdjacencyMatrix(matrix):
    print('', end = '\t')
    for i in range(len(matrix)):
        print(i, end = '\t')
    print('')
    for i in range(len(matrix)):
        print(i, end = ' ')
        for j in range(len(matrix)):
            print(" " * (7 - len(str(matrix[i][j]))) + str(matrix[i][j]), end=" ")
        print('')
   
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
		print("T" + str(k))
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

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main():
	validity = 1
	while(validity):
		clear()
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
				index = int(input("		        Choose the graph: "))
			except ValueError:
				print("       The number must be between 1 and 13")
				continue
			if index < 1 or index > 13:
				print("       The number must be between 1 and 13")
				continue
			else:
				break
		#open the file execution
		print("")
		print("Raw Data:")
		newGraph = setGraph(str(index))
		print(newGraph.adjMatrix)
		print("")
		print("The adjacency matrix:")
		printAdjacencyMatrix(newGraph.adjMatrix)
		floydWarshall(newGraph)
		print("")
		test = input("Do you want to test another graph ? Y/N: ")
		while((test.upper() != 'Y') and (test.upper() != 'N')):
			test = input("Please enter the letter Y or N: ")
		
		if(test == 'N' or test == 'n'):
			validity = 0
		

if __name__ == "__main__":
    main()

print("")
print("")