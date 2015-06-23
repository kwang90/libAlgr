#Bellman-Ford
from Graph import *

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
	