import os
import platform

import subprocess

import cats_service


def download_cats(folder):
    print('Contacting server to download casts')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cats {}'.format(name))
        cats_service.get_cat(folder, name)
    print('done')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)
    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def display_cats(folder):
    # open folder after detecting OS
    if platform.system() == 'Darwin':
        subprocess.call(['open',folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer',folder])
    if platform.system() == 'Linux':
        subprocess.call(['xdg-open',folder])


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder {}'.format(folder))

    download_cats(folder)
    display_cats(folder)    # display cats


def print_header():
    print('--------------------------------')
    print('       CAT Factory')
    print('--------------------------------')
    print('')


if __name__ == '__main__':
    main()
