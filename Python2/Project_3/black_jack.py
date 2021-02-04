# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Assignment 2: Counting Characters
# Date: 2/11/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

import random
import deck_classes

class create_deck:
    """This Class creates a new deck"""
    suits = ["Diamonds","Spades","Hearts","Clubs"]
    deck = []
    for suit in suits:
        for i in range(1,14):
            deck.append([i,suit])

def display_hand(cards):
    """This deff prints numerated as string w/ faces cards"""
    for card in cards:
        if card[0] == 1:
            card[0] == "Ace"
        elif card[0] == 11:
            card[0] == "Jack"
        elif card[0] == 12:
            card[0] == "Queen"
        elif card[0] == 13:
            card[0] == "King"
        elif card[0] == 14:
            card[0] = "Ace"
        else:
            card[0] = str(card[0])

        print(card[0], "of", card[1])


def deal_game():
    """This Function deals the game"""
    players = input("How Many Players? ")
    dealer = create_deck()
    delt_deck = dealer.deck

    delt_hand = random.sample(delt_deck, 2)
    display = display_hand(delt_hand)
# print(delt_hand)

def main():
    """This main function allows the code to be run through the command line. It will also print out the dictionary
    that is returned from search flags in csv format"""
    ## Can search the comand line with set up
    # args = sys.argv[1:]
    # d = searchflags(args)
    deal_game()

## If the name is main. Run the main Function
if __name__ == "__main__":
    main()