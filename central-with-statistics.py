# 608-mod2
# NWMSU Data Analytics Fundamentals SP21 - Module 2

import statistics

print("\n\n------------ Central With Statistics ------------")
grades = [85, 93, 45, 89, 85]
print("Data: \t\t", grades)

count = len(grades)
s = sum(grades)
mean = statistics.mean(grades)
median = statistics.median(grades)
mode = statistics.mode(grades)

print("Count: \t\t", count)
print("Sum: \t\t", s)
print("Mean: \t\t", mean)
print("Median: \t", median)
print("Mode: \t\t", mode, "\n\n")