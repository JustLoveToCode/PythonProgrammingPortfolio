# Getting the User Input Here:
date = input("Enter today Date in DD-MM-YYYY:\n")
mood = input("How do you rate your mood today from 1 to 10?\n")
thought = input("Write down your thought for today:\n")

# Open the file which is called f " ./journal/{date}.txt" with 'w' Method:
# with keyword is used for File Handling Purposes:
# Once the code is executed, the file is automatically closed:
with open(f"./journal/{date}.txt", 'w') as file:
    # This is the First Line:
    file.write('This is my mood: ' + mood + 2 * '\n')
    # This is the Second Line:
    file.write(thought)
