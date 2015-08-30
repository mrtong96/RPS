
### Overview ###

This is a bot that can run and play a set number of Rock Paper Scissors (RPS) games. This bot tries to predict what it's opponent will play in order to maximize its winning percentage.

### Instructions for Playing ###

1) Download this repository

```
$ git clone git@github.com:mrtong96/RPS.git
```

2) Run main.py

```
$ python main.py
```

3) Enter information when prompted to start game

4) Start playing

### Technical Details ###

* This bot tries to estimate the probabilities that its opponent will play rock, paper, or scissors based on looking at the outcome of the last game. In the case of the first game, a random move is chosen.
* There are 9 conditional probability tables that estimate the chances of its opponent playing a certain move given the previous match's outcome (3 possible bot responses and 3 possible opponent responses).
* To decide which move to play, the bot selects the relevant table and selects the move that will maximize its expected value. The bot assumes that a loss is worth -1, a win is worth 1, and a draw is worth 0 points.
* After each game, the bot records the outcome and updates the relevant table. The probabilities are updated by multiplying all of the values by the constant ALPHA and then adding (1 - ALPHA) for the opponent's response.

### Notes ###

* This bot was designed to take advantage of the fact that humans are generally not very good at acting randomly and exploit patterns.
* In general, it takes around 50-100 games before the bot begins to exploit patterns in its human opponents.
* If the bot plays itself, all of the games except for the first one are draws.

### Contact ###

* email: mrtong96@gmail.com
