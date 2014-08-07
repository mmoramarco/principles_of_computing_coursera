"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 150 # Number of trials to run
MCMATCH = 1.0 # Score for squares played by the machine player
MCOTHER = 1.0 # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
	"""
	randomly play the game for both player until either wins or a draw
	board will be modified
	return None
	"""
    while board.check_win() == None:
        empty_lst = board.get_empty_squares()
        next_move = random.choice(empty_lst)
        temp_row = next_move[0]
        temp_col = next_move[1]
        board.move(temp_row, temp_col, player)
        if board.check_win() == None:
            player = provided.switch_player(player)
        else:
            return None

def mc_update_scores(scores, board, player):
    """
	score completed board
	squares of winner get positive, the other party get negative
	"""
    if board.check_win() == provided.DRAW:
        return None   
    elif board.check_win() == player:
        board_dim = board.get_dim()
        for dummy_i in range(board_dim):
            for dummy_j in range(board_dim):
                if board.square(dummy_i, dummy_j) == player:
                    scores[dummy_i][dummy_j] += MCMATCH
                elif board.square(dummy_i, dummy_j) == provided.switch_player(player):
                    scores[dummy_i][dummy_j] -= MCOTHER
    elif board.check_win() == provided.switch_player(player):
        board_dim = board.get_dim()
        for dummy_i in range(board_dim):
            for dummy_j in range(board_dim):
                if board.square(dummy_i, dummy_j) == player:
                    scores[dummy_i][dummy_j] -= MCMATCH
                elif board.square(dummy_i, dummy_j) == provided.switch_player(player):
                    scores[dummy_i][dummy_j] += MCOTHER
        
def get_best_move(board, scores):
    """
	given the board and scores
	find the empty sqaures that of greatest score to be the best move
	"""
    empty_squares = board.get_empty_squares()
    scores_lst = []
    max_squares_lst = []
    for square in empty_squares:
        row = square[0]
        col = square[1]
        scores_lst.append(scores[row][col])
    for dummy_i in range(len(scores_lst)):
        if scores_lst[dummy_i] == max(scores_lst):
            max_squares_lst.append(empty_squares[dummy_i])
    best_move = random.choice(max_squares_lst)
    return best_move

def mc_move(board, player, tirals):
    """
	CLONE THE GIVEN BOARD, NOT A FRESH BOARD
	perform monte carlo simulation and make the optimized move
	"""
    board_dim = board.get_dim()
    scores = [[0 for dummy_col in range(board_dim)] for dummy_row in range(board_dim)]
    for dummy_i in range(tirals):
        temp_board = board.clone()
        mc_trial(temp_board, player)
        mc_update_scores(scores, temp_board, player)
    return get_best_move(board, scores)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)