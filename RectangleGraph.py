import networkx as nx
import configparser as config
import math
import sys

config = config.ConfigParser()
config.read('config/network.cfg')

PE = 'PENode'
Mem = 'MemoryNode'
Bus = 'Bus'
Global = 'DRAM'

PE_sram = float(config.get(PE, 'SRAMsize'))
PE_energy = float(config.get(PE, 'EnergyCost'))
PE_cycle = float(config.get(PE, 'ComputTime'))
Mem_dram = float(config.get(Mem, 'DRAMsize'))
Mem_energy = float(config.get(Mem, 'EnergyCost'))
Mem_cycle = float(config.get(Mem, 'TransferTime'))
Bus_cycle = float(config.get(Bus, 'Latency'))
Bus_energy = float(config.get(Bus, 'EnergyCost'))
Global_dram = float(config.get(Global, 'DRAMsize'))
Global_energy = float(config.get(Global, 'EnergyCost'))
Global_cycle = float(config.get(Global, 'TransferTime'))

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
    G = nx.MultiDiGraph()
    G.add_node('G', type = 'Memory') # Global buffer's node
    node_num = 1

    for i in range(arg[0]):
        node_num *= arg[i+1]
    for i in range(node_num):
        G.add_node(i, type = 'PE')

    # Initialize the edges of all nodes.
    # 2D matrix
    if(arg[0] == 2):
        for i in range(node_num):
            G.add_edge('G',i, gid=0, energy=Global_energy, time=Global_cycle)
            row = i//arg[2]
            col = i%arg[2]
            if(col+1 < arg[2]):
                G.add_edge(i, i+1, gid=1, energy=Bus_energy, time=Bus_cycle)
            if(row+1 < arg[1]):
                G.add_edge(i, i+arg[2], gid=2, energy=Bus_energy, time=Bus_cycle)

    # 3D matrix
    elif(arg[0] == 3):
        plane_num = arg[1]*arg[2] #One plane's node number.
        for i in range(node_num):
            G.add_edge('G', i, gid=0, energy=Global_energy, time=Global_cycle)
            row =(i%plane_num)//arg[2]
            col = (i%plane_num)%arg[2]
            height = i//plane_num
            if(col+1 < arg[2]):
                G.add_edge(i, i+1, gid=1, energy=Bus_energy, time=Bus_cycle)
            if(row+1 < arg[1]):
                G.add_edge(i, i+arg[2], gid=1, energy=Bus_energy, time=Bus_cycle)
            if(height+1 < arg[3]):
                G.add_edge(i, i+plane_num, gid=1, energy=Bus_energy, time=Bus_cycle)

    else:
        print("Dimension Error!!!")
        sys.exit(2)

    return G

def eyeriss(row_id,col_id): #12*14
    G = nx.MultiDiGraph()
    G.add_node('G', type = 'Memory') # Global buffer's node
    for i in range(12*14):
        G.add_node(i, type= 'PE')
    for j in range(14):
        for i in range(12):
            v=i*14+j
            G.add_edge('G', v, gid=i, energy=Bus_energy, time=Bus_cycle) # filter edge
            G.add_edge('G', v, gid=12+col_id[i][j]+row_id[i]*32, energy=1.0, time=0.4) # imap edge
            if(i!=0):
                G.add_edge(v, v-14, gid=400, energy=1.0, time=0.3) # omap edge
    return G

def arrayToGraph(array):
    G = nx.MultiDiGraph()
    G.add_node('G', type = 'Memory') # Global buffer's node
    l=len(array)
    for i in range(l):
        G.add_node(i, type = 'PE')
    for i in range(l):
        for j in range(l):
            if type(array[i][j])==list:
                for x in array[i][j]:
                    G.add_edge(i, j, gid=x, energy=Bus_energy, time=Bus_cycle)
            elif array[i][j]==None:
                continue
            else:
                G.add_edge(i, j, gid=int(array[i][j]), energy=Bus_energy, time=Bus_cycle)
    return G

# Turn the graph to adjacency matrix with the edge's gid by using 3D list.
def graph2Array(G):
    relation = []
    for node in range(MG.number_of_nodes()-1):
        rel = []
        for i in range(MG.number_of_nodes()-1):
            if i in MG.successors(node):
                # If there're more than two edges connected.
                if(len(MG[node][i])>1):
                    extra = []
                    for j in range(len(MG[node][i])):
                        extra.append(MG[node][i][j]['gid'])
                    rel.append(extra)
                else:
                    rel.append(MG[node][i][0]['gid'])
            else:
                rel.append(0)

        relation.append(rel)
    return(relation)

# edgelist example: [(2,3), (1,4), (3,9), ....]
def addGroup(graph, group, *edgelist):
    graph.add_edges_from(edgelist, group = group)
