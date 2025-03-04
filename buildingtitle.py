n = int(input())

for i in range(n):
    num = int(input())
    lines = [input().split(" ") for i in range(num)]
    #print(lines)
    last = ""
    first = lines[0][0]
    bigword = ""
    lastword = ""

    for line in lines:
        last = line[-1]
        print(first,last)
        if(last == first):
            bigword += lastword + " ".join(last[1:])
        first = line
        lastword = " ".join(line)
        if(bigword == ""):
            pass
            
    
