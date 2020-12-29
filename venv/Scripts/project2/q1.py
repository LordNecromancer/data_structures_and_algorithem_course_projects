import math
#import numpy as np
class Heap:
    def __init__(self):

         self.elements=[None]
         self.heapSize = 0







    def getMinChild(self,elemIndex):

        i=elemIndex*2

        if (i+1>self.heapSize):
            minIndex = i
        else:
            minIndex = i  if self.elements[i ] < self.elements[i+1] else i+1

        return minIndex

    def bubbleUp(self,elemIndex):
        i = int(elemIndex / 2)
        while (i  > 0 and self.elements[elemIndex] < self.elements[i]):
            self.elements[elemIndex] ,self.elements[i]= self.elements[i],self.elements[elemIndex]
            elemIndex = i
            i = int(elemIndex / 2)


    def bubbleDown(self,elemIndex):

        i = elemIndex*2


        while (i <=self.heapSize ):
            #print(self.elements)
            #print(i)




            #print(self.elements)
            minIndex=self.getMinChild(elemIndex)
            if(self.elements[minIndex]>=self.elements[elemIndex]):
                return
            self.elements[elemIndex],self.elements[minIndex] = self.elements[minIndex],self.elements[elemIndex]
            elemIndex = minIndex
            i = elemIndex*2


    def insert(self,elem):
        self.elements.append(elem)
        self.heapSize+=1
        elemIndex = self.heapSize

        self.bubbleUp(elemIndex)



    def deleteMin(self):

        if (self.heapSize == 0):
            return
        self.elements[1],self.elements[self.heapSize]=self.elements[self.heapSize],self.elements[1]




        final=self.elements.pop()
        self.heapSize-=1


        if(self.heapSize<1):
            return final

        elemIndex = 1
        self.bubbleDown(elemIndex)

        return  final







n=int(input())
#for numbers bigger than median
minHeap=Heap()
#for numbers smaller than median
maxHeap=Heap()

median=None
for i in range (0,n):

    new = int(input())

    if(minHeap.heapSize==0 and maxHeap.heapSize==0) :
        maxHeap.insert(-1*new)
        median=-1*maxHeap.elements[1]


    elif(new>=median):
        if(minHeap.heapSize>maxHeap.heapSize):
            maxHeap.insert(-1*minHeap.deleteMin())
            minHeap.insert(new)
            median=-1*maxHeap.elements[1]
        elif(minHeap.heapSize<maxHeap.heapSize):
            minHeap.insert(new)
            median=-1*maxHeap.elements[1]
        else:
            minHeap.insert(new)
            median = minHeap.elements[1]
    else:
        if (maxHeap.heapSize > minHeap.heapSize):
            minHeap.insert(-1*maxHeap.deleteMin())
            maxHeap.insert(-1*new)
            median =-1* maxHeap.elements[1]
        elif (maxHeap.heapSize < minHeap.heapSize):
            maxHeap.insert(-1*new)
            median = -1 * maxHeap.elements[1]
        else:
            maxHeap.insert(-1*new)
            median = -1*maxHeap.elements[1]

    print(median)

#
#    # print(heap.elements)
#
#    #
#    #  tempH=Heap(list(tempSorted))
#    #  tempH.insert(new)
#    #  #print(tempH.elements)
#    # # print(tempH.elements)
#    #
#    #  #print(tempH.elements)
#    #  tempSorted=[]
#     #print(tempH.elements)
# sorted=[]
# for i in range(0,n):
#     sorted.append(heap.deleteMin())
#     #print(tempSorted)
#
#
#
# tempSorted=[None]*n
# for i in range(0,n):
#     ind=sorted.index(entries[i])
#     tempSorted[ind]=entries[i]
#     sorted[ind]=None
#     temp=[x for x in tempSorted if x is not None]
#     p=int(len(temp)/2) if len(temp)%2==1 else int(len(temp)/2)-1
#     print(int(temp[p]))
# tempSorted=np.int32(np.empty(n))
# for i in range(0,n):
#     ind=sorted.index(entries[i])
#     tempSorted[ind]=entries[i]
#     sorted[ind]=-1.5
#     temp=tempSorted[tempSorted>0]
#     p=int(temp.size/2) if temp.size%2==1 else int(temp.size/2)-1
#     print(temp[p])

#     median.append(heap.elements[int((i+1)/2 )])
#
# print(median)
# sort=[]
# for i in range (n):
#
#     sort.append(heap.deleteMin())
#     print(res[math.ceil(i/2 )])
#print(res)
#print(heap.deleteMin())
