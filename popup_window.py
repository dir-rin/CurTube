import curses

class PopupWindow(object):
    def __init__(self, pos, label):
        self.size_y = 10
        self.size_x = 40
        self.window = curses.newwin(self.size_y, self.size_x, pos[0], pos[1] - self.size_x // 2)
        self.window.box(0, 0)
        self.window.keypad(1)
        self.window.addstr(0, 1, label)
        self.position = 0

        self.buttons = ()
        self.options = ()

    def add_buttons(self, items):
        self.buttons = items

    def add_options(self, options):
        self.options = options
        self.options.append(("Exit", "Exit"))

    def navigation(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0

        elif self.position >= len(self.options) and self.options != ():
            self.position = len(self.options) - 1
        elif self.position >= len(self.buttons) and self.buttons != ():
            self.position = len(self.buttons) - 1

    def display(self):
        if len(self.buttons) > 1:
            self.window.box(0, 0)
            while True:
                pos = 2
                for index, item in enumerate(self.buttons):
                    if index == self.position:
                        mode = curses.A_REVERSE
                    else:
                        mode = curses.A_NORMAL

                    self.window.addstr(8, pos, item, mode)
                    pos += 10

                key = self.window.getch()

                if key in [curses.KEY_ENTER, ord("\n")]:
                    if self.position == len(self.buttons) - 1:
                        return 0
                    else:
                        self.buttons[self.position][1]()

                elif key == curses.KEY_LEFT:
                    self.navigation(-1)
                elif key == curses.KEY_RIGHT:
                    self.navigation(1)

            self.window.clear()
            curses.doupdate()

        elif len(self.buttons) == 1:
            self.window.box(0, 0)
            mode = curses.A_REVERSE
            self.window.addstr(8, 15, self.buttons[0], mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                return 0

        elif self.options != ():
            while True:
                pos = 4
                for index, item in enumerate(self.options):
                    if index == self.position:
                        mode = curses.A_REVERSE
                    else:
                        mode = curses.A_NORMAL

                    self.window.addstr(pos + index, pos, item[0], mode)

                key = self.window.getch()

                if key in [curses.KEY_ENTER, ord("\n")]:
                    if self.position == len(self.options) - 1:
                        return 0
                    else:
                        self.options[self.position][1]()

                elif key == curses.KEY_UP:
                    self.navigation(-1)
                elif key == curses.KEY_DOWN:
                    self.navigation(1)

            self.window.clear()
            curses.doupdate()

    def addstr(self, pos, string):
        self.window.addstr(pos[0], pos[1], string)
