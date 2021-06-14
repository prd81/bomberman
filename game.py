""" Implementation for single session """
from random import choice
from bomb import Bomb
from timer import inp

def game(unpack):
    """ Main method """
    lives, level, score, boa, per, eny = unpack
    bot, bas = 0, 3
    time = 600 * level
    while True:
        boa.show(lives, level, score, time)
        time -= 1
        if not time:
            if bot:
                xbomb.dispose()
            return ('out', lives, level, score)
        charx = inp()
        chx = per.char(charx)
        if per.char('x') == 'e' or chx == 'E':
            if bot:
                xbomb.dispose()
            return ('out', lives, level, score)
        if charx == 'q':
            query = "do you want to quit current game? (Y/n) : "
            sinp = input(query).lower()
            if sinp != 'n':
                return ('quit', lives, level, score)
            continue
        if charx == 'b' and not bot:
            xbomb = Bomb(per)
            bot = bas + 2
        elif charx and chx == ' ':
            per.move(charx)
        if bot:
            boa.set(xbomb.blx, xbomb.bly, str(bot-2))
            if bot == 1:
                xbomb.dispose()
            elif bot == 2:
                score += xbomb.blast()
            bot -= 1
        for i in range(len(eny)-1, -1, -1):
            if eny[i].char('x') == 'e':
                del eny[i]
                continue
            sch = ['a', 'd', 'w', 's']
            while sch:
                nsel = choice(sch)
                chx = eny[i].char(nsel)
                if chx == 'B':
                    if bot:
                        xbomb.dispose()
                    boa.show(lives, level, score, time)
                    return ('out', lives, level, score)
                if chx == ' ':
                    eny[i].move(nsel)
                    break
                sch.remove(nsel)
        if not eny:
            boa.show(lives, level, score, time)
            return ('cross', lives, level, score)
