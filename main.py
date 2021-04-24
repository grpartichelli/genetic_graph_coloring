import sys
import random

#my imports
from input import ReadInput
from graph import *
from coloring import Coloring
from genetic import *

#constants
NUM_ARGUMENTS = 2
RANDOM_SEED = 4

NUM_SEPARATORS = 50

def main():
	random.seed(RANDOM_SEED)
	# total arguments
	if(len(sys.argv)-1 != NUM_ARGUMENTS):
		print("ERROR: Please use the command: python main.py <pathToInputFile> <population>")
		exit(1);

	pathToInputFile = sys.argv[1]

	try:
		population = int(sys.argv[2])
	except:
		print("Please enter a valid population number")
		exit(1)

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


	geneticSolve(coloring,separators)

if __name__ == "__main__":
    main()