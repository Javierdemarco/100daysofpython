# Exercise 1
number = input("What number do you want to be added: ")
print("The Added digits are: " + str(int(number[0]) + int(number[1])))

# Exercise 2
weight = float(input("What is your weight (kg): "))
height = float(input("What is your height (m): "))
print("Your BMI is: " + str(round((weight / height ** 2), 3)))

# Exercise 3
age = input("What is your age? ")
years = 90 - int(age)
months = round (years * 12)
weeks = round (years * 52)
days = round (years * 365)
print(f"You have {days} days, {weeks} and {months} months left.")
