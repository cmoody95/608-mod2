# 608-mod2
# NWMSU Data Analytics Fundamentals SP21 - Module 2
import random
import statistics
print("\n\n------------ Bonus ------------")

grades = random.sample(range(0,100),100)
print("Data: \t", grades, "\n")

print("Count: \t\t", len(grades))
print("Sum: \t\t", sum(grades))
print("Mean: \t\t", statistics.mean(grades))
print("Median: \t", statistics.median(grades))
print("Mode: \t\t", statistics.mode(grades))