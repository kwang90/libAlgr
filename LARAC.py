'''
   ================== General Graph Definition ===================
'''
from Basic_Graph_Algorithms import *
from copy import *

#Graph Transformation
def toGraph(graphDclc, lambda_delay):
	dic = {}
	G = Graph(dic)
	
	for k,v in graphDclc.graphDic.items():
		dic[k] = {}
		for n, metrics in v.items():
			if lambda_delay is INFINITE:
				# metric is only delay
				dic[k][n] = metrics['delay']
			else:
				# metric is the combination of cost and delay
				dic[k][n] = metrics['cost'] + lambda_delay * metrics['delay']
	return G

#LARAC
def algr_LARAC(G_dclc, src, dest, delay_constrain):

	pathC = dijkstra_pair(toGraph(G_dclc, 0), src, dest)

	if  pathCostDelay_dclc(G_dclc, pathC)[1] <= delay_constrain:
		print("least cost path", pathCostDelay_dclc(G_dclc, pathC))
		return pathC
		
	pathD = dijkstra_pair(toGraph(G_dclc, INFINITE), src, dest)
	print('path d : ')
	printPaths(pathD.path)

	if pathCostDelay_dclc(G_dclc, pathD)[1] > delay_constrain:
		print("No solution")
		return None
		
	while True:
		print('*************************** new loop ********************')
		lam = (pathCostDelay_dclc(G_dclc, pathC)[0] - pathCostDelay_dclc(G_dclc, pathD)[0])/(pathCostDelay_dclc(G_dclc, pathD)[1] - pathCostDelay_dclc(G_dclc, pathC)[1])
		r = dijkstra_pair(graphLam, src, dest)
		printGraphDic(G_dclc)
		print(pathCostDelay_dclc(G_dclc, pathC), pathCostDelay_dclc(G_dclc, pathD), 'lamda : ',lam)
		printPaths(r.path)
		if pathCost(graphLam, r) == pathCost(graphLam, pathC):
			print("solution found")
			return pathD
		elif pathCostDelay_dclc(G_dclc, r)[1] <= delay_constrain:
			pathD = r
			print("path d is r")
		else: 
			pathC = r
			print("path c is r")
		