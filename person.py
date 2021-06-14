""" Module for the Bomberman and his Enemies """
from board import Board
class Person(Board):
    """ Single Class for both """
    def __init__(self, char, blx, bly):
        self.icon = char
        self.blx = blx
        self.bly = bly
        self.set(blx, bly, char)

    def coor(self, char):
        """ Gives coordinates around the position """
        dct = {'a':(-1, 0), 'd':(1, 0), 'w':(0, -1), 's':(0, 1)}
        dis = dct.get(char, (0, 0))
        return self.blx + dis[0], self.bly + dis[1]

    def char(self, char):
        """ Gives character on the grid at a coordinate """
        blx, bly = self.coor(char)
        return Board.grid[bly][blx]

    def move(self, char):
        """ Move in specified direction """
        blx, bly = self.coor(char)
        self.set(self.blx, self.bly, ' ')
        self.blx, self.bly = blx, bly
        self.set(blx, bly, self.icon)
