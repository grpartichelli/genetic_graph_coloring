import random

def geneticSolve(graph,solutions, separators,crossOverRate,mutationRate):
	populationSize = len(solutions)
	separatorsSize = len(separators)

	#Mutate the population (probably will only be applied to the kids)
	for i in range(populationSize):
		if(random.uniform(0,1) <= mutationRate):
			mutate(i,graph,solutions)

		
########################################################################################
#MUTATE
#what function should we use?
def getNumMutations(graph):
	return int(graph.numVertices/3)

def mutate(solutionId,graph, solutions):
	
	#mutate one third of the graph
	numMutations =getNumMutations(graph)

	for _ in range(numMutations):
		#change color of a random vertice:
		i = random.randint(0, graph.numVertices-1)
		newColor = solutions[solutionId].findLessWeightColorNotUsedByNeighbors(i, False)
		solutions[solutionId].swapColors(i,newColor)
		
########################################################################################
#CROSSOVER	

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
			solutions[son].swapColors(v, solutions[p1].colorOfVertice[v])
		
		if separator[v] == 2: #will go to parent 2
			solutions[son].swapColors(v, solutions[p2].colorOfVertice[v])
	

	for v in mustFix:	
		color = solutions[son].findLessWeightColorNotUsedByNeighbors(v,True)
		solutions[son].swapColors(v, color)
	
		
########################################################################################