student_scores = {
    "Harry": 81,
    "Ron": 76,
    "Hermione": 73,
    "Draco": 70,
    "Nerville": 65
}

## Create the Empty Dictionaries:
student_grades = {}

for score in student_scores:
    final_score = student_scores[score]
    if 91 <= final_score <= 100:
        student_grades[score] ="Outstanding"
        print(f"{score},Your score of {final_score} is Outstanding.")
    elif 81 <= final_score <= 90:
        student_grades[score] = "Exceed Expectation"
        print(f"{score},Your score of {final_score} has Exceed Expectation.")
    elif 71 <= final_score <= 80:
        student_grades[score] ="Acceptable"
        print(f"{score},Your score of {final_score} is Acceptable.")
    else:
        student_grades[score] ="You have failed"
        print(f"{score},Your score of {final_score} have Failed.")
print(student_grades)
