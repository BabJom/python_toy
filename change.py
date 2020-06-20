import os
from moviepy.editor import *


def change_file(paths, object):
    """change mp4 to mp3 """
    """  
     for x in os.listdir(dirs): print(x) 
    """
    check_path = paths + "\changer"

    for x in object:
        pass_data = False
        name = x.split('.')[0]
        for y in os.listdir(check_path):
            if name in y:
                pass_data = True

        if pass_data:
            pass
        else:
            vid = VideoFileClip(os.path.join(paths, "", x))

            vid.audio.write_audiofile(os.path.join(
                paths, "changer", name+".mp3")
            )
    show_result(check_path)


def show_dir():
    """ show dir """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_lists = []

    for x in os.listdir(dir_path):
        if ".py" in x:
            pass
        elif "." not in x:
            pass
        else:
            file_lists.append(x)
    change_file(dir_path, file_lists)


def show_result(paths):
    for x in os.listdir(paths):
        print(x)


def main():
    show_dir()

if __name__ == "__main__":
    main()
