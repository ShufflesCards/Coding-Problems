# Benjamin Kellman
# 10/15

# if there are 1 or 2 people, return -1

# n[0]+n[1]..../(n.len()*2) = unhappy amount
# get middle n, round up
# add the min number to get unhappy amount > mid number

times = int(input())
for i in range(times):
    peopleAmount = int(input())
    peopleLis= list(map(int,input().split()))
    peopleLis.sort()
    mid = (peopleAmount//2)
    if peopleAmount <= 2:
        print(-1)
    else:
        gold = peopleLis[mid]*peopleAmount*2-sum(peopleLis)
        gold += 1
        # use math
        # unhappyAmount = (sum(peopleLis)+gold)/(peopleAmount*2)
        # unhappyAmount*peopleAmount*2 = (sum(peopleLis)+gold)
        # unhappyAmount*peopleAmount*2-sum(peopleLis)= gold
        
        #gold += 1
        #unhappyAmount = (sum(peopleLis)+gold)/(peopleAmount*2)

        print(max(gold,0))

