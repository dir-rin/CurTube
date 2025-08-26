import curses

class PopupWindow(object):
    def __init__(self, pos, items):
        self.window = curses.newwin(10, 20, pos[0], pos[1])
        self.window.box(0, 0)
        self.window.addstr(0, 1, items)

        self.buttons = ("Enter", "Cancel")
        self.position = 0

    def navigation(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.buttons):
            self.position = len(self.buttons) - 1

    def display(self):
        pos = 2
        for index, item in enumerate(self.buttons):
            if index == self.position:
                mode = curses.A_REVERSE
            else:
                mode = curses.A_NORMAL

            self.window.addstr(8, pos, item, mode)
            pos += 10
            self.window.refresh()

    def addstr(self, pos, string):
        self.window.addstr(pos[0], pos[1], string)

    def do_smth(self):
        if self.position == 0:
            self.window.addstr(5, 5, "HELL HEAH")
        else:
            return
