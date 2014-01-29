#!/usr/bin/python

__author__ = 'Viktor Malieichyk'
__version__ = 'v0.1'

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


class LaunchImageProcessor:
    def __init__(self):
        #third value shows if image without status bar required
        self.ios = {'iPad-Portrait': [768, 1024, True],
                    'iPad-Landscape': [1024, 768, True],
                    'iPhone-Portrait': [320, 480, False],
                    'iPhone-Portrait-568h': [320, 568, False]}
        self.double_size_postfix = '@2x'
        self.result_folder_name = 'splashscreens'

    def process_image(self, icon_name):

        save_path = join(dirname(icon_name), self.result_folder_name)
        if not exists(save_path):
            mkdir(save_path)

        try:
            source_image = Image.open(icon_name)
            rt_image = 0
            sd_image = 0
            width, height = source_image.size
            if width != 2048 or height != 2048:
                if width == 1024 or height == 1024:
                    rt_image = source_image.resize((2048, 2048), Image.ANTIALIAS)
                    sd_image = source_image
                print('Wrong image size. Should be 2048x2048')
                exit(-1)
            else:
                rt_image = source_image
                sd_image = source_image.resize((1024, 1024), Image.ANTIALIAS)

            print 'Processing image: ' + icon_name + '. Image size: ' + repr(width) + 'x' + repr(height) + ':',

            for key, value in self.ios.iteritems():
                size = max(value)
                offset_x = (size - value[0]) / 2
                offset_y = (size - value[1]) / 2


                if value[0] < 1024 and value[1] < 1024:
                    sd_splash = sd_image.resize((size, size), Image.ANTIALIAS).crop((offset_x, offset_y, size - offset_x, size - offset_y))
                    rt_splash = rt_image.resize((size * 2, size * 2), Image.ANTIALIAS).crop((offset_x * 2, offset_y * 2, size * 2 - offset_x * 2, size * 2 - offset_y * 2))
                else:
                    sd_splash = sd_image.crop((offset_x, offset_y, size - offset_x, size - offset_y))
                    rt_splash = rt_image.crop((offset_x * 2, offset_y * 2, size * 2 - offset_x * 2, size * 2 - offset_y * 2))



                try:
                    file_name = join(save_path, key)
                    sd_splash.save(file_name + '.png', 'PNG')
                    rt_splash.save(file_name + self.double_size_postfix + '.png', 'PNG')

                    if value[2]:
                        sd_splash_no_status = sd_splash.crop((0, 20, value[0], value[1]))
                        rt_splash_no_status = rt_splash.crop((0, 20 * 2, value[0] * 2, value[1] * 2))
                        sd_splash_no_status.save(file_name + '_NoStatusBar.png', 'PNG')
                        rt_splash_no_status.save(file_name + '_NoStatusBar' + self.double_size_postfix + '.png', 'PNG')
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
    LaunchImageProcessor().process_image(args.filename[0])


if __name__ == "__main__":
    main()
