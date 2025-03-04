for c in range(int(input())):
    s = 0
    for n in range(int(input())):
        s += sum(list(map(int, input().split())))
    #print(s - 40) if 40 < (s) else print(40 - s)
    print(s - 40)