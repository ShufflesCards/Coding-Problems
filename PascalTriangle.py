# Benjamin Kellman
# 2/14/25

import math
row = 4

for c in range(row):
    print(f"{row}!/({row}-{c})!{c}!")

for c in range(row+1):
    top = math.factorial(row)
    bottomIn = math.factorial(row-c)
    bottomOut = math.factorial(c)
    #print(f"{top}/({bottomIn}*{bottomOut})")
    print(top/(bottomIn*bottomOut))