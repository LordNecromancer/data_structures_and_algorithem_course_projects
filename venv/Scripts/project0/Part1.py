import math
import time
import matplotlib.pyplot as plt
# n=int(input())

# nums=input('').split(' ')
value=[]
elementNum=[]
for l in range(1,21):
  #  start = time.clock()*1000
    str = "C:/Users/lordNecromancer/PycharmProjects/ds_project1/in/input{}.txt"
    str = str.format(l)
    file = open(str, 'rt')
    nums = [int(r) for r in file.read().replace('\n', ' ').split(' ')]
    max=0
    counter=0
    for i in range(len(nums)):
        for j in range(i,len(nums)+1):
         current=nums[i:j]
         sum=0
         for x in current :
             sum+=int(x)
             counter+=1
         if(sum>max):
             max=sum

   # end = time.clock() * 1000
    #print(end)
    value.append(counter)
    elementNum.append(len(nums))
print(value)
print(elementNum)
plt.plot(elementNum, value, 'ro')
plt.show()