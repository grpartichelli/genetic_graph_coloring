import random

def geneticSolve(graph,solutions, separators):
	populationSize = len(solutions)
	separatorsSize = len(separators)

	

	i=0
	while(i <100):
		crossover(0,1,2,graph,solutions,separators,separatorsSize)
		crossover(2,0,1,graph,solutions,separators,separatorsSize)
		crossover(1,2,0,graph,solutions,separators,separatorsSize)
		i+=1

#p1 = parent 1
#p2 = parent 2
#son = where it will be stored, deletes old solution
def crossover(p1,p2,son,graph,solutions,separators,separatorsSize):

	
	#randomly choose what separator will be used
	separator = separators[random.randint(0,separatorsSize-1)]

	mustFix = []
	for v in range(graph.numVertices):

		if separator[v] == 0: #will go to smallest available color
			mustFix.append(v)

		if separator[v] == 1: #will go to parent 1
			solutions[son].swapColors(v,solutions[son].colorOfVertice[v], solutions[p1].colorOfVertice[v])
		
		if separator[v] == 2: #will go to parent 2
			solutions[son].swapColors(v,solutions[son].colorOfVertice[v], solutions[p2].colorOfVertice[v])
	

	for v in mustFix:	
		color = solutions[son].findSmallestColorNotUsedByNeighbors(v)
		solutions[son].swapColors(v,solutions[son].colorOfVertice[v], color)
	
