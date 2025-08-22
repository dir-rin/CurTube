import ffmpeg
import os

def convert_to_mp3(file, res, output):
    user_choice = input("Convert to mp3? Y/n\n")

    if(user_choice == "n"):
        return 0
    else:
        stream = ffmpeg.input(output + "/" + file + res)
        stream = ffmpeg.output(stream, output + "/" + file + ".mp3")
        ffmpeg.run(stream)
        os.remove(output + "/" + file + res) 
        print("Finished")

