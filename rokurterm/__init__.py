import sys
from control import RokuConnector
from cli import CLParser
from util import *

getch = Getch()

def main():
    sys.stdout.write('\x1b]2;RokuRTerm\x07')
    sys.stdout.write('Press / to exit, ? for help\n')

    roku = RokuConnector(sys.argv[1])
    sys.stdout.write('Roku IP: %s\n' % roku.ip());

    cli = CLParser(roku)

    while(True):
        c = getch()
        cli.parse_cl(c)
