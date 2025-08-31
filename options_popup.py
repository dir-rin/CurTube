from popup_window import PopupWindow
from curses.textpad import Textbox
import download
import curses
import set_config

class Config(object):
    def __init__(self, pos_y, pos_x, screen):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.screen = screen

        self.window = PopupWindow((pos_y, pos_x), "Config")
        self.window.add_options([("Show current", self.info_box), ("Edit config", curses.flash)])
        self.window.display()

    def info_box(self):
        info_box = PopupWindow((self.pos_y, self.pos_x), "Info")
        info_box.add_buttons(["Close"])
        info_box.addstr((1, 1), set_config.get_config())
        info_box.display()

        del info_box
        self.screen.touchwin()
        self.screen.refresh()


class SetUrl(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Set Url")
        self.window.add_buttons(("Enter", "Cancel"))

        self.window.display()
        #self.textbox = Textbox(self.window)

class DownloadW(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Download")
        self.window.add_options([("Download", curses.flash), ("Convert to mp3", curses.flash)])
        #self.window.addstr((0, 0), download.get_title())

        self.window.display()

def create_popup(window, pos_y, pos_x, screen):
    if window == "Config":
        newpopup = Config(pos_y, pos_x, screen)
    elif window == "Set Url":
        newpopup = SetUrl(pos_y, pos_x)
    elif window == "Download":
        newpopup = DownloadW(pos_y, pos_x)

    del newpopup
    screen.touchwin()
    screen.refresh()
