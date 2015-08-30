
from cpu import CPU
from human import Human

class GameSet():
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.moves = []

        while True:
            p1 = raw_input('player 1: human or cpu?\n')
            if p1 == 'human' or p1 == 'cpu':
                break
            else:
                print "error, please enter 'human' or 'cpu'"
        if p1 == 'human':
            self.p1 = Human(1)
        else:
            self.p1 = CPU(1)

        while True:
            p2 = raw_input('player 2: human or cpu?\n')
            if p2 == 'human' or p2 == 'cpu':
                break
            else:
                print "error, please enter 'human' or 'cpu'"
        if p2 == 'human':
            self.p2 = Human(2)
        else:
            self.p2 = CPU(2)

        while True:
            out = raw_input('how many games?\n')
            try:
                self.num_games = int(out)
                break
            except:
                print 'error, please enter a number'

    def play_game(self):
        move1 = self.p1.choose_move(self)
        move2 = self.p2.choose_move(self)

        self.moves.append((move1, move2))

        self.p1.process_moves(self)
        self.p2.process_moves(self)

        if move1 == move2:
            print('tie\n')
            return 0
        elif (move1 == 'p' and move2 == 'r') or (move1 == 'r' and move2 == 's') or (move1 == 's' and move2 == 'p'):
            print ('player 1 wins\n')
            return 1
        else:
            print ('player 2 wins\n')
            return -1