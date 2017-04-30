#Dijkstra 
#Problem 6
#

#---------------C Code from http://infolab.stanford.edu/~ullman/fcsccode/fig9.44-47.txt -------------
'''''
void Dijkstra(GRAPH G, POT P, int *pLast)
{
	NODE u, v; /* v is the node we select to settle */
	LIST ps; /* ps runs down the list of successors of v;
			u is the successor pointed to by ps */

	initialize(G, P, pLast);
	while ((*pLast) > 1) {
		v = P[1];
		swap(1, *pLast, G, P);
		--(*pLast);
		bubbleDown(1, G, P, *pLast);
		ps = G[v].successors;
		while (ps != NULL) {
			u = ps->nodeName;
			if (G[u].dist > G[v].dist + ps->nodeLabel) {
				G[u].dist = G[v].dist + ps->nodeLabel;
				bubbleUp(G[u].toPOT, G, P);
			}
			ps = ps->next;
		}
	}
}
'''

#-----------------------------------------------------------------------------------

from collections import defaultdict
from heapq import * #heap = priority queue

def Dijkstra(graph, start, end):
    lst = defaultdict(list)

    for g,r,l in graph: #for graph, right, left values in graph
        lst[g].append((l,r))

    heap, seen = [(0,start,())], set() #x = starting point/exist. 

    while heap: #while there is something not seen
        (cost, v1, path) = heappop(heap) #apply 3 variables to the smallest item in heap
        if v1 not in seen: #check if first smallest variable hasn't been passed by
            seen.add(v1) #add it
            path = (v1, path) #create/add to the path count
            if v1 == end: #if everything is done
                return(cost, path) #return first and last
            
            for l, v2 in lst.get(v1,()): #for left and v2(imagine it is i=0, a new var) inside the list
                if v2 not in seen: #if that v2 not seen
                    heappush(heap, (cost+l, v2, path)) #push value item onto heap by 
                    

    return float("inf")

if __name__=="__main__":
    graph = [ #A=1, B=2, C=3, D=4, E=5, F=6
        ("A","B", 4),
        ("A","C", 1),
        ("A","D", 5),
        ("A","E", 8),
        ("A","F", 10),
        ("C","B", 2),
        ("D","E", 2),
        ("E","F", 1)
    ]

    print "-----------Dijkstra---------------"
    print graph
    print "Test, A to E"
    print Dijkstra(graph, "A", "E")