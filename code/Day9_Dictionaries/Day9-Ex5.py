#HINT: You can call clear() to clear the output in the console.
import art
dict = {}
person = ""
bid = 0
bidding_finished = False

def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for person in dict:
        if dict[person] > highest_bid:
            highest_bid = dict[person]
            winner = person
    print(f"The winner is: {winner}, with {highest_bid}$")

print(art.logo)

while not bidding_finished:
    person = input("What is your name? ")
    bid = int(input("What is your bid? "))
    dict[person] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or 'no' ")
    if continue_bid == "no":
        bidding_finished = True
        find_highest_bidder(dict)
