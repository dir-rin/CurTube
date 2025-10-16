# download.py
from pytubefix import YouTube
import json
import convert
import os

def get_configs():
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
            variables = json.load(config)

    url = variables["url"]
    res = variables["resolution"]
    symbols_remove = variables["incorrect_symbols_remove"]
    convert = variables["convert_to_mp3"]
    output = variables["output_path"]

    return url, res, symbols_remove, convert, output


def download(url, res, symbols_remove, convert, output):

    yt = YouTube(url, use_oauth=False, allow_oauth_cache=True)

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

    if res == ".m4a":
        ys = yt.streams.get_audio_only()
    elif res == ".mp4":
        #360p support only
        ys = yt.streams.get_highest_resolution()
    #elif user_choice == ".mp4_720":
        #dosomething

    ys.download(output_path=output, filename=file + res)
    return file

def get_title():
    url = get_configs()
    yt = YouTube(url[0])
    return yt.title

