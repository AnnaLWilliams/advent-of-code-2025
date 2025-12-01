dialPos = 50
zeroCount = 0
import os
print (os.getcwd())
#with open("day-1-secret-entrance/input/inputTest.txt") as fin:
with open("input/inputTest.txt") as fin:
    for line in fin:
        moveCalc = int(line[1:])
        while moveCalc >= 100:
            zeroCount += 1
            moveCalc -= 100
            
        if line[0] == "L":
            dialPos -= int(line[1:])
            if dialPos < 0:
                zeroCount += 1
                dialPos = dialPos % 100
        elif line[0] == "R":
            dialPos -= int(line[1:])
            if dialPos > 0:
                zeroCount += 1
                dialPos = dialPos % 100
print(zeroCount)