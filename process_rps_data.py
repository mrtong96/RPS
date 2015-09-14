
import json
import matplotlib.pyplot as plt
import copy
import numpy as np

outfiles = [
    'data/rps_data_vy.txt',
    'data/rps_data_alice.txt',
    'data/rps_data_eric.txt',
    'data/rps_data_michael.txt',
    'data/rps_data_michael2.txt',
    'data/rps_data_subhodeep.txt',
    'data/rps_data_random.txt'
]

MOVE_TO_INDEX = {'r': 0, 'p': 1, 's': 2}
INDEX_TO_MOVE = {0: 'r', 1: 'p', 2: 's'}
ALPHA = .95

for outfile in outfiles:
    print ('file name: {}'.format(outfile))
    wins, losses, draws = (0, 0, 0)
    text = open(outfile, 'r').read()
    text = text.split('\n')

    scores = []
    moves = []
    for line in text:
        data = line.split(',')
        if len(data) == 3:
            score = int(data[0])
            if score == 1:
                wins += 1
            elif score == -1:
                losses += 1
            else:
                draws += 1
            scores.append(score)
            moves.append(data[1:])

    sizes = [10, 20, 50, 100, 200]
    for size in sizes:
        out = []
        for i in range(len(scores) // size):
            out.append(sum(scores[i * size: i * size + size]))
        print ('overall score for every {} games: {}'.format(size, out))
    
    prob_matrix = [([1.0 / 3] * 3)[:] for i in range(9)]
    prob_matrices = []
    for i in range(len(moves) - 1):
        index = MOVE_TO_INDEX[moves[i][1]] * 3 + MOVE_TO_INDEX[moves[i][0]]
        probs = prob_matrix[index]

        probs = [el * ALPHA for el in probs]
        move_index = MOVE_TO_INDEX[moves[i + 1][0]]
        probs[move_index] += 1.0 - ALPHA
        prob_matrix[index] = probs

        prob_matrices.append(copy.deepcopy(prob_matrix))

    print ('probability matrix')
    for i, el in enumerate(prob_matrix):
        print ('human: {}, cpu: {}, table: {}'.format(INDEX_TO_MOVE[i % 3], INDEX_TO_MOVE[i // 3], el))

    plt.suptitle(outfile + '\n rock=red, paper=blue, scissors=green')
    prob_matrices = zip(*prob_matrices)
    x_values = np.arange(1., float(len(scores)), 1.)
    for i, p_tables in enumerate(prob_matrices):
        r_list, p_list, s_list = zip(*p_tables)
        human_move = INDEX_TO_MOVE[i % 3]
        cpu_move = INDEX_TO_MOVE[i // 3]
        plt.subplot(331 + i)
        plt.title('human: {}, cpu: {}'.format(INDEX_TO_MOVE[i % 3], INDEX_TO_MOVE[i // 3]))
        plt.plot(x_values, r_list, 'ro', x_values, p_list, 'bo', x_values, s_list, 'go')
    plt.show()

    print ('p1: {}\np2: {}\ndraws: {}'.format(wins, losses, draws))
    print ('total games: {}'.format(wins + losses + draws))

