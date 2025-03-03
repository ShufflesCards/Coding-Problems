# Benjamin Kellman
# 1/15/25

decimal_count = 1


def format(name, grade, letter):
    print(f"{name} {grade}% {letter}")


times = int(input())
for i in range(times):
    peopleNum, key = input().split()
    peopleNum = int(peopleNum)
    

    for k in range(peopleNum):
        person, answer = input().split()
        correct = 0
        for k, a in zip(key, answer):
            if (k==a):
                correct+=1
        
        grade = (correct/len(key))*100

        grade=int(grade * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count)
        if grade < 60:
            format(person, grade, "F")
        elif grade < 70:
            format(person, grade, "D")
        elif grade < 80:
            format(person, grade, "C")
        elif grade < 90:
            format(person, grade, "B")
        else:
            format(person, grade, "A")

 