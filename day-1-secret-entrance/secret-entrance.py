dialPos = 50
zeroCount = 0
import os
print (os.getcwd())
#Debugger Path with open("day-1-secret-entrance/input/input.txt") as fin:
with open("input/input.txt") as fin:
    for line in fin:
        if line[0] == "L":
            dialPos = (dialPos - int(line[1:])) % 100
        elif line[0] == "R":
            dialPos = (dialPos + int(line[1:])) % 100
        if dialPos == 0:
            zeroCount += 1
print(zeroCount)