import sys

def ClearData(G):
    global cycle_count
    global cycle_time
    global total_energy
    global total_time
    cycle_time=0
    cycle_count=0
    total_energy=0
    total_time=0
    for node in G.nodes:
        G[node]['output_gid']=None

def NextCycle(G):
    global cycle_count
    global cycle_time
    global total_time
    total_time+=cycle_time
    cycle_time=0
    cycle_count+=1
    for node in G.nodes:
        G[node]['output_gid']=None
    

def FlowGid(G,gid):
    global cycle_time
    global total_energy
    global total_time
    for node in G.nodes:
        for edge in G.edges(node,data=True):
            if(edge[2]['gid']==gid):
                if G[node]['output_gid'] != gid and G[node]['output_gid'] != None:
                    print("Can't flow different gid from same node!")
                    sys.exit(2)
                total_energy+=edge[2]['energy']
                cycle_time=max(cycle_time,edge[2]['time'])
            G[node]['output_gid']=gid


