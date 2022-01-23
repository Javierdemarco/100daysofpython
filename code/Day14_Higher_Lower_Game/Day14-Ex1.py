# Higher or Lower
from game_data import data


def compare_followers(guess, first, second):
    if first > second:
        return guess == "A"
    else:
        return guess == "B"


def print_compare(data):
    return f"{data['name']}, a {data['description']}, from {data['country']}"


def game():
    score = 0
    game_continues = True
    compare_a = {}
    compare_b = {}
    print("Welcome to Higher or Lower.")
    while compare_a == compare_b:
        compare_a = choice(data)
        compare_b = choice(data)

    while game_continues:
        while compare_a == compare_b:
            compare_b = choice(data)
        print(f"Compare A: {print_compare(data)}")
        print("VS")
        print(f"Compare b: {print_compare(data)}")
        player_selection = input("Who has more followers: Type 'A' or 'B': ")

        is_correct = compare_followers(
            player_selection, compare_a["folower_count"], compare_b["follower_count"]
        )

        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            game_continues = False
            print(f"Sorry, that is wrong. Final Score: {score}")


game()
