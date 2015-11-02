import Sudoku_board

def view():
    n=len(Sudoku_board.board.rowList())

    for num in range(n):
        for item in Sudoku_board.board.rowList()[(n-1)-num].contains(): #Prints them in reverse order.
            print repr(item.value()).rjust(2), 
        print ""
        