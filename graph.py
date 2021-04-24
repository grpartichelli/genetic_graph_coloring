
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
			
	
	def bfs(self, start):
		vertice_levels = [-1]*self.numVertices
		edges_of_level = []

		flag = True
		level = 0
		#vizinhos começam como sendo só o inicial
		neighbors = [start]
		0
		while flag:
			num_edges = 0
			#para cada vizinho marca ele como tendo o nivel atual
			for n in neighbors:
				vertice_levels[n] = level
			
			
			new_neighbors = []
			#adiciona como sendo novos vizinhos os vizinhos antigos que não foram visitados ainda
			flag = False
			for old_n in neighbors:
				for new_n in self.vertices[old_n].neighbors:
					if vertice_levels[new_n] == -1:
						vertice_levels[new_n] = 0 #temporarly
						new_neighbors.append(new_n)
						num_edges+= 1
						flag = True
			
			neighbors = new_neighbors
			edges_of_level.append(num_edges)
			level+= 1

		
		#print(vertice_levels)
		print(self.numVertices)
		print(edges_of_level)



	def print(self,printVertices):
	
	
		print("---------------------------------------------------------")
		print("Num Vertices: " + str(self.numVertices))
		print("Num Edges: " + str(self.numEdges))
		print("k: " + str(self.k))
		
		i=0
		if(printVertices):
			for v in self.vertices:
				
				print("Vertice: " +  str(i) + " | Weight: " +str(v.weight))
				print("Connected to: {", end ="")
				
				for v2 in v.neighbors:
					print(str(v2) + ",", end="")
				
				print("}")
				i+=1;
		

