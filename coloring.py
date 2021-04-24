

class Coloring:
	def __init__(self, g):
		self.score = -1;
		self.numColors = 0;
	
		self.graph = g;

		self.colorOfVertice = [] #color of the vertice i
		

		self.numVerticesOfColor = [] #number of vertices with this color
		self.weightOfColor = [] #how many weight the sum of all vertices of this color has

		for i in range(g.numVertices): #colors are only numbers >= 0
			self.colorOfVertice.append(-1)


	


	def findSmallestColorNotUsedByNeighbors(self, verticeId):
	
		neighborColor = 0;

		#array of colors starting at 0
		colors = [0] * self.numColors

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
		return self.createNewColor()
		

	def swapColors(self,v,oldColor,newColor):
		self.uncolorVertice(v,oldColor)
		self.colorVertice(v,newColor)


	def fixColors(self):
		#Remap the colors in such way as to remove useless colors	
		colormap = {}
		color = 0
		for i in range(self.graph.numVertices):
				
			if self.colorOfVertice[i] not in colormap:
				colormap[self.colorOfVertice[i]] = color
				color+= 1
			self.swapColors(i,self.colorOfVertice[i],colormap[self.colorOfVertice[i]])
		


		i=0
		#Remove useless colors
		while i < self.numColors:
			if(self.numVerticesOfColor[i] == 0):
				self.numVerticesOfColor.pop(i)
				self.weightOfColor.pop(i)
				self.numColors -= 1
				print("popped")
			i+=1
			

	def uncolorVertice(self,verticeId, color):
		#self.colorOfVertice[verticeId] = -1

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
		
			vColor = self.findSmallestColorNotUsedByNeighbors(i)
			self.colorVertice(i, vColor)
			
			
			i+=1
			#iterate as circular
			if i == self.graph.numVertices:
				i = 0
			
			
			count+=1;

	#THIS SHOULD NOT BE USED ON THE ALGORITHM, ONLY FOR TESTING
	def isColoringValid(self):
		for e in self.graph.edges:
			if self.colorOfVertice[e[0]] == self.colorOfVertice[e[1]]:
				return False
		return True


	#Check is a valid solution for our proble
	def isValid(self):
		return self.numColors <= self.graph.k;


	def print(self,printTheColors):

		print("Score: " + str(self.score) + " | Valid: " + str(self.isValid()) + " | Num Colors: " + str(self.numColors) + "| K: " + str(self.graph.k) )
		print("---------------------------------------------------------")

		if(printTheColors):
			print("Coloring: {", end="")
			for color in enumerate(self.colorOfVertice):	
				print(str(color), end =",")
			print("}\n")



			print("Num Vertices and Weight Painted with Color: {", end="")
			for i in range(self.numColors):	
				print("Color: " + str(i) + " Vertices: " + str(self.numVerticesOfColor[i]) + " Weight" + str(self.weightOfColor[i]) , end =",")
			print("}")

				
				
