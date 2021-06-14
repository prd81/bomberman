""" Module contains functionality of bomb objects """
from board import Board
from person import Person
class Bomb(Person):
    """ Sole class of the module """
    echar = 'e'
    def __init__(self, bomber):
        self.blx = bomber.blx
        self.bly = bomber.bly

    def blast(self):
        """ Blasts the bomb """
        score = 0
        lis = {'/':20, 'E':100}
        for i in 'adwsx':
            gridx, gridy = self.coor(i)
            chx = self.char(i)
            if chx != Board.wchar:
                self.set(gridx, gridy, Bomb.echar)
                score += lis.get(chx, 0)
        return score

    def dispose(self):
        """ Dispose the bomb after blasting """
        bombx, bomby = self.blx, self.bly
        self.set(bombx, bomby, ' ')
        for i in 'adws':
            gridx, gridy = self.coor(i)
            if Board.grid[gridy][gridx] == Bomb.echar:
                self.set(gridx, gridy, ' ')
