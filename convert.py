import ffmpeg
import os

def convert_to_mp3(file, res, output):
    stream = ffmpeg.input(output + "/" + file + res)
    stream = ffmpeg.output(stream, output + "/" + file + ".mp3", loglevel="quiet")
    ffmpeg.run(stream)
    os.remove(output + "/" + file + res) 

