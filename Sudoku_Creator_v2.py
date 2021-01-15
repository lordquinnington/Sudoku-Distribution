#~~~~~ Sudoku Creator v2 ~~~~~#

import random, csv, copy
from Sudoku_Generator_v2 import generateCompletedGrid
from Sudoku_Solver_Without_Guessing import solve, formatSudokuGridTo5DFrom2D

################################################ formatting functions ################################################

def writeNewGridToCSV(gridArray2D,gridNumber):    # function to write the new grid to a file 
    with open("Sudoku_Grid_New_"+gridNumber+".csv","w",newline='') as newGridFile:
        toWrite = csv.writer(newGridFile,delimiter=',')
        for row in gridArray2D:
            toWrite.writerow(row)

def findGridName():     # finds the next available grid name to call the new file (to avoid overwriting previous grids)
    available = False
    x = 1
    while not available:
        try:
            open("Sudoku_Grid_New_"+str(x)+".csv","x")
            return str(x)
        except FileExistsError:     # if the file already exists then it moves onto the next one
            x += 1

################################################ creating functions ################################################

def removeRandomNumber(gridArray):    # function to remove a random number from the grid
    zero = True
    while zero:
        options = [0,1,2,3,4,5,6,7,8]
        a = random.choice(options)    # generates 4 random coordinates to remove from
        b = random.choice(options)
        if gridArray[a][b] != 0:    # only removes it if the square is filled in
            gridArray[a][b] = 0
            zero = False
        else:    # if the square is 0, it will have to generate another set of random coordinates
            zero = True
    return gridArray

def createNewPuzzle(newGrid,difficulty):
    origGrid = copy.deepcopy(newGrid)
    squaresToKeep = random.randint((25+5*difficulty),((25+5*difficulty)+5))    # decides how many numbers to keep - 40-45 easy, 35-40 medium, 30-35 hard, 25-30 expert
    for i in range(81-squaresToKeep):
        prevGrid = copy.deepcopy(newGrid)
        valid = False
        j = 0
        while not valid:
            j += 1
            newGrid = removeRandomNumber(newGrid)
            tempGrid = solve(formatSudokuGridTo5DFrom2D(newGrid,3),3)     # a bit of a slower way of generating but should be better for solving for the user
            if tempGrid == None:
                newGrid = copy.deepcopy(prevGrid)
            elif j > 81:
                newGrid = createNewPuzzle(origGrid,difficulty)     # a bit of recursion to start again for if the program generates a grid which can't be easily solved
                return newGrid
            else:
                valid = True
    return newGrid
