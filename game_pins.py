
# coding: utf-8

# In[4]:

import numpy as np


# #### Necessary functions

# In[37]:

def createBoard():
    board = np.flipud(np.tril(np.ones((5,5), dtype=bool)))
    board[0][0] = False
    return board
    
#     x y 
#     0 4
#     1 3
#     2 2
#     3 1
#     4 0
def isPin(board, x, y):
    # if queried outside of the board just return True
    if(x < 0 or x > 4 or y < 0 or y > 4 - x):
        return True
    return board[x][y]
    
def generatePossibleMovesForField(board, x, y):
    # 6 directions: +x, -x, +y, -y, +xy, -xy
    possibleMoves = list()

    # if position to check is empty
    if not isPin(board,x,y):
        return possibleMoves

    # not clause comes first because the odds are 
    # that we are going to make a lot of comparisons 
    # outside of the board so it will be more efficient

    # +x
    if(not isPin(board,x+2, y) and isPin(board,x+1, y)):
        possibleMoves.append((x,y,x+2,y))
    # -x
    if(not isPin(board,x-2, y) and isPin(board,x-1, y)):
        possibleMoves.append((x,y,x-2,y))
    # +y
    if(not isPin(board,x, y+2) and isPin(board,x, y+1)):
        possibleMoves.append((x,y,x,y+2))
    # -y
    if(not isPin(board,x, y-2) and isPin(board,x, y-1)):
        possibleMoves.append((x,y,x,y-2))
    # +x-y
    if(not isPin(board,x+2, y-2) and isPin(board,x+1, y-1)):
        possibleMoves.append((x,y,x+2,y-2))
    # -x+y
    if(not isPin(board,x-2, y+2) and isPin(board,x-1, y+1)):
        possibleMoves.append((x,y,x-2,y+2))

    return possibleMoves

def generateAllPossibleMovesForBoard(board):
    possibleMoves = list()

    for x in xrange(5):
        for y in xrange(5-x):
            possibleMoves += generatePossibleMovesForField(board, x, y)

    return possibleMoves

def makeMove(board, x, y, xx, yy):
    board = board.copy()
    if not isPin(board,x,y) or not isPin(board,(x+xx)/2,(y+yy)/2) or isPin(board,xx, yy):
        raise Exception('Invalid move x={} y={} xx={} yy={}'.format(x, y, xx, yy))
        return None
    board[x][y] = False
    board[(x+xx)/2][(y+yy)/2] = False
    board[xx][yy] = True
    return board


# In[28]:

def bt(c, count, boards):
#     print(c.astype(int))

    boards = list(boards)

    boards.append(c)

#     if count % 100 == 0: 
#         print count
    
    possibleMoves = generateAllPossibleMovesForBoard(c)
    
    if np.sum(c) == 1: 
        print('MADE IT')
        return (True, count + 1, boards)
    
    if not possibleMoves: return (False, count + 1, boards)
    
    for possibleMove in possibleMoves:
        s = makeMove(c, *possibleMove)
        isWin, count, winningBoards = bt(s, count, boards)
        
        if isWin:
            return (True, count + 1, winningBoards)
    
    return (False, count + 1, boards)


# #### Solution

# In[36]:

board = createBoard()
isWin, count, winningBoards = bt(board,0,[])

print('Steps to win: {}'.format(count))

for b in winningBoards:
    print b.astype(int)
    print('')


# #### Tests

# In[35]:

board = np.zeros((5,5), dtype=bool)
board[0][0] = 1
board[0][2] = 1
board[0][3] = 1
isWin, count, winningBoards = bt(board,0,[])

print(count)
for b in winningBoards:
    print b.astype(int)


# In[31]:

board = createBoard()
print(board.astype(int))
print(generateAllPossibleMovesForBoard(board)[0])
board = makeMove(board, *generateAllPossibleMovesForBoard(board)[0])# 0, 2, 0, 0)
print(board.astype(int))


# In[32]:

board = createBoard()
print(board.astype(int))
generatePossibleMovesForField(board, 2,0)


# In[33]:

board = createBoard()
board[0][0] = True
board[3][1] = False
print(board.astype(int))
generatePossibleMovesForField(board,1,3)


# In[26]:

board = createBoard()
board[0][0] = True
board[0][4] = False
board[4][0] = False
print(board.astype(int))
generatePossibleMovesForField(board,2,2)

