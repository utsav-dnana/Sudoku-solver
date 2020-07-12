import math
board=[[8,0,0,5,0,1,0,0,9],
        [0,9,0,6,0,0,0,8,0],
        [0,0,0,0,2,8,7,0,0],
        [0,8,0,3,0,2,0,1,0],
        [6,3,0,0,1,0,0,0,8],
        [0,0,5,7,0,9,0,4,0],
        [0,0,8,0,7,0,1,0,5],
        [0,2,0,1,0,6,0,3,0],
        [4,0,0,0,9,0,0,0,2]]

def solve_sudoku(grid):
    '''
    :param grid : given 9*9 grid of unsolved soduko
    
    '''
    li=[0,0]
    if(not(empty(grid,li))):
        return True
    row=li[0]
    col=li[1]
    for k in range(1,len(grid)+1):
        if(is_safe(grid,row,col,k)==True):
            grid[row][col]=k
            if(solve_sudoku(grid)):
                return True
            grid[row][col]=0
    return False
    
def empty(grid,li):
    for m in range(len(grid)):
        for n in range(len(grid)):
            if(grid[m][n]==0):
                li[0]=m
                li[1]=n
                return True
    return False

def is_safe(grid,i,j,k):
    for m in range(len(grid)):
        if(grid[i][m]==k):
            return False
    for n in range(len(grid)):
        if(grid[n][j]==k):
            return False
    s=int(math.sqrt(len(grid)))
    rs=i-i%s
    cs=j-j%s
    for m in range(s):
        for n in range(s):
            if(grid[m+rs][n+cs]==k):
                return False
    return True

'''if(solve_sudoku(board)):
    print(board)
else:
    print('No solution exist')'''