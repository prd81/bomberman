# BombermanXtreme

The board script consists of the basic board generation of game, including walls and bricks. Everytime an instance of board class is created, the game board is generated.

This module also consists of various dimensions and settings, like length and breadth of board, block grids, color schemes, etc.

Default dimensions of board are 60 * 18, that of blocks are 4 * 2.

Next, the person module has person class to create bomberman and enemies.

The differentiating factor among all elements on the board is the character repersenting them, on the Board.grid array. This is the array containing info. of all elements on the board at any time. It is used to print the board.

Therefore, bomberman and enemies are distinguished by 'B', 'E'.

The bomb module contains methods about bomb, including generation, blasting, and disposal.

The timer module handles the input method of characters, during the gameplay. It works in such a way that, the game waits for 1 sec for user input, else automatically a 'none' character is entered.

The game function in game module handles all the control flows during a single game session, i.e. during 1 life of bomberman, and issues various return calls, containing how the session ended, at termination.

The game runs under the run module, which compares the various return values of the game function, and behaves accordingly.

## Controls :

Basic movement controls - 'a','d','w','s' for left,right,up,down resp.
Drop bomb - 'b'
Quit game - 'q'

All the above mentioned controls are in lower case.

## Gameplay :

Given version of game is controlled by no. of steps or time indirectly.
3 lives are given to bomberman to kill all enemies.
Bomberman is spawned at 1,1 at every game.
There are 3 difficulty levels, with varying time limit,
no. of enemies, and no. of bricks.

LEVEL 1 - 2 enemies, low no. of bricks, 600 moves.
LEVEL 2 - 4 enemies, med no. of bricks, 1200 moves.
LEVEL 3 - 8 enemies, high no. of bricks, 1800 moves.

At end of every life, board setup is maintained.
However, at new level, it changes accordingly.

The bomberman can plant 1 bomb at time, at any empty block it stands at. It takes 3 frames/secs to blast the bomb. If enemy is caught in explosion, 100 pts are added to score. If bomberman is caught, he loses 1 life. Each brick adds 20 pts. At new level/life, previously planted bombs are disposed.

It is preferrable to play it on light background setup.

### Additional Python libraries used :

 ==> signal, time, termcolor, random, os

### To start the game, run the run.py file :
```
python3 run.py
```
