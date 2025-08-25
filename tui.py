import curses
from curses import panel
import download
import set_config
import convert

class MenuItem(object):
    def __init__(self, items, stdscreen):
        self.size_x = curses.COLS // 2
        self.size_y = curses.LINES // 2

        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.start_color()

        self.logo = stdscreen.subwin(self.size_y, self.size_x, self.size_y - self.size_y // 2, self.size_x - self.size_x // 2)
        self.logo.keypad(1)
        self.logo.bkgdset(' ', curses.color_pair(1) | curses.A_REVERSE)

        self.logo.addstr(1, 0, r'''
    ____ _   _ ____ _____ _   _ ____  _____
   / ___| | | |  _ \_   _| | | | __ )| ____|
  | |   | | | | |_) || | | | | |  _ \|  _|
  | |___| |_| |  _ < | | | |_| | |_) | |___
   \____|\___/|_| \_\|_|  \___/|____/|_____|
''')
        self.logo.box(0, 0)

        self.window = stdscreen.subwin(self.size_y // 2, self.size_x, self.size_y, self.size_x - self.size_x // 2)
        self.window.keypad(1)
        self.window.bkgdset(' ', curses.color_pair(1))

        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

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
        self.panel.top()
        self.panel.show()

        while True:
            self.window.refresh()
            curses.doupdate()

            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = "%d. %s" % (index, item[0])
                self.window.addstr(1 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    return 0
                else:
                    self.items[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class App(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        self.screen.box(0, 0)  # Границы как и screen.border(0)
        self.screen.addstr(0, 0, "Curtube by DIRrinn ", curses.A_DIM)

        curses.curs_set(0)

        menu_items = [
            ("Config", set_config.configuration),
            ("Set Url", set_config.set_url),
            ("Download", download.download)
        ]
        menu = MenuItem(menu_items, self.screen)
        menu.display()


if __name__ == "__main__":
    curses.wrapper(App)
