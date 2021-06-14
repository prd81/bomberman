""" Main module """
from random import choice
from time import sleep
from os import system as do
from board import Board
from person import Person
from game import game

def welcome():
    """ Welcome screens """
    do('clear')
    time = 3
    for i in range(time, 0, -1):
        for j in (i, ' '):
            do('clear')
            print('Welcome to BombermanXtreme')
            print('Game begins in .....', j)
            sleep(0.5)
    do('clear')
    print('Start...')
    sleep(0.5)
    do('clear')

def main():
    """ Main method """
    welcome()

    def new(level):
        """ Initialising method """
        xlev = Board(level)
        xen, eco = [], 1<<level
        for i in range(eco):
            i += 0
            blx, bly = choice(Board.eloc)
            xen += [Person('E', blx, bly)]
            Board.eloc.remove((blx, bly))
        return xlev, xen

    def reset():
        """ Resetting reference """
        xlives, xlevel, xscore = 3, 1, 0
        return xlives, xlevel, xscore
    lives, level, score = reset()
    boa, eny = new(level)
    hscore = 10
    while True:
        per = Person('B', 1, 1)
        stat, lives, level, score = game((lives, level, score, boa, per, eny))
        per.set(per.blx, per.bly, ' ')
        if stat == 'out':
            lives -= 1
            if not lives:
                print('Game Over.')
            else:
                print('OOPS!! Remaining LIVES : %d. Loading...'%lives)
                sleep(3)
                continue
        elif stat == 'cross':
            level += 1
            if level == Board.mlevel + 1:
                print('Victory!')
            else:
                print('Yeah, LEVEL %d completed! Loading...'%(level - 1))
                sleep(3)
                boa, eny = new(level)
                continue
        elif stat == 'quit':
            print('Game quit.')
        print('Your SCORE :', score)
        if score > hscore:
            hscore = score
            print('NEW HIGHSCORE!')
        query = 'New Game? (y/N) : '
        sinp = input(query).lower()
        if sinp == 'y':
            lives, level, score = reset()
            boa, eny = new(level)
        else:
            do('clear')
            print('Goodbye. See you soon.')
            sleep(1)
            do('clear')
            break

main()
