# Benjamin Kellman
# 2/26/25

from collections import Counter

# TLE
# Works, TLE because python hashing is slow

'''
You can replace
k ints in the list arr with any number you want
then find how many unique numbers there are
make the list arr into a set, then use length

replace numbers with the fewest dups
ex
k = 2
list = 1,1,1,1,3,3,4,5
replace 4 and 5 with 1 or 3
'''

times = int(input())
for j in range(times):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    '''
    arr = (input().split())
    arr = [int(x) for x in arr]
    same speed
    '''
    freqArr = Counter(arr).most_common()


    while k>0:
        if (freqArr[-1][1]<=k):
            k-=freqArr[-1][1]
            freqArr.pop()
        else:
            break
        
    if(len(freqArr)==0):
        print(1)
    else:
        print(len(freqArr))

