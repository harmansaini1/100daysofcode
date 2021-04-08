#Tip Calculator
print("Welcome to tip calculator.")
totalbill = input("What was the total bill?\n")
float_totalbill = float(totalbill)
tip = input("How much tip you want to give? 12, 15, 17?")
float_tip = float(tip)
total_tip = (float_tip / 100)*float_totalbill
#total_percent_tip = total_tip*float_totalbill
billwithtip = total_tip + float_totalbill
persons = input("In how much persons do you want to split the bill?\n")
int_persons = int(persons)
billbyeach = billwithtip/int_persons
billtopay_by_each = print("Each Person should pay ", round(billbyeach, 2))