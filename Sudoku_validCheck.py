import Sudoku_board

def validChecker(tileList):
    """Takes as input a list of tiles to check. Updates all the valid and invalid values for these items.
    NEW: returns a list of the currently unassigned tiles."""
    unassigned_tiles=[]
    
    for item in tileList:
        col=Sudoku_board.board.columnList()[item.col()-1]
        row=Sudoku_board.board.rowList()[item.row()-1]
        square=Sudoku_board.board.squareList()[item.square()-1]
        
        if item.value()!=-1:
            item.setAllInvalid()
            
        if item.value()==-1:
            unassigned_tiles.append(item)
            for n in range(1,10):
                if (col.valueExists(n) or row.valueExists(n) or square.valueExists(n)): 
                    if n not in item.invalidValues():
                        item.addInvalidValue(n)
                else:
                    if n not in item.validValues():
                        item.addValidValue(n)
    return unassigned_tiles



def validSetter(tileList):
    for item in tileList:
        col=Sudoku_board.board.columnList()[item.col()-1]
        row=Sudoku_board.board.rowList()[item.row()-1]
        square=Sudoku_board.board.squareList()[item.square()-1]
        if len(item.validValues())==1 and not (col.valueExists(item.validValues()[0]) or row.valueExists(item.validValues()[0]) or square.valueExists(item.validValues()[0])):
            item.setValue(item.validValues()[0])                    
            item.resetValidValues()
            item.setAllInvalid()
            return True
        else:
            return False

def validCheck(tileList):
    validChecker(tileList)
    validSetter(tileList)
    
def bSearch(value, List):
    mid=int(len(List)/2)
    if List[mid]==value:
        return True
    if len(List)==0 or len(List)==1:
        return False
        
    else:
        if value>List[mid]:
            return bSearch(value,List[mid:])
        elif value<List[mid]:
            return bSearch(value, List[:mid])
            