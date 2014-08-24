#!/usr/bin/env python
#-*- coding: utf-8 -*-

# RokuRTerm v0.2
# dan-nixon.com
# 24/08/2013
# Allows control of a Roku player over the external control API

import httplib, sys, socket

## Set this to your Roku player IP
roku_ip = "192.168.1.120"

class Getch:
    def __init__(self):
        try:
            self.impl = GetchWindows()
        except ImportError:
            self.impl = GetchUnix()

    def __call__(self): return self.impl()

class GetchUnix:
    def __init__(self):
        import tty

    def __call__(self):
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = Getch()

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

def send_key_cmd(cmd_string):
    try:
        conn = httplib.HTTPConnection(roku_ip + ":8060")
        conn.request("POST", "/keypress/" + cmd_string)
        conn.close()
    except socket.error:
        print "Network error!"

def print_help():
    print "RokuRTerm"
    print "Keys:"
    print "? - Help"
    print "/ - Exit Remote App"
    print "w - Up"
    print "a - Left"
    print "s - Down"
    print "d - Right"
    print "z - Select"
    print "b - Back"
    print "q - Quit"
    print "p - Play/Pause"
    print "< or , - Reverse"
    print "> or . - Forward"
    print "i - Info (* on Roku Remote)"
    print "r - Instant Replay"
    print "k - keyboard mode"

run = 1
keymode = False

def parse_cl(cl_input):
    global keymode
    function = cl_input.upper()
    if keymode:
        if ( (cl_input <= 'z' and cl_input >= 'a') or
             (cl_input <= '9' and cl_input >= '0') ):
                cmd = "Lit_" + cl_input
                send_key_cmd(cmd)
        if cl_input == ' ':
                send_key_cmd("Lit_%20")
        if cl_input == "\x08":
                send_key_cmd("InstantReplay")
        if cl_input == "\x1b":
                keymode = False
                print "Exit keyboard mode"
    else:
        for case in switch(function):
            if case('/'):
                sys.exit(0);
                break
            if case('Q'):
                sys.exit(0);
                break
            if case('P'):
                send_key_cmd("Play")
                break
            if case('W'):
                send_key_cmd("Up")
                break
            if case('A'):
                send_key_cmd("Left")
                break
            if case('S'):
                send_key_cmd("Down")
                break
            if case('D'):
                send_key_cmd("Right")
                break
            if case('<'):
                send_key_cmd("Rev")
                break
            if case(','):
                send_key_cmd("Rev")
                break
            if case('>'):
                send_key_cmd("Fwd")
                break
            if case('.'):
                send_key_cmd("Rev")
                break
            if case('H'):
                send_key_cmd("Home")
                break
            if case('Z'):
                send_key_cmd("Select")
                break
            if case('B'):
                send_key_cmd("Back")
                break
            if case('R'):
                send_key_cmd("InstantReplay")
                break
            if case('I'):
                send_key_cmd("Info")
                break
            if case('K'):
                keymode = True
                print "Entering keyboard mode, <ESC> to exit"
                break
            if case('?'):
                print_help()
                break

def main():
    sys.stdout.write("\x1b]2;RokuRTerm\x07")
    print "Press / to exit, ? for help"
    print "Roku IP: " + roku_ip
    while(1):
        c = getch()
        parse_cl(c)

if __name__ == "__main__":
    main()
