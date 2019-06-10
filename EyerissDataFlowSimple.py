import RectangleGraph
import FlowControl

raw_id = [0,1,1,1,1,1,1,1,1,1,1,1]
col_id = [
    [ 0,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31]
]

eyeriss = RectangleGraph.eyeriss(raw_id,col_id)
FlowControl.ClearData(eyeriss)

for i in range(100):
    FlowControl.FlowGid(eyeriss,0) #filter
    FlowControl.NextCycle(eyeriss)
    FlowControl.FlowGid(eyeriss,12+0+0*32) #imap
    FlowControl.NextCycle(eyeriss)
    FlowControl.FlowGid(eyeriss,50) #omap
    FlowControl.NextCycle(eyeriss)

FlowControl.PrintStatus()