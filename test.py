#!/bin/python3
# Created by Jacobus Burger (2025-06-14)
# Info:
#   Play the game Pong in terminal!
# See:
#   https://en.wikipedia.org/wiki/Pong
from math import floor, ceil
from os import system
from random import choice
from sys import argv
import threading
from time import sleep
import argparse
import curses



# DONE:
# - add const variable for paddle height  (before 2025-06-25, added 2025-06-23)
# - add CLI controls for madness-mode and paddle_height among other things like refresh speed and more.  (before 2025-06-25, added 2025-06-23)
# - interestingly, logic lets paddles move on x too. Add as feature activated with "--madness" flag  (before 2025-06-25, added 2025-06-23) 
# TODO:
# - check it works on other platforms  (before 2025-06-30)
# - use threads to handle ball and paddle movements as independent events? (otherwise keypresses are blocking and ball speed increases with paddle movement) (look at ncurses arcade project)  (before 2025-06-28)
# - create distributions  (before 2025-06-30)
#   - setup project so it's available through PyPI
#   - publish on itch.io
# - finished, move on to make ultrapong with pygame or something...



def pong():
    while True:
        # get input
        key = win.getch()
        # quit on q key
        if key == ord('q'):
            break
        if key == ord('o'):
            win.addch(10, 10, ord("*"))
        if key == ord('p'):
            win.addch(10, 10, ord("@"))



if __name__ == '__main__':
    # initialize ncurses
    stdscr = curses.initscr()
    curses.curs_set(False)
    curses.noecho()
    curses.cbreak()
    curses.start_color()

    # set up colors
    blank_color = 1
    blank_char = " "
    ball_color = 2
    ball_char = "*"
    player_color = 3
    opponent_color = 4
    paddle_char = "I"
    curses.init_pair(blank_color, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(ball_color, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(player_color, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(opponent_color, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # initialize game window
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)
    win.timeout(0)
    win.border()

    # begin threads
    input_thread = threading.Thread(target=win.refresh)
    input_thread.start()

    # play game
    try:
        pong()
    except:
        pass

    # end threads
    input_thread.join()

    # clean up and end
    curses.curs_set(True)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    system("clear")
