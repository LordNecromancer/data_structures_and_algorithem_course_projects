import math
import time
import matplotlib.pyplot as plt
# n=int(input())

# nums=input('').split(' ')
value=[]
elementNum=[]
for l in range(1,21):
 #start = time.clock() *1000
 p=[]
 str="C:/Users/lordNecromancer/PycharmProjects/ds_project1/in/input{}.txt"
 str=str.format(l)
 file=open(str,'rt')
 nums=[int(r) for r in file.read().replace('\n',' ').split(' ')]
 prev=0
 max=0
 counter=0
 for i in range(len(nums)):
     p.append(prev+int(nums[i]))
     prev=prev+int(nums[i])
     counter+=2

 m = 0
 for i in range(len(nums)):

     counter+=1

     if(p[i]-m>max):
         max=p[i]-m
         counter += 1

     m=min(p[i],m)

 #end = (time.clock()*1000 )
 value.append(counter)
 elementNum.append(len(nums))
print(value)
print(elementNum)
plt.plot(elementNum,value,'ro')
plt.show()
