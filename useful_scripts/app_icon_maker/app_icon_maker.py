#!/usr/bin/python

__author__ = 'Ihor Rusin'
__version__ = 'v0.2'

import argparse

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

ios = {'iTunesArtwork': 512,
       'Icon-29': 29,
       'Icon-40': 40,
       'Icon-60': 60,
       'Icon-76': 76}
double_size_postfix = '@2x'


def process_image(icon_name):
    try:
        prep_icon = Image.open(icon_name)

        width, height = prep_icon.size
        print 'Processing image: ' + icon_name + '. Image size: ' + repr(width) + 'x' + repr(height)

        for key, value in ios.iteritems():
            standard_image = prep_icon.resize((value, value), Image.ANTIALIAS)
            retina_image = prep_icon.resize((value*2, value*2), Image.ANTIALIAS)

            try:
                standard_image.save(key + '.png', 'PNG')
                retina_image.save(key + double_size_postfix + '.png', 'PNG')
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
    process_image(args.filename[0])
    return


if __name__ == "__main__":
    main()
