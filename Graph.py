'''
   ================== General Graph Definition ===================
'''
INFINITE = 10000
def printPaths(pathStack):
	print("---> path: ")
	for p in pathStack:
		if p.parent is None:
			print(p.tag, p.distance)
		else:
			print(p.tag, p.distance, p.parent.tag)
			
def printGraphDic(G):
	for k,v in G.graphDic.items():
		print('======>')
		for n, c in v.items():
			print('......', k.tag,n.tag,c)

#Basic Graph definition
class Graph:	
	'''an example of the adjacency list of a weighted graph
		e.g.: graph = {'n1':{'n2':3,
							'n3':4}},
					  'n2':{'n1':3,
							'n3':2}},
					  'n3':{'n1':4,
							'n2':2}}}
	'''	
	def __init__(self, graph):
		self.graphDic = graph
		
	def getWeight(self,n1,n2):
		if self.graphDic != None:
			w = self.graphDic[n1][n2]
			return w
		else:
			return 'No link exists between them'
	
	def allNodes(self):
		return list(self.graphDic.keys())
		
#Graph for DCLC problems
class GraphDCLC(Graph):
	'''an example of the adjacency list of a DCLC graph
		e.g.: graph = {'n1':{'n2':{'cost':2, 'delay':3}}
							'n3':{'cost':3, 'delay':2}}},
					  'n2':{'n1':{'cost':4, 'delay':1},
							'n3':{'cost':5, 'delay':1}}},
					  'n3':{'n1':{'cost':3, 'delay':2},
							'n2':{'cost':2, 'delay':5}}}}
	'''	
	# def __init__(self, graphDCLC):
		# self.graphDic = graphDCLC		
	

#Node definition
class Node:
	def __init__(self, tag):
		self.tag = tag
		self.parent = None
		self.distance = INFINITE

#Path definition
class Path:
	def __init__(self, p):
		self.path = p
		self.cost = 0
'''============================================================'''
