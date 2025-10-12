from popup_window import PopupWindow
import download
import curses
import set_config
import pytubefix
import urllib
import convert

class Config(object):
    def __init__(self, pos_y, pos_x, screen):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.screen = screen

        self.window = PopupWindow((pos_y, pos_x), "Config")
        self.window.add_options([("Show current", self.info_box), ("Edit config", self.edit_win)])
        self.window.display()

        del self.window
        self.screen.touchwin()
        self.screen.refresh()

    def info_box(self):
        info_box = PopupWindow((self.pos_y, self.pos_x), "Info")

        info_box.add_buttons(["Close"])
        info_box.addstr((1, 1), set_config.get_config())
        info_box.addstr((0, 0), "Info")

        info_box.display()

        del info_box
        self.window.touchwin()
        self.window.refresh()
    
    def edit_win(self):
        self.win = PopupWindow((self.pos_y, self.pos_x), "Edit")
        self.win.add_options([("Resolution", self.edit_res), ("Remove incorrect symbols", self.rem_sym), ("Convert to mp3", self.convert), ("Output path", self.path)])
        self.win.display()

        del self.win
        self.window.touchwin()
        self.window.refresh()

    def edit_res(self):
        edit = PopupWindow((self.pos_y, self.pos_x), "Set resolution")
        edit.add_options([(".m4a", set_config.set_res, ".m4a"), (".mp3", set_config.set_res, ".mp3")])
        edit.display()

        del edit
        self.win.touchwin()
        self.win.refresh()

    def rem_sym(self):
        win = PopupWindow((self.pos_y, self.pos_x), "Remove incorrect symbols")
        win.add_buttons([("True", set_config.set_sym, True), ("False", set_config.set_sym, False)])
        win.addstr((2, 4), '''Remove incorrect symbols?
    Example: /#$;:,.'[] etc.''')
        win.display()

        del win
        self.win.touchwin()
        self.win.refresh()

    def convert(self):
        win = PopupWindow((self.pos_y, self.pos_x), "Convert to mp3")
        win.add_buttons([("True", set_config.set_conv, True), ("False", set_config.set_conv, False)])
        win.addstr((2, 4), '''Convert to mp3?
    The default resolution of audio file is .m4a,
    so you might want to convert it to .mp3''')
        win.display()

        del win
        self.win.touchwin()
        self.win.refresh()

    def path(self):
        win = PopupWindow((self.pos_y, self.pos_x), "Output path")
        win.add_buttons([("Enter", set_config.set_path), ("Cancel", "Cancel")])

        win.display_textbox("path")

        del win
        self.win.touchwin()
        self.win.refresh()


class SetUrl(object):
    def __init__(self, pos_y, pos_x):
        self.window = PopupWindow((pos_y, pos_x), "Set Url")
        self.window.add_buttons([("Enter", set_config.set_url), ("Cancel", "Cancel")])

        self.window.display_textbox("url")

class DownloadW(object):
    def __init__(self, pos_y, pos_x):
        self.pos_y = pos_y
        self.pos_x = pos_x

        self.window = PopupWindow((pos_y, pos_x), "Download options")
        self.window.add_options([("Download", self.download_win), ("Convert to mp3", self.convert)])
        self.window.display()

    def download_win(self):
        win = PopupWindow((self.pos_y, self.pos_x), "Download")
        opt = download.get_configs()
        win.addstr((2, 2), "Trying...")
        win.addstr((6, 2), "Ctrl+Z to stop")
        win.refresh()

        try:
            win.addstr((2, 2), download.get_title()[0:50] + "...")
        except pytubefix.exceptions.RegexMatchError:
            win.addstr((2, 2), "No valid url.")
        except urllib.error.URLError:
            win.addstr((2, 2), "You seem to be offline.         ")
        else:
            win.addstr((4, 2), "Downloading video...")
            win.refresh()
            file = download.download(opt[0], opt[1], opt[2], opt[3], opt[4])
            if opt[3] == True:
                win.addstr((4, 2), "Converting video...")
                win.window.refresh()
                convert.convert_to_mp3(file, opt[1], opt[4])

            win.addstr((4, 2), "Download has been finished!")

        win.addstr((6, 2), "- Press any button to exit")
        win.window.getch()

        del win
        self.window.touchwin()
        self.window.refresh()

    def convert(self):
        win = PopupWindow((self.pos_y, self.pos_x), "Convert to mp3")
        win.add_buttons([("True", set_config.set_conv, True), ("False", set_config.set_conv, False)])
        win.addstr((2, 4), '''Convert to mp3?
    The default resolution of audio file is .m4a,
    so you might want to convert it to .mp3''')
        win.display()

        del win
        self.window.touchwin()
        self.window.refresh()


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
