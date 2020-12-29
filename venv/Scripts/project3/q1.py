
import math


str=input('')
fromFirst=[]
fromLast=[]
hashMode=1000000005721*1000000005721

initial=ord("a")

powers=[1]





def makeCumulativeArrays(string):
    sumF = 0
    sumL = 0

    global fromFirst,fromLast
    fromFirst=[]
    fromLast=[]

    for i in range(len(string)):
        sumF =((sumF*26)%hashMode+ (ord(string[i]) - initial) )%hashMode
        fromFirst.append(sumF)
    for i in range(len(string) - 1, -1, -1):
        sumL = ((sumL*26)%hashMode+(ord(string[i]) - initial) )%hashMode
        fromLast.insert(0, sumL)
# def makeCumulativeArrays(string):
#     sumF = 0
#     sumL = 0
#
#     global fromFirst,fromLast
#     fromFirst=[]
#     fromLast=[]
#
#     for i in range(len(string)):
#         sumF += ((ord(string[i]) - initial) * 26 ** i)
#         fromFirst.append(sumF)
#     for i in range(len(string) - 1, -1, -1):
#         sumL += ((ord(string[i]) - initial) * 26 ** (len(string) - 1 - i))
#         fromLast.insert(0, sumL)


def findMaxSymmetry(string):
    makeCumulativeArrays(string)
    #print(fromFirst, fromLast)

    #print(fromFirst)
    #print(fromLast)
    max=0
    for ind, mid in enumerate(string):
        if(ind==0 or ind==len(string)-1):
            continue

        #print("inddddd")
        interval = min(ind, len(string) - 1 - ind)
        leftInd = ind - interval
        rightInd = ind + interval
        iter = 0

        if (interval > 0):
            limit = int(math.log2(interval))
        else:
            limit = -1

        interval = int(interval / 2) if int(interval / 2) != 0 else 1
        while (iter <= limit+3 and leftInd < rightInd):
            iter += 1
            #print(leftInd,rightInd)
            #print(interval)

           # leftVal = (((fromFirst[ind] - fromFirst[leftInd-1 +hashMode])%hashMode) /  powers[leftInd])%hashMode if (leftInd-1)>=0 else ((fromFirst[ind] ) / ( powers[leftInd]))%hashMode
            #rightVal = (((fromLast[ind] - fromLast[rightInd+1])%hashMode) / (powers[len(string) -1 - rightInd]))%hashMode if (rightInd+1)<len(string) else ( (fromLast[ind] ) / (powers[len(string) -1 - rightInd]))%hashMode
            leftVal = (fromFirst[ind] - ((powers[(ind-leftInd+1)]*fromFirst[leftInd - 1])%hashMode)+hashMode)%hashMode if (leftInd - 1) >= 0 else (fromFirst[ind])
            rightVal = (fromLast[ind] - ((powers[(rightInd-ind+1)]*fromLast[rightInd+1])%hashMode)+hashMode)%hashMode  if (rightInd+1)<len(string) else  (fromLast[ind])
            #print(leftVal,rightVal)

            if (leftVal == rightVal):
                if ((rightInd - leftInd) > max):
                    #print("oooooooo")
                    max = (rightInd - leftInd) + 1
                    #print(max)
                if (leftInd == 0 or rightInd == len(string) - 1):
                    break
                leftInd = leftInd - int(interval) if (leftInd - int(interval)) > 0 else 0
                rightInd = rightInd + math.ceil(interval) if (rightInd + math.ceil(interval)) < len(string) else len(
                    string) - 1
            else:
                # if(int(leftInd / 2)==0 or math.ceil (rightInd / 2)==0):
                #      print("oooooooooopppppppppppppsssssssssss")
                #      break
                # temp=  leftInd / 2
                leftInd = int(interval) + leftInd
                rightInd = rightInd - math.ceil(interval)

            interval = int(interval / 2) if int(interval / 2) != 0 else 1
    return max


#maximumOdd = findMaxSymmetry(str)

newStr='a'
for s in str:
    newStr=newStr+s+'a'

#print(newStr)
for i in range(1,len(newStr)):
    powers.append((powers[i-1]*26)%hashMode)
maximum=int(findMaxSymmetry(newStr)/2)
#print(maximumEven)



print(maximum)