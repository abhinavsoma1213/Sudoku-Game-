
#Sudoku is a logic based number placement puzzle. The objective is to fill each individual sub grids of the whole board.
#To solve the puzzle, you need to fill in the blank squares with numbers ranging from 1 to 9. The catch is that each
# square must contain a value that is unique to that row, column, and box. 
#This is a 9 by 9 grid or also a matrix

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



#This is the backtracking algorithm function. We would be using recursion and we will do this by calling the function from 
#inside the function. Our base case assumption would be that the board is full. 
def solve(bo):

    #This will find if any squares in the board are empty and if does not find anything empty it returns True
    #The find_empty is triggered when the function below and it triggers it 
    find = find_empty(bo)
    if not find:
        return True
    #This else statement states that there is a row and column to solve/ is empty

    else:
        row, col = find
    
    #The if and else statement and the find_empty function is the base case for recursion

    #We will loop through values from 1 to 9 and we will attempt to put those values in our solution
    for i in range(1,10):
        #We will use a conditional statement to make sure the values we add in the board are valid
        if valid(bo, i, (row, col)):
            #We will plug in the value
            #If the value is valid we will add it in the board

            bo[row][col] = i

            #We will solve the solution here by recursively trying to finish the solution by calling solve on our new board
            #We will keep on calling solve and keep on trying until we looped through all the values and get the solution
            #or we get to the point where we tried all the solutions and we none are valid


            if solve(bo):
                return True

            #Which means that if we return False, that means that the solve(boa) is not true so we will backtrack and say
            #that the last element we added and we reset it and we try the for loop again with different values

            bo[row][col] = 0

    #if we try all the solutions and none are valid we return False
    return False

#We need to find if the current board is valid
#We check the row, the column, and the square we are in
def valid(bo, num, pos):
    # Check row
    #First step check the row, we loop through every column in the given row
    for i in range(len(bo[0])):
        #We check every column/ each element in the row and we are going to check if it is equal to the number we added
        #The second part of the and statement is that we will ignore a position that we already inserted into to.
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    #We check the column here

    for i in range(len(bo)):
        #As the first for loop above that checks the row, we check the columns which go from 0 - 8 and we check if our current
        # column value is equal to the same number we inserted for each row and the second statement in the and logical operator
        # checks if we did not insert a number into a position that has a number already inserted into to.


        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    #Check the boxes, which the numbers lie in. This will check which box we are currently located in.
    #The boxes houses a group of numbers that we will solve for.
    box_x = pos[1] // 3
    box_y = pos[0] // 3


    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

#This whole function is to formate the board 
def print_board(bo):

    #This first for loop will go through the columns
    for i in range(len(bo)):

        #This will do down 3 columns that are not equal to 0 and it prints a seperation dashed line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        #This second for loop will go through the rows and iterate through them
        for j in range(len(bo[0])):
            #We will check if it is the third element/ multiple of 3 and we will draw the row line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            #This if and else statement will check if we are at the end of the element and we will backslach and go to the next line
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#This function will find an empty square we can use our algorithm in and return the position of the square
def find_empty(bo):

    #The empty square is denoted with the number 0
    #This checks the element in the row of the board
    for i in range(len(bo)):

        #This checks every element in the column of the board
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                #This will return the position of the empty square 
                return (i, j)  # row = i, column = j

    #This return None statement means that if there are no squares that are 0 or left empty it returns that the board is full
    return None

#We will print board which the matrix above. 
#We call function called print board and we call board in the arguement
print_board(board)
#We call solve and put the arguement of board in it. This solves it and changes it 
solve(board)

print("___________________")

#This is when all the recursion and the backtracking algorithm changes the board so we can solve it algorithmically.
#We call function called print board and we call board in the arguement
print_board(board)