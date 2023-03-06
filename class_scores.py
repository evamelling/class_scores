##
# class_scores.py
# Calculates the mean, lowest and highest scores
# of class_a list and class_b list combined
# Then prints them out
# Author: Eva Melling
# Date: 02.03.2023

# Print the 'Class Scores Part 1'
print("Class Scores Part 1\n")

# Defines class_a list and class_b list
class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

# Combine class_a list and class_b list
combined_list = class_a + class_b

# Create variables
count = 0
total_score = 0

for score in combined_list:
    count += 1
    total_score += score

# Print mean, lowest and highest score
print("The mean score is: {}".format(total_score / count))
print("The lowest score is: {}".format(min(combined_list)))
print("The highest score is: {}".format(max(combined_list)))


