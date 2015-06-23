#Testing
from Graph import * ### not necessary ###
from Dijkstra import *
from Bellman_Ford import *

#Print Result
def printResult(algrName,aGraph):
	print(algrName,"--->")
	for n in aGraph.allNodes():
		if n.parent is None:
			print (n.tag, n.distance, n.parent)
		else: 
			print (n.tag, n.distance, n.parent.tag)

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

#Dijkstra testing
dijkstra(G,s)
printResult('Dijkstra',G)

#Bellman-Ford testing
bellman_ford(G2,s)
printResult('Bellman-Ford',G2)
