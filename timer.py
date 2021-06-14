""" For setting time limit on user inputs """
import signal
from getch import getch
def inp():
    """ Main method """
    signal.signal(signal.SIGALRM, lambda signum, frame: None)
    def pre():
        """ Helper method """
        try:
            cur = getch()
            if cur in 'adswbq':
                return cur
            return
        except OverflowError:
            return
    signal.alarm(1)
    out = pre()
    signal.alarm(0)
    return out
