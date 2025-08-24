import curses

# Основной экран
def screen():
    screen = curses.initscr()
    curses.start_color()

    # Цвета
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)

    curses.noecho()  # Выкл сообщений в консоль
    curses.cbreak()
    curses.curs_set(0)
    screen.box(0, 0)  # Границы как и screen.border(0)
    screen.addstr(0, 0, "Youtube Downloader by DIRrinn", curses.A_DIM)

    # Размер окна
    lines = curses.LINES  # y
    cols = curses.COLS    # x
    win_size_y = lines // 2
    win_size_x = cols // 2
    screen.refresh() # Обновление экрана

    # Меню (y, x)
    menu = curses.newwin(win_size_y, win_size_x, win_size_y - win_size_y // 2, win_size_x - win_size_x // 2)
    menu.box(0, 0)
    menu.bkgd(' ', curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
    menu.refresh()

    user_input = ""
    while user_input != "A" and user_input != "KEY_UP":
        user_input = screen.getkey()  # Ожидания ввода символа
        menu.addstr(0, 0, f"The key is {user_input}")
        menu.refresh()
    screen.getch()

screen()

# Окончание работы с окном
curses.nocbreak()
curses.echo()
curses.endwin()

