#Write your code below this line 👇
from math import sqrt, ceil
def prime_checker(number):
    prime = True
    if number == 1:
        print("It's a prime number.")
    elif number == 4:
        print("It's not a prime number.")
    else:
        root_number = ceil(sqrt(number))
        for num in range(2, root_number):
            if number % num == 0:
                prime = False
        if prime == False:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
