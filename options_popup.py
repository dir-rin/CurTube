from popup_window import PopupWindow
from curses.textpad import Textbox
import download
import curses
import set_config

class Config(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Config")
        self.window.add_options([("Show current", self.set_str), ("Edit config", curses.flash)])
        self.window.display()

    def set_str(self):
        configs = set_config.get_config()
        self.window.addstr((0, 0), configs)

class SetUrl(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Set Url")
        self.window.add_buttons(("Enter", "Cancel"))

        self.window.display()
        #self.textbox = Textbox(self.window)

class DownloadW(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Download")
        self.window.addstr((0, 0), download.get_title())

def create_popup(window, pos_y, pos_x, screen):
    if window == "Config":
        newpopup = Config(pos_y, pos_x)
    elif window == "Set Url":
        newpopup = SetUrl(pos_y, pos_x)
    elif window == "Download":
        newpopup = DownloadW(pos_y, pos_x)

    del newpopup
    screen.touchwin()
    screen.refresh()
