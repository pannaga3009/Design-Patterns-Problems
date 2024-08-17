"""
Designing a Snake and Ladder board game involves several components that should be 
designed for flexibility and modularity. To start with, it's crucial to gather
specific requirements and constraints to ensure that the design meets the 
expected functionality and can be easily extended or modified in the future.


Design Approach

Entities and Responsibilities:

Board: Represents the game board with configurable size and positions for snakes and ladders.
Player: Represents a player in the game, including their position and turn management.
Dice: Handles dice rolling to generate random numbers.
Game: Manages the game flow, turns, and interactions between players.
Design Patterns

Strategy Pattern: For handling different dice rolling strategies if needed 
(e.g., standard dice, custom dice with different number ranges).
Observer Pattern: To notify players about changes in the game state 
(e.g., when a player’s position changes).
Factory Pattern: For creating different types of snakes, ladders, and boards if 
variations are required.
Command Pattern: To handle player actions like rolling the dice or moving pieces, 
which allows for easy extension or modification of player actions.
Class Design

Board Class
Manages the layout of the board, including snakes and ladders.
Allows for configuration of board size and positions.

Player Class
Manages player position and turn.

Dice Class
Handles dice rolling.

Game Class
Manages the game flow and interactions.
"""

class Board:
    def __init__(self, size):
        """
        Initialize the board with a given size.
        :param size: The number of cells on the board.
        """
        self.size = size  # Stores the size of the board
        self.snakes = {}  # Dict to store the snake positions: {head: tail}
        self.ladders = {}  # Dict to store ladder positions: {bottom: top}

    def add_snake(self, start, end):
        """
        Add a snake to the board.
        :param start: The position of the snake's head (where the snake starts).
        :param end: The position of the snake's tail (where the snake ends).
        """
        self.snakes[start] = end

    def add_ladder(self, start, end):
        """
        Add a ladder to the board.
        :param start: The position of the ladder's bottom (where the ladder starts).
        :param end: The position of the ladder's top (where the ladder ends).
        """
        self.ladders[start] = end

    def get_new_position(self, position):
        """
        Get the new position of a player after moving.
        :param position: The current position of the player.
        :return: The new position after considering snakes and ladders.
        """
        if position in self.snakes:  # Check if the current position is in snake's head.
            return self.snakes[position]  # Move the player to the snake's tail
        elif position in self.ladders:  # Check if the current position is at the bottom of the ladder
            return self.ladders[position]  # Move the player to the top of the ladder
        return position  # If no snake or ladder, the position remains the same


class Player:
    def __init__(self, name):
        """
        Initialize a player with a name and starting position.
        :param name: The player's name.
        """
        self.name = name
        self.position = 0  # Start at the beginning of the board

    def move(self, steps):
        """
        Move the player forward by a certain number of steps.
        :param steps: The number of steps to move the player.
        """
        self.position += steps


import random


class Dice:
    """
    Handles dice rolling.
    """
    def roll(self):
        """
        Roll the dice to generate a random number between 1 and 6.
        :return: The result of the dice roll.
        """
        return random.randint(1, 6)


class Game:
    """
    Manages the game flow and interactions between players.
    """
    def __init__(self, board, players):
        """
        Initialize the game with a board and a list of players.
        :param board: The game board.
        :param players: A list of players participating in the game.
        """
        self.board = board
        self.players = players
        self.current_player_index = 0  # Start with the first player

    def play_turn(self):
        """
        Simulate a single turn of the game.
        :return: Boolean indicating if the game has ended with a winner.
        """
        player = self.players[self.current_player_index]
        dice_roll = Dice().roll()
        player.move(dice_roll)
        new_position = self.board.get_new_position(player.position)
        player.position = new_position
        print(f"{player.name} rolled a {dice_roll} and moved to position {player.position}")

        # Check if the player has won
        if player.position >= self.board.size:
            print(f"{player.name} has won the game!")
            return True

        # Move to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return False


if __name__ == "__main__":
    """
    Key Points:
    Board: Manages the positions of snakes and ladders and provides the logic for moving players.
    Player: Represents a player, keeping track of their position on the board.
    Dice: Handles the randomness of dice rolls.
    Game: Manages the flow of the game, including player turns, movement, and checking for a winner.

    Design Patterns:
    Strategy Pattern could be applied if you want different dice rolling strategies.
    Observer Pattern could be useful if you want to notify players of changes, like when a player lands on a snake or ladder.
    Command Pattern could be applied to encapsulate player actions (like rolling the dice) and handle them uniformly.
  
    """
    # Create a board of size 100
    board = Board(100)

    # Add snakes (from head to tail)
    board.add_snake(14, 7)
    board.add_snake(31, 26)
    board.add_snake(78, 39)
    board.add_snake(98, 79)

    # Add ladders (from bottom to top)
    board.add_ladder(3, 22)
    board.add_ladder(5, 8)
    board.add_ladder(11, 26)
    board.add_ladder(20, 29)
    board.add_ladder(17, 95)

    # Create players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player3 = Player("Player 3")

    # Create a game with the board and players
    game = Game(board, [player1, player2, player3])

    # Play the game until there's a winner
    winner = False
    while not winner:
        winner = game.play_turn()

