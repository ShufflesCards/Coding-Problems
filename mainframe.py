n = int(input())

for i in range(n):
    bitLen = int(input())
    maxVal = 2**bitLen - 1
    values = [int(x) for x in input().split(" ")]
    result = sum([(value > maxVal) for value in values])
    print(maxVal,end=" ")
    print("TRUE" if not result else "FALSE")