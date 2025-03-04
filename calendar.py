amount = int(input())
for i in range(amount):
    catPics = int(input())
    attention = list(map(int, input().split()))
    modAttention = [0]*catPics
    ans = False

    for j in range(catPics):
        modAttention[j] = attention[j]%15330
    modAttention.sort()
    if 0 in modAttention:
        print(":)")
    else:
        lowI = 0
        highI = len(modAttention)-1

        while(lowI<highI):
            if modAttention[lowI] + modAttention[highI] == 15330:
                ans = True
                lowI = highI
            elif modAttention[lowI] + modAttention[highI] > 15330:
                highI -=1
            elif modAttention[lowI] + modAttention[highI] < 15330:
                lowI +=1


        
        if ans == True:
            print(":)")
        else:
            print(":(")

