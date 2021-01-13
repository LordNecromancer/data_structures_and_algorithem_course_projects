
from heapq import *
import math



weights=[]
possibleWithJump=[]
nodes=100
graph= {}
heap=[]
seen=[]
result=-1
dists= {}
inf=math.inf

numButtonStatus=list(map(int,input('').strip().split(' ')))
utilButtonStatus=list(map(int,input('').strip().split(' ')))
for i in range(10):
    new=list(map(int,input('').strip().split(' ')))
    weights=weights+new


positions=list(map(int,input('').strip().split(' ')))
src=positions[0]
dst=positions[1]


for i in range(10):
    if(numButtonStatus[i]==1):
        possibleWithJump.append(i)

if(utilButtonStatus[0]==1):
    for i in range (10,nodes):
        r = i % 10
        q = i // 10
        if (numButtonStatus[r] == 1 and numButtonStatus[q] == 1):
            possibleWithJump.append(i)


for i in range(nodes):
    graph[i]={}
    if(utilButtonStatus[1]==1):
        graph[i][((i +1)%100)]=weights[i]+1
    if (utilButtonStatus[2] == 1):
        graph[i][((i -1)%100)] = weights[i]+1
for i in range(nodes):
    for j in possibleWithJump:
        if(j not in graph[i] and i!=j):
            if(j//10)==0:
                graph[i][j] =weights[i]+1
            else:
                graph[i][j]=weights[i]+3



heappush(heap,(0,src))
dists[src]=0
for i in range(100):
    if(i!=src):
        heappush(heap,(inf,i))
        dists[i]=inf
while True:


        minDist=heappop(heap)


        if(minDist[0]>=inf ):
            break
        node=minDist[1]
        if(node not in seen):
            seen.append(node)
        if(node==dst):
            if(dists[node]<inf):
                result=dists[dst]+weights[dst]
            break
        for n in graph[node]:
            if n not in seen:



                if(dists[node]+graph[node][n]<dists[n] and n not in seen):
                    dists[n]=dists[node]+graph[node][n]
                    heappush(heap,(dists[n],n))




print(int(result))