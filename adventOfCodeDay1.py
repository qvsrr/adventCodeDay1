# part 1
file = open("inputday1.txt")
arrayOfInputs = file.readlines()
file.close()

list1 = []
list2 = []

for line in arrayOfInputs:
    left, right = line.strip().split()
    list1.append(int(left))
    list2.append(int(right))

list1.sort()
list2.sort()

answer = 0
for i in range(len(list1)):
    answer += abs(list1[i] - list2[i])

print(answer)

# part 2
similarity = 0

for i in range(len(list1)):
    count = list2.count(list1[i])
    similarity += count * list1[i]
    count = 0
print(similarity)