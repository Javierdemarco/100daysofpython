#!/usr/bin/env python3

tip_values = [10, 12, 15]
pay_value = 0
flag = False
percentage_value = 0
print("Welcome to the tip calculator.")
bill_value = float(input("What was the total bill? $"))
people = float(input("How many people to split the bill? "))
while(flag != True):
   percentage_value = float(input("What percentage top would you like to give? 10, 12 or 15? "))
   if percentage_value in tip_values:
       flag = True
       break
   print("Not a correct number")
pay_value = bill_value / people + (bill_value / people) * (percentage_value / 100)
print("Each person should pay: $" + str(pay_value))
