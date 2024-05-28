def is_valid(board,row,col,num):
  for i in range(9):
    if board[row][i]==num or board[i][col]==num:
      return False
  zero_row=(row//3)*3
  zero_col=(col//3)*3
  for i in range(3):
    for j in range (3):
      if board[zero_row+i][zero_col+j]==num:
        return False
  return True

def solve_sudoko(board):
  for row in range(9):
    for col in range(9):
      if board[row][col]==0:
        for num in range(1,10):
          if is_valid(board,row,col,num):
            board[row][col]=num
            if solve_sudoko(board):
              return True
            board[row][col]=0
        return False
  return True
board=[[2,0,4,3,1,0,0,5,7],
       [1,3,0,2,5,7,0,4,6],
       [0,6,5,0,3,0,8,0,9],
       [3,2,4,0,5,0,7,0,0],
       [5,1,4,3,0,0,2,0,0],
       [6,5,0,0,2,0,1,0,8],
       [7,0,4,5,8,0,0,9,1],
       [9,0,1,4,5,7,0,8,0],
       [0,1,0,4,0,5,0,7,6]]
        
solution=solve_sudoko(board)
if solution:
  for row in solution:
    print(row)
else:
  print("No solution")