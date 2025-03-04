times = int(input())
for j in range(times):
    arr = list(map(int, input().split()))
    p1 = arr[0:3]
    p2=arr[3:6]
    p1.sort()
    p2.sort()
    if (p1[2]>p2[2]):
        print("PLAYER 1")
    elif (p1[2]<p2[2]):
        print("PLAYER 2")
    elif (p1[1]>p2[1]):
        print("PLAYER 1")
    elif (p1[1]<p2[1]):
        print("PLAYER 2")
    else:
        print("WAR!")