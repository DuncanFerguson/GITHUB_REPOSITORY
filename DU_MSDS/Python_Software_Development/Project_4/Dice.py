import random

# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Project 4: Dice
# Date: 3/4/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

# This program lets a user play a game of dice against a computer.
# The start of the game the user will choose how many sides to the dice.
# The amount of dice, and a starting amount of money. The user will then select how much they would like to wager
# For each round of the game. If the user runs out of money they are prompted to see if they want to play again.
# The winner is determined by the sum of the dice in their cup.
# IF both players roll the same amount, the game is a wash
# Function: User_Inputs, is where the user enters the game variables.
# Function: Dice_rolling is where the user enters wager amounts and game logic
# Class: Dice creates dice based on the size chosen by the user
# Class: Cup_O_Dice creates a cup filled with x amount of the same type of x sided dice
# Notes: The die roll themselves upon creation.


class Dice:
    """This Class is to create a die. The user selects the amount of 'sides'. There is also a roll function that
    will return a random number inbetween 1 and the number of dice."""
    def __init__(self, sides):
        """default constructor"""
        self.sides = sides  # Making sides to dice
        self.die_value = self.roll()  # Rolling the die on creation

    def __str__(self):
        """String Magic Method prints the type of die that is being used"""
        return str("Type of Die: {} sides".format(self.sides))

    def __repr__(self):
        """Shows the rolled die and what it's rolled value was"""
        return "Rolled a {} sided die and received {}".format(self.sides, self.die_value)

    #All comparison magic methods (6 in total listing in slides)
    #All comparisons are looking at the value of the die
    def __eq__(self, other):
        """Shows if the die is equal to another die"""
        return self.die_value == other.die_value

    def __gt__(self, other):
        """Greater than"""
        return self.die_value > other.die_value

    def __ge__(self, other):
        """# Greater than or Equal to >= __ge__"""
        return self.die_value >= other.die_value

    def __ne__(self, other):
        """# Not Equals != __ne__"""
        return self.die_value != other.die_value

    def __lt__(self, other):
        """# Strictly Less Than < __lt__"""
        return self.die_value < other.die_value

    def __le__(self, other):
        """# Less Than or equal to <= __le__"""
        return self.die_value <= other.die_value

    def __add__(self, other):
        """Add two dice together"""
        print("Adding a die that has been rolled {}"
              " to another die rolled {}".format(str(self.die_value), str(other.die_value)))
        return self.die_value + other.die_value

    def roll(self):
        """This function rolls the dice and returns it's new value"""
        self.die_value = random.randint(1, self.sides)  # Randomly picking a value on the die and returning value
        return self.die_value


class CupODice:
    """A cup of dice class which includes a type of sided dice and the number of them. When rolled the rolled_sum
    will add the values of the rolled dice."""
    def __init__(self, sides, numdice):
        """Default constructor"""
        self.gamedice = Dice(sides)
        self.numdice = numdice
        self.cup_w_dice = [self.gamedice for i in range(numdice)]  # A List of dice upon creation
        self.rolled_sum = 0  # Starting the cups value out as zero

    def __str__(self):
        """ String Magic Method"""
        return str("{} dice with {} sides for a total sum of {}"
                   .format(self.numdice, self.gamedice.sides, self.rolled_sum))

    def __repr__(self):
        """ Returns the number of dice and what their rolled sum value is"""
        return "A cup of {} dice\n{}\nRolled sum {}".format(self.numdice, self.gamedice, self.rolled_sum)

    def __add__(self, other):
        """Adding the rolled sum of two cups of dice"""
        print("Adding a cup of {} to a cup {}".format(str(self.rolled_sum), str(other.rolled_sum)))
        return self.rolled_sum + other.rolled_sum

    #All comparison magic methods (6 in total listing in slides)
    #All comparisons are looking at the rolled sum of the cup
    def __eq__(self, other):
        """both rolled sums equal each other"""
        return self.rolled_sum == other.rolled_sum

    def __ne__(self, other):
        """Not Equal to rolled sum"""
        return self.rolled_sum != other.rolled_sum

    def __gt__(self, other):
        """Adding in grater than rolled sum"""
        return self.rolled_sum > other.rolled_sum

    def __ge__(self, other):
        """Greater than or equal to rolled sum"""
        return self.rolled_sum >= other.rolled_sum

    def __lt__(self, other):
        """Less than rolled sum"""
        return self.rolled_sum < other.rolled_sum

    def __le__(self, other):
        """Less than or equal to rolled sume"""
        return self.rolled_sum <= other.rolled_sum

    def roll_cup(self):
        """ Rolling all the dice in the cup and summing their values. Returns the value of the sum of rolled
        dice."""
        self.rolled_sum = 0
        for i in range(len(self.cup_w_dice)):  # Looping through the list of dice objects and rolling them
            self.cup_w_dice[i].roll()  # Die roll
            print(repr(self.gamedice))  # Printing out the Rolled die value
            self.rolled_sum += self.cup_w_dice[i].die_value  # Adding die value to rolled sum
        return self.rolled_sum


def dice_rolling(type_o_die, num_dice, starting_amount):
    """This Function is meant for the rolling of the dice. The user will enter how much money they want to bet.
    You and a computer will both roll the amount of dice, and determine the winner (by sum of dice). If the sum
    is the same the game is a wash. If you run out of money the game ends"""
    #You will choose an amount you are betting on the cup of dice rolling
    wager = 0  # Starting wager of 0
    try:
        wager = int(input("How much of the ${} do you want to best? ".format(starting_amount)))
        if wager > starting_amount:
            print("Nice try, but that's cheating... Good Bye")
            exit()
        elif wager < 1:
            print("Needs to be a positive amount of money")
            dice_rolling(type_o_die, num_dice, starting_amount)
    except ValueError:
        print("Wrong Value typed, Lets try this again.")
        dice_rolling(type_o_die, num_dice, starting_amount)

    print("Roller: You")
    gamecup = CupODice(type_o_die, num_dice)  # Creating a cup of dice
    gamecup.roll_cup()  # Rolling that cup of dice
    print("You rolled", gamecup, "\n")  # Printing out

    print("Roller: The computer")
    computercup = CupODice(type_o_die, num_dice)  # Creating computers cup of dice
    computercup.roll_cup()  # Rolling computers cup of dice
    print("The Computer rolled", computercup, "\n")

    #You will gain or lose the money bet
    if computercup == gamecup:
        print("Game is a Wash")
    elif gamecup < computercup:
        starting_amount -= wager
        print("You lose ${} dollars and now have ${} Total\n".format(wager, starting_amount))
    elif gamecup > computercup:
        starting_amount += wager
        print("You win ${} dollars and now have ${} Total\n".format(wager, starting_amount))
    else:
        print("No Logic hitting")  # Mostly meant for testing purposes

    #You will then choose to bet again or to cash out
    #The game will continue until you cash out or are bankrupt
    if starting_amount <= 0:
        losemoremoney = input("YOU BROKE, Want to play again? (Y/N)")
        if losemoremoney == "y" or losemoremoney == "Y":  # If they don't hit Y it just exits.
            user_inputs()  # Restarting the game from the top
        else:
            exit()

    playagain = str(input("Would you like to test your luck again (Y) or run with the money and cash out (M)? (Y/M): "))
    if playagain == "y" or playagain == "Y":
        dice_rolling(type_o_die, num_dice, starting_amount)  # Restarting with the same variables
    elif playagain == "m" or playagain == "M":  # Cashing out
        print("You have cashed out with ${} dollars. Comeback Again!".format(starting_amount))
    else:
        print("Wrong Entry, Good bye")
        exit()


def user_inputs():
    """This function starts the game and asks the user for the game variabels, how many sided dice,
    how many dice to be included in the game, and the starting amount of money."""
    print("We're going to play a game. But first you must make some choices")
    try:
        type_o_die = int(input("How many sides to the dice? "))  # User input how many dice they are rolling.
        num_o_dice = int(input("How many dice Would you like to use? "))  # User input the Number of sides on the dice.
        starting_amount = int(input("How much money would you like to start with? "))  # Starting Bank Amount
        print("\nGreat! We shall begin!\n")  # Displaying that the game will begin
        dice_rolling(type_o_die, num_o_dice, starting_amount)  # Passing the user_inputs over to dice_rolling
    except ValueError:
        print("Wrong Value type, lets try this again")
        user_inputs()


def test_game():
    """Testing Reason to get rid of user inputs. Mocks user_inputs def. All class logic can be tested here.
    Not all all the logic is used for the game, so this is a good testing space"""
    dice_rolling(6, 2, 100)


def main():
    """The Real main function for starting the code is user_inputs. The start game function is meant for testing."""
    # test_game()  # For Fast Testing
    user_inputs()  # For User input


if __name__ == "__main__":
    main()
