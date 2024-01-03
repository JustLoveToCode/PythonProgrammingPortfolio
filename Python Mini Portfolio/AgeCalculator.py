age = input("What is your Current Age?")

Converted_Age = int(age)

End_Of_Life = 90

years_remaining = End_Of_Life - Converted_Age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f" You have {days_remaining} days, {weeks_remaining} weeks,"
      f"and {months_remaining} months")
