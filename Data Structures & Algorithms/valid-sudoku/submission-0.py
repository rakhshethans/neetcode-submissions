class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to check the rows and columsn for duplicates simply use hash table
        # need a way to do the same thing for each square
        # how do we separate the input into squares -> each square is 3x3.
        # square 1 : board[0][0-2] and board[1][0-2] and board[2][0-2]
        # square 2 : board[0][3-5] and board[1][3-5] adn board[2][3-5]
        # square 3 : board[0][6-8] and board[1][6-8] and board[2][6-8]
        # and on (square 4 : board[3][0-2]...)

        # check all rows for duplicates
        for i in range(0, 9):
            row = board[i]
            currentRow = {}
            for number in row:
                # if the number isn't in the dictionary yet add it
                if number not in currentRow:
                    currentRow[number] = number
                elif number == ".":
                    continue
                # if it is then it is a duplicate so return false
                else:
                    return False
        
        # check all columns for duplicates
    
        for i in range(0, 9):
            # dictionary storing the current column
            currentColumn = {}
            for j in range(0, 9):
                number = board[j][i]
                if number not in currentColumn:
                    currentColumn[number] = number
                elif number == ".":
                    continue
                else:
                    return False

        # check squares
        
        # generate the squares first
        squares = self.generateSquares(board)
        # squares will look like [1,2,3], [4,5,6], [7,8,9]

        for square in squares:
            squareDict = {}
            for i in range(0, 3):
                for j in range(0, 3):
                    number = square[i][j]
                    if number not in squareDict:
                        squareDict[number] = number
                    elif number == ".":
                        continue
                    else:
                        return False
            
        return True
    

    def generateSquares(self, board):
        # generate the squares of a board
        # when i = 0, square 0 : board[0][0-2] and board[1][0-2] and board[2][0-2]
        # i = 1, square 1: board[0][3-5] and board[1][3-5] adn board[2][3-5]
        # i = 2, square 2: board[0][6-8] and board[1][6-8] and board[2][6-8]
        # i = 3: square 3: board[4][0-2] and board[5][0-2] and board[6][0-2]

        squares = []

        for i in range(0, 9):
            match i:
                case 0:
                    squares.append([board[0][0:3], board[1][0:3], board[2][0:3]])
                case 1:
                    squares.append([board[0][3:6], board[1][3:6], board[2][3:6]])
                case 2:
                    squares.append([board[0][6:9], board[1][6:9], board[2][6:9]])
                case 3:
                    squares.append([board[3][0:3], board[4][0:3], board[5][0:3]])
                case 4:
                    squares.append([board[3][3:6], board[4][3:6], board[5][3:6]])
                case 5:
                    squares.append([board[3][6:9], board[4][6:9], board[5][6:9]])
                case 6:
                    squares.append([board[6][0:3], board[7][0:3], board[8][0:3]])
                case 7:
                    squares.append([board[6][3:6], board[7][3:6], board[8][3:6]])
                case 8:
                    squares.append([board[6][6:9], board[7][6:9], board[8][6:9]])
        
        return squares

            
        