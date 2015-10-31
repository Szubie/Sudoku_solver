import Sudoku_board

def view():
    n=len(Sudoku_board.board.rowList())
#    for num in range(n):
#        Sudoku_board.board.rowList()[n-num-1].print_contents()
    for num in range(n):
        for item in Sudoku_board.board.rowList()[(n-1)-num].contains():
            print repr(item.value()).rjust(2),   #Neat trick to remember
        print ""
        