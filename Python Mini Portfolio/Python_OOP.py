class Question:
    def __init__(self, q_text, q_answer):
        # q_text come from the def __init__:
        self.text = q_text
        # q_answer come from the def __init__:
        self.answer = q_answer


# Instantiating an Object from the Class Blueprint:
question_1 = Question("2+3=5", "True")
question_2 = Question("5*3=15", "True")

print(question_1.text)
print(question_1.answer)
print(question_2.text)
print(question_2.answer)
