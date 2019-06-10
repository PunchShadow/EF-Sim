import sys

def PrintStatus():
    global total_energy
    global total_time
    print("total energy: ",total_energy)
    print("total time: ",total_time)

def ClearData(G):
    global cycle_count
    global cycle_time
    global total_energy
    global total_time
    cycle_time=0
    cycle_count=0
    total_energy=0
    total_time=0
    for (node,data) in G.nodes(data=True):
        data['output_gid']=None

def NextCycle(G):
    global cycle_count
    global cycle_time
    global total_time
    total_time+=cycle_time
    cycle_time=0
    cycle_count+=1
    for (node,data) in G.nodes(data=True):
        data['output_gid']=None
    

def FlowGid(G,gid):
    global cycle_time
    global total_energy
    global total_time
    for (node,data) in G.nodes(data=True):
        for edge in G.edges(node,data=True):
            if(edge[2]['gid']==gid):
                if data['output_gid'] != gid and data['output_gid'] != None:
                    print("Can't flow different gid from same node!")
                    sys.exit(2)
                total_energy+=edge[2]['energy']
                cycle_time=max(cycle_time,edge[2]['time'])
            data['output_gid']=gid

def GraphCheck(G):
    for node in G.nodes:
        for edge in G.edges(node,data=True):
            if(edge[1]==node):
                print("Self cycle!")
                sys.exit(2)


