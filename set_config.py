import json

def configuration():
    if input('''
                1. Show current
                2. Edit
''') == "1":
        with open("config.json", "r") as config:
            variables = json.load(config)
        print(f'''
            Current config:
url: {variables["url"]}
resolution: {variables["resolution"]}
incorrect symbols remove: {variables["incorrect_symbols_remove"]}
convert to mp3: {variables["convert_to_mp3"]}
output_path: {variables["output_path"]}
                ''')
        input("Press enter to exit")
        return 0

    with open("config.json", "r") as config:
        variables = json.load(config)

    options = {1: ".mp4", 2: ".m4a"}
    user_choice = int(input("\nOptions:\n1: Video (mp4)\n2: Only Audio (m4a)\n"))
    variables["resolution"] = options[user_choice]

    user_choice = input("Remove incorrect symbols? (y/n)\n")
    if user_choice == "y":
        variables["incorrect_symbols_remove"] = True
    elif user_choice == "n":
        variables["incorrect_symbols_remove"] = False
    else:
        print("Try again (Set by default")

    print(f"Current output path: {variables["output_path"]}")
    new_path = input("New output path (leave empty to not change):\n")

    if new_path != "":
        variables["output_path"] = new_path

    print(f'''
            Current config:
            url: {variables["url"]}
            resolution: {variables["resolution"]}
            incorrect symbols remove: {variables["incorrect_symbols_remove"]}
            convert_to_mp3: {variables["convert_to_mp3"]}
            output_path: {variables["output_path"]}\n
            ''')
    with open("config.json", "w") as config:
        json.dump(variables, config)

def set_url():
    with open("config.json", "r") as config:
        variables = json.load(config)

    variables["url"] = input("Enter URL\n")
    print(f"Current url: {variables["url"]}\n")

    with open("config.json", "w") as config:
        json.dump(variables, config)

