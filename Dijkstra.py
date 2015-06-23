#Dijkstra
from Graph import *

def dijkstra(G, s):

	initSingleSrc(G, s)
	path = []
	nodes = G.allNodes()
	
	while nodes != []:
		minNode = extractMin(nodes)
		path.append(minNode)
		for n in G.graphDic[minNode]:
			relaxation(G,minNode,n)
			
	return path
