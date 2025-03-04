# Benjamin Kellman
# 2/6/25

'''
https://codeforces.com/problemset/problem/2051/C
'''

#only pass if you know all

times = int(input())

for i in range(times):
    n, m, k = input().split()
    n = int(n)
    m = int(m)
    k = int(k)

    questionList = list(map(int, input().split()))
    knownAnswers = list(map(int, input().split()))

    
    '''
2 2 1
1 2
1

should output
01
    '''


    ans=""
    if (n-1>k):
        for j in range(m):
            ans+="0"
    elif(n-1<k):
        for j in range(m):
            ans+="1"
    else:
        qIndex = 0
        kIndex = 0
        while kIndex<len(knownAnswers) and qIndex<len(questionList):
            # i think this is wrong when known answers goes up by 2
            if(questionList[qIndex]==knownAnswers[kIndex]):
                ans+='0'
                qIndex+=1
                kIndex+=1
            else:
                ans+='1'
                qIndex+=1
    
    while(len(ans)<m):
        ans="0"+ans
    print(ans)