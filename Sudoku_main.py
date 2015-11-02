import Sudoku_board
import Sudoku_solver
import Sudoku_scenario
import Sudoku_validCheck
import Sudoku_recursive2 
import timeit


def isComplete():        
    for item in Sudoku_board.board.tileList():
        if item.value()==-1:
            return False
    return True
    
def reset():
        for thing in Sudoku_board.board.tileList(): 
            thing.resetValue()
            thing.resetValidValues()
            thing.resetInvalidValues()
    
    
def continues():
    user=""
    while user!="y" and user!="n":
        user = raw_input("Continue? y/n: ")
    if user=="n":
        return False
    else:
        return True
        
def main():
    Continue=True
    while Continue==True:
        reset()
        scen=Sudoku_scenario.createScenario()
        if scen==3:
            start_time = timeit.default_timer()
            Sudoku_validCheck.validChecker(Sudoku_board.board.tileList())
            Sudoku_solver.solveSudoku(Sudoku_board.board.tileList())
            elapsed = timeit.default_timer() - start_time
            print elapsed
        else:
            start_time = timeit.default_timer()
            Sudoku_recursive2.solveSudoku(Sudoku_board.board.tileList())
            elapsed = timeit.default_timer() - start_time
            print elapsed
        Continue=continues()
        
    print "Thanks for playing!"
    return 
    
    
main()


