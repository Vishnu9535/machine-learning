# give the code to build tic tac toe game
# compltere the code for the game

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    a=actions(board)
    if player(board)==X:
        v=-100000
        for i in a:
            v=max(v,min_value(result(board,i)))
            if v==1:
                return i
    else:
        v=100000
        for i in a:
            v=min(v,max_value(result(board,i)))
            if v==-1:
                return i
    return i

