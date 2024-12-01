import csv

list1 = []
list2 = []

with open('1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        list1.append(row[0])
        list2.append(row[1])

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    total += abs(int(list1[i]) - int(list2[i]))

simScore = 0

for number1 in list1:
    count = 0
    for number2 in list2:
        if number1 == number2:
            count += 1
    simScore += int(number1) * count

print(total)
print(simScore)