import random

# This is a game of Black Jack. There are Card, Deck, Table and Hand Classes.
# The Program starts with dealgame. A player is asked if they would like to play the game and how many players
# They would like to add. After which those players are asked for their name into the Table Class.
# After the players are entered. The Game Begins. The dealer calls up the deck function, shuffles and deals each player
# Two cards into their hand. The table is then called up. And each player goes through the hit loop
# function. The dealer goes first due to his spot on the list.
# The dealer will automatically hit until he or she gets 17. After the dealer will stay.
# The rest of the players will then continue to hit through the loophit function. If they bust or get 21 or choose to
# Stay they get out of the loop

class Card:
    """ Card Class to keep track of the card details (suit/color, value, etc."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

##Display The Face Cards
    def __str__(self):
        """Displaying the cards face values"""
        displayval = str(self.value)  # shallow copy for the purpose of display
        if self.value == 1: displayval = "Ace"
        elif self.value == 11: displayval = "Jack"
        elif self.value == 12: displayval = "Queen"
        elif self.value == 13: displayval = "King"
        return displayval + " of " + self.suit


class Deck:
    """ Building a Deck out of the Cards"""
    def __init__(self):
        """Storying a Deck of Cards"""
        self.cards = []  # Class list of cards make up the deck
        self.create_deck()

    def create_deck(self):
        """Making a normal 52 card deck. Ace counting as 1"""
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))  # Appending individual cards to self.cards list

    def shuffle(self):
        """Shuffling the Deck three times. It is more of a wash pile shuffle than
        traditional"""
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)

    def show_deck(self):
        """This function shows the cards that are in the self.cards list. Primarily used for testing reasons"""
        for card in self.cards:
            card.show()

    def deck_count(self):
        """This function counts the amount of cards that are in the deck. It is used primarily for testing reasons"""
        print(len(self.cards))

    def dealcard(self):
        """Deal a card and pop it off of the deck"""
        return self.cards.pop()


class Table:
    """Creating a class of Players"""
    players = ["Dealer"]  # Every Game Must Have a Dealer!

    def __init__(self, player):
        """Adding Players to the table. This is a list of 'strings' """
        self.players.append(player)  # Adding Player to Table

    def return_table(self):
        """This function returns the list of players. """
        return self.players


class Hand:
    def __init__(self, nam):
        """The hand class is composed of a name, a list of cards, a card value count, and an ace card count"""
        self.name = nam  # Naming the players hand
        self.cards = []  # No Cards in the hand to start
        self.value = 0  # Hand Starts with a count of zero
        self.ace_count = 0  # Adding in count for aces

    def add_card(self, card):
        """Adding the value of the card. All face cards are 10. Ace's are either 1 or 11 depending on the count"""
        self.cards.append(card)  # Add a card to the hand
        if 1 < card.value < 11: self.value += card.value
        elif card.value == 13: self.value += 10
        elif card.value == 12: self.value += 10
        elif card.value == 11: self.value += 10
        elif card.value == 1:  # Dealing with the aces
            self.value += 11
            self.ace_count = 1
        if self.ace_count == 1 and self.value > 21:
            self.value -= 10
            self.ace_count = 0


def show_hand(player, name):
    """Showing the Players Hand"""
    print(name, "Cards: ")
    for card in player.cards:
        print(card)
    print("Total Count:", player.value, "\n")


def loophit(hittinghand, name, deck):
    """Loop Hit is the process of a player deciding to stay or add a card. If they add to many cards that add to
    a value over 21 they bust. In this function the dealer goes first. The dealer will continue to hit until the
    dealer has a hand of 17 after this the dealer will stay. The next up will be the players prompted. The loop
    is composed of the players hand, name, and the deck of cards."""
    keephitting = True  # Adding a loop to keep the function going while the player wants to continue
    while keephitting:
        if hittinghand.value == 21:  # 21 is an automatic win
            return hittinghand.value
        elif hittinghand.value > 21:  # If the hand is over 21 return 0. Indicating a loss.
            print(name, "Busts\n")
            return 0
        elif hittinghand.value < 21:
            if name == "Dealer" and hittinghand.value < 17:  # Dealer Auto hits unless at 17
                hittinghand.add_card(deck.dealcard())  # Calling a card from the deck
                print("Dealer Hits\n")
                show_hand(hittinghand, name)  # Displaying the hand
                pass
            elif name == "Dealer" and hittinghand.value >= 17:
                print("Dealer Stays\n")
                return hittinghand.value
            else:
                h_n = input("Would you Like another Card (Y/N)?\n")  # Player input for deciding to add a card
                if h_n.lower() == "y":
                    hittinghand.add_card(deck.dealcard())  # Calling a card from the deck
                    show_hand(hittinghand, name)  # Displaying the hand.
                elif h_n.lower() == "n":
                    print(name, "Stays\n")
                    return hittinghand.value  # returning the value of the hand class


def scoretable(game_dict):
    """This function scores the table and determines the winner. If there is a tie the Dealer Wins!"""
    # Printing out the game results.
    for val in game_dict:
        if game_dict[val] == 0: print(val, ": Bust")
        else: print(val, ":", game_dict[val])

    # Finding The winning hand. If there is a tie the dealer wins.
    winning_hand = max(list(game_dict.values()))  # Picking the winning Hand
    for player in game_dict:
        if game_dict[player] == winning_hand:
            if player == "Dealer":
                print(player, "wins with", winning_hand)
                break
            else:
                print(player, "wins with", winning_hand)


def dealgame():
    """This is the main function of the game. It starts with an empty dictionary and asks for the user input.
    The number of players are selected. Those are then put into the seat table class. From there the dealer
    creates the deck and then shuffles it. The dealer then hits his own hand. Then subsequent players. """
    member_score_dict = {}  # Blank Dictionary for keeping score
    try:
        playgame = input("Would You Like To Play Black Jack (Y/N)?")  # Starting the game.
    except: pass  # If y is not entered the game ends

    if playgame.lower() == "y":
        deck = Deck()  # Creating the deck from the deck class
        deck.shuffle()  # Shuffling the cards from the deck class
    else:
        print("Good Bye")
        exit()

    # Number of player input
    while True:
        try:
            num_players = int(input("How Many Players? "))
            break
        except ValueError: print("Not a valid Integer")

    # Setting the table with that amount of players. Asking each for their name.
    for seat in range(num_players):
        seat = Table(input("Enter Player Name: "))  # Calling in the stable Class

    # Dealing deck for players in game
    for member in seat.return_table():
        member_hand = Hand(member)  # Deep Copy
        member_hand.add_card(deck.dealcard())  # Initial Dealing Card
        member_hand.add_card(deck.dealcard())  # Initial Dealing Card
        show_hand(member_hand, member)  # Displaying the and
        member_score_dict[member] = loophit(member_hand, member, deck)  # Running through the hit loop
    scoretable(member_score_dict)  # Calling up the End Game Score
    print("Game Over\n")


def main():
    """Starting the Game by running dealgame"""
    dealgame()


if __name__ == "__main__":
    main()
