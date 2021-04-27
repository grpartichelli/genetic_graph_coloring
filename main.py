import random

#my imports
from input import *
from graph import *
from genetic import *

#constants
RANDOM_SEED = 40

NUM_SEPARATORS = 100



def main():
	random.seed(RANDOM_SEED)
	
	pathToInputFile,population,elitism,crossOverRate,mutationRate,maxTime,maxNonImprovingGens = getTerminalInput()

	problemInfo = ReadInput(pathToInputFile)
	graph = Graph(problemInfo)
	graph.print(False)

	separators = []
	#get separators used in crossover
	for i in range(NUM_SEPARATORS):
		separators.append(graph.get_separated_graph(random.randint(0,graph.numVertices-1)))

	geneticSolve(graph,separators,population, elitism, crossOverRate,mutationRate,maxTime,maxNonImprovingGens)

if __name__ == "__main__":
	main()


