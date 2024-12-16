file = open("input.txt")

def dec(report):
    false_level_count = 0
    i = 0
    while i < len(report)-1:
        i += 1
        if not (report[i-1] > report[i] and report[i-1] - report[i] <= 3):
            report.pop(i)
            false_level_count += 1
            i = 1
        if false_level_count > 1:
            return False
    return True

def inc(report):
    false_level_count = 0
    i = 0
    while i < len(report)-1:
        i += 1
        if not (report[i-1] < report[i] and report[i] - report[i-1] <= 3):
            report.pop(i)
            false_level_count += 1
            i = 1
        if false_level_count > 1:
            return False
    return True

safe_count = 0

for line in file:
    report = [int(i) for i in line.split()]
    if report[0] > report[1]:
        if dec(report):
            safe_count += 1
    elif report[0] < report[1]:
        if inc(report):
            safe_count += 1
    
print(safe_count)
