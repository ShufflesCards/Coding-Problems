# Benjamin Kellman
# 2/19/25

leng = int(input())
total = list(map(int, input().split()))

'''
leng = 8
total = [1,3,4,5,6,7,8,2]

output: 1 0 0 0 0 0 0 1
'''
'''
sum of intigers in order
(n / 2)(first number + last number)

compare that to prefix sum at different parts
'''

def permExist(permLen, mainPrefix):
    target = int((permLen/2)*(1+permLen))
    for x in range(len(mainPrefix)-permLen):
        if mainPrefix[x+permLen]-mainPrefix[x] == target:
            return 1
    return(0)


mainPreSum = [0]
for i in range(leng):
    mainPreSum.append(mainPreSum[i]+total[i]) 

ans = ""
for i in range(leng):
    ans+=str(permExist(i+1, mainPreSum))
    ans+= " "

print(ans)