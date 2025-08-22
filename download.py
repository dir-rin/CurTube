# download.py
from pytubefix import YouTube
from pytubefix.cli import on_progress
import json
import convert

def download():
    with open("config.json", "r") as config:
        variables = json.load(config)

    url = variables["url"]
    res = variables["resolution"]
    symbols_remove = variables["incorrect_symbols_remove"]
    output = variables["output_path"]

    if input("Start downloading? (y/n)\n") == "n":
        print("Stopped")
        return 0

    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)

    #incorrect symbols might break the save process, so they need to be deleted from file's name
    if symbols_remove == True:
        eng = "abcdefghijklmnopqrstuvwxyzZYXWVUTSRQPONMLKJIHGFEDCBA"
        ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        space = " "
        numbers = "1234567890"
        correct_symbols = eng + ru + numbers + space

        title = yt.title
        file = ""


        for c in title:
            if c in correct_symbols:
                file += c
    else:
        file = yt.title

    print(f"The title is: {file}\n")

    if res == ".m4a":
        ys = yt.streams.get_audio_only()
    elif res == ".mp4":
        #360p support only
        ys = yt.streams.get_highest_resolution()
    #elif user_choice == ".mp4_720":
        #dosomething

    ys.download(output_path=output, filename=file + res)
    print('Download finished successfully.')
    convert.convert_to_mp3(file, res, output)

