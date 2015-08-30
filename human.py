class Human():
    def __init__(self, player_num):
        self.type = 'human'
        self.player_num = player_num

        self.counter = 0

    # gamestate variable not used, for compatibility with CPU method
    def choose_move(self, gamestate):
        valid_responses = ['r', 'p', 's', 'rock', 'paper', 'scissors']
        while True:
            response = raw_input('choose a move\n')
            if response in valid_responses:
                break
            print ('error: need a valid response, valid responses: {}'.format(valid_responses))
        return response[0]

    def process_moves(self, gamestate):
        return