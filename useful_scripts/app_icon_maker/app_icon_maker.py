#!/usr/bin/python

__author__ = 'Ihor Rusin'
__version__ = 'v0.4'

import argparse
from os import mkdir
from os.path import join, exists, dirname


try:
    from PIL import Image
except ImportError:
    Image = None
    print('*****\n'
          'Error loading Pillow library.\n'
          'Before using this script you should install Pillow library.\n'
          'To do this you should open terminal and execute:\n'
          '     sudo easy_install Pillow\n'
          'or\n'
          '     sudo easy_install pip\n'
          '     sudo pip install Pillow\n'
          'and after try to run this script again.\n'
          '*****')
    exit(-1)


class IconProcessor:
    def __init__(self):
        self.ios = {'iTunesArtwork': 512,
                    'Icon-29': 29,
                    'Icon-40': 40,
                    'Icon-50': 50,
                    'Icon-60': 60,
                    'Icon-72': 72,
                    'Icon-76': 76,
                    'Icon': 57}
        self.double_size_postfix = '@2x'
        self.result_folder_name = 'icons'

    def process_image(self, icon_name):
        save_path = join(dirname(icon_name), self.result_folder_name)

        if not exists(save_path):
            mkdir(save_path)

        try:
            prep_icon = Image.open(icon_name)

            width, height = prep_icon.size
            print 'Processing image: ' + icon_name + '. Image size: ' + repr(width) + 'x' + repr(height) + ':',

            for key, value in self.ios.iteritems():
                standard_image = prep_icon.resize((value, value), Image.ANTIALIAS)
                retina_image = prep_icon.resize((value*2, value*2), Image.ANTIALIAS)

                try:
                    file_name = join(save_path, key)
                    standard_image.save(file_name + '.png', 'PNG')
                    retina_image.save(file_name + self.double_size_postfix + '.png', 'PNG')
                except IOError:
                    print "Error processing image."
                    exit(-1)

            print 'Done.'
        except IOError:
            print "Unable to load image."


def main():
    parser = argparse.ArgumentParser(description='Script for preparing icons for iOS application.')
    parser.add_argument('filename', metavar='F', type=str, nargs='+',
                        help='Icon file which will be used for other icons preparation.')

    args = parser.parse_args()
    IconProcessor().process_image(args.filename[0])


if __name__ == "__main__":
    main()
