#Current position of the dial
dialPos = 50

#Number of time the dial has stepped onto or over 0
zeroCount = 0

#For each line in the file
with open("day-1-secret-entrance/input/input.txt") as fin:
    for line in fin:
        
        #Get the number of times the dial needs to move
        moveCount = int(line[1:])

        #Every 100 times the dial needs to move is one full rotation and so = one pass by 0
        #While the movement count is greater than 100
        while moveCount >= 100:
            #Increment the zero count
            zeroCount += 1
            #Subtract 100 from the movement count
            moveCount -= 100
            
        #Check if the movement is left (negative) or right (positive)
        if line[0] == "L":
            #Move the dial left by the remaining move count
            dialPos -= moveCount
            #If the dial is on or past 0
            if dialPos <= 0:
                #Increment the zero count
                zeroCount += 1
                #Mod the dial position to wrap it back around into the 0-99 range
                dialPos = dialPos % 100
        elif line[0] == "R":
            #Move the dial right by the remaining move count
            dialPos += moveCount
            #If the dial is greater than 99
            if dialPos > 99:
                #Increment the zero count
                zeroCount += 1
                #Mod the dial position to wrap it back around into the 0-99 range
                dialPos = dialPos % 100

#Print the result
print(zeroCount)