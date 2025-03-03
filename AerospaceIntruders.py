# Benjamin Kellman
# 1/16/25
import re

def format(name, xLocation):
    print(f"Destroyed Ship: {name} xLoc: {xLocation}")
times = int(input())
#times = 1
for i in range(times):
    shipAmount = int(input())
    #shipAmount = 3
    remainingShips = []
    
    for j in range(shipAmount):
        temp = input()
        #temp = "DOOM_A:123,1444"
        borb = re.split('_|:|,', temp)
        borb[2] = int(borb[2])
        borb[3] = int(borb[3])
        remainingShips.append(borb)

    
    for j in range(shipAmount):
        remainingShips.sort(key=lambda x: (x[2], -x[3]))
        destroy = remainingShips.pop(0)
        format(destroy[0], destroy[2])
        for k in range(len(remainingShips)):
            if remainingShips[k][1]=="A":
                remainingShips[k][2]-=10
            elif remainingShips[k][1]=="B":
                remainingShips[k][2]-=20
            else:
                remainingShips[k][2]-=30