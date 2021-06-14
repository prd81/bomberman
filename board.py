""" Primary module containing board configuration """
from random import getrandbits as rnd
from os import system as do
from termcolor import colored as col
class Board:
    """ Main class """
    GridX, GridY = 15, 9
    BlockX, BlockY = 4, 2
    mlevel = 3
    wchar, bchar = 'X', '/'
    color = {'E':'red', 'B':'green', '/':'yellow', 'X':'blue'}
    def set(self, locx, locy, char):
        """ Setter method """
        Board.grid[locy][locx] = char
    def get(self, locx, locy):
        """ Getter method """
        return Board.grid[locy][locx]
    def __init__(self, level):
        Board.grid = [[' ']*Board.GridX for i in range(Board.GridY)]
        Board.eloc = []
        for bly in range(Board.GridY):
            for blx in range(Board.GridX):
                bool1 = bly in (0, Board.GridY-1)
                bool2 = blx in (0, Board.GridX-1)
                bool3 = not (blx&1)|(bly&1)
                if bool1 or bool2 or bool3:
                    self.set(blx, bly, Board.wchar)
                elif max(blx, bly) >= 4:
                    if rnd(Board.mlevel-level+1):
                        Board.eloc += [(blx, bly)]
                    else:
                        self.set(blx, bly, Board.bchar)
    def show(self, lives, level, score, time):
        """ Printing method """
        do('clear')
        disx = 30
        for row in Board.grid:
            for i in range(Board.BlockY):
                i += 0
                for char in row:
                    colchar = col(char, Board.color.get(char, 'grey'))
                    print((colchar + ' ') * Board.BlockX, end='')
                print('\n')
        print(("LIVES : %d"%lives).ljust(disx), end='')
        print(("SCORE : %d"%score).ljust(disx), end='')
        print(("LEVEL : %d"%level).ljust(disx), end='')
        print("TIME :", time)
