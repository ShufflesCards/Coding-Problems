# Benjamin Kellman
# 1/17/25



# work backwords

# make a copy of keyword in alphabetical order
# put inputs into grid of [columns[rows]]
# move around columns so the keyword is back to original state
# remove any gaps of charachters
'''
[
[a, b, c],
[d, e, f],
[g, , i]
]
the [g, "" , i]
becomes
[g, i, ""]
]
'''
# then use the updated grid to check against the alphabet grid of [rows[columns]]


times = int(input())
#times = 1

letterToNum = {
  "A": 0,
  "D": 1,
  "F": 2,
  "G": 3,
  "V": 4,
  "X": 5
}


for i in range(times):
    alphabetGrid = []
    
    for j in range(6):
        alphabetGrid.append(list(input()))
    

    keyWord = list(input())
    #keyWord = list("martin")
    orderedKeyWord = sorted(keyWord)
    scrambledGrid = [] 





    bigString = input()
    #bigString = "DDAGAVVXGFAAVAGFGDFVVFDDFV"
 
    for j in range(len(bigString)//len(keyWord)+1):
        #puts input into grid when keyword is in alphabetic order
        scrambledGrid.append(list(bigString[len(keyWord)*j:len(keyWord)*j+len(keyWord)]))

    # you can tell where the letters should by seeing if they should shift over 
    lastRow = scrambledGrid.pop(-1)

    #print(scrambledGrid)
    unscrambledGrid = [] 
  
    for j in range(len(keyWord)):
    # keyword is used to take list out of alphabetical order

        checkingLetter = keyWord[j]
        for k in range(len(orderedKeyWord)):

            if checkingLetter == orderedKeyWord[k]:
                x=0
                for column in zip(*scrambledGrid):
                    
                    if x==k:
                        unscrambledGrid.append(list(column))
                    x+=1

    # add lastRow to the unscrambledGrid

    # check how many letters are in there
    # check the first letter in the alphabeicaly sorted key and place that in the unscrambledGrid


    '''
    MAKE FASTER

    Add padding to use .zip
    
    '''
    
    for j in range(len(lastRow)):
        #check place value of ordered keyword and how it compares to unordered

        # move below zip stuff

        for k in range(len(keyWord)-j):
            checkingLetter = orderedKeyWord[k+j]
            letterIndex = keyWord.index(checkingLetter)

        

            if letterIndex < len(lastRow):
                unscrambledGrid[letterIndex].append(lastRow[j])
                break
        #print(checkingLetter)
        #print(letterIndex)



    #print(unscrambledGrid)
    # this moved the grid to be in the order of [[row], [row]...]

    FixedunscrambledGrid = [[] for x in range(len(unscrambledGrid[0]))]
    for x in range(len(unscrambledGrid)):
        for y in range(len(unscrambledGrid[x])):
            FixedunscrambledGrid[y].append(unscrambledGrid[x][y])

    

    

    
    thing=FixedunscrambledGrid[0]
    for j in range(len(FixedunscrambledGrid)-1):
        thing+=FixedunscrambledGrid[j+1]


    oneString = ''.join(thing)
    #print(oneString)
    ans = ""
    for j in range(len(oneString)//2):
        Letters = oneString[2*j:2+j*2]
        x=Letters[0:1]
        y=Letters[1:2]
        ans+=alphabetGrid[letterToNum[x]][letterToNum[y]]
    
    print(ans)



