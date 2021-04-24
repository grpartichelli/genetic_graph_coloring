
class Vertice():
	def __init__(self,weight):
		self.weight = weight
		self.neighbors = []

class Graph():
	

	def __init__(self, p):
		self.numVertices = p.numVertices;
		self.numEdges = p.numEdges;
		self.k = p.k;
		self.edges = []
		self.vertices = []

	
		for w in p.weights:
			self.vertices.append(Vertice(w));
	

	
		for e in p.edges:
			self.edges.append(e)
			self.vertices[e[0]].neighbors.append(e[1])
			self.vertices[e[1]].neighbors.append(e[0])
			
	

	def print(self):
	
	
		print("---------------------------------------------------------")
		print("Num Vertices: " + str(self.numVertices))
		print("Num Edges: " + str(self.numEdges))
		print("k: " + str(self.k))
		
		i=0
		for v in self.vertices:
			
			print("Vertice: " +  str(i) + " | Weight: " +str(v.weight))
			print("Connected to: {", end ="")
			
			for v2 in v.neighbors:
				print(str(v2) + ",", end="")
			
			print("}")
			i+=1;
		

