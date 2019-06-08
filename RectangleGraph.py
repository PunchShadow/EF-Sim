import networkx as nx
import math
import sys

# Initialize the graph
# arg[0] = dimension (determine how many arguments are there)
# arg[1] = first argument (row)
# arg[2] = second argument (column)
# arg[3] .....
# Default: Undirected graph
# <<NOTICE>>: allow 2D and 3D only !!!!

def createRecGraph(*arg):
    # Exception control
    if((len(arg) != (arg[0]+1)) or (arg[0] == 1)):
        print("Initialization fault !! Please check your argument numbers!")
        sys.exit(1)
    G = nx.Graph()
    G.add_node('G') # Global buffer's node
    node_num = 1
    
    for i in range(arg[0]):
        node_num *= arg[i+1]
    for i in range(node_num):
        G.add_node(i);
    
    # Initialize the edges of all nodes.
    # 2D matrix
    if(arg[0] == 2):
        for i in range(node_num-1):
            G.add_edge(i, 'G')
            row = math.floor(i/arg[2])
            col = i%arg[2]
            if(col+1 <= arg[2]-1):
                G.add_edge(i, i+1)
            if(row+1 <= arg[1]-1):
                G.add_edge(i, i+arg[2])

        G.add_edge(node_num-1, 'G')
    # 3D matrix
    elif(arg[0] == 3):
        plane_num = arg[1]*arg[2] #One plane's node number.
        for i in range(node_num-1):
            G.add_edge(i, 'G')
            row = math.floor((i%plane_num)/arg[2])
            col = (i%plane_num)%arg[2]
            height = math.floor(i/plane_num)
           
            if(col+1 <= arg[2]-1):
                G.add_edge(i, i+1)
            if(row+1 <= arg[1]-1):
                G.add_edge(i, i+arg[2])
            if(height+1 <= arg[3]-1):
                G.add_edge(i, i+plane_num)
        G.add_edge(node_num-1, 'G')
    else:
        print("Dimension Error!!!")
        sys.exit(2)
    
    
    return G


# edgelist example: [(2,3), (1,4), (3,9), ....]
def addGroup(graph, group, *edgelist):
    graph.add_edges_from(edgelist, group = group)



