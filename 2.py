import csv

reports = []

with open('2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        reports.append(row)

def checkReport(report):
    report = [int(i) for i in report]

    for i in range(len(report)):
        if i == len(report) - 1:
            return 1
        if abs(report[i] - report[i + 1]) > 3 or abs(report[i] - report[i + 1]) < 1:
            return 0
        
        if report[i] < report[i + 1]:
            for j in range(len(report)):
                if j == len(report) - 1:
                    pass
                elif report[j] > report[j+1]:
                    return 0
        if report[i] > report[i + 1]:
            for j in range(len(report)):
                if j == len(report) - 1:
                    pass
                elif report[j] < report[j+1]:
                    return 0
    return 1

safeCount = 0

for report in reports:
    #safeCount += checkReport(report)

    copyReport = report[:]
    if checkReport(report) == 0:
        print(report)
        for i in range(len(report)):
            newReport = copyReport[:]
            newReport.pop(i)
            print(newReport)
            if checkReport(newReport) == 1:
                safeCount += 1
                break
        print("-----\n")
    else:
        safeCount += 1

print(safeCount)
