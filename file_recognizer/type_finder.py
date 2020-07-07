"""
> Text Extension
https://www.file-extensions.org/filetype/extension/name/text-files
"""


def is_image(ext):
    ext = ext.lower()
    img_ext_list = ['.jpg', '.png', '.gif', '.nef', '.webp', '.tiff', '.psd', '.raw', '.bmp', '.heif', '.indd',
                    '.jpeg 2000']
    if ext in img_ext_list:
        return True
    else:
        return False


def is_text(ext):
    ext = ext.lower()
    text_ext_list = ['.txt', '.java', '.c', '.cpp', '.py', '.sh', '.md', '.html', '.json', '.csv', ]
    if ext in text_ext_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_image('.PNG'))
    print(is_text('.java'))
