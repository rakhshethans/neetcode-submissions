class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to check the rows and columsn for duplicates simply use hash table
        # need a way to do the same thing for each square
        # how do we separate the input into squares -> each square is 3x3.
        # square 1 : board[0][0-2] and board[1][0-2] and board[2][0-2]
        # square 2 : board[0][3-5] and board[1][3-5] adn board[2][3-5]
        # square 3 : board[0][6-8] and board[1][6-8] and board[2][6-8]
        # and on (square 4 : board[3][0-2]...)

        # check all rows and columns for duplicates
        squares = {
            (0, 0) : set(),
            (0, 1) : set(),
            (0, 2) : set(),
            (1, 0) : set(),
            (1, 1) : set(),
            (1, 2) : set(),
            (2, 0) : set(),
            (2, 1) : set(),
            (2, 2) : set()
        }
        for i in range(0, 9):
            row = board[i]
            currentRow = set()
            for number in row:
                # if the number isn't in the dictionary yet add it
                if number not in currentRow:
                    currentRow.add(number)
                elif number == ".":
                    continue
                # if it is then it is a duplicate so return false
                else:
                    return False
            
            # dictionary storing the current column
            # check square at the same time
            currentColumn = set()

            for j in range(0, 9):

                number = board[j][i]

                if number not in currentColumn:
                    currentColumn.add(number)
                elif number == ".":
                    continue
                else:
                    return False

                # square duplicates logic
                # if row number DIV 3 is 0 -> left, 1 -> middle -> right
                # if column number DIV 3 is 0 -> top, 1 -> middle, 2 -> bottom

                r = j // 3
                c = i // 3

                if number not in squares[(r, c)]:
                    squares[(r, c)].add(number)
                elif number == ".":
                    continue
                else:
                    return False

        return True



