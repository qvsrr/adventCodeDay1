# part 1
file = open("inputday2.txt")
arrayOfInputs = file.readlines()
file.close()

data = []

# turns .txt into an array of arrays
for line in arrayOfInputs:
    numbers = []
    for num in line.split():
        numbers.append(int(num))
    data.append(numbers)

# defines the function to check if it's increasing/decreasing
def safety(line):
    increasing = line[0] < line[1]
    for i in range(len(line)-1):
        if increasing == True and line[i+1]-line[i] <= 0:
            return False
        elif increasing == False and line[i+1]-line[i] >= 0:
            return False
        elif abs(line[i+1]-line[i]) > 3:
            return False
    return True

safetyCount = 0

for testCase in data:
    if safety(testCase) == True:
        safetyCount += 1

print(safetyCount)

# part 2

safetyCount = 0

for testCase in data:
    line = testCase[:]
    for i in range(len(line)):
        del line[i]
        if safety(line) == True:
            safetyCount += 1
            break
        line = testCase[:]

print(safetyCount)