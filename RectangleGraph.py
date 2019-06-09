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
        G.add_node(i)
    
    # Initialize the edges of all nodes.
    # 2D matrix
    if(arg[0] == 2):
        for i in range(node_num):
            G.add_edge('G',i, gid=0, energy=2.0)
            row = i//arg[2]
            col = i%arg[2]
            if(col+1 < arg[2]):
                G.add_edge(i, i+1, gid=1, energy=0.5)
            if(row+1 < arg[1]):
                G.add_edge(i, i+arg[2], gid=2, energy=0.5)

    # 3D matrix
    elif(arg[0] == 3):
        plane_num = arg[1]*arg[2] #One plane's node number.
        for i in range(node_num):
            G.add_edge('G', i, gid=0, energy=2.0)
            row =(i%plane_num)//arg[2]
            col = (i%plane_num)%arg[2]
            height = i//plane_num
            if(col+1 < arg[2]):
                G.add_edge(i, i+1, gid=1, energy=0.5)
            if(row+1 < arg[1]):
                G.add_edge(i, i+arg[2], gid=1, energy=0.5)
            if(height+1 < arg[3]):
                G.add_edge(i, i+plane_num, gid=1, energy=0.5)

    else:
        print("Dimension Error!!!")
        sys.exit(2)

    return G

def eyeriss(config): #12*14
    G = nx.Graph()
    G.add_node('G') # Global buffer's node
    for i in range(12*14):
        G.add_node(i)
    for j in range(14):
        for i in range(12):
            v=i*14+j
            G.add_edge('G', v, gid=i, energy=0.5) # filter edge
            G.add_edge('G', v, gid=12+config[i][j], energy=1.0) # imap edge
            if(i!=0):
                G.add_edge(v, v-14, gid=50, energy=1.0) # omap edge


# edgelist example: [(2,3), (1,4), (3,9), ....]
def addGroup(graph, group, *edgelist):
    graph.add_edges_from(edgelist, group = group)

G = createRecGraph(2,5,5)