# Benjamin Kellman
# 2/10/25


from collections import deque
def twoColor(g):
        v = [0 for n in g]
        color = [-1 for n in g]
        q = deque()
        q.append(0)
        v[0] = 1
        color[0]=0

        V = len(g)
        for u in range(1,V):
            for i in g[u]:
                if (color[i]!=-1):
                    v[color[i]]=True
                    
            cr = 0
            while cr < u:
                if (v[cr] == False):
                    break
                cr += 1
            if cr>1:
                return(False)
            color[u]=cr
            for i in g[u]:
                if (color[i]!=-1):
                    v[color[i]]= False
        return(True)


# n is gear amount
# m is gear pairs
n, m = map(int, input().split())

# gears is an adjacency array
# at index 
'''
[[1,2],[0,2],[0,1]]
at index 0 you have what gear 0 is adjacent to
ad index 1 you have what gear 1 is adjecent to
'''
'''
Sample input
4 3
0 1
1 3
0 2

True
'''
gears = [[] for i in range(n)]
for i in range(m):
    pair1, pair2 = map(int, input().split())
    gears[pair1].append(pair2)
    gears[pair2].append(pair1)

adjs = [[1,2],[0,2],[0,1]]
oth = [[1,2],[0,3],[0],[1]]
if (twoColor(gears)):
    print("Big money to come!")
else:
    print("Nothing to see here...")

if False:
    def addEdge(adj, v, w):
        
        adj[v].append(w)
        
        # Note: the graph is undirected
        adj[w].append(v)  
        return adj
    
    # Assigns colors (starting from 0) to all
    # vertices and prints the assignment of colors
    def greedyColoring(adj, V):
        
        result = [-1] * V
    
        # Assign the first color to first vertex
        result[0] = 0
    
    
        # A temporary array to store the available colors. 
        # True value of available[cr] would mean that the
        # color cr is assigned to one of its adjacent vertices
        available = [False] * V
    
        # Assign colors to remaining V-1 vertices
        for u in range(1, V):
            
            # Process all adjacent vertices and
            # flag their colors as unavailable
            for i in adj[u]:
                if (result[i] != -1):
                    available[result[i]] = True
    
            # Find the first available color
            cr = 0
            while cr < V:
                if (available[cr] == False):
                    break
                
                cr += 1
            if cr>1:
                print("bad")
                break
            # Assign the found color
            result[u] = cr 
    
            # Reset the values back to false 
            # for the next iteration
            for i in adj[u]:
                if (result[i] != -1):
                    available[result[i]] = False
    
        # Print the result
        for u in range(V):
            print("Vertex", u, " --->  Color", result[u])
    
    # Driver Code
    if __name__ == '__main__':
        
        g1 = [[] for i in range(4)]
        g1 = addEdge(g1, 0, 2)
        g1 = addEdge(g1, 1, 2)
        g1 = addEdge(g1, 0, 1)

        print(g1)
        print("Coloring of graph 1 ")
        greedyColoring(g1, 4)