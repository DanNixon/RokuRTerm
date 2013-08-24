#!/usr/bin/env python
#-*- coding: utf-8 -*-

## RokuRTerm v0.1
## dan-nixon.com
## 24/08/2013
## Allows control of a Roku player over the external control API

import httplib

##Set this to your Roku player IP
roku_ip = "192.168.1.120"

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

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
	conn = httplib.HTTPConnection(roku_ip + ":8060")
	conn.request("POST", "/keypress/" + cmd_string)

def print_help():
	print "RokuRTerm v0.1"
	print "Commands:"
        print "? - Help"
        print "/ - Exit Remote App"
	print "w - Up"
	print "a - Left"
        print "s - Down"
        print "d - Right"
        print "z - Select"
        print "q - Back"
        print "p - Play/Pause"
        print "< or , - Reverse"
        print "> or . - Forward"
        print "I - Info (* on Roku Remote)"
        print "R - Instant Replay"

run = 1

def parse_cl(cl_input):
	global run
	function = cl_input.upper()
	for case in switch(function):
		if case('/'):
			run = 0
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
                if case('Q'):
                        send_key_cmd("Back")
                        break
                if case('R'):
                        send_key_cmd("InstantReplay")
                        break
                if case('I'):
                        send_key_cmd("Info")
                        break
		if case('?'):
			print_help()
			break
def main():
	print "Press / to exit, ? for help"
	print "Roku IP: " + roku_ip
	while(run):
		c = getch()
		parse_cl(c)

main()
