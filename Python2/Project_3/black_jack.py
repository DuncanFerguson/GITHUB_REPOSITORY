# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Assignment 2: Counting Characters
# Date: 2/11/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

import random
import deck_classes

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


def settable():
    """This Function Sets up the table."""
    table = {}
    players = input("How Many Players? ")
    for player in range(int(players)):
        table[player] = []
    return table


def countcards(player):
    """ Count's a players cards"""
    z = 0
    for i in player:
        z += i[0]
        if z > 21:
            print("Bust")
            bust = "n"
        else:
            bust = "y"
    return bust
    print("Hand Equals: ", z)


def deal_more_cards(players, delt_deck):
    """ This is the function to run the logic around for dealing the cards"""
    for player in players:
        hit = "y"
        bust = "no"
        while hit != "n" or bust = "y":
            print("Player: ", player)
            hit = countcards(players[player])
            hit = input("Would You Like Another Card? (Y/N)")
            if hit == "y":
                extra_card = random.sample(delt_deck, 1)
                players[player] += extra_card
                print("Player", players[player])
            else:
                pass


def deal_game():
    """This Function deals the game"""
    players = settable()
    dealer = deck_classes.create_deck()
    delt_deck = dealer.deck
    for player in players:
        ##TODO pop the card off the deck
        delt_hand = random.sample(delt_deck, 2)
        players[player] = delt_hand
    deal_more_cards(players, delt_deck)

    # print(players)



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
<<<<<<< HEAD:black_jack.py

#Testing Push
=======
>>>>>>> 0e733a5c1746c659042cac5658a7988ee0e0f6c9:Project_3/black_jack.py
