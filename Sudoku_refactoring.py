import timeit

board=[]

#def sizeOfBoard():
#    n=raw_input("How big should the board be? \n")
    
for x_axis in range(9):
    board.append([])
    
for x_axis in range(9):
    for n in range(9):
        board[x_axis].append(-1)
        

""" A Backtracking program  in Python to solve Sudoku problem"""
 

def findUnassignedLocation(board):
    """This function finds an entry in grid that is still unassigned. 
        Returns Boolean false if it can't find an unassigned item. Otherwise, returns item."""
    for x in xrange(9):
        for y in xrange(9):
            if board[x][y]==-1:
                return (x, y)
    return False
        
    
def isValid(col, row, num):
    """Checks whether it will be legal to assign num to the given tile. 
    NOTE: this function doesn't check whether the item is unassigned. Don't call this on already assigned tiles, or it will overwrite them."""
    
    if not (inCol(col, num) or inRow(row, num) or inSquare(col, row, num)):
        return True
    else:
        return False
        
def inCol(col, num):
    for row in xrange(9):
        if board[col][row]==num:
            return True
    return False

def inRow(row, num):
    for col in xrange(9):
        if board[col][row]==num:
            return True
    return False
    
def inSquare(col, row, num):
    colStart=col-col%3
    rowStart=row-row%3
    for col in xrange(colStart,colStart+3):
        for row in xrange(rowStart, rowStart+3):
            if board[col][row]==num:
                return True
    return False


def solveSudoku(board):
    """ Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes) """
    index=findUnassignedLocation(board)
    
 
    # If there is no unassigned location, we are done
    if (index==False):
#       Sudoku_view.view()
       return True # success!
 
    # consider valid digits
    for num in xrange(1,10):
        if (isValid(index[0], index[1], num)):
            board[index[0]][index[1]]=num
            if solveSudoku(board):
                return True
            board[index[0]][index[1]]=-1
    return False # this triggers backtracking


def view():
    for row in xrange(9):
        for col in xrange(9):
            x=board[col][8-row]
            print repr(x).rjust(2),
        print ""
        
        
def createScenario1():
    board[0][0]=4
    board[0][1]=7
    board[0][2]=2
    board[0][4]=1
    board[0][5]=5
    board[1][4]=6
    board[1][6]=4
    board[1][7]=2
    board[1][8]=7
    board[2][0]=3
    board[2][2]=8
    board[2][3]=4
    board[2][6]=1
    board[2][8]=5
    board[3][1]=8
    board[3][2]=4
    board[3][5]=3
    board[3][6]=5
    board[3][8]=2
    board[4][0]=7
    board[4][4]=2
    board[4][5]=4
    board[4][7]=1
    board[4][8]=6
    board[5][0]=6
    board[5][1]=2
    board[5][4]=5
    board[5][5]=7
    board[5][6]=3
    board[5][7]=4
    board[6][1]=3
    board[6][2]=6
    board[6][3]=2
    board[6][4]=4
    board[6][6]=7
    board[7][1]=4
    board[7][3]=5
    board[7][6]=6
    board[7][7]=3
    board[7][8]=9
    board[8][0]=5
    board[8][2]=1
    board[8][3]=7
    board[8][5]=6
    board[8][7]=8
    
def createScenario2():
    board[1][7]=8
    board[2][7]=4
    board[3][6]=5
    board[4][7]=1
    board[5][8]=8
    board[5][7]=6
    board[6][6]=1
    board[8][8]=4
    board[0][5]=1
    board[0][4]=6
    board[2][5]=3
    board[2][4]=8
    board[2][3]=2
    board[3][5]=8
    board[5][3]=9
    board[6][5]=9
    board[6][4]=4
    board[6][3]=5
    board[8][4]=3
    board[8][3]=1
    board[0][0]=2
    board[2][2]=7
    board[3][0]=3
    board[3][1]=7
    board[4][1]=8
    board[5][2]=2
    board[6][1]=2
    board[7][1]=6
    
def createScenario3():
    board[0][8]=8
    board[1][0]=9
    board[1][5]=5
    board[1][6]=7
    board[2][1]=8
    board[2][2]=1
    board[2][7]=3
    board[3][1]=5
    board[3][3]=1
    board[3][7]=6
    board[4][4]=4
    board[4][6]=9
    board[5][4]=5
    board[5][5]=7
    board[6][0]=4
    board[6][4]=7
    board[6][6]=2
    board[7][1]=1
    board[7][2]=6
    board[7][3]=3
    board[8][2]=8
    
def main():
    user=raw_input("Please choose a scenario: 1 is easy, 2 is intermediate, 3 is hard (warning, takes a while!): \n")
    if user!= "1" and user!= "2" and user!= "3":
        main()
    else:
        if user=="1":
            createScenario1()
        elif user=="2":
            createScenario2()
        elif user=="3":
            createScenario3()
    view()
    start_time = timeit.default_timer()
    solveSudoku(board)
    elapsed = timeit.default_timer() - start_time
    print elapsed
    print
    view()
    
main()

"""
print elapsed
    
createScenario3()
view()
print

start_time = timeit.default_timer()
solveSudoku(board)
elapsed = timeit.default_timer() - start_time
print elapsed

print
view()
"""

#Interesting. If left without any board assignemnts, this algorithm will generate a sudoku puzzle. Not sure if it has a unique solution, however, which is a characteristic of a true sudoku puzzle.