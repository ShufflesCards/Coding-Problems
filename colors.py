n = int(input())

for i in range(n):
    data = input()
    if(data.count("blue")):
        print("blue")
    elif(data.count("red")):
        print("red")
    else:
        print("no color found")
        