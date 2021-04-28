import random
import copy
from coloring import Coloring
import time

positive_infnity = float('inf')

def geneticSolve(graph,separators,populationSize, elitism, crossOverRate,mutationRate, maxTime , maxNonImprovingGens):
	startTime = time.time()
	separatorsSize = len(separators)

	solutions = getStartingPopulation(populationSize,graph)
	nonImprovingGens = 0
	bestScore = positive_infnity
	print("---------------------------------------------------------------------------")
	#START ALGORITHM
	while shouldKeepGoing(maxTime, time.time() - startTime, maxNonImprovingGens,nonImprovingGens):
		#Get the best solution
		solutions = orderPopulationByScore(solutions,populationSize)

		#Display it
		#solutions[0].print(False)

		#Check if there was improvement
		if(bestScore <= solutions[0].getScore()):
			nonImprovingGens+= 1
			print(nonImprovingGens)
			print("Execution Time: " + str(round(time.time() - startTime,2)) + "s")
			print(solutions[0].numVerticesOfColor)
			solutions[0].print(False)
		else:
			bestScore = solutions[0].getScore()
			nonImprovingGens = 0
			print("Execution Time: " + str(round(time.time() - startTime,2)) + "s")
			print(solutions[0].numVerticesOfColor)
			solutions[0].print(False)


		#Elitism preserves the <elitism> first solutions
		newSolutions = []
		for i in range(0,elitism):
			newSolutions.append(copy.deepcopy(solutions[i])) #deepcopy is easier


		#The rest of the solutions will be created by a crossover
		for i in range(elitism,populationSize):
			#EXECUTE CROSSOVER
			p1,p2 = selectParents(solutions,populationSize,"random")
			if(random.uniform(0,1) < crossOverRate):
				newSolutions.append(crossover(p1,p2,graph,solutions,separators,separatorsSize))
			else:
				newSolutions.append(copy.deepcopy(solutions[p1])) #melhor entre os dois
			#EXECUTE MUTATION
			#mutate(i, graph, solutions)

			#TRY TO FIND BETTER COLORING
			#for c in range(newSolutions[i].numColors):
			#newSolutions[i].search(c)
		solutions = newSolutions
		for solution in solutions:
			solution.print(False)
		nonImprovingGens+=1




########################################################################################
#MUTATE
#what function should we use to getNumMutations?
def getNumMutations(graph):
	return int(graph.numVertices)

def new_mutate(solutionId, solutions,graph, mutationRate):
	""" Mutate in the old fashion way"""
	for i in range(graph.numVertices):
		newColor = random.randint(0, solutions[solutionId].numColors)
		if random.uniform(0,1) < mutationRate:
			if newColor not in solutions[solutionId].restrictedColors[i]:
				solutions[solutionId].swapColors(i, newColor)


def mutate(solutionId,graph, solutions):
	#how many mutations
	numMutations=getNumMutations(graph)

	for _ in range(numMutations):
		#change color of a random vertice:
		i = random.randint(0, graph.numVertices-1)

		if(solutions[solutionId].isValid()):
			newColor = solutions[solutionId].findLeastWeightColorNotUsedByNeighbors(i,False)
		else:
			newColor = solutions[solutionId].findSmallestColorNotUsedByNeighbors(i,False)
		solutions[solutionId].swapColors(i,newColor)

		#solutions[solutionId].fixColors()

########################################################################################
#CROSSOVER

#p1 = parent 1
#p2 = parent 2
def crossover(p1,p2,graph,solutions,separators,separatorsSize):
	#randomly choose what separator will be used
	separator = separators[random.randint(0,separatorsSize-1)]

	#Create copy of first parent
	son = copy.deepcopy(solutions[p1])

	randomPoint = random.randint(0, graph.numVertices)
	#mustFix = []
	for v in range(0, randomPoint):

		#if separator[v] == 0: #will go to another available color
			if solutions[p2].colorOfVertice[v] not in son.restrictedColors[v]:
				son.swapColors(v, solutions[p2].colorOfVertice[v])
			#mustFix.append(v)

		#if separator[v] == 1: #will go to parent 1 Not needed since we made a copy of parent 1
			#solutions[son].swapColors(v, solutions[p1].colorOfVertice[v])
		#if separator[v] == 2: #will go to parent 2
		#son.swapColors(v, solutions[p2].colorOfVertice[v])
#		for v in mustFix:
#			if(son.isValid()):
#				color = son.findLeastWeightColorNotUsedByNeighbors(v,True)
#			else:
#				color = son.findSmallestColorNotUsedByNeighbors(v,True)
#			son.swapColors(v, color)
#		son.fixColors()

	return son

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
	percentage = 0.25
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
		print("Maximum number of non improving generations reached: " + str(nonImprovingGens-1))
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
		solutions[i].restrictedColors
	return solutions


def orderPopulationByScore(solutions,populationSize):
	solutions.sort(key=lambda s : s.getScore())
	return solutions
