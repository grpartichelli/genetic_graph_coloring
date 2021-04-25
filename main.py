import random

#my imports
from input import *
from graph import *
from coloring import Coloring
from genetic import *

#constants
RANDOM_SEED = 4

NUM_SEPARATORS = 100



def main():
	random.seed(RANDOM_SEED)
	
	pathToInputFile,population,crossOverRate,mutationRate = getTerminalInput()

	problemInfo = ReadInput(pathToInputFile)
	graph = Graph(problemInfo)
	graph.print(False)

	separators = []
	#get separators used in crossover
	for i in range(NUM_SEPARATORS):
		separators.append(graph.get_separated_graph(random.randint(0,graph.numVertices-1)))


	#get colorings
	coloring = []
	for i in range(population):
		coloring.append(Coloring(graph))

		startingPoint = random.randint(0,graph.numVertices-1)
		coloring[i].colorGreedy(startingPoint)

	
	
	geneticSolve(graph,coloring,separators,crossOverRate,mutationRate)

if __name__ == "__main__":
	main()


