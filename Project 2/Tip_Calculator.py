#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Gather input from user
print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

#Calculate the total amount of the bill to be paid
total_bill = bill + ((tip / 100) * bill)

#Ask how many people the bill has to be split into
people = int(input("How many people to split the bill? "))

#Round and present the final amount to be paid per person
bill_per_person = total_bill / people
final_amount = round (bill_per_person , 2)

print(f"Each person should pay: ${final_amount}")



