import Sudoku_board

def elimination(tile):
    print "TEST"
    print colNeighbourTiles(tile)
    col = getCommonInvalidValues(colNeighbourTiles(tile))
    row = getCommonInvalidValues(rowNeighbourTiles(tile))
    square = getCommonInvalidValues(squareNeighbourTiles(tile))
    if len(col)==1 and col!=0:
        return col[0]
    elif len(row)==1 and col!=0:
        return row[0]
    elif len(square)==1 and col!=0:
        return square[0]
    else:
        print "Elimination couldn't find a value that cannot fit anywhere else in the column/row/square."
        return -1

def colNeighbourTiles(tile):
    """Fetches the tiles of the column this tile is in. Do this by requesting the method within tile to return vLine."""
    neighbour_tiles=[]
    
    
    print "Tile = " + str(tile.name())
    
    print "Column = " + str(tile.col())
    Sudoku_board.board.columnList()[tile.col()-1].print_contents()
    columns = []
    for colTile in Sudoku_board.board.columnList()[tile.col()-1].contains():
        if colTile != tile:
            columns.append(colTile)
    print "Column - this tile = " 
    for colTile2 in columns:
        print colTile2.name(),
    print
    for colTile in columns:
        if colTile not in neighbour_tiles:
            neighbour_tiles.append(colTile)
            
    print "All the related tiles to the input tile: "
    for item in neighbour_tiles:
        print item.name(),
        
    return neighbour_tiles


def rowNeighbourTiles(tile):    
    """Fetch the tiles of the rows this tile is in."""
    neighbour_tiles=[]
    
    print "Row = " + str(tile.row())
    Sudoku_board.board.rowList()[tile.row()-1].print_contents()
    rows = []
    for rowTile in Sudoku_board.board.rowList()[tile.row()-1].contains():
        if rowTile != tile:
            rows.append(rowTile)
    print "Row - this tile = " 
    for rowTile2 in rows:
        print rowTile2.name(),
    print
    for rowTile in rows:
        if rowTile not in neighbour_tiles:
            neighbour_tiles.append(rowTile)
            
    print "All the related tiles to the input tile: "
    for item in neighbour_tiles:
        print item.name(),
        
    return neighbour_tiles

def squareNeighbourTiles(tile):
    """Fetches the tiles of the squares this tile is in."""
    neighbour_tiles=[]
    
    print "Square = " + str(tile.square())
    Sudoku_board.board.squareList()[tile.square()-1].print_contents()
    squares = []
    for squareTile in Sudoku_board.board.squareList()[tile.square()-1].contains():
        if squareTile != tile:
            squares.append(squareTile)
    print "Square - this tile = " 
    for squareTile2 in squares:
        print squareTile2.name(),
    print
    for squareTile in squares:
        if squareTile not in neighbour_tiles:
            neighbour_tiles.append(squareTile)
    
    
    print "All the related tiles to the input tile: "
    for item in neighbour_tiles:
        print item.name(),
        
    return neighbour_tiles

    #Ok, tested, this successfully narrows it down to checking the correct squares in relation to the main square.
    
def getAllNeighbourTiles(tile):
    neighbour_tiles=colNeighbourTiles(tile)[:]
    
    for thing in rowNeighbourTiles(tile):
        if thing not in neighbour_tiles:
            neighbour_tiles.append(thing)

    
    for thing in squareNeighbourTiles(tile):
        if thing not in neighbour_tiles:
            neighbour_tiles.append(thing)
        
    return neighbour_tiles

def getCommonInvalidValues(tiles):
    """Takes a list of tile as input (intended to be the list of releated neighbour tiles to a certain tile), and then returns a list of invalid values that they all share.
    This value must go into the tile, as it is invalid everywhere else."""
    #Actually, this check must be made 3 times: once for the column, once for the row, and once for the square.
    
    invalidValues=[]
    
    #First, create a list of invalid values for the first tile in the list.

    print tiles
    if tiles[0]==0:
        return invalidValues
    invalidValues=tiles[0].invalidValues()[:]
    

    print "Invalid values for first element in list: "
    print invalidValues
    
    #Then, check that list against the list of invalid values for the rest of the tiles.
    #If any are repeated, keep them, else, drop them from the list?
    
    #Almost works, just need to also check to make sure that the invalid values aren't already assigned within the col, row or square.
    for tile in tiles:
        output=[]
        print tile.name()
        print "Invalid values: ", tile.invalidValues()
        for thing in invalidValues:
            if thing in tile.invalidValues():
                if thing!=tile.value():
                    output.append(thing)
                    print "Current invalid values list: "
                    print output
            invalidValues=output[:]
    
    print invalidValues
    return invalidValues
    
#Double check to make sure this works, please. TODO.
