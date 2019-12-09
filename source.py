import string
def roundUpToNearestNumber(lst,number):
  res = min(enumerate(lst), key=lambda x: abs(number - x[1]))
  if(res[1]<number):
    newIndex = res[0]+1
    if(lst[newIndex]!= None):
      res = (newIndex,lst[newIndex])
    else:
     res = (newIndex+1,lst[newIndex+1])
  return res
def roundUpToNearestDepth(depth):
  depthList = [10,12,14,16,18,20,22,25,30,35,40,42]
  return roundUpToNearestNumber(depthList,depth)
  

depthToLstOfTime = {
  10: [10,20,25,30,34,37,41,45,50,54,59,64,70,75,82,88,95,104,112,122,133,145,160,178,199,219],
  12: [9,17,23,26,29,32,35,38,42,45,49,53,57,62,66,71,76,82,88,94,101,108,116,125,134,147],
  14: [8,15,19,22,24,27,29,32,35,37,40,43,47,50,53,57,61,64,68,73,77,82,87,92,98],
  16: [7,13,17,19,21,23,25,27,29,32,34,37,39,42,45,48,50,53,56,60,63,67,70,72],
  18: [6,11,15,16,18,20,22,24,26,28,30,32,34,36,39,41,43,46,48,51,53,55,56],
  20: [6,10,13,15,16,18,20,21,22,24,25,27,29,30,32,34,36,38,40,42,44,45],
  22: [5,9,12,13,15,16,18,19,21,22,24,25,27,29,30,32,34,36,37],
  25: [4,8,10,11,13,14,15,17,18,19,21,22,23,25,26,28,29],
  30: [3,6,8,9,10,11,12,13,14,15,16,17,19,20],
  35: [3,5,7,8,9,9,10,11,12,13,14],
  40: [2,5,6,7,7,8,9],
  42: [2,4,6,6,7,8]
}

ntrToRestTimeLst = {
'A' : [0],
'B' : [48,0],
'C' : [70,22,0],
'D' : [79,31,9,0],
'E' : [78,39,17,8,0],
'F' : [95,47,25,16,8,0],
'G' : [102,54,32,23,14,7,0],
'H' : [108,60,38,29,21,13,6,0],
'I' : [114,66,44,35,27,19,12,6,0],
'J' : [120,72,50,41,32,25,18,12,6,0],
'K' : [125,77,55,46,38,30,23,17,11,5,0],
'L' : [130,82,60,51,43,35,28,22,16,10,5,0],
'M' : [135,86,65,56,47,40,33,26,20,15,10,5,0],
'N' : [139,91,69,60,52,44,37,31,25,19,14,9,4,0],
'O' : [144,95,73,64,56,48,42,35,29,24,18,16,9,4,0],
'P' : [148,99,77,68,60,52,46,39,33,28,22,17,13,8,4,0],
'Q' : [151,103,81,72,64,56,49,43,37,31,26,21,17,12,8,4,0],
'R' : [155,107,85,76,68,60,53,47,41,35,30,25,20,16,12,8,4,0],
'S' : [159,110,88,79,71,64,57,50,44,39,33,28,24,19,15,11,7,4,0],
'T' : [162,114,92,83,74,67,60,54,48,42,37,32,27,23,18,14,11,7,3,0],
'U' : [165,117,95,86,78,70,63,57,51,45,40,35,30,26,22,18,14,10,7,3,0],
'V' : [168,120,98,89,81,73,66,60,54,48,43,38,34,29,25,21,17,13,10,6,3,0],
'W' : [171,123,101,92,84,76,69,63,57,51,46,41,37,32,28,24,20,16,13,9,6,3,0],
'X' : [174,126,104,95,87,79,72,66,60,54,49,44,40,35,31,27,23,19,16,12,9,6,3,0],
'Y' : [177,129,107,98,90,82,75,69,63,57,52,48,42,38,34,30,26,22,19,15,12,9,6,3,0],
'Z' : [180,132,110,101,92,85,78,72,66,60,55,50,45,41,36,32,29,25,21,18,15,12,9,6,3,0]
}

def minSurface(ntrLvl,restTime):
  index=0
  timeLst = ntrToRestTimeLst.get(ntrLvl)
  while timeLst[index] > restTime:
    index+=1
  return index,timeLst[index]

#adjusted no decom limit
ANDL = [
  [209,199,193,189,185,182,178,174,169,165,160,155,149,144,137,131,124,115,107,97,86,74,59,41,20],
  [138,130,124,121,118,118,115,112,109,105,102,98,90,85,81,76,71,65,59,53,46,39,31,22,13],
  [90,83,79,76,74,71,69,66,63,61,58,55,51,48,45,41,37,34,30,25,21,16,11,6],
  [65,59,55,53,51,49,47,45,43,40,38,35,33,30,27,24,22,19,16,12,9,5,2],
  [50,45,41,40,38,36,34,32,30,28,26,24,22,20,17,15,13,10,8,5,3],
  [39,35,32,30,29,27,25,24,22,20,19,17,15,13,11,9,7,5,3],
  [32,28,25,24,22,21,19,18,16,15,13,12,10,8,7,5,3],
  [25,21,19,18,16,15,14,12,11,10,8,7,6,4,3],
  [17,14,12,11,10,9,8,7,6,5,4,3],
  [11,9,7,6,5,5,4,3],
  [7,4]
]


def maxTimeForDepth(depth):
  timeLst = depthToLstOfTime.get(depth)
  return timeLst[-1]

nitrogenLst = list(string.ascii_uppercase)

def getNitrogenLevelForFirstDive(depth,time):
  timeLst = depthToLstOfTime.get(depth)
  key, time = roundUpToNearestNumber(timeLst,time)
  return nitrogenLst[key]


depth = int(input('Enter depth for first dive : '))
while(depth>42  or  depth<=0):
  print('Input a depth less than or equal to 42 and greater then 0.')
  depth = int(input('Enter depth for first dive : '))
depthKey , depth = roundUpToNearestDepth(depth)
maxTime = maxTimeForDepth(depth)
print('Maxtime for first dive is: ', maxTime)
actualTime = int(input('Enter actualTime for first dive : '))
while(actualTime>maxTime):
  print('Please input a number less than or equal to ',maxTime)
  actualTime = int(input('Enter actualTime for first dive : '))
ntrLevel = getNitrogenLevelForFirstDive(depth, actualTime)
print('Nitrogrn level is : ', ntrLevel)
restTime = int(input('What is your rest time in minutes?: '))
ntrKey,rest = minSurface(ntrLevel,restTime)
print('New nitrogen level is: ',nitrogenLst[ntrKey])
depth = int(input('Enter depth for second dive : '))
while(depth>40  or  depth<=0):
  print('Input a depth less than or equal to 40 and greater then 0.')
  depth = int(input('Enter depth for second dive : '))
depthKey,depth  = roundUpToNearestDepth(depth)
print('Maxtime for second dive is: ', ANDL[depthKey][ntrKey])
actualTime = int(input('Enter actualTime for second dive : '))
while(actualTime>maxTime):
  print('Please input a number less than or equal to ', ANDL[depthKey][ntrKey])
  actualTime = int(input('Enter actualTime for first dive : '))
#TBT = RNT + ABT
TBT = (depthToLstOfTime[depth])[ntrKey] + actualTime
ntrLevel = getNitrogenLevelForFirstDive(depth, TBT)
print('Nitrogrn level is : ', ntrLevel)
restTime = int(input('What is your rest time in minutes?: '))
ntrKey,rest = minSurface(ntrLevel,restTime)
print('New nitrogen level is: ',nitrogenLst[ntrKey])
depth = int(input('Enter depth for third dive : '))
while(depth>40  or  depth<=0):
  print('Input a depth less than or equal to 35 and greater then 0.')
  depth = int(input('Enter depth for second dive : '))
depthKey,depth  = roundUpToNearestDepth(depth)
print('Maxtime for third dive is: ', ANDL[depthKey][ntrKey])

