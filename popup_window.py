import curses

class PopupWindow(object):
    def __init__(self, pos, label):
        self.window = curses.newwin(10, 20, pos[0], pos[1])
        self.window.box(0, 0)
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
        elif self.position >= len(self.buttons):
            self.position = len(self.buttons) - 1

    def display(self):
        if self.buttons != None:
            pos = 2
            for index, item in enumerate(self.buttons):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                self.window.addstr(8, pos, index + 1 + ". " + item[0], mode)
                pos += 10

            self.window.refresh()

        if self.options != None:
            pos = 3
            for index, item in enumerate(self.options):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                self.window.addstr(pos + index, pos, item[0], mode)

            self.window.refresh()

    def addstr(self, pos, string):
        self.window.addstr(pos[0], pos[1], string)
