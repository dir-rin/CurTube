import curses
import curses.textpad

# Основной экран
def screen():
    global screen
    screen = curses.initscr()
    curses.start_color()

    # Цвета
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    curses.noecho()  # Выкл сообщений в консоль
    curses.cbreak()
    curses.curs_set(0)
    screen.box(0, 0)  # Границы как и screen.border(0)
    screen.addstr(0, 0, "Curtube by DIRrinn ", curses.A_DIM)

    # Размер окна
    lines = curses.LINES  # y
    cols = curses.COLS    # x
    win_size_y = lines // 2
    win_size_x = cols // 2
    screen.refresh() # Обновление экрана

    # Меню (y, x)
    menu = curses.newwin(win_size_y, win_size_x, win_size_y - win_size_y // 2, win_size_x - win_size_x // 2)
    menu.bkgd(' ', curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)

    # Лого
    menu.addstr(1, 0, r'''
    ____ _   _ ____ _____ _   _ ____  _____
   / ___| | | |  _ \_   _| | | | __ )| ____|
  | |   | | | | |_) || | | | | |  _ \|  _|
  | |___| |_| |  _ < | | | |_| | |_) | |___
   \____|\___/|_| \_\|_|  \___/|____/|_____|
''')

    menu.box(0, 0)

    # Текст в меню (кнопки) - Заготовка. Сделать через curses.textpad.Textbox
    buttons = ["Config", "Set url", "Download", "Exit"]
    pos = 10
    for i in buttons:
        menu.addstr(pos, 3, i, curses.A_BOLD)
        pos += 2

    menu.refresh()

    screen.getch()

screen()

# Окончание работы с окном
curses.nocbreak()
curses.echo()
curses.endwin()
