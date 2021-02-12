import math
from sys import stdin



def getMin(a,b):
    return a if a<=b else  b
def createSegmentTree(arr,curr,startInd,endInd):
    #print(curr,len(tree),len(arr))
    if(startInd==endInd):
        tree[curr]=arr[startInd]
        return arr[startInd]

    tree[curr]=getMin(
        createSegmentTree(arr,curr*2+1,startInd,startInd+(endInd-startInd)//2),
        createSegmentTree(arr, curr * 2 + 2, startInd+(endInd-startInd)//2+1, endInd)

    )
    return tree[curr]


def query(curr,startInd,endInd,startRange,endRange):
   # print(curr,startInd,endInd,startRange,endRange)
    if(startRange<=startInd and endRange>=endInd):
        return tree[curr]
    if(startRange>endInd or endRange<startInd):
        return 10**6+1
    mid=startInd + (endInd - startInd) // 2
    return getMin(
        query( curr * 2 + 1, startInd, mid,startRange,endRange),
        query( curr * 2 + 2, mid + 1, endInd,startRange,endRange)
    )





n,m=list(map(int,stdin.readline().strip().split(' ')))

arr=list(map(int,stdin.readline().strip().split(' ')))
tree=[-1]*(2*(2**math.ceil(math.log2(n)))-1)
createSegmentTree(arr,0,0,len(arr)-1)
#print(tree)
q=[]
for i in range(m):
    s,e=map(int,stdin.readline().strip().split(' '))

    q.append((s,e))

for s,e in q:
    print(query(0,0,len(arr)-1,s-1,e-1))