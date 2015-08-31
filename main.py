
import random
from gameset import GameSet
import json
import os


def main():
    outfile = 'rps_data.txt'
    gameSet = GameSet()

    if os.path.isfile(outfile):
        os.remove(outfile)
    f = open(outfile, 'awr')
    f.write('p1: {}\np2: {}\n'.format(gameSet.p1.type, gameSet.p2.type))

    wins, losses, draws = (0, 0, 0)
    results = []
    for i in range(gameSet.num_games):
        print 'on game {} of {}'.format(i + 1, gameSet.num_games)
        result = gameSet.play_game()
        if result == 1:
            wins += 1
        elif result == 0:
            draws += 1
        elif result == -1:
            losses += 1
        f.write('{}, {}\n'.format(result, json.dumps(gameSet.moves[-1])))

    f.close()
    print 'p1 wins: {}\np2 wins: {}\ndraws: {}'.format(wins, losses, draws)

if __name__ == '__main__':
    main()
