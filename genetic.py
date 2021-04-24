import random

def geneticSolve(solutions, separators):
	populationSize = len(solutions)
	separatorsSize = len(separators)

	
	crossover(0,1,2,solutions,separators,separatorsSize)


#p1 = parent 1
#p2 = parent 2
#son = where it will be stored, deletes old solution
def crossover(p1,p2,son,solutions,separators,separatorsSize):
	solutions[p1].print(False)
	solutions[p2].print(False)
	solutions[son].print(False)
	print(solutions[son].isColoringValid())




	solutions[p1].print(False)
	solutions[p2].print(False)
	solutions[son].print(False)
	print(solutions[son].isColoringValid())