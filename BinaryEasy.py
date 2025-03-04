# Benjamin Kellman
# 12/4/24

'''
s = sum or target
Use binary search to run though number in the range 0<n<10^3 to print what 2 numbers add to that sum

'''

left = 0
right = 10**4
target = 259
while left<right:
    middle = (left+right)//2
    if left + right == target:
        print(left, right)
        break
    elif left+right < target:
        left = middle
    elif left+right > target:
        right = middle
        