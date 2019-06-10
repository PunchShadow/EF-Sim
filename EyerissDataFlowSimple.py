import RectangleGraph
import FlowControl

raw_id = [15,0,1,2,3,0,1,2,3,0,1,2]
col_id = [
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [ 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6],
    [ 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6],
    [ 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6],
    [ 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6],
    [ 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7],
    [ 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7],
    [ 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7],
    [ 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7],
    [ 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8],
    [ 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8],
    [ 2, 3, 4, 5, 6, 7, 8, 2, 3, 4, 5, 6, 7, 8]
]

eyeriss = RectangleGraph.eyeriss(raw_id,col_id)
FlowControl.ClearData(eyeriss)

for i in range(10):
    for j in range(12):
        FlowControl.FlowGid(eyeriss,i) #filter
        FlowControl.NextCycle(eyeriss)
    for x in range(4):
        for y in range(9):
            FlowControl.FlowGid(eyeriss,12+x+y*32) #imap
            FlowControl.NextCycle(eyeriss)
    FlowControl.FlowGid(eyeriss,50) #omap
    FlowControl.NextCycle(eyeriss)

FlowControl.PrintStatus()