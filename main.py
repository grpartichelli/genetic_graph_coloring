import sys
import random

#my imports
from input import ReadInput
from graph import *
from coloring import Coloring

#constants
NUM_ARGUMENTS = 2
RANDOM_SEED = 2


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

	NUM_PARTITIONS = 50
	for i in range(NUM_PARTITIONS):
		graph.bfs(random.randint(0,graph.numVertices-1))


	solutions = []
	for i in range(population):
		solutions.append(Coloring(graph))


	
	for i in range(population):
		startingPoint = random.randint(0,graph.numVertices-1)
		solutions[i].colorGreedy(startingPoint)
		solutions[i].print(False)
		if(solutions[i].isColoringValid()):
			print("Valid coloring")

if __name__ == "__main__":
    main()