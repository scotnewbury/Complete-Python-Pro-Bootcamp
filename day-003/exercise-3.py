# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

divisible_by_4 = year % 4
divisible_by_100 = year % 100
divisible_by_400 = year % 400

if divisible_by_4:
    print("Not leap year.")
elif not divisible_by_100:
    if not divisible_by_400:
        print("Not leap year.")
    print("Not leap year.")
else:
    print("Leap year.")
