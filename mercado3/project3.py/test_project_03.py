from battleshipClass import Battleship
import unittest

# tests to check the game functionality
class TestShip(unittest.TestCase): 
    
    # tests if the game is over 
    def test_isGameOver_True(self): #tested
        #Arrange
        battleship = Battleship()
        #sets up the game board
        board = [["."]* 10 for _ in range(10)]
        battleship.targets = []
        #Act
        # designates where the ships in the game will be placed
        board[5][5] = "X"
        board[2][9] = "X"
        board[4][2] = "X"
        board[2][3] = "X"
        board[1][7] = "X"
        #Assert
        #if the targets array is empty, the game will be over
        self.assertEqual(battleship.isGameOver(board), True)
    
    def test_isGameOver_False(self): #tested
        #Arrange
        battleship = Battleship()
        #sets up the game board
        board = battleship.setupBoard() 
        #Act
        # adds a ship coordinate to the target array in the game board
        battleship.targets = [[0,1]]
        #Assert
        #if the targets array is NOT empty, the game will NOT be over
        self.assertEqual(battleship.isGameOver(board), False)
        
    def test_setupBoard_numShips(self): #tested
        #Arrange
        battleship = Battleship()
        #Act
        #sets up the game board
        battleship.setupBoard() 
        #Assert
        # will check if the length of the target array is 5. if it is 5, we have
        # successfully set up the game board with 5 ships.
        self.assertEqual(len(battleship.targets), 5)
        
    def test_setupBoard_blankSpaces(self): 
        #Arrange
        battleship = Battleship()
        #sets up the game board
        a = battleship.setupBoard()     
        grid_size = 10
        #Act
        count = 0
        # loops through the game board and calculate the number of times
        # the "." char appears and stores it in the variable named count
        # there should be 95 "."s in the board once we set it up.
        for i in range(grid_size):
            for j in range(grid_size):
                if a[i][j] == ".":
                    count += 1
        self.assertEqual(count, 95)
        
        
    def test_checkHitOrMiss_Hit(self): #tested
        #Arrange
        battleship = Battleship()
        # creates board 2D ARRAY
        board = [["."]* 10 for _ in range(10)]
        
        #Act
        # adds target coordinates to the board
        board[5][5] = "S"
        board[2][9] = "S"
        board[4][2] = "S"
        board[2][3] = "S"
        board[1][7] = "S"
        # saves the coordinates in the targets array
        battleship.targets = [[5,5],[2,9],[4,2],[2,3],[1,7]]
        #Assert
        # checks if the inputs the user gave are in the targets array. If they are,
        # the user has sunk a ship!
        self.assertEqual(battleship.checkHitOrMiss(5,5, board), "HIT! You sunk a ship")
        
        
    def test_checkHitOrMiss_Miss(self): #tested
        #Arrange
        battleship = Battleship()
        # adds target coordinates to the board
        board = [["."]* 10 for _ in range(10)]
        
        #Act
        # saves the coordinates in the targets array
        board[5][5] = "S"
        board[2][9] = "S"
        board[4][2] = "S"
        board[2][3] = "S"
        board[1][7] = "S"
        #Assert
        # checks if the inputs the user gave are in the targets array. 
        # If they are NOT in the targets array, the 'MISS! No ship in here :(' will be displayed.
        self.assertEqual(battleship.checkHitOrMiss(7,5, board), 'MISS! No ship in here :(')
        
if __name__ == '__main__':
    unittest.main()