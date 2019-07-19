import random

# This creates a list of possible moves.
moves = ['rock', 'paper', 'scissors']

# This evaluates if the user's input is a valid choice.


def valid_input(words, options):
    while True:
        choice = input(words).lower()
        for option in options:
            if option in choice:
                return choice
        print("You must've made a typo, try again.")

# This determines if either player has won the game.


def win_check(self):
    if self.p1_score == self.p2_score + 2:
        print("Player 1 wins the game!")
        play_again()
    elif self.p2_score == self.p1_score + 2:
        print("Player 2 wins the game!")
        play_again()

# This asks the user if they would like to play again.


def play_again():
    play = valid_input("Would you like to play again?\n"
                       "Yes or No?\n", ["yes", "no"])
    if "yes" in play:
        new_game = Game(HumanPlayer(), RandomPlayer())
        new_game.play_game()
    elif "no" in play:
        print("Thanks for playing!")
        quit()

# Defines the original player class, with the default move 'rock'.


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# Creates a subclass of player that randomizes its moves.


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# Creates the user subclass.


class HumanPlayer(Player):
    def move(self, valid_input):
        player_move = valid_input("You know how this goes, please choose "
                                  "between Rock, Paper, or Scissors.\n"
                                  "Or type quit to stop playing.\n",
                                  ["rock", "paper", "scissors", "quit"])
        if player_move == "rock":
            return "rock"
        elif player_move == "paper":
            return "paper"
        elif player_move == "scissors":
            return "scissors"
        elif player_move == "quit":
            print("Thanks for playing!")
            quit()

# Creates a subclass that learns player's moves and copies them.


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move

    def move(self):
        if self.their_move is None:
            return Player.move(self)
        else:
            return self.their_move

# Creates a subclass that simply cycles through the moves.


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.my_move = None

    def move(self):
        choice = None
        if self.my_move is None:
            choice = Player.move(self)
        else:
            index = moves.index(self.my_move) + 1
            if index >= len(moves):
                index = 0
            choice = moves[index]
        self.my_move = choice
        return choice

# This creates the Game class.


class Game():

    # Defines the initialization of the game.
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    # Defines how a round is played.
    def play_round(self):
        move1 = self.p1.move(valid_input)
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.beats(move1, move2)

    # Is the actual game function.
    def play_game(self):
        print("Game start!\n")
        round_number = 1
        while win_check(self) is not True:
            print(f"Round {round_number}:")
            self.play_round()
            round_number += 1
        print("Game over!")

    # Function that determines that outcome of a round.
    def beats(self, one, two):
        if (
                (one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock')):
            print("Player 1 Wins the round!")
            self.p1_score += 1
        elif (
                (two == 'rock' and one == 'scissors') or
                (two == 'scissors' and one == 'paper') or
                (two == 'paper' and one == 'rock')):
            print("Player 2 Wins the round!")
            self.p2_score += 1
        elif one == two:
            print("It's a tie!")


# Actually runs the game.
if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
