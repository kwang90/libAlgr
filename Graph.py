'''
   ================== General Graph Definition ===================
'''
INFINITE = 10000

#Graph definition
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

#Node definition
class Node:
	def __init__(self, tag):
		self.tag = tag
		self.parent = None
		self.distance = INFINITE

'''============================================================'''
		
'''
   ================= Single Source Shortest Path =================
'''
#Initialization
def initSingleSrc(G, nodeO):
	for n in G.allNodes():
		n.distance = INFINITE
		n.parent = None
	nodeO.distance = 0
	
#Relaxation
def relaxation(G, n1, n2):
	if n2.distance > (n1.distance + G.getWeight(n1, n2)):
		n2.distance = n1.distance + G.getWeight(n1, n2)
		n2.parent = n1

#Min node in List
def extractMin(nodeQ):
	if nodeQ is None:
		return None
	else: 
		nodeQ.sort(key = lambda n:n.distance)
		return nodeQ.pop(0)
		
'''============================================================'''
