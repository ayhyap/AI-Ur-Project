# AI-Ur-Project

Originally a project for an AI course.
Simulates the Royal Game of Ur, using optional turtle graphics (setting in globalVars.py).

Currently being rewritten for Python 3.6.3.

Run play.py to play. Enter inputs (where relevant) into IDE.

Currently, only human input and expectimax has been implemented. Genetic NN will be added when complete.

## The Royal Game of Ur

Ur is an ancient board game played around 2500BC. The "official" rules have been lost to time, but several rulesets have been derived from various recovered documents.

Ur is a turn-based 2-player versus game, where players must race to move their pieces across the board before the opponent, similar to backgammon.

The number of moves a player can make per turn is determined by 4 tetrahedral dice rolls. The result is equivalent to 4 coin tosses, and is perfectly estimated by Binom(4,0.5). This means it is possible to roll 0, and get 0 moves.

All pieces must follow a set path of tiles along the board. Each tile can only hold 1 piece. Moving a piece onto an opponent's piece displaces the opponent's piece, and sends it back to the start. Moving a piece onto your own piece is an invalid move.

There are also 5 flower tiles, which grant displacement immunity and an extra turn to the player who lands on it.

For this rendition, each player has 7 pieces.

## Expectimax

This AI is implemented by searching a game tree which shows all possible game states from the current state.

The board state, result of the diceroll and player is inputted, and a tree is generated.

```
MIN/MAX               DEPTH: 1
|||branches/node = 7 (each player has 7 pieces)
EXPECT                DEPTH: 1
|||branches/node = 5 (diceroll can range from 0 to 4)
MAX/MIN               DEPTH: 2
|||branches/node = 7
.
.
.
EXPECT                DEPTH: n
|||branches = 5
EVALUATION
```
Upon reaching the input search depth, an evaluation function is called to calculate an approximate score. The score is calculated as: Player2 Progress - Player1 Progress. Thus, player1 is trying to minimize this score, and player2 is trying to maximize it.

The branching factor is 35^n.

Testing has revealed that expectimax performance increases with depth, but becomes much slower. In addition, increasing the depth has diminishing performance returns: depth 1 (d1) lost to d4 in all matches, but d2 and d4 were already quite evenly matched (46 - 54). 

Curiously, d3 performed worse than d2 against d4 (42 - 58), though that could be a result of poor dicerolls.

Perhaps worthy of note, is that odd depths stop their evaluation after one of their OWN moves, while even depths stop after an opponent's move.
