def is_image(ext):
    ext = ext.lower()
    img_ext_list = ['.jpg', '.png', '.gif', '.webp', '.tiff', '.psd', '.raw', '.bmp', '.heif', '.indd', '.jpeg 2000']
    if ext in img_ext_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_image('.PNG'))
