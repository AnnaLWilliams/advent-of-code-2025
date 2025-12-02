dialPos = 50
zeroCount = 0
import os
print (os.getcwd())
with open("day-1-secret-entrance/input/input.txt") as fin:
    for line in fin:
        moveCalc = int(line[1:])
        while moveCalc >= 100:
            zeroCount += 1
            moveCalc -= 100
            
        if line[0] == "L":
            dialPos -= moveCalc
            if dialPos < 0:
                zeroCount += 1
                dialPos = dialPos % 100
        elif line[0] == "R":
            dialPos += moveCalc
            if dialPos > 99:
                zeroCount += 1
                dialPos = dialPos % 100
print(zeroCount)