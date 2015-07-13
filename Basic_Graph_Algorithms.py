'''=== Graph Algorithms ==='''
from Graph import *

#Dijkstra
def dijkstra(G, s):
	initSingleSrc(G, s)
	nodes = G.allNodes()
	
	while nodes != []:
		minNode = extractMin(nodes)
		for n in G.graphDic[minNode]:
			relaxation(G,minNode,n)
			
	return True

#Bellman-Ford
def bellman_ford(G,s):
	initSingleSrc(G, s)
	
	for i in range(1, len(G.allNodes())-1):
		for k,linkDic in G.graphDic.items():
			for k2,weight in linkDic.items():
				relaxation(G, k, k2)
				
	for k,linkDic in G.graphDic.items():
			for k2,weight in linkDic.items():
				if k2.distance > k.distance + weight:
					return False
	
	return True

	
#Dijkstra Single Pair
def dijkstra_pair(G, s, dest):
	initSingleSrc(G, s)	
	nodes = G.allNodes()

	while nodes != []:
		minNode = extractMin(nodes)

		if minNode.tag == dest.tag:
			path = [dest]
			pre = dest
			while pre.parent != None:
				pre = pre.parent
				path.insert(0,pre)
			p = Path(path)
			p.cost = pathCost(G, p)
			return p
		for n in G.graphDic[minNode]:
			relaxation(G,minNode,n)
	return None

#LamdaCost of a path
def pathCost(graph, p):
	costLam = 0
	for it in iter(p.path):
		costLam =  costLam + it.distance
	return costLam
	
	
#Cost & Delay of a path
def pathCostDelay_dclc(graph_dclc, p):
	cost = 0
	delay = 0 
	for it in reversed(p.path):
		if it.parent != None:
			cost = cost + graph_dclc.graphDic[it][it.parent]['cost']
			delay = delay + graph_dclc.graphDic[it][it.parent]['delay']
	return (cost, delay)
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
	if n2.distance > (n1.distance + G.getWeight(n1, n2)) and n1.parent != n2:
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
