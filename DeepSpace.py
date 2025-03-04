alphabet = list("abcdefghijklmnopqrstuvwxyz")
print(alphabet)

times = int(input())
for j in range(times):
    word = input()
    out = ""
    for i in range(len(word)):
        if (word[i:i+1].isnumeric()):
            if(i+2<len(word) and word[i:i+2].isnumeric()):
                temp = int(word[i:i+2])
                #print(temp)
                out+=alphabet[temp-1]
                i+=2
            else:
                temp = int(word[i:i+1])
                print(temp)
                out+=alphabet[temp-1]
    print(out)