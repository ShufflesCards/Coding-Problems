# Benjamin Kellman
# 2/14/25

n, q = map(int, input().split())

exam = list(map(int, input().split()))
'''
n, q = 3, 4
exam = [10,10,11]
'''
exam.sort()


for i in range(q):
    request, d = map(int, input().split())


    if (request == 1): # remove the easiest problem strictly > than d
        if (d>=exam[-1]):
            print(-1)
        else:
            ind = (next(x[0] for x in enumerate(exam) if x[1] > d))
            print(exam[ind])
            exam.pop(ind)
    elif (request == 2):

        if (len(exam)==0):
            print(-1)
        elif (len(exam)==1):
            if(exam[0]<=d):
                print(exam[0])
                exam.pop()
            else:
                print(-1)
        elif(d<exam[0]):
            print(-1)
        else:
            ind = (next(x[0] for x in enumerate(exam) if x[1] > d))
            print(exam[ind-1])
            exam.pop(ind-1)
            #print("mathed")
        #print(exam)
        


# back up
# it can find thing
if False:
    for i in range(q):
        request, d = map(int, input().split())
        if (request == 1): # remove the easiest problem strictly > than d
            low = 0
            high = len(exam)-1
            
            found = False
            while low<high:
                mid= low+(high-low)//2
                #print(low,mid,high)
                if(exam[mid]==d):
                    print(exam[mid])
                    exam.pop(mid)
                    found =True
                    break
                elif(exam[mid]<d):
                    low = mid+1
                else:
                    high = mid
            if (found!=True):
                print(-1)