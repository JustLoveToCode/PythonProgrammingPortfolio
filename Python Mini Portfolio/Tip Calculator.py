print("Welcome to the Tip Calculator")

bill = float(input("What is the Total Bill?\n"))
tip = int(input("How much tip would you like to give? \n"))
people = int(input("How many people to split the bill\n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay {final_amount} dollars ")

