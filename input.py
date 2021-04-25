import sys

NUM_ARGUMENTS = 4
def getTerminalInput():
	# total arguments
	if(len(sys.argv)-1 != NUM_ARGUMENTS):
		print("ERROR: Please use the command: python main.py <pathToInputFile> <population> <crossOverRate> <mutationRsate>")
		exit(1);

	pathToInputFile = sys.argv[1]

	try:
		population = int(sys.argv[2])
	except:
		print("Please enter a valid population number")
		exit(1)

	try:
		crossOverRate = float(sys.argv[3])
		if(crossOverRate < 0 ):
			crossOverRate = 0
		if(crossOverRate > 1):
			crossOverRate = 1

	except:
		print("Please enter a valid crossOverRate number")
		exit(1)

	try:
		mutationRate = float(sys.argv[4])
		if(mutationRate < 0 ):
			mutationRate = 0
		if(mutationRate > 1):
			mutationRate = 1
	except:
		print("Please enter a valid mutationRate number")
		exit(1)

	return pathToInputFile,population,crossOverRate,mutationRate




class ReadInput():
	
	numVertices = 0
	numEdges = 0
	k = 0
	weights = []
	edges = []

	def __init__(self, pathToInput):

		try:
			f = open(pathToInput, "r")
		except IOError:
			print("Could not open this file: " + pathToInput)
			exit(1)

		cout = 0 
		for line in f:
			split = line.strip().split(" ")
			if cout == 0:
				self.numVertices = int(split[0])
				self.numEdges =  int(split[1])
				self.k =  int(split[2])
				
			if cout == 1:
				for w in split:
					self.weights.append(float(w))

			if cout > 1:
				if(split != ['']):
					self.edges.append( ( int(split[0]), int(split[1]) ) )



			cout+= 1
		
		
		f.close()



