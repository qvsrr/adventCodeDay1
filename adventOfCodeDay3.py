# part 1
import re

f = open("inputday3.txt")
mull = f.read()
f.close()

mul = re.findall(r"mul\((\d+),(\d+)\)", mull)

total = 0

for i in mul:
    total += int(i[0])*int(i[1])

print(total)

# part 2

dodont = re.split(r"(do\(\))|(don't\(\))", mull)

doOrDont = True
total = 0

for set in dodont:
    if set == None:
        continue
    if set == "don't()":
        doOrDont = False
    elif set == "do()":
        doOrDont = True
    if doOrDont == True:
        mul = re.findall(r"mul\((\d+),(\d+)\)", set)
        for i in mul:
            total += int(i[0])*int(i[1])

print(total)