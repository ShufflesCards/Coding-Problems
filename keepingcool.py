n = int(input())

for weweff in range(n):
    numberVals, min, avg, max = [float(x) for x in input().split(" ")]
    values = [float(x) for x in input().split(" ")]
    valAvg = sum(values)/numberVals
    values.sort()
    minVal, maxVal  = values[0], values[-1]

    if(minVal < min):
        print("TOO COOL")
    elif(maxVal > max):
        print("TOO HOT")
    elif(valAvg > avg):
        print("WARNING")
    else:
        print("OK")