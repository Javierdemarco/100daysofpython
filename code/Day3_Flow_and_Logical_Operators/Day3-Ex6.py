# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
name_combined = name1.lower() + name2.lower()
true_string_for = 0
love_string_for = 0
true_string_if = 0
love_string_if = 0

print(" -------- FOR METHOD --------")

for token in "true":
    true_string_for += name_combined.count(token)
for token in "love":
    love_string_for += name_combined.count(token)

score_for = int(str(true_string_for) + str(love_string_for))

if score_for <= 10 and score_for >= 90:
    print(f"Your scre is {score_for}, you go together like coke and mentos.")
elif score_for >= 40 and score_for <= 50:
    print(f"Your scre is {score_for}, you are alright together.")
else:
   print(f"Your scre is {score_for}")

print ("------- IF METHOD -------")
true_string_if += name_combined.count("t")
true_string_if += name_combined.count("r")
true_string_if += name_combined.count("u")
true_string_if += name_combined.count("e")

love_string_if += name_combined.count("l")
love_string_if += name_combined.count("o")
love_string_if += name_combined.count("v")
love_string_if += name_combined.count("e")

score_if = int(str(true_string_if) + str(love_string_if))

if score_if <= 10 and score_if >= 90:
    print(f"Your scre is {score_if}, you go together like coke and mentos.")
elif score_if >= 40 and score_if <= 50:
    print(f"Your scre is {score_if}, you are alright together.")
else:
   print(f"Your scre is {score_if}")
