import statistics

"two lines of input"
numTemps = "5"
tempList = "-10 -30 -11"
sensorList = "14 -5 39 -5 7"

"casting numTemps as an integer, splitting tempList as a list of ints"
numTemps = int(numTemps)
tempList = tempList.split()
tempList = [int(i) for i in tempList]

sensorList = sensorList.split()
sensorList = [int(i) for i in sensorList]
print(sensorList)

"function below is for problem 1"
def tempChange(numTemps, tempList):
    increase = 0
    decrease = 0
    same = 0
    for i in range(1,numTemps):
        tempDif = tempList[i] - tempList[i-1]
        if tempDif > 0:
            increase = increase + 1
        elif tempDif == 0:
            same = same + 1
        else:
            decrease = decrease + 1
    print(increase, same, decrease)

"function below is for problem 2"
def belowZero(numTemps, tempList):
    underZero = 0
    for i in range(0,numTemps):
        if tempList[i] < 0:
            underZero = underZero + 1
        else:
            underZero = underZero
    print(underZero)



"function below is for problem 3"
def relevantAverage(numTemps, sensorList):
    newList = []
    for item in sensorList:
        if item < 0:
            newList = newList
        else:
            newList.append(item)
    print(newList)
    if newList != []:
        print(statistics.mean(newList))
    else:
        print("INSUFFICIENT DATA")

'''for problem 4'''
def findRange(tempList):
    minimum = min(tempList)
    maximum = max(tempList)
    newRange = maximum - minimum
    print(newRange)
'''
tempChange(numTemps, tempList)
belowZero(numTemps, tempList)
'''
relevantAverage(numTemps, sensorList)
findRange(tempList)