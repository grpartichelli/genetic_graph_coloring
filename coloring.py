

class Coloring:
	def __init__(self, g):
		self.score = -1;
		self.numColors = 0;
		self.k = g.k;

		self.colorOfVertice = [] #color of the vertice i

		self.numVerticesOfColor = [] #number of vertices with this color
		self.weightOfColor = [] #how many weight the sum of all vertices of this color has

		for i in range(g.numVertices): #colors are only numbers >= 0
			self.colorOfVertice.append(-1)
	



	def isValid(self):
		return self.numColors <= self.k;

	def print(self,printTheColors):
		print("Score: " + str(self.score) + " | Valid: " + str(self.isValid()) + " | Num Colors: " + str(self.numColors) + "| K: " + str(self.k) )
		print("---------------------------------------------------------")

		if(printTheColors):
			print("Coloring: {", end="")
			for color in enumerate(self.colorOfVertice):	
				print(str(color), end =",")
			print("}")


			print("Num Vertices and Weight Painted with Color: {", end="")
			for i in range(self.numColors):	
				print(str(self.numVerticesOfColor[i]) + " " + str(self.weightOfColor[i]) , end =",")
			print("}")

				
				
