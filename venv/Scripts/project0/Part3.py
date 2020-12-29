import math
import time
import matplotlib.pyplot as plt
# n=int(input())

# nums=input('').split(' ')
value=[]
elementNum=[]
for l in range(1,21):
    #start = time.clock()*1000
    p = []
    str = "C:/Users/lordNecromancer/PycharmProjects/ds_project1/in/input{}.txt"
    str = str.format(l)
    file = open(str, 'rt')
    nums = [int(r) for r in file.read().replace('\n', ' ').split(' ')]
    counter=0


    def findMax(start,end):
        global counter
        counter+=1
        if(end-start<1):
            if(nums[end]<=0):
                return 0
            else:
                return nums[end]
        else:
            mid=int((end-start)/2)
            counter += 2

            f=findMax(start,mid+start)
            s=findMax(start+mid+1,end)
            ff=0
            ss=0
            pref=0
            pres=0
            for i in range(mid+start,start-1,-1) :
                pref=pref+nums[i]
                counter += 1

                if(pref>ff):
                    ff=pref
            for i in range(start+mid+1, end+1, 1):
                pres = pres + nums[i]
                counter += 1

                if (pres > ss):
                    ss = pres

            return max(ss+ff,f,s)
    findMax(0, len(nums) - 1)

    # end = time.clock()*1000
    # print(end)
    value.append(counter)
    elementNum.append(len(nums))
print(value)
print(elementNum)
plt.plot(elementNum, value, 'ro')
plt.show()

