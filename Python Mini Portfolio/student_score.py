student_scores = input('Input the List of the Student Scores\n').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


# Assign the initial highest_score be equal to 0
highest_score = 0
# Using the for keyword to loop through
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)


