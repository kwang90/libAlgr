'''
   ================== General Graph Definition ===================
'''
from Basic_Graph_Algorithms import *
from copy import *

#Graph Transformation
def toGraph(graphDclc, lambda_delay):
	G = Graph(deepcopy(graphDclc.graphDic))
	
	for k,v in G.graphDic.items():
		for n, metrics in v.items():
			if lambda_delay is INFINITE:
				# metric is only delay
				v[n] = metrics['delay']
			else:
				# metric is the combination of cost and delay
				v[n] = metrics['cost'] + lambda_delay * metrics['delay']
	return G

#LARAC
def algr_LARAC(G_dclc, src, dest, delay_constrain):

	pathC = dijkstra_pair(toGraph(G_dclc, 0), src, dest)
	
	for n in pathC.path:
		print('path C :', n.tag, n.distance, n.parent)
	
	if  pathCostDelay_dclc(G_dclc, pathC)[1] <= delay_constrain:
		print("least cost path", pathCostDelay_dclc(G_dclc, pathC)[1] )
		return pathC
		
	pathD = dijkstra_pair(toGraph(G_dclc, INFINITE), src, dest)
	if pathCostDelay_dclc(G_dclc, pathD)[1] > delay_constrain:
		print("No solution")
		return None
	
	while True:
		lam = (pathCostDelay_dclc(G_dclc, pathC)[0] - pathCostDelay_dclc(G_dclc, pathD)[0])/(pathCostDelay_dclc(G_dclc, pathD)[1] - pathCostDelay_dclc(G_dclc, pathC)[1])
		graphLam = toGraph(G_dclc, lam)
		r = dijkstra_pair(graphLam, src, dest)
		if pathCost(graphLam, r) == pathCost(graphLam, pathC):
			print("solution found")
			return pathD
		elif pathCostDelay_dclc(G_dclc, r) <= delay_constrain:
			pathD = r
			print("path d is r")
		else: 
			pathC = r
			print("path c is r")
		