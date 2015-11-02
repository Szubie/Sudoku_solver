class Board:
    def __init__(self, ColumnsList, RowsList, SquareList, TilesList):
        self.ColumnsList=ColumnsList.contains()
        self.RowsList=RowsList.contains()
        self.SquareList=SquareList.contains()
        self.TilesList=TilesList.contains()
    def columnList(self):
        return self.ColumnsList
    def rowList(self):
        return self.RowsList
    def squareList(self):
        return self.SquareList
    def tileList(self):
        return self.TilesList
        
    
class Column:
    def __init__(self, columnNum, row1, row2, row3, row4, row5, row6, row7, row8, row9, letter):
        self.columnNum=columnNum
        self.row1=row1
        self.row2=row2
        self.row3=row3
        self.row4=row4
        self.row5=row5
        self.row6=row6
        self.row7=row7
        self.row8=row8
        self.row9=row9
        self.Letter=letter
        self.List=[row1, row2, row3, row4, row5, row6, row7, row8, row9]
    
    def letter(self):
        return self.Letter
    def num(self):
        return self.columnNum
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"."
        
    def valueExists(self, x):
        for item in self.List:
               if item.value()==x:
                   return True
        return False
        
class Row:
    def __init__(self, rowNum, col1, col2, col3, col4, col5, col6, col7, col8, col9):
        self.rowNum=rowNum
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.col4=col4
        self.col5=col5
        self.col6=col6
        self.col7=col7
        self.col8=col8
        self.col9=col9
        self.List=[col1, col2, col3, col4, col5, col6, col7, col8, col9]
        
    def num(self):
        return self.rowNum
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"."
    
    def valueExists(self, x):
        for item in self.List:
               if item.value()==x:
                   return True
        return False
        
class Square:
    def __init__(self, squareNum, a3, b3, c3, a2, b2, c2, a1, b1, c1):
        self.squareNum=squareNum
        self.a3=a3
        self.b3=b3
        self.c3=c3
        self.a2=a2
        self.b2=b2
        self.c2=c2
        self.a1=a1
        self.b1=b1
        self.c1=c1
        self.List=[a3, b3, c3, a2, b2, c2, a1, b1, c1]
    
    def num(self):
        return self.squareNum
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"."
    def valueExists(self, x):
        for item in self.List:
               if item.value()==x:
                   return True
        return False
           
    
class Tiles(object):
    def __init__(self, Name, VLine, HLine, Square, Value=-1):
        self.Name=Name
        self.VLine=VLine
        self.HLine=HLine                        
        self.Square=Square
        self.Value=Value
        self.ValidValues=[]
        self.InvalidValues=[]
    
    def name(self):                             
        return self.Name
    def value(self):                            
        return self.Value
    def setValue(self,x):
        self.Value=x
    def resetValue(self):
        self.Value=-1
    def col(self):
        return self.VLine
    def row(self):
        return self.HLine
    def square(self):
        return self.Square
    
    def validValues(self):
        return self.ValidValues
    def addValidValue(self,x):
        self.ValidValues.append(x)
    def resetValidValues(self):
        for item in self.ValidValues:
            self.ValidValues.remove(item)
            
    def invalidValues(self):
        return self.InvalidValues
    def addInvalidValue(self, x):
        self.InvalidValues.append(x)
    def setAllInvalid(self):
        self.InvalidValues=[1,2,3,4,5,6,7,8,9]
    def resetInvalidValues(self):
        self.InvalidValues=[]

class ColumnsList(object):
    def __init__(self, col1, col2, col3, col4, col5, col6, col7, col8, col9):
        self.List=[col1, col2, col3, col4, col5, col6, col7, col8, col9]
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"."
      
        
class RowsList(object):
    def __init__(self, row1, row2, row3, row4, row5, row6, row7, row8, row9):
        self.List=[row1, row2, row3, row4, row5, row6, row7, row8, row9]
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"." 
        
class SquaresList(object):
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9):
        self.List=[s1, s2, s3, s4, s5, s6, s7, s8, s9]
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"."
    
    
class TilesList(object):
    def __init__(self, a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9):
        self.List=[a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9]
    def list(self):  
        return self.List
    def contains(self):
        return self.List
    def print_contents(self):
        for item in range(0, len(self.List)-1):
            print self.List[item].name()+",",
        print self.List[-1].name()+"."
        
#81 Tiles



a1=Tiles("a1", 1, 1, 7)
a2=Tiles("a2", 1, 2, 7)
a3=Tiles("a3", 1, 3, 7)
a4=Tiles("a4", 1, 4, 4)
a5=Tiles("a5", 1, 5, 4)
a6=Tiles("a6", 1, 6, 4)
a7=Tiles("a7", 1, 7, 1)
a8=Tiles("a8", 1, 8, 1)
a9=Tiles("a9", 1, 9, 1)

b1=Tiles("b1", 2, 1, 7)
b2=Tiles("b2", 2, 2, 7)
b3=Tiles("b3", 2, 3, 7)
b4=Tiles("b4", 2, 4, 4)
b5=Tiles("b5", 2, 5, 4)
b6=Tiles("b6", 2, 6, 4)
b7=Tiles("b7", 2, 7, 1)
b8=Tiles("b8", 2, 8, 1)
b9=Tiles("b9", 2, 9, 1)

c1=Tiles("c1", 3, 1, 7)
c2=Tiles("c2", 3, 2, 7)
c3=Tiles("c3", 3, 3, 7)
c4=Tiles("c4", 3, 4, 4)
c5=Tiles("c5", 3, 5, 4)
c6=Tiles("c6", 3, 6, 4)
c7=Tiles("c7", 3, 7, 1)
c8=Tiles("c8", 3, 8, 1)
c9=Tiles("c9", 3, 9, 1)

d1=Tiles("d1", 4, 1, 8)
d2=Tiles("d2", 4, 2, 8)
d3=Tiles("d3", 4, 3, 8)
d4=Tiles("d4", 4, 4, 5)
d5=Tiles("d5", 4, 5, 5)
d6=Tiles("d6", 4, 6, 5)
d7=Tiles("d7", 4, 7, 2)
d8=Tiles("d8", 4, 8, 2)
d9=Tiles("d9", 4, 9, 2)

e1=Tiles("e1", 5, 1, 8)
e2=Tiles("e2", 5, 2, 8)
e3=Tiles("e3", 5, 3, 8)
e4=Tiles("e4", 5, 4, 5)
e5=Tiles("e5", 5, 5, 5)
e6=Tiles("e6", 5, 6, 5)
e7=Tiles("e7", 5, 7, 2)
e8=Tiles("e8", 5, 8, 2)
e9=Tiles("e9", 5, 9, 2)

f1=Tiles("f1", 6, 1, 8)
f2=Tiles("f2", 6, 2, 8)
f3=Tiles("f3", 6, 3, 8)
f4=Tiles("f4", 6, 4, 5)
f5=Tiles("f5", 6, 5, 5)
f6=Tiles("f6", 6, 6, 5)
f7=Tiles("f7", 6, 7, 2)
f8=Tiles("f8", 6, 8, 2)
f9=Tiles("f9", 6, 9, 2)

g1=Tiles("g1", 7, 1, 9)
g2=Tiles("g2", 7, 2, 9)
g3=Tiles("g3", 7, 3, 9)
g4=Tiles("g4", 7, 4, 6)
g5=Tiles("g5", 7, 5, 6)
g6=Tiles("g6", 7, 6, 6)
g7=Tiles("g7", 7, 7, 3)
g8=Tiles("g8", 7, 8, 3)
g9=Tiles("g9", 7, 9, 3)

h1=Tiles("h1", 8, 1, 9)
h2=Tiles("h2", 8, 2, 9)
h3=Tiles("h3", 8, 3, 9)
h4=Tiles("h4", 8, 4, 6)
h5=Tiles("h5", 8, 5, 6)
h6=Tiles("h6", 8, 6, 6)
h7=Tiles("h7", 8, 7, 3)
h8=Tiles("h8", 8, 8, 3)
h9=Tiles("h9", 8, 9, 3)

i1=Tiles("i1", 9, 1, 9)
i2=Tiles("i2", 9, 2, 9)
i3=Tiles("i3", 9, 3, 9)
i4=Tiles("i4", 9, 4, 6)
i5=Tiles("i5", 9, 5, 6)
i6=Tiles("i6", 9, 6, 6)
i7=Tiles("i7", 9, 7, 3)
i8=Tiles("i8", 9, 8, 3)
i9=Tiles("i9", 9, 9, 3)

TileList=TilesList(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9)

#9 Columns

colA=Column(1, a1, a2, a3, a4, a5, a6, a7, a8, a9, "a")
colB=Column(2, b1, b2, b3, b4, b5, b6, b7, b8, b9, "b")
colC=Column(3, c1, c2, c3, c4, c5, c6, c7, c8, c9, "c")
colD=Column(4, d1, d2, d3, d4, d5, d6, d7, d8, d9, "d")
colE=Column(5, e1, e2, e3, e4, e5, e6, e7, e8, e9, "e")
colF=Column(6, f1, f2, f3, f4, f5, f6, f7, f8, f9, "f")
colG=Column(7, g1, g2, g3, g4, g5, g6, g7, g8, g9, "g")
colH=Column(8, h1, h2, h3, h4, h5, h6, h7, h8, h9, "h")
colI=Column(9, i1, i2, i3, i4, i5, i6, i7, i8, i9, "i")

ColList=ColumnsList(colA, colB, colC, colD, colE, colF, colG, colH, colI)

#9 Rows

row1=Row(1, a1, b1, c1, d1, e1, f1, g1, h1, i1)
row2=Row(2, a2, b2, c2, d2, e2, f2, g2, h2, i2)
row3=Row(3, a3, b3, c3, d3, e3, f3, g3, h3, i3)
row4=Row(4, a4, b4, c4, d4, e4, f4, g4, h4, i4)
row5=Row(5, a5, b5, c5, d5, e5, f5, g5, h5, i5)
row6=Row(6, a6, b6, c6, d6, e6, f6, g6, h6, i6)
row7=Row(7, a7, b7, c7, d7, e7, f7, g7, h7, i7)
row8=Row(8, a8, b8, c8, d8, e8, f8, g8, h8, i8)
row9=Row(9, a9, b9, c9, d9, e9, f9, g9, h9, i9)

RowList=RowsList(row1, row2, row3, row4, row5, row6, row7, row8, row9)

#9 Squares

sq1=Square(1, a9, b9, c9, a8, b8, c8, a7, b7, c7)
sq2=Square(2, d9, e9, f9, d8, e8, f8, d7, e7, f7)
sq3=Square(3, g9, h9, i9, g8, h8, i8, g7, h7, i7)
sq4=Square(4, a6, b6, c6, a5, b5, c5, a4, b4, c4)
sq5=Square(5, d6, e6, f6, d5, e5, f5, d4, e4, f4)
sq6=Square(6, g6, h6, i6, g5, h5, i5, g4, h4, i4)
sq7=Square(7, a3, b3, c3, a2, b2, c2, a1, b1, c1)
sq8=Square(8, d3, e3, f3, d2, e2, f2, d1, e1, f1)
sq9=Square(9, g3, h3, i3, g2, h2, i2, g1, h1, i1)

SquareList=SquaresList(sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9)


#1 board (9x9 square).

board=Board(ColList, RowList, SquareList, TileList)