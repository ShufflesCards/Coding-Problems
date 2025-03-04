for c in range(int(input())):
    n = int(input())
    req = input().split(",")
    req = list(map(lambda x: x.split("-")[1], req))
    
    for i in range(n):
        res = []
        ch = (input().split())
        prefix = ch[0].split("-")[0]
        ch = set(map(lambda x: x.split("-")[1], ch))
        for item in req:
            if not item in ch: res.append(item)
        res.sort()
        if len(res) == 0:
            print("FULL COVERAGE")
        else:
            res = map(lambda x: prefix + "-" + x, res)
            print(",".join(res))