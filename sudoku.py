print("\nThis is a game of Sudoku ")
print("\nWelcome to my Game of Sudoku!")
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
for i in range(len(grid)):
    for j in range(len(grid)):
        if (j+1)%3!=0 :
            print(grid[i][j],end=" | ")
        else:
            if j+1!=9:
                print(grid[i][j],end="  +  ")
            else:
                print(grid[i][j],end="")
    if (i+1)%3!=0 or i+1==9 :
        print("\n_ _ _ _ _  +  _ _ _ _ _  +  _ _ _ _ _ _ \n")    
    else:
        print("\n\n+ + + + + + + + + + + + + + + + + + + +")
        print()
    