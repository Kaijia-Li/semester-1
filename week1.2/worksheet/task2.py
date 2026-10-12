# Worksheet 1.2: Task 2 Solution
from util import read_numbers
score = read_numbers()

sorted_score = sorted(score)

minimum = min(score)
print(minimum)
maximum = max(score)
print(maximum)
mean = sum(score) / len(score)
print(mean)
median = sorted_score[len(score)//2]
print(median)
