# Benjamin Kellman
# 1/24/25

decimal_count = 3

times = int(input())
for i in range(times):
    name, scores =  input().split(":")
    scoreList = scores.split(",")
    slg=0
    
    totalBats=len(scoreList)
    for j in range(len(scoreList)):
        if scoreList[j]=="1B":
            slg+=1
        elif scoreList[j]=="2B":
            slg+=2
        elif scoreList[j]=="3B":
            slg+=3
        elif scoreList[j]=="HR":
            slg+=4
        elif scoreList[j]=="BB":
            totalBats-=1

    #print(f"slg: {slg} bats: {totalBats}")
    if (totalBats>0):
        slg/=totalBats
        slg=int(slg * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count)
        hi = format(slg, ".3f")
    else:
        sgl=0.000
        hi = format(slg, ".3f")
    print(f"{name}={hi}")
