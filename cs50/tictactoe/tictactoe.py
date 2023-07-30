"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

# complete the below code for the game
def initial_state():
    """
    Returns starting state of the board.
    """
    a=list()
    a= [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
    return a
    # raise NotImplementedError


def player(board):
    """ 
    Returns player who has the next turn on a board.
    """
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                count=count+1
    if count%2==0:
        return O
    else:
        return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                a.add((i,j))
    return a
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a=player(board)
    board[action[0]][action[1]]=a
    return board


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=EMPTY:
            return board[i][0]
        elif board[0][i]==board[1][i]==board[2][i]!=EMPTY:
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2]!=EMPTY:
        return board[0][0]
    elif board[0][2]==board[1][1]==board[2][0]!=EMPTY:
        return board[0][2]
    else:
        return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j]==EMPTY:
                    return False
        return True
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board)==X:
        v=-math.inf
        for action in actions(board):
            k=min_value(result(board,action))
            if k>v:
                v=k
                move=action
    else:
        v=math.inf
        for action in actions(board):
            k=max_value(result(board,action))
            if k<v:
                v=k
                move=action

    return move
def min_value(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,max_value(result(board,action)))
    return v
def max_value(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):
        v=max(v,min_value(result(board,action)))
    return v
a=list()
a=initial_state()
print(a)
player(a)