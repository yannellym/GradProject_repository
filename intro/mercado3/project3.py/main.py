from tkinter import Y
from battleshipClass import Battleship
from mercado8.art import logo

battleship = Battleship() 
BOARD = battleship.setupBoard()

#main function to welcome the user, create the gameboard, display the board, and start the game.
def main():
    print(logo)
    print("""How to play the game:\n 
        There are 5 ships hidden in the gameboard.\n
        Guess the columns and rows of the 5 ships to try and sink them \n
        Sink all of the ships, you WIN!""")
    print("\n" * 2)
    
    start_game = input("Type 'y' to start the game: \n").lower()
    if start_game == 'y':
        game_process(BOARD)
    else:
        print("Goodbye!")

#function will set up the gameboard, call the ask_input func, and call the validate_inputs func.             
def game_process(BOARD):
    print("\n" * 10)
    battleship.drawBoard(BOARD)
    
    while len(battleship.targets) > 0:  
        inputs = ask_input() 
        validate_inputs(inputs[0], inputs[1])
    
    #if user sunk all ships, the game will be over.
    if battleship.isGameOver(BOARD):
        print("Game over. You won!")  
    else:
        print("Game is not over yet, keep trying.")

# will validate that the user has inputted valid numbers as an input    
def validate_inputs(userCol, userRow):
    nums = [0,1,2,3,4,5,6,7,8,9]
    if int(userCol) in nums and int(userRow)in nums:
        print(battleship.checkHitOrMiss(int(userCol), int(userRow), BOARD))
        battleship.drawBoard(BOARD)
    else:
        if int(userCol) not in nums:
            print("Invalid column, please enter a digit from 0-9")
        else:
            print("Invalid row, please enter a digit from 0-9")
            
#asks users for their inputs  and returns the value as a list         
def ask_input():
    userCol = input("Please enter one column number (0-9) (X): ")
    userRow = input("Please enter one row number (0-9) (Y): ")
    return [userCol, userRow]
    
main()