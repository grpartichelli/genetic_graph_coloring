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