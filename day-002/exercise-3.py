# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Convert age to an integer
age = int(age)

# Determine maximum days, weeks, and months based on a max year value
maxYears = 90
maxMonths = maxYears * 12
maxWeeks = maxYears * 52
maxDays = maxYears * 365

# Determine remaining time

remainingMonths = maxMonths - (age * 12)
remainingMWeeks = maxWeeks - (age * 52)
remainingDays = maxDays - (age * 365)


print(f"You have {remainingDays} days, {remainingMWeeks} weeks, and {remainingMonths} months left.")