from collections import Counter

times = int(input())
for i in range(times):
    s1 = input().lower().split(" ")
    s2 = input().lower().split(" ")
    word1 = s1[5]
    word2 = s2[7]
    x =(Counter(word1).most_common())
    y=(Counter(word2).most_common())
    x.sort()
    y.sort()
    if x==y:
        print("Verified")
    else:
        print("Intercepted")
'''
The missile defense system requires secure protocols
Specific rules must be followed during the rescue mission
'''