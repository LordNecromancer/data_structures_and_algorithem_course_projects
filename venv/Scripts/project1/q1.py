from sys import stdin
#import pandas as pd
initials = input('').split(' ')
seen=[]
current=None
class Node:
    next=None
    data=0
    prev=None
    points=0
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev
class LinkedList:
    head=None
    def __init__(self, head):
        self.head = head


    def insertAfter(self,cur,data):
        if (cur):
            new=Node(data,cur.next,cur)
            if(cur.next ):
                cur.next.prev=new
            cur.next=new
            return new
        else:
            new=Node(data,None,None)
            return new

    def removeAt(self,cur):
        if(cur is self.head):
            self.head=cur.next
        if(cur.next ):
            cur.next.prev=cur.prev
        if(cur.prev ):

            cur.prev.next=cur.next


linkedList=LinkedList(None)
linkedList.head = linkedList.insertAfter(current,int(stdin.readline().strip()))
current=linkedList.head

for i in range(1,int(initials[0])):


    new=linkedList.insertAfter(current,int(stdin.readline().strip()))
    current=new




seen.append(linkedList.head)

current=linkedList.head

# commands=[]
# for i in range(int(initials[1])):
#     commands.append(stdin.readline().strip().replace('\n',' ').split(' '))
for i in range(int(initials[1])):
    command=input().split(' ')



    if(len(command)==1) :
        command=int(command[0])
        if (command==1):
            n=current.next
            if( n):

                linkedList.removeAt(current)
                current=n
                seen.append(current)

            else:
                linkedList.removeAt(current)
                current = current.prev
                seen.append(current)






        elif(command==3) :

          n=current.next
          if(n):
              current=n
              seen.append(current)


        elif (command == 4):

            p = current.prev
            if (p):
                current = p
                seen.append(current)




    else:
        number=int(command[1])
        linkedList.insertAfter(current,number)


stack=[]
stack.append(seen[0])
elem=1
max=0
maxNum=0


while(elem<len(seen)) :


    if (seen[elem].points > max or (seen[elem].points == max and seen[elem].data> maxNum)):
        max = seen[elem].points
        maxNum = seen[elem].data
    if(seen[elem].data>stack[len(stack)-1].data):
        seen[elem].points+=2
        stack.pop()
        if(len(stack)==0 ):
            stack.append(seen[elem])

            elem+=1


    else:
        stack.append(seen[elem])

        elem += 1

# for x in newSeen:
#     print(x.data,x.points)

stack=[]
stack.append(seen.pop())
elem=0
while(len(seen)>0) :
    elem = len(seen) - 1

    if (seen[elem].points > max or (seen[elem].points == max and seen[elem].data > maxNum)):
        max = seen[elem].points
        maxNum = seen[elem].data
    if(seen[elem].data<stack[len(stack)-1].data):
        seen[elem].points+=1
        stack.pop()
        if (len(stack) == 0):
            stack.append(seen.pop())


    else:
        stack.append(seen.pop())

print(maxNum)
# max=0
# maxNum=0
# for h in uniqueSeen :
#     if (uniqueSeen[h]['points'] > max or (uniqueSeen[h]['points'] == max and uniqueSeen[h]['num'] > maxNum)):
#       max=uniqueSeen[h]['points']
#       maxNum=uniqueSeen[h]['num']
