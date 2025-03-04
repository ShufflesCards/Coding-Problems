# Benjamin Kellman
# 2/14/25

import math
n = int(input())
lis = list(map(int, input().split()))

lis.sort()
#print(lis)
'''
5
3 6 5 1 4

out 159
'''
total = 0
for i in range(n):
    cur=lis.pop()
    row = len(lis)
    for c in range(len(lis)+1):
        top = math.factorial(row)
        bottomIn = math.factorial(row-c)
        bottomOut = math.factorial(c)
        #print(f"{top}/({bottomIn}*{bottomOut})")
        #print(f"{row}*{row}!/({row}-{c})!*{c}!")
        fac=top/(bottomIn*bottomOut)
        #print(fac)
        #print(f"{cur}*{fac}")
        total+=(cur)*(fac)
print(int(total))