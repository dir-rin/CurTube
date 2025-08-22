import set_config
import convert
import download

# MENU
def menu():
    while True:
        print('''
                1. Config
                2. Set url
                3. Download
                4. Exit
            ''')

        choice = int(input())
        if choice == 1:
            set_config.configuration()
        elif choice == 2:
            set_config.set_url()
        elif choice == 3:
            download.download()
        elif choice == 4:
            return 0
        else:
            print("Uncorrect")

menu()
