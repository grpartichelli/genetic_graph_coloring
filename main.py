import random

#my imports
from input import *
from graph import *
from genetic import *

#constants
NUM_SEPARATORS = 100

def main():
    pathToInputFile,population,elitism,crossOverRate,mutationRate,maxTime,maxNonImprovingGens,randomSeed = getTerminalInput()

    random.seed(randomSeed)

    problemInfo = ReadInput(pathToInputFile)
    graph = Graph(problemInfo)
        #graph.print(False)

    separators = []
    #get separators used in crossover
    for i in range(NUM_SEPARATORS):
        separators.append(graph.get_separated_graph(random.randint(0,graph.numVertices-1)))

    geneticSolve(graph, separators, population, elitism, crossOverRate, mutationRate, maxTime, maxNonImprovingGens)

if __name__ == "__main__":
    main()
