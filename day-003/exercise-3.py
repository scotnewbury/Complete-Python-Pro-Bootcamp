# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

print(f"The year is: {year}")

divisible_by_4 = year % 2
divisible_by_100 = year % 100
divisible_by_400 = year % 400

print(f"Divisible by   4 is {divisible_by_4}")
print(f"Divisible by 100 is {divisible_by_100}")
print(f"Divisible by 400 is {divisible_by_400}")

if divisible_by_4:
    print("Not leap year - not divisible by 4.")
elif not divisible_by_100:
    if not divisible_by_400:
        print("Not leap year - divisible by 400.")
    print("Not leap year - divisible by 100.")
else:
    print("Leap year.")
