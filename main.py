import sys
from read_input import ReadInput
from graph import *
from coloring import Coloring

def main():

	NUM_ARGUMENTS = 2

	# total arguments
	if(len(sys.argv)-1 != NUM_ARGUMENTS):
		print("ERROR: Please use the command: python main.py <pathToInputFile> <population>")
		exit(1);

	pathToInputFile = sys.argv[1]
	population = int(sys.argv[2])
	 
	problemInfo = ReadInput(pathToInputFile)
	graph = Graph(problemInfo)
	graph.print(False)

	solutions = []
	for i in range(population):
		solutions.append(Coloring(graph))

	for i in range(population):
		solutions[i].print(False)

if __name__ == "__main__":
    main()