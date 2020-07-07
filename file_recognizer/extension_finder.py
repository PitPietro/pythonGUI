import os


def find_extension(path):
    file_name, file_ext = os.path.splitext(path)
    return [file_name, file_ext]


if __name__ == '__main__':
    print(find_extension('/home/oasiwild01/Documents/pythonGUI/pySimpleGUI/cookbook/themes.py'))