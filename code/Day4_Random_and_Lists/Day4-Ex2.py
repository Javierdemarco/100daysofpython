# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Random method
import random

names_size = len(names) - 1
number = random.randint(0, names_size)
print(f"{names[number]} is goint to buy the meal today!")

# Choice method
print(f"{random.choice(names)} is going to buy the meal today!")
