"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cx= sum(row.count('X') for row in board)
    co =  sum(row.count('O') for row in board)
    if cx ==  co:
        return 'X'
    return 'O'
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves=set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 'EMPTY'):
                moves.add((i,j))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i , j=action
    if(board[i][j] != 'EMPTY'):
        raise ValueError(" not a valid move")
    
    to_add = player(board)
    board[i][j] = to_add
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
