# 608-mod2
# NWMSU Data Analytics Fundamentals SP21 - Module 2
print("\n\n------------ Central Native ------------")
grades = [85, 93, 45, 89, 85]
print("Data: ", grades)

mean = sum(grades) / len(grades)
print("\t...sorting data...")
grades.sort()

median = grades[int(len(grades)/2)]
s = 0
count = 0

modeDictionary = {}

for val in grades:
    count += 1
    s += val
    if val in modeDictionary.keys(): 
        modeDictionary[val] += 1
    else :
        modeDictionary[val] = 1

mode = []
for val in grades:
    for (k, v) in modeDictionary.items():
        if (v == max(modeDictionary.values())):
            if  (not k in mode):
                mode.append(k)

print("Count: \t\t", count)
print("Sum: \t\t", s)
print("Mean: \t\t", mean)
print("Median: \t", median)
print("Mode: \t\t", mode, "\n\n")