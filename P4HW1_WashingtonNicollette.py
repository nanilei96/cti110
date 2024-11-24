# Nicollette Washington
# P4HW1
# 11/7/2024
# Reprograming an old assignment to use loops and display a letter grade.

scores = []

# Get scores
for i in range(1, 6):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Score should be between 0 and 100")
        except ValueError:
            if i == 3:
                print("Invalid Score entered. Please enter Score #3 again.")
            else:
                print("Invalid Score entered!!!")

# Calculate results
lowest_score = min(scores)
modified_list = [score for score in scores if score != lowest_score]
scores_average = sum(modified_list) / len(modified_list)

# Get grade
if scores_average >= 90:
    grade = "A"
elif scores_average >= 80:
    grade = "B"
elif scores_average >= 70:
    grade = "C"
elif scores_average >= 60:
    grade = "D"
else:
    grade = "F"

# Print Results
print("--------------Results------------")
print(f"Lowest Scores : {lowest_score:.1f}")
print(f"Modified List : {[float(x) for x in modified_list]}")
print(f"Scores Average: {scores_average:.2f}")
print(f"Grade         : {grade}")
