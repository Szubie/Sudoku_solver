import Sudoku_board

"""Goal: to change the functionality of this. Instead of always running it on the whole board, it should accept arguments. This, it can be run on the whole board, but also on a specific set of tiles.
This is useful, because we only want to run this on tiles related to the current tile when we update something."""

"""Meanwhile, update to remove unneeded functionality? completion check?""" #Implement them elsewhere though! Perhaps in the main.
#Actually, it does make sense to have changeFlag check in here. Since this is where the changes will be happening. However, functions can only return one thing? Instead, use objects with instance variables that can be checked?
#Oooh, not sure about how to do this with objects though. Need to be instantiated...

def validCheck(tileList):
    """Takes as input a list of tiles to check. Updates all the valid and invalid values for these items."""
    for item in tileList:
        print item.name()
        col=Sudoku_board.board.columnList()[item.col()-1]
#            print "col= " + str(col.num())
        row=Sudoku_board.board.rowList()[item.row()-1]
#            print "row= " + str(row.num())
        square=Sudoku_board.board.squareList()[item.square()-1]
#            print "square= "+ str(square.num())
            
#            print "value= " + str(item.value())
#           print ""
        if item.value()!=-1:
            item.setAllInvalid()
            
        if item.value()==-1:
            for n in range(1,10):
#                    print ""
#                    print "n= "+str(n)
#                    print "col.valueExists= " +str(col.valueExists(n))
#                    print "row.valueExists= " +str(row.valueExists(n))
#                    print "square.valueExists= " +str(square.valueExists(n))
                if not (col.valueExists(n) or row.valueExists(n) or square.valueExists(n)): #Misleading method names. Actually, this loop is never entered, as the methods actually return false if they find the number. FIXED.
                       if n not in item.validValues(): #Add to list only if n is not already in validValues list.
                           item.addValidValue(n)                                                       #Boolean logic is wrong here as well. "Or", not "and".

 #                           print "The condition passed, we added a valid value to the list."
                elif n not in item.invalidValues(): #Only add it if it isn't already in there.
                    item.addInvalidValue(n)
            for y in item.validValues():
                if col.valueExists(y) or row.valueExists(y) or square.valueExists(y):   #This should keep the validValue lists up to date with changing situation.
                    item.validValues().remove(y)
                    if y not in item.invalidValues():
                        item.addInvalidValues(y)

            print item.name(),item.validValues()
            if len(item.validValues())==1:
                item.setValue(item.validValues()[0])                    #Oops! This will always set the value to n (which will always be 9 at the end of the loop. FIXED
                print "VALUE SET: " +str(item.validValues()[0])
                item.resetValidValues()
                item.setAllInvalid()



            print item.name(), item.value()
            print item.name(), "Valid values: ",item.validValues()
            print item.name(), "Invalid values: ", item.invalidValues()
            print ""
