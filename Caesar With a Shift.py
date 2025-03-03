# Benjamin Kellman
# 1/15/25

# A = 65
# Z = 90


times = int(input())

for i in range(times):
    
    scrambled = input()
    far = list(map(int, input().split()))
    direction = list(map(int, input().split()))
    

    ans = ""
    j=0
    for h in range(len(scrambled)):

        
        if (ord(scrambled[h])<65 or ord(scrambled[h])>90):
            ans+=scrambled[h]
        else:
            if (direction[j%len(direction)]==1):
                ans+= chr((ord(scrambled[h])-far[j%(len(far))]-65)%26+65)
            else:
                ans+= chr((ord(scrambled[h])+far[j%(len(far))]-65)%26+65)
            j+=1

    print(ans.lower())