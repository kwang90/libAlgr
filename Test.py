#Testing
from Basic_Graph_Algorithms import *
from LARAC import *

#Print Result
def printResult(algrName,aGraph):
	print(algrName,"--->")
	for n in aGraph.allNodes():
		if n.parent is None:
			print (n.tag, n.distance, n.parent)
		else: 
			print (n.tag, n.distance, n.parent.tag)

def printPaths(pathStack):
	print("---> path: ")
	for p in pathStack:
		if p.parent is None:
			print(p.tag, p.distance)
		else:
			print(p.tag, p.distance, p.parent.tag) 


#Initialization
s = Node('S')
t = Node('T')
x = Node('X')
y = Node('Y')
z = Node('Z')

graph = {s:{t:10, y:5},
		 t:{y:2, x:1}, 
		 x:{z:4},
		 y:{t:3,x:9,z:2},
		 z:{s:7,x:6}}
G = Graph(graph)

graph2 = {s:{t:6, y:7},
		 t:{y:8, x:5,z:-4}, 
		 x:{t:-2},
		 y:{x:-3,z:9},
		 z:{s:2,x:7}}
G2 = Graph(graph2)

'''
#Dijkstra testing
dijkstra(G,s)

#printResult('Dijkstra',G)
pathStack = dijkstra_pair(G,s,x)

#Bellman-Ford testing
bellman_ford(G2,s)
'''
#=======================================================================================================

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

graph3 = {  a:{	b:{'cost':1, 'delay':4}, d:{'cost':16, 'delay':2 }},#c:{'cost':4, 'delay':3}, 
			b:{	a:{'cost':1, 'delay':4}, c:{'cost':2, 'delay':1}, d:{'cost':1, 'delay':8 }},
			c:{ b:{'cost':2, 'delay':1}, d:{'cost':4, 'delay':3 }},#a:{'cost':4, 'delay':3},
			d:{	a:{'cost':16, 'delay':2}, b:{'cost':1, 'delay':8}, c:{'cost':4, 'delay':3 }}}			
G3 = GraphDCLC(graph3)

#LARAC testing
p = algr_LARAC(G3, a, c, 10)
printPaths(p.path)