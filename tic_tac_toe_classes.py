#Python Tic Tac Toe game created by Sergio M. 

#Import random package or random PC choices. 
import random

#class for Board
class Board:
    def __init__(self):
        self.board = {i: ' ' for i in range(1, 10)}  # Board positions 1-9
    
    #prints the current board
    def print_board(self):
        b = self.board
        print(f" | {b[1]} | {b[2]} | {b[3]} |")
        print(" ------------- ")
        print(f" | {b[4]} | {b[5]} | {b[6]} |")
        print(" ------------- ")
        print(f" | {b[7]} | {b[8]} | {b[9]} |")
    
    #updates the board with position and symbol
    def update(self, position, symbol):
        self.board[position] = symbol
    
    #gets list of available positions
    def get_available_positions(self):
        return [pos for pos, val in self.board.items() if val == ' ']
    
    #checks to see if there is a player has 3 in a row. 
    def check_winner(self):
        winning_combos = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical
            [1, 5, 9], [3, 5, 7]              # Diagonal
        ]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    #checks to see if the board is full
    def is_full(self):
        return all(val != ' ' for val in self.board.values())

#initiates the Player class
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    #Gets available positions and asks the Player to select a move. 
    def make_move(self, board):
        while True:
            try:
                position = int(input(f"{self.name}, enter a position (1-9): "))
                if position in board.get_available_positions():
                    return position
                print("Invalid position, please choose an empty spot.")
            except ValueError:
                print("Please enter a valid number.")

#initiates the Computer Class which selects a random spot on the board. 
class ComputerPlayer(Player):
    def make_move(self, board):
        position = random.choice(board.get_available_positions())
        print(f"Computer chooses position {position}")
        return position

#initiates the game class
class Game:
    def __init__(self, player_name):
        self.board = Board()
        self.player = Player(player_name, 'X')
        self.computer = ComputerPlayer("Computer", 'O')
        self.current_turn = self.player
    
    #switch turn from current player to computer
    def switch_turn(self):
        self.current_turn = self.player if self.current_turn == self.computer else self.computer
    
    #starts the game
    def play(self):
        print(f"\nWelcome to Tic Tac Toe, {self.player.name}!")
        while True:
            self.board.print_board()
            position = self.current_turn.make_move(self.board)
            self.board.update(position, self.current_turn.symbol)
            
            if self.board.check_winner():
                self.board.print_board()
                print(f"{self.current_turn.name} wins!")
                break
            elif self.board.is_full():
                self.board.print_board()
                print("It's a tie!")
                break
            
            self.switch_turn()
        self.play_again()

    #checks if the player wants to play again
    def play_again(self):
        response = input("Do you want to play again? (yes or no): ").lower()
        if response == 'yes':
            self.__init__(self.player.name)  # Reset the game with the same player name
            self.play()
        else:
            print("Thanks for playing!")

#runs the Game
player_name = input("Enter your name: ")
game = Game(player_name)
game.play()
