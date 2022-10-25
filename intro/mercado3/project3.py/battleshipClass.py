import random

#Project 3
#In this project, you will implement a variation of the board game “Battleship”.
# You may have played this game as a kid (or an adult).  In Battleship, 5 ships are 
# placed on a 10 x 10 grid and then you and your opponent take turns calling out a row/column 
# until all the ships on your opponent’s grid are “hit” and “sunk”.  The first player to sink 
# all of his/her opponent's ships wins.

'''
    File name: project_03.py
    Author: Yannelly Mercado
    Date created: 9/10/2022
    Date last modified: 9/15/2022
    Python Version: 2.7.18
'''

class Battleship: 
      def __init__(self):
            self.num_of_ships = 5
            self.rows = 10
            self.cols = 10
            self.targets = []

      # This method ‘drawBoard’, takes one parameter as input: a 10 x 10 array of chars, draws a frame, and return the game board. 
      def drawBoard(self, BOARD):
            width = len(str(max(self.rows,self.cols)-1))
            contentLine = "# | values |"
            
            #  x - axis numbers top numbers
            numberLine = contentLine.replace("|"," ")
            numberLine = numberLine.replace("#"," "*width)
            column_nums = "  ".join(f"{i:<{width}d}" for i in range(self.cols))
            numberLine = numberLine.replace("values",column_nums)
            print(numberLine)

            #creates dashes between the rows
            dashes = "-".join("-"*width for _ in range(self.cols))
            frame = contentLine.replace("values",dashes)
            frame = frame.replace("#"," "*width)
            frame = frame.replace("| ","+-----").replace(" |","-----+")
            
            # y axis left numbers
            for i,row in enumerate((BOARD),0):
              values = "  ".join(f"{v:{width}s}" for v in row)
              line = contentLine.replace("values",values)
              line = line.replace("#",f"{i:{width}d}")
              print(line)
              print(frame)
            return BOARD
      
      #sets ups the board with 5 ships randomly selected on the board       
      def setupBoard(self):
            arr_content = [["."]* self.cols for _ in range(self.rows)]
            BOARD = arr_content
            
            if len(self.targets) != 5:
                  for i in range(0,self.num_of_ships):
                        randomRow = random.randint(0, self.rows - 1)
                        randomCol = random.randint(0, self.cols - 1)
                        self.targets.append([randomRow,randomCol])
                        BOARD[randomRow][randomCol] = 'S'
            return BOARD
      
      #will check if the user has hit a cell with a ship. 
      #Will check if the user has already guessed that cell before      
      def checkHitOrMiss(self,userCol, userRow, BOARD):
            print("\n" * 10)
            if BOARD[userRow][userCol] == "S":
                  BOARD[userRow][userCol] = "X"
                  self.targets.remove([userRow,userCol])
                  return "HIT! You sunk a ship"
            elif BOARD[userRow][userCol] == "X":
                  return "HIT! You already sunk this ship. Try again!" 
            elif BOARD[userRow][userCol] == "O":
                  return "MISS, You already guessed this spot. Try again!"
            else:
                  BOARD[userRow][userCol] = "O"
                  return "MISS! No ship in here :("
      
      #Takes in BOARD and returns true if all the target ships have been hit, and false otherwise
      def isGameOver(self, BOARD):
            for arr in BOARD:
                  if "S" in arr:
                        return False
            return True
            
  
            
              
              
            
                  

                  
                  
            
        
  



