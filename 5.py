import math

with open("5rules.txt", 'r') as file:
    rules = [list(map(int, line.strip().split('|'))) for line in file]

with open("5pages.csv", 'r') as file:
    manuals = [list(map(int, line.strip().split(','))) for line in file]

total = 0


####### PART 1 #######

# for manual in manuals:
#     validFlag = True
    
#     for rule in rules:
#         if rule[0] in manual and rule[1] in manual:
#             if manual.index(rule[0]) > manual.index(rule[1]):
#                 validFlag = False
#                 break

#     if validFlag:
#         total += int(manual[math.floor(len(manual)/2)])



####### PART 2 #######

for manual in manuals:
    validFlag = False
    
    for _ in range(5):
        for rule in rules:
            if rule[0] in manual and rule[1] in manual:
                if manual.index(rule[0]) > manual.index(rule[1]):
                    print(manual)
                    print(rule)
                    manual.insert(manual.index(rule[0]),manual.pop(manual.index(rule[1])))
                    validFlag = True
                    print(manual)
                    print("")

    if validFlag:
        total += int(manual[math.floor(len(manual)/2)])

print(total)