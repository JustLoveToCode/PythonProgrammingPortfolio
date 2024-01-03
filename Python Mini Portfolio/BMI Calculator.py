# This is the string type:
height = input("Enter your Height in meters: \n")
# This is the string type:
weight = input("Enter your Weight in kg: \n")


BMI = round(int(weight)/float(height) ** 2)
print(BMI)


if BMI < 18.5:
    print(f"You are underweight, your bmi is {BMI}")
elif 18.5 < BMI <= 25:
    print(f"You have a Normal Weight, your bmi is {BMI}")
elif 25 < BMI <= 35:
    print(f"You are Overweight, your bmi is {BMI}")
elif 30 < BMI <= 35:
    print(f"You are Obese, your bmi is {BMI}")
else:
    print(f"You are Clinically Obese, your bmi is {BMI}")


