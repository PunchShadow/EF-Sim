import RectangleGraph
import FlowControl

config = [
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

eyeriss = RectangleGraph.eyeriss(config)
FlowControl.ClearData(eyeriss)

for i in range(100):
    FlowControl.FlowGid(eyeriss,0) #filter
    FlowControl.NextCycle(eyeriss)
    FlowControl.FlowGid(eyeriss,12+0) #imap
    FlowControl.NextCycle(eyeriss)
    FlowControl.FlowGid(eyeriss,50) #omap
    FlowControl.NextCycle(eyeriss)

FlowControl.PrintStatus()