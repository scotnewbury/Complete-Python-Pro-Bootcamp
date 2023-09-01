# Application to calculate the amount of the tip for a given bill
# and after determine what individual's share should be

print ("Welcome to the tip calculator.")

# Grab the needed user input
bill_amount = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
number_of_patrons = int(input("How many people to split the bill? "))

total_bill = bill_amount * (1 + (tip / 100))

portion = total_bill / number_of_patrons

print (f"Each person should pay: ${portion:.2f}")