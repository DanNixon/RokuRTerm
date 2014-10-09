import sys
from util import switch


class CLParser(object):
    """
    Processes characters read from command line.
    """

    def __init__(self, roku):
        self._roku = roku
        self._keymode = False


    def print_help(self):
        """
        Prints key mappings.
        """

        print 'Keys:'
        print '? - Help'
        print '/ - Exit'
        print 'w - Up'
        print 'a - Left'
        print 's - Down'
        print 'd - Right'
        print 'z - Select'
        print 'b - Back'
        print 'q - Quit'
        print 'p - Play/Pause'
        print '< or , - Reverse'
        print '> or . - Forward'
        print 'i - Info (* on Roku Remote)'
        print 'r - Instant Replay'
        print 'k - keyboard mode'


    def parse_cl(self, cl_input):
        """
        Parses a given character.

        @param cl_input Input from command line
        """

        function = cl_input.upper()
        if self._keymode:
            if (cl_input <= 'z' and cl_input >= 'a') or (cl_input <= '9' and cl_input >= '0'):
                cmd = "Lit_" + cl_input
                self._roku.send_key_cmd(cmd)
            if cl_input == ' ':
                self._roku.send_key_cmd('Lit_%20')
            if cl_input == '\x08':
                self._roku.send_key_cmd('InstantReplay')
            if cl_input == '\x1b':
                self._keymode = False
                print 'Exit keyboard mode'
        else:
            for case in switch(function):
                if case('/'):
                    sys.exit(0);
                    break
                if case('Q'):
                    sys.exit(0);
                    break
                if case('P'):
                    self._roku.send_key_cmd('Play')
                    break
                if case('W'):
                    self._roku.send_key_cmd('Up')
                    break
                if case('A'):
                    self._roku.send_key_cmd('Left')
                    break
                if case('S'):
                    self._roku.send_key_cmd('Down')
                    break
                if case('D'):
                    self._roku.send_key_cmd('Right')
                    break
                if case('<'):
                    self._roku.send_key_cmd('Rev')
                    break
                if case(','):
                    self._roku.send_key_cmd('Rev')
                    break
                if case('>'):
                    self._roku.send_key_cmd('Fwd')
                    break
                if case('.'):
                    self._roku.send_key_cmd('Rev')
                    break
                if case('H'):
                    self._roku.send_key_cmd('Home')
                    break
                if case('Z'):
                    self._roku.send_key_cmd('Select')
                    break
                if case('B'):
                    self._roku.send_key_cmd('Back')
                    break
                if case('R'):
                    self._roku.send_key_cmd('InstantReplay')
                    break
                if case('I'):
                    self._roku.send_key_cmd('Info')
                    break
                if case('K'):
                    self._keymode = True
                    print 'Entering keyboard mode, <ESC> to exit'
                    break
                if case('?'):
                    self.print_help()
                    break
