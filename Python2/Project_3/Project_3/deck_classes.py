
## TODO A card class to keep track of the card details (suit / color, value, etc.)
class create_deck:
    """This Class creates a new deck"""
    suits = ["Diamonds","Spades","Hearts","Clubs"]
    deck = []
    for suit in suits:
        for i in range(1,14):
            deck.append([i,suit])
    # return(deck)


##TODO Comments noting any time you use an alias, reference, deep copy, or shallow copy (likely drawing cards or other interactions)


##TODO (4pt) The project is uploaded correctly to your git repository

##TODO (10pt) This criterion is linked to a Learning OutcomeComments on Aliases, References, Shallow Copies, and Deep copies
## You commented on EACH occurrence of the above topics
