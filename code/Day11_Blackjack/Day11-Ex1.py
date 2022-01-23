############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
import random

from art import logo


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def giveCard(hand):
    ranN = random.randint(0, len(deck) - 1)
    hand.append(deck[ranN])


def calculateHandScore(hand):
    score = 0
    for card in hand:
        score += card
    return score


def showGameState(player, dealer):
    print(f"Your Cards: {player}, current score {calculateHandScore(player)}")
    print(f"Computer's first card: {dealer[0]}")


def showGameFinalState(player, dealer):
    print(f"Your Cards: {player}, current score {calculateHandScore(player)}")
    print(f"Computer Cards: {dealer}, current score {calculateHandScore(dealer)}")


def dealerPlays(dealerHand, playerScore):
    score = calculateHandScore(dealerHand)
    while score < 21:
        if score >= playerScore:
            return score
        if score < 17 or score < playerScore:
            giveCard(dealerHand)
            score = calculateHandScore(dealerHand)
    return score


def game():
    # Define variables
    moreCardsFlag = True
    playerHand = []
    playerScore = 0
    dealerHand = []
    dealerScore = 0

    if input("Do you want to play a game of Blackyack? (yes or no) ") == "no":
        return
    print(logo)
    # Give Initial Cards
    for _ in range(0, 2):
        giveCard(playerHand)
        giveCard(dealerHand)
    # Show initial status
    showGameState(playerHand, dealerHand)

    while moreCardsFlag:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
            moreCardsFlag = False
        else:
            giveCard(playerHand)
            showGameState(playerHand, dealerHand)
        playerScore = calculateHandScore(playerHand)
        if playerScore > 21:
            print("Computer Wins!")
            return
    dealerScore = dealerPlays(dealerHand, playerScore)
    showGameFinalState(playerHand, dealerHand)
    if dealerScore > 21:
        print("Player Wins!")
        return
    if playerScore > dealerScore:
        print("Player Wins!")
        return
    else:
        print("Computer Wins!")
        return


game()
