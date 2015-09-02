
class Human():
    def __init__(self, player_num):
        self.type = 'human'
        self.player_num = player_num

        self.counter = 0

    # gamestate variable not used, for compatibility with CPU method
    def choose_move(self, gamestate):
        valid_responses = ['r', 'p', 's', 'q', 'w', 'e', 'rock', 'paper', 'scissors']
        while True:
            response = raw_input('choose a move\n')
            if response in valid_responses:
                break
            print ('error: need a valid response, valid responses: {}'.format(valid_responses))
            print ('q=rock, w=paper, e=scissors')
        shortcuts = ['q', 'w', 'e']
        shortcut_key = {'q': 'r', 'w': 'p', 'e': 's'}
        if response in shortcuts:
            response = shortcut_key[response]
        return response[0]

    def process_moves(self, gamestate):
        return
