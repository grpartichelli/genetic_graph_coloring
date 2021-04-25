from math import ceil,log10

class Coloring:


	def __init__(self, g):
		self.numColors = 0;
		self.score = 0
		
		self.graph = g;

		self.colorOfVertice = [] #color of the vertice i
		
		self.numVerticesOfColor = [] #number of vertices with this color
		self.weightOfColor = [] #how many weight the sum of all vertices of this color has

		for i in range(g.numVertices): #colors are only numbers >= 0
			self.colorOfVertice.append(-1)

		self.sumWeights = 0
		for v in self.graph.vertices:
			self.sumWeights += v.weight

		self.sumWeights = pow(10,ceil(log10(self.sumWeights))) #making a power of 10 so its easier to visualize

	##############################################
	#create a copy of this solution
	def createCopy(self):
		c = Coloring(self.graph)
	
		
		c.score =self.score

		c.colorOfVertice = self.colorOfVertice[:]

		c.numColors = self.numColors
		c.weightOfColor =  self.weightOfColor[:]
		c.numVerticesOfColor = self.numVerticesOfColor[:]
		
		return c

		
	########################################################
	#SCORE
	def getScore(self):

		
		if(self.isValid()):
			self.score = max(self.weightOfColor)
		else:
			self.score = self.calculatePunishment()
	

		return self.score

	#calculate punishment	
	def calculatePunishment(self):
		punish = 0
		for i in range(self.graph.k,self.numColors):
			punish += self.sumWeights #diffenciate between k levels and always be bigger then any weight
			punish += self.numVerticesOfColor[i] #differenciate between num of vertices
			
		return punish
		

	
	########################################################
	#COLORING

	def swapColors(self,v,newColor):
		self.uncolorVertice(v)
		self.colorVertice(v,newColor)


	def uncolorVertice(self,verticeId):
		

		color = self.colorOfVertice[verticeId]

		self.weightOfColor[color] -= self.graph.vertices[verticeId].weight
		
		if(self.weightOfColor[color] <= 0.000001):
			self.weightOfColor[color] = 0

		self.numVerticesOfColor[color] -= 1
		
		
		

	def colorVertice(self,verticeId, color):
		
		

		while(self.numColors <= color):
			self.createNewColor()
		
		#now let's color it
		self.colorOfVertice[verticeId] = color
		self.weightOfColor[color] += self.graph.vertices[verticeId].weight
		self.numVerticesOfColor[color] += 1
		
		

	def createNewColor(self):
	
		newColor = self.numColors;
		
		
		self.numColors+=1;
		self.numVerticesOfColor.append(0);

		self.weightOfColor.append(0);

		return newColor


	#greedly color the graph
	def colorGreedy(self,start):
		
		count = 0	
		i = start
		while count < self.graph.numVertices:
		
			vColor = self.findSmallestColorNotUsedByNeighbors(i,False)
			self.colorVertice(i, vColor)
			
			
			i+=1
			#iterate as circular
			if i == self.graph.numVertices:
				i = 0
			
			
			count+=1;

	#Keeping colored ordered correctly
	def fixColors(self):
	

		#Remap the colors in such way as to remove useless colors	
		colormap = {}
		color = 0
		for i in range(self.graph.numVertices):
				
			if self.colorOfVertice[i] not in colormap:
				colormap[self.colorOfVertice[i]] = color
				color+= 1
			self.swapColors(i,colormap[self.colorOfVertice[i]])
		


		i=0
		#Remove useless colors
		while i < self.numColors:
			if(self.numVerticesOfColor[i] == 0):
				self.numVerticesOfColor.pop(i)
				self.weightOfColor.pop(i)
				self.numColors -= 1
			i+=1

	##############################################################
	#VALIDATION
	#THIS SHOULD NOT BE USED ON THE ALGORITHM, ONLY FOR TESTING
	def isColoringValid(self):
		for e in self.graph.edges:
			if self.colorOfVertice[e[0]] == self.colorOfVertice[e[1]]:
				return False
		return True


	#Check is a valid solution for our problem
	def isValid(self):
		return self.numColors <= self.graph.k;

		########################################################
	#SEARCH
	def search(self,color):
		for v in range(self.graph.numVertices):
			if self.colorOfVertice[v] == color:
				if self.isValid():
					self.swapColors(v,self.findLeastWeightColorNotUsedByNeighbors(v,True))
				else:
					self.swapColors(v,self.findSmallestColorNotUsedByNeighbors(v,True))
		
		self.fixColors()


	##############################################################
	#FINDING NEIGHBORS
	def findSmallestColorNotUsedByNeighbors(self, verticeId,tryToGetNewColor):

		neighborColor = 0;

		#array of colors starting at 0
		colors = [0] * self.numColors

		#not allowing to pick same color (for mutations)
		if tryToGetNewColor:
			colors[self.colorOfVertice[verticeId]] = 1

		#Set colors to 1 if a neighbor is using it
		for neighbor in self.graph.vertices[verticeId].neighbors:
			neighborColor = self.colorOfVertice[neighbor]

			if(neighborColor != -1):
				colors[neighborColor] = 1

		

		#Search for a non set color
		for i in range(self.numColors):
			if colors[i] == 0:
				return i

			
		
		#If it gets here all colors are used
		if tryToGetNewColor: #Failed to get new color, let's set to the old color instead of creating a new one
			return self.colorOfVertice[verticeId]
		else:	
			return self.createNewColor()	

	def findLeastWeightColorNotUsedByNeighbors(self, verticeId,allowSameColor):

		neighborColor = 0;

		#array of colors starting at 0
		colors = [0] * self.numColors

		#not allowing to pick same color (for mutations)
		if not allowSameColor:
			colors[self.colorOfVertice[verticeId]] = 1

		#Set colors to 1 if a neighbor is using it
		for neighbor in self.graph.vertices[verticeId].neighbors:
			neighborColor = self.colorOfVertice[neighbor]

			if(neighborColor != -1):
				colors[neighborColor] = 1

		
		color = -1
		mincolor = 100000000000000000
		#Search for a non set color
		for i in range(self.numColors):
			if colors[i] == 0:
				if self.weightOfColor[i] < mincolor:
					mincolor = self.weightOfColor[i]
					color = i
		
		if color != -1:
			return color

		#If it gets here all colors are used
		if not allowSameColor: #allowing the same color to avoid growing
			return self.colorOfVertice[verticeId]
		else: 
			return self.createNewColor()	


	
	#########################################################################
	#PRINT
	def print(self,printTheColors):
		s = self.getScore()
		print("Score: " + str(round(s,2)) + " | Valid Solution: " + str(self.isValid()) + " | Num Colors: " + str(self.numColors) + " | K: " + str(self.graph.k) )
		print("---------------------------------------------------------------------------")
		if(printTheColors):
			print("Coloring: {", end="")
			for color in enumerate(self.colorOfVertice):	
				print(str(color), end =",")
			print("}\n")



			print("Num Vertices and Weight Painted with Color: {", end="")
			for i in range(self.numColors):	
				print("Color: " + str(i) + " Vertices: " + str(self.numVerticesOfColor[i]) + " Weight" + str(self.weightOfColor[i]) , end =",")
			print("}")


	def smallprint(self):

		print(" Score: " + str(round(self.getScore(),3)) +" | Num Colors: " + str(self.numColors), end ="" )		


	