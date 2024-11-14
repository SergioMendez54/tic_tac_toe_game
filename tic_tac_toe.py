#Python Tic Tac Toe game created by Sergio M. 

#Import random package for random PC choices. 
import random

#Function to print the board to the Command Line.
def printBoard(board):
    print(f" | {board['t-l']} | {board['t-m']} | {board['t-r']} |")
    print(" ------------- ")
    print(f" | {board['m-l']} | {board['m-m']} | {board['m-r']} |")
    print(" ------------- ")
    print(f" | {board['b-l']} | {board['b-m']} | {board['b-r']} |")

#Checks to see if someone has 3 in a row. 
def checkThree(board):
    #Check horizontals
    if board['t-l'] == board['t-m'] == board['t-r'] != ' ':
        return True
    elif board['m-l'] == board['m-m'] == board['m-r'] != ' ':
        return True
    elif board['b-l'] == board['b-m'] == board['b-r'] != ' ':
        return True
    #Check verticals
    elif board['t-l'] == board['m-l'] == board['b-l'] != ' ':
        return True
    elif board['t-m'] == board['m-m'] == board['b-m'] != ' ':
        return True
    elif board['t-r'] == board['m-r'] == board['b-r'] != ' ':
        return True
    #check diagonals
    elif board['t-l'] == board['m-m'] == board['b-r'] != ' ':
        return True
    elif board['b-l'] == board['m-m'] == board['t-r'] != ' ':
        return True
    #Else if no three in a row, return False
    else:
        return False

#Returns available spaces on the board.
def possibleChoices(board):
    options = []
    count = 1
    for i in board:
        if board[i] == ' ':
            options.append(count)
        count +=1    
    return options

#Updates the board with the Player or PC's choice.
def selection(tic_tac, position, board):
    if position == 1:
        board['t-l'] = str(tic_tac)
    elif position == 2:
        board['t-m'] = str(tic_tac)
    elif position == 3:
        board['t-r'] = str(tic_tac)
    elif position == 4:
        board['m-l'] = str(tic_tac)
    elif position == 5:
        board['m-m'] = str(tic_tac)
    elif position == 6:
        board['m-r'] = str(tic_tac)
    elif position == 7:
        board['b-l'] = str(tic_tac)
    elif position == 8:
        board['b-m'] = str(tic_tac)
    elif position == 9:
        board['b-r'] = str(tic_tac)
    
#PC makes a selection from the available options
def pcpicks(board):
    options = possibleChoices(board)
    pcChoice = random.choice(options)
    print("PC made a selection, adding 'O' to spot # " + str(pcChoice))
    selection('O',pcChoice, board)

#Sets up the starting board
def newBoard():
    board = {
        't-l': ' ', #1
        't-m': ' ', #2
        't-r': ' ', #3
        'm-l': ' ', #4
        'm-m': ' ', #5
        'm-r': ' ', #6
        'b-l': ' ', #7
        'b-m': ' ', #8
        'b-r': ' ', #9
    }
    return board

#Starts a new game.
def startGame():  
    winner = None
    board = newBoard()
    for i in range(1,10):   #Only 9 available turns between Player and PC. 
        printBoard(board) 
        availableChoices = possibleChoices(board)
        if i % 2 == 1:       #Alternate turns between Player and PC. Player goes first.
            while True:                    
                try:
                    userChoice = int(input("Choose a spot on the board, options are: " + str(availableChoices) + " "))
                    validChoice = userChoice in availableChoices
                    while validChoice == False:
                        userChoice = int(input("Not an empty spot, try again. Options are: " + str(availableChoices) + " "))
                        validChoice = userChoice in availableChoices
                    break
                except ValueError:
                    #Error handling when player enters a number that is not 1-9
                    print("Not a valid choice, try again.")
                    
            print("Great choice, adding 'X' to #" + str(userChoice))
            selection('X',userChoice, board)
            userWon = checkThree(board)
            if userWon == True:
                winner = name
                printBoard(board)
                print("You won! Congrats!\n")
                return winner
        
        #PC's turn
        else:
            pcpicks(board)
            pcWon = checkThree(board)
            if pcWon == True:
                winner = 'PC'
                printBoard(board)
                print("Sorry, the PC won this time.")
                return winner
    if winner == None:
        printBoard(board)
        print("It's a tie!")
    
    return winner

#Main Game
playAgain = True

name = input("Hi, what is your name?\n")
print("\nHi {}, let's play tic tac toe.".format(name))

while playAgain:     #starts the game once and then restarts as long as player wants to continue. 
    startGame()
    while True:
        try:
            nextPlay = (input("Would you like to play again {0}? Enter yes or no. ".format(name)))
            nextPlay = nextPlay.lower()
            if nextPlay == "yes":
                break
            elif nextPlay == "no":
                playAgain = False
                break
            else:
                print("Not a valid choice, try again.")
        except ValueError:
            print("Not a valid choice, try again.")
#Exiting the game
input("Press Enter to exit.")

