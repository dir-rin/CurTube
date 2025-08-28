from popup_window import PopupWindow
from curses.textpad import Textbox
import download
import curses

class Config(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Config")
        self.window.add_options([("Show current", "Just show it"), ("Edit config", "Edit")])
        self.window.display()

class SetUrl(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Set Url")
        self.window.add_buttons(("Enter", "Cancel"))
        #self.textbox = Textbox(self.window)

    def dosmth(self):
        print("Hello")

class DownloadW(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Download")
        self.window.addstr((0, 0), download.get_title())

    def dosmth(self):
        print("Hello")

def create_popup(window, pos_y, pos_x):
    if window == "Config":
        newpopup = Config(pos_y, pos_x)
    elif window == "Set Url":
        newpopup = SetUrl(pos_y, pos_x)
    elif window == "Download":
        newpopup = DownloadW(pos_y, pos_x)

    del newpopup
