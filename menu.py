#!./venv/bin/python

# pip install console-menu
from consolemenu import ConsoleMenu


import sys,os
import curses
from threading import Thread


def draw_main_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    conn_status = "Not Connected"

    i = 0
    # Loop where k is the last character pressed
    while (k != ord('q')):
        i += 1

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # if k == curses.KEY_DOWN:
        #     cursor_y = cursor_y + 1
        # elif k == curses.KEY_UP:
        #     cursor_y = cursor_y - 1
        # elif k == curses.KEY_RIGHT:
        #     cursor_x = cursor_x + 1
        # elif k == curses.KEY_LEFT:
        #     cursor_x = cursor_x - 1
        #
        # cursor_x = max(0, cursor_x)
        # cursor_x = min(width-1, cursor_x)
        #
        # cursor_y = max(0, cursor_y)
        # cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        # title = "Curses example"[:width-1]
        # subtitle = "Written by Clay McLeod"[:width-1]
        # keystr = "Last key pressed: {}".format(k)[:width-1]
        # statusbarstr = f"Press 'q' to exit | {i} {conn_status}"
        # if k == 0:
        #     keystr = "No key press detected..."[:width-1]

        # Centering calculations
        # start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        # start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        # start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        # start_y = int((height // 2) - 2)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        render_status(conn_status, height, i, stdscr, width)

        # Turning on attributes for title
        # stdscr.attron(curses.color_pair(2))
        # stdscr.attron(curses.A_BOLD)

        # Rendering title
        # stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        # stdscr.attroff(curses.color_pair(2))
        # stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        # stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        # stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        # stdscr.addstr(start_y + 5, start_x_keystr, keystr)
        # stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def render_status(conn_status, height, i, stdscr, width):
    # Render status bar
    statusbarstr = f"Press 'q' to exit | {i} {conn_status}"
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height - 1, 0, statusbarstr)
    stdscr.addstr(height - 1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))


def main():
    curses.wrapper(draw_main_menu)

if __name__ == "__main__":
    main()