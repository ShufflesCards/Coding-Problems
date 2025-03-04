#Benjamin Kellman
#12/2/24

times = int(input())
for i in range(times):
    numberOfTerms, sumArr = map(int, input().split())
    left = 0
    right = 10**10  # max value
    while right - left > 1:
        medianNumber = (left + right) // 2 # this is devided by 2 because we check if you are in the left or right half
        middleIndex = numberOfTerms // 2 + 1 # this is also the average
        if middleIndex * medianNumber <= sumArr: # sum/terms = average, so terms*average = sum
            left = medianNumber
        else:
            right = medianNumber
    print(left)
