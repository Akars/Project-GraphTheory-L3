from os import system, name 
import sys
from int_1_2_display import printAdjacencyMatrix
from int_1_2_floydWarshall import floydWarshall


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

def menu():
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
	writeFile()

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def writeFile():
	for i in range(1,14):
		f = open("Executions/execution-" + str(i)+ ".txt","w")
		sys.stdout = f
		newGraph = setGraph(str(i))
		print("")
		print("Raw Data:")
		print(newGraph.adjMatrix)
		print("")
		print("The adjacency matrix:")
		printAdjacencyMatrix(newGraph.adjMatrix)
		floydWarshall(newGraph)
		print("")
		del newGraph
		f.close()



if __name__ == "__main__":
    menu()
	


