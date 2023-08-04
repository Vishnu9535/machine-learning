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
    cx = sum(row.count('X') for row in board)
    co = sum(row.count('O') for row in board)
    if cx == co:
        return 'X'
    return 'O'
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 'EMPTY'):
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if (board[i][j] != 'EMPTY'):
        raise ValueError(" not a valid move")

    to_add = player(board)
    new_board = board
    new_board[i][j] = to_add
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[0][i] == board[1][i] and board[2][i] == board[1][i]:
            return board[0][i]

    for i in board:
        if i == ['X', 'X', 'X']:
            return 'X'
        if i == ['O', 'O', 'O']:
            return 'O'

    if (board[0][0] != '.' and
        board[0][0] == board[1][1] and
            board[0][0] == board[2][2]):
        return board[0][0]

    if (board[0][2] != '.' and
            board[0][2] == board[1][1] and
            board[0][2] == board[2][0]):
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    
    if winner(board) == 'O':
        return -1
    
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curr_player= player(board)
    if curr_player == 'X':
        action=max_value(board)
        return action

    if curr_player == 'O':
        action= min_value(board)
        return action 

def max_value(board):
    
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    best_action = None

    for action in actions(board):
        new_board= result(board,action)
        value = min_value(new_board)
        if v < value :
            v= value
            best_action = action
        
        return best_action


def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf
    best_action = None

    for action in actions(board):
        new_board= result(board,action)
        value = max_value(new_board)
        if v > value :
            v = value
            best_action = action
                
        return best_action
