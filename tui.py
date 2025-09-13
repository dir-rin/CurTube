import curses
import download
import set_config
import convert
from popup_window import PopupWindow
from options_popup import create_popup

class MenuItem(object):
    def __init__(self, items, screen):
        self.screen = screen
        self.size_x = curses.COLS // 2
        self.size_y = curses.LINES // 2

        self.window = curses.newwin(self.size_y, self.size_x, self.size_y - self.size_y // 2, self.size_x - self.size_x // 2)
        self.window.keypad(1)
        self.window.bkgd(' ', curses.color_pair(1))

        self.window.addstr(1, 0, r'''\
    ____ _   _ ____ _____ _   _ ____  _____
   / ___| | | |  _ \_   _| | | | __ )| ____|
  | |   | | | | |_) || | | | | |  _ \|  _|
  | |___| |_| |  _ < | | | |_| | |_) | |___
   \____|\___/|_| \_\|_|  \___/|____/|_____|

   A small TUI app to download Youtube videos.

   Move with arrows. Enter to choose option.
''')
        self.position = 0
        self.items = items
        self.items.append(("Exit", "Exit"))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):

        while True:
            self.window.refresh()
            curses.doupdate()
            self.window.box(0, 0)


            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = "%d. %s" % (index, item[0])
                self.window.addstr(15 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    return 0
                else:
                    self.items[self.position][1](self.items[self.position][0], self.size_y, self.size_x, self.screen)

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.window.clear()
        curses.doupdate()
        
class App(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        self.screen.box(0, 0)  # Границы как и screen.border(0)
        self.screen.addstr(0, 0, "Curtube by DIRrinn ", curses.A_DIM)
        self.screen.refresh()

        pos_y = curses.LINES
        pos_x = curses.COLS

        # COLORS
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)
        curses.curs_set(0)

        menu_items = [
            ("Config", create_popup),
            ("Set Url", create_popup),
            ("Download", create_popup)
        ]
        self.menu = MenuItem(menu_items, self.screen)
        self.menu.display()


if __name__ == "__main__":
    curses.wrapper(App)

