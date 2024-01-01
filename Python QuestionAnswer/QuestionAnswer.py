import json

with open("./files/questions.json", 'r') as file:
    # This will print out as a string
    content = file.read()

# This will convert into a Dictionary Lists
data = json.loads(content)

# Setting the Initial score to be equal to 0


for question in data:
    # This will return the question when we tried to access the key here
    print(question["question_text"])
    # The alternative is inside the data Lists here
    # Using Nested Loop when there is a list within the list
    for index, alternative in enumerate(question["alternatives"]):
        index = index + 1
        print(index, '-', alternative)
    user_choice = int(input('Enter your Answer?'))

    # Appending the question['user_choice'] to the question dictionary list
    question["user_choice"] = user_choice

    # {'question_text': 'What are Dolphin?', 'alternatives': ['Amphibians', 'Fish', 'Mammals', 'Bird'],
    #  'correct_answer': 3, 'user_choice': 2}

# 2nd Iteration
# enumerate is used to iterate over the sequence
# such as the list or tuple:
score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer: "
    else:
        result = "Wrong Answer: "
    message = f"{index + 1}-{result} Your Answer: {question['user_choice']}, " \
              f"Correct Answer is : {question['correct_answer']}"
    print(message)

# [{"question_text": "What are Dolphin?",
#   "alternatives": ["Amphibians", "Fish", "Mammals", "Bird"],
#   "correct_answer": 3},
#
#  {"question_text": "What Occupies Most of the Earth Surface?",
#   "alternatives": ["Land", "Water"],
#   "correct_answer": 2}]

print(f"Your score is {score} / {len(data)}")

# In this case, the len(data) is equal to 2 here since we have 2 Dictionary
