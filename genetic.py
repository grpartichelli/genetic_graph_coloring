import random
from coloring import Coloring
import time

positive_infnity = float('inf')

def geneticSolve(graph,separators,populationSize, elitism, crossOverRate,mutationRate, maxTime , maxNonImprovingGens):
	startTime = time.time()
	separatorsSize = len(separators)

	solutions = getStartingPopulation(populationSize,graph)
	nonImprovingGens = 0

	#START ALGORITHM
	while shouldKeepGoing(maxTime, time.time() - startTime, maxNonImprovingGens,nonImprovingGens):
		#Get the best solution
		solutions = orderPopulationByScore(solutions,populationSize)
		bestScore = solutions[0].getScore()
		#Display it
		#solutions[0].print(False)

		#Elitism preserves the <elitism> first solutions
		for i in range(elitism,populationSize):
			p1,p2 = selectParents(solutions,populationSize,"tournament")
			



		nonImprovingGens+=1

	'''
	#Mutate the population (probably will only be applied to the kids)
	for i in range(populationSize):
		if(random.uniform(0,1) <= mutationRate):
			mutate(i,graph,solutions)
	'''
#######################################################################################
#PARENT SELECTION
def selectParents(solutions,populationSize,type):
	if type == "tournament":
		return tournamentSelection(solutions,populationSize)
	if type == "random":
		return randomSelection(solutions,populationSize)
	

	print("Parent selection type doesn't exist")
	exit(1)
#RANDOM
def randomSelection(solutions,populationSize):
	
	p1,p2 = 0,0
	while(p1 == p2):
		p1 = random.randint(0, populationSize-1) 
		p2 = random.randint(0, populationSize-1) 

	return p1,p2 

#TOURNEY
def getNumCompetitors(populationSize):
	percentage = 0.15
	if(populationSize > 2/percentage):
		num = int(populationSize*percentage)
	else: 
		num = 2
	return num

def tournamentSelection(solutions,populationSize):
	p1,p2 = positive_infnity,positive_infnity
	numCompetitors = getNumCompetitors(populationSize)
	
	while(p1 == positive_infnity or p2 == positive_infnity):
		
		for _ in range(numCompetitors):
			c = random.randint(0,populationSize-1)
			
			if c < p1:
				p1 = c
			else:
				if c < p2 and c != p1:
					p2 = c

	
	return p1,p2

#######################################################################################
#STOPPING CONDITIONS
def shouldKeepGoing(maxTime,time,maxNonImprovingGens,nonImprovingGens):
	if(maxTime <= time):
		print("Maximum time reached: " + str(time) + " seconds")
		return False

	if(maxNonImprovingGens <= nonImprovingGens):
		print("Maximum number of non improving generations reached: " + str(nonImprovingGens))
		return False

	return True


########################################################################################
#POPULATION

#Initial solutions (correctly colored with any number of colors)
def getStartingPopulation(populationSize,graph):
	solutions = []
	for i in range(populationSize):
		solutions.append(Coloring(graph))
		startingPoint = random.randint(0,graph.numVertices-1)
		#Greedly color the graph starting at a random point
		solutions[i].colorGreedy(startingPoint)
	return solutions


def orderPopulationByScore(solutions,populationSize):
	solutions.sort(key=lambda s : s.getScore())
	return solutions


########################################################################################
#MUTATE
#what function should we use to getNumMutations?
def getNumMutations(graph):
	return int(graph.numVertices*0.25)

def mutate(solutionId,graph, solutions):
	
	#how many mutations
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