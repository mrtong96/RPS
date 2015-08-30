
import random
from gameset import GameSet


def main():
    gameSet = GameSet()

    wins, losses, draws = (0, 0, 0)
    for i in range(gameSet.num_games):
        result = gameSet.play_game()
        if result == 1:
            wins += 1
        elif result == 0:
            draws += 1
        elif result == -1:
            losses += 1
    print 'p1 wins: {}\np2 wins: {}\ndraws: {}'.format(wins, losses, draws)

if __name__ == '__main__':
    main()
