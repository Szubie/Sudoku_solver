import Sudoku_board

#Game logic here. Might transfer it over into methods in the objects actually.

#But we do need to create an algorithm that looks at each square on the board in turn, and continues looping through the puzzle until it has solved it.

"""from each square, we want to check the legal values that could be placed in it.
Create a list of legal values? (Values from 1-9 that don't already exist in the same row, column, or square).
If that list is of length 1, assign that value to the square"""


def createScenario1():
    Sudoku_board.b8.setValue(8)
    Sudoku_board.c8.setValue(4)
    Sudoku_board.d7.setValue(5)
    Sudoku_board.e8.setValue(1)
    Sudoku_board.f9.setValue(8)
    Sudoku_board.f8.setValue(6)
    Sudoku_board.g7.setValue(1)
    Sudoku_board.i9.setValue(4)
    Sudoku_board.a6.setValue(1)
    Sudoku_board.a5.setValue(6)
    Sudoku_board.c6.setValue(3)
    Sudoku_board.c5.setValue(8)
    Sudoku_board.c4.setValue(2)
    Sudoku_board.d6.setValue(8)
    Sudoku_board.f4.setValue(9)
    Sudoku_board.g6.setValue(9)
    Sudoku_board.g5.setValue(4)
    Sudoku_board.g4.setValue(5)
    Sudoku_board.i5.setValue(3)
    Sudoku_board.i4.setValue(1)
    Sudoku_board.a1.setValue(2)
    Sudoku_board.c3.setValue(7)
    Sudoku_board.d1.setValue(3)
    Sudoku_board.d2.setValue(7)
    Sudoku_board.e2.setValue(8)
    Sudoku_board.f3.setValue(2)
    Sudoku_board.g2.setValue(2)
    Sudoku_board.h2.setValue(6)


createScenario1()  
"""Scenario 1 is too hard right now. It involves more complex logic than process of elimination. Leave it for later."""

"""Created a way to reset the value of the tiles. Can iterate through all the tiles and reset them when needed."""

def createScenario2():
    Sudoku_board.a1.setValue(4)
    Sudoku_board.a2.setValue(7)
    Sudoku_board.a3.setValue(2)
    Sudoku_board.a5.setValue(1)
    Sudoku_board.a6.setValue(5)
    Sudoku_board.b5.setValue(6)
    Sudoku_board.b7.setValue(4)
    Sudoku_board.b8.setValue(2)
    Sudoku_board.b9.setValue(7)
    Sudoku_board.c1.setValue(3)
    Sudoku_board.c3.setValue(8)
    Sudoku_board.c4.setValue(4)
    Sudoku_board.c7.setValue(1)
    Sudoku_board.c9.setValue(5)
    Sudoku_board.d2.setValue(8)
    Sudoku_board.d3.setValue(4)
    Sudoku_board.d6.setValue(3)
    Sudoku_board.d7.setValue(5)
    Sudoku_board.d9.setValue(2)
    Sudoku_board.e1.setValue(7)
    Sudoku_board.e5.setValue(2)
    Sudoku_board.e6.setValue(4)
    Sudoku_board.e8.setValue(1)
    Sudoku_board.e9.setValue(6)
    Sudoku_board.f1.setValue(6)
    Sudoku_board.f2.setValue(2)
    Sudoku_board.f5.setValue(5)
    Sudoku_board.f6.setValue(7)
    Sudoku_board.f7.setValue(3)
    Sudoku_board.f8.setValue(4)
    Sudoku_board.g2.setValue(3)
    Sudoku_board.g3.setValue(6)
    Sudoku_board.g4.setValue(2)
    Sudoku_board.g5.setValue(4)
    Sudoku_board.g7.setValue(7)
    Sudoku_board.h2.setValue(4)
    Sudoku_board.h4.setValue(5)
    Sudoku_board.h7.setValue(6)
    Sudoku_board.h8.setValue(3)
    Sudoku_board.h9.setValue(9)
    Sudoku_board.i1.setValue(5)
    Sudoku_board.i3.setValue(1)
    Sudoku_board.i4.setValue(7)
    Sudoku_board.i6.setValue(6)
    Sudoku_board.i8.setValue(8)
    
#createScenario2()

def validCheck():
    complete=False
    changeFlag=True        #If the program runs through the whole set and does nothing to change it, it will terminate. (It's stuck here).
    while changeFlag==True and complete!=True: #If the algorithm completes the puzzle, or makes no changes in an iteration, it will stop iterating.
        changeFlag=False
        for item in Sudoku_board.board.tileList():
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
                            changeFlag=True
 #                           print "The condition passed, we added a valid value to the list."
                    elif n not in item.invalidValues(): #Only add it if it isn't already in there.
                        item.addInvalidValue(n)
                for y in item.validValues():
                    if col.valueExists(y) or row.valueExists(y) or square.valueExists(y):   #This should keep the validValue lists up to date with changing situation.
                        item.validValues().remove(y)
                        if y not in item.invalidValues():
                            item.addInvalidValues(y)
                        changeFlag=True
                print item.name(),item.validValues()
                if len(item.validValues())==1:
                    item.setValue(item.validValues()[0])                    #Oops! This will always set the value to n (which will always be 9 at the end of the loop. FIXED
                    print "VALUE SET: " +str(item.validValues()[0])
                    item.resetValidValues()
                    item.setAllInvalid()
                    changeFlag=True


            print item.name(), item.value()
            print item.name(), "Valid values: ",item.validValues()
            print item.name(), "Invalid values: ", item.invalidValues()
            print ""
#        for item in Sudoku_board.board.tileList():
#            print item.name(), item.value()



                    
#        elimination() #Run elimination  
                              
#        if isComplete():
        complete=True

def isComplete():        
    for item in Sudoku_board.board.tileList():
        if item.value()==-1:
            return False
    return True
    
def reset():
        for thing in Sudoku_board.board.tileList(): 
            thing.resetValue()
        for things in Sudoku_board.board.tileList():
            things.resetValidValues()
        for things in Sudoku_board.board.tileList():
            things.resetInvalidValues()
        
  
def elimination():
    """Works by a process of elimination, checking where values CAN'T be stored. If the value can't fit in any other tile within the square, or it can't fit in any other tile in the column, or it can't fit within any other tile on
    the row, then it MUST go in this square."""
    
    #I need to create and store a list of these for each tile? Values that CAN'T be stored in that tile. Then, a tile will check all its valid values against its neighbours, to see if the value can't go anywhere else.
    print ""
    print "ELIMINATION BEGINNING"
    
    for item in Sudoku_board.board.tileList():
        col=Sudoku_board.board.columnList()[item.col()-1]
        colValid=item.validValues()
#        print "col= " + str(col.num())
        row=Sudoku_board.board.rowList()[item.row()-1]
        rowValid=item.validValues()
#        print "row= " + str(row.num())
        square=Sudoku_board.board.squareList()[item.square()-1]
        squareValid=item.validValues()
        
        #Check whole column for invalid values
        for c in col.contains():
                if c!=item:
                    for thing in c.validValues():
                        print thing
                        if thing in colValid:
                            colValid.remove(thing)
                            print "removed from colValid"
                        
        if len(colValid)==1:
                item.setValue(colValid[0])                   
                print item.name(), "VALUE SET: " +str(colValid[0])
                item.resetValidValues()
                item.setAllInvalid()
            
        #Check  whole row for invalid values
        for r in row.contains():
            if r!=item:
                for p in c.validValues():
                    print p
                    if p in rowValid:
                        rowValid.remove(p)
                        print "removed from rowValid"
                        
        if len(rowValid)==1:
                item.setValue(rowValid[0])                   
                print item.name(),"VALUE SET: " +str(rowValid[0])
                item.resetValidValues()
                item.setAllInvalid()
                
        for s in square.contains():
            if s!=item:
                    for things in s.validValues():
                        print things
                        if things in squareValid:
                            squareValid.remove(things)
                            print "removed from squareValid"
                        
        if len(squareValid)==1:
                item.setValue(squareValid[0])                   
                print item.name(),"VALUE SET: " +str(squareValid[0])
                item.resetValidValues()
                item.setAllInvalid()
                
    print "ELIMINATION ENDING"
    print ""
            
def commonElements(list1, list2):
    """Takes in two lists, returns the common elements between the two"""
    list3=[]
    for item in list1:
        if item in list2:
            list3.append(item)
    return list3
    
def view():
    n=len(Sudoku_board.board.rowList())
#    for num in range(n):
#        Sudoku_board.board.rowList()[n-num-1].print_contents()
    for num in range(n):
        for item in Sudoku_board.board.rowList()[(n-1)-num].contains():
            print repr(item.value()).rjust(2),   #Neat trick to remember
        print ""
        
#Ok, but this prints the table upside down at the moment!
                              

"""Now, going to add "valueExists" checker to columns, rows and squares"""
"""Done."""

"""Now, for each tile, we want a list of the valid numbers for that tile. Stored in the tile itself."""
"""So, first we must create the methods for this in the tile object."""
"""Done"""

"""Ok, still some problems.
Never terminates.
One problem I noticed was: there is no limit to the values that you can append into validValues list. It should check to make sure you aren't entering the same values again.
Additionally, we are never removing values from that list, so we'll never get to only 1 choice left.

This doesn't work towards a solution yet."""

"""The fact that we are never seeing any printing of validValue lists seems to indicate that we are never entering that logical branch, which might mean that something is wrong there."""
"""Correct, it appears that the checks are looking for the value within the number of the rows or columns, rather than the values within the tiles within those respective rows or columns."""

"""After placing numerous print statements, I have noticed that it is also checking validValues for tiles that already have (non-default) values. That has to change, or this will never work."""
"""The square should be skipped if it already has a non-default value assigned to it. Otherwise we'll actually be overwriting already set values for the squares, ruining our solution. (This way is also more efficient)."""

"""More print statements, there's definitely something wrong with the adding of the validValues. The conditions are passing at the wrong time, incorrect values are getting in. Not sure why."""
"""Never mind, human error. I was counting columns instead of rows. Typical!"""


"""Ah, this is a tricky Sodoku puzzle, one that CANNOT be solved simply by the logic of 'I can place that there!'. There are no certainties on this one. Something I need to work towards, to incorporate in the future."""


"""Ok, so this can solve super-simple puzzles that require just following the line of only possible numbers. But the game is much deeper than that. We also need to account for the process of elimination: you know that
(although there are several different candidates for a spot), one of them must be correct simply because they cannot be fit in anywhere else in the square, or on the column, or on the row."""

"""And even that will only take you so far! Need to be able to take the next logical step after that..."""


"""Ah, every item that is set to a value must have every value in the invalid list"""


"""There is definitely some errors ever since implementing the elimination function.
Looking at the logs, it appears that the elimination triggers multiple times per item, setting the value many different times for the same item? Yep."""

"""Another thing to learn from today: you need to reset items. Objects don't automatically reset, even if you restart the kernel of the shell. This influences future results, and ruins tests."""


""""""



"""Day 2:"""

"""Ok, need to re-do the elimination process. Perhaps rewrite it as a function that takes arguments (could even be a class with methods), runs those sequentially. Double check error logs for validValue errors."""
"""Currently, elimination runs across the whole puzzle for every single tile that is being examined by the checkValid function. Clearly, very inefficient. It may be the cause of the bugs as well, although exactly how that happens
I don't know. Curious how it can be bugged: it's supposed to only compare possible validValues across column, row and then square."""
"""Certainly, it shouldn't be allowed to set the same value multiple times."""

"""Case study: h5 Tile. One loop only. It has the correct valid values after validCheck runs but before elimination runs. However, after elmination runs, somehow that valid value list becomes 0. How?
-Is something removing from that list?
-Are other values on the board being assigned incorrectly, leaving no correct choices left for h5?"""

"""Testing would be easier if we had somthing in place to print the board to the shell. Maybe I should start on that, so we can see the big picture."""


"""Ok, view built. Will have to rebuild the elimination function sometime. Gotta go for now though."""