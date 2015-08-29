
import random

MOVE_TO_INDEX = {'r': 0, 'p': 1, 's': 2}
ALPHA = .95

class CPU():
    def __init__(self, player_num):
        self.player_num = player_num
        self.type = 'cpu'

        # 9 options for each rps combination for human and cpu
        self.prob_matrix= [([1.0 / 3] * 3)[:] for i in range(9)]

    def choose_move(self, gamestate):
        moves = ['r', 'p', 's']

        if gamestate.moves:
            previous_move = gamestate.moves[-1]
        else:
            return random.choice(moves)

        own_move, opp_move = previous_move
        if self.player_num == 2:
            opp_move, own_move = previous_move
        index = MOVE_TO_INDEX[own_move] * 3 + MOVE_TO_INDEX[opp_move]
        probs = self.prob_matrix[index]

        expected_points = {}
        expected_points['r'] = probs[MOVE_TO_INDEX['s']] - probs[MOVE_TO_INDEX['p']]
        expected_points['p'] = probs[MOVE_TO_INDEX['r']] - probs[MOVE_TO_INDEX['s']]
        expected_points['s'] = probs[MOVE_TO_INDEX['p']] - probs[MOVE_TO_INDEX['r']]

        return max(expected_points, key=lambda x: expected_points[x])

    def process_moves(self, gamestate):
        if len(gamestate.moves) <= 1:
            return

        prev_move = gamestate.moves[-2]
        cur_move = gamestate.moves[-1]

        if self.player_num == 1:
            prev_own_move, prev_opp_move = prev_move
            cur_own_move, cur_opp_move = cur_move
        else:
            prev_opp_move, prev_own_move = prev_move
            cur_opp_move, cur_own_move = cur_move

        index = MOVE_TO_INDEX[prev_own_move] * 3 + MOVE_TO_INDEX[prev_opp_move]
        probs = self.prob_matrix[index]

        probs = [el * ALPHA for el in probs]
        move_index = MOVE_TO_INDEX[cur_opp_move]
        probs[move_index] += 1.0 - ALPHA
        self.prob_matrix[index] = probs
