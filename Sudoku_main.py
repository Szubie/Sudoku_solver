import Sudoku_board
import Sudoku_solver
import Sudoku_scenario
import Sudoku_validCheck
import Sudoku_view
import timeit
import cProfile


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
        Sudoku_scenario.createScenario()
        Sudoku_view.view()
        print 
        start_time = timeit.default_timer()
        unassignedTiles=Sudoku_validCheck.validChecker(Sudoku_board.board.tileList())
        Sudoku_solver.solveSudoku(unassignedTiles)
        elapsed = timeit.default_timer() - start_time
        print elapsed

        Continue=continues()
        
    print "Thanks for playing!"
    return 
    
 

#cProfile.run('main2()')   
main()


