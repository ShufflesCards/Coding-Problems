#Benjamin Kellman
#9/18/24

times = int(input())

for i in range(times):
    ones, twos = map(int, input().split())

    if ones%2==1:
        #if there are an odd number of ones, you cant get 0
        print("NO")
        continue

    # removing pairs of twos
    twos = twos%2
    
    #checking if there are no twos left
    if twos%2==0:
        #if there are an even number of ones, they cancle
        if ones%2==0:
            print("YES")
        else:
            print("NO")
    else:
        #there is one two, and I need an even number of ones
        if (ones%2 == 0) and (ones>1):
            print("YES")
        else:
            print("NO")

