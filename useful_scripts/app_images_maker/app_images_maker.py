#!/usr/bin/python

__author__ = 'Ihor Rusin'
__version__ = 'v0.1'

import argparse
from os import listdir
from os import mkdir
from os.path import isfile, join, exists, splitext

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


class ImageProcessor:
    def __init__(self):
        self.double_size_postfix = '@2x'
        self.conflict_folder_name = 'conflict'
        self.result_folder_name = 'result'

        self.total_processed_files = 0
        self.total_failed_files = 0
        self.total_conflict_files = 0

    def create_result_folder(self, path):
        if not exists(join(path, self.result_folder_name)):
            mkdir(join(path, self.result_folder_name))

    def create_conflict_folder(self, path):
        if not exists(join(path, self.conflict_folder_name)):
            mkdir(join(path, self.conflict_folder_name))

    def process_image(self, path, image_name):
        self.total_processed_files += 1
        full_path = join(path, image_name)
        print 'Processing: ' + image_name + ':',

        try:
            prep_image = Image.open(full_path)

            width, height = prep_image.size
            is_squared = (width % 2 == 0) and (height % 2 == 0)

            try:
                if is_squared:
                    standard_image = prep_image.resize((width / 2, height / 2), Image.ANTIALIAS)
                    save_path = join(path, self.result_folder_name)
                    file_name = join(save_path, splitext(image_name)[0])
                    standard_image.save(file_name + '.png', 'PNG')
                    prep_image.save(file_name + self.double_size_postfix + '.png', 'PNG')
                    print 'Done.'
                else:
                    self.create_conflict_folder(path)
                    save_path = join(path, self.conflict_folder_name)
                    file_name = join(save_path, splitext(image_name)[0])
                    # TODO: Just copy source file. Will be released in next version
                    prep_image.save(file_name + self.double_size_postfix + '.png', 'PNG')
                    self.total_conflict_files += 1
                    print 'Conflict.'
            except IOError:
                print "Failed saving."
                exit(-1)

        except IOError:
            self.total_failed_files += 1
            print "Failed opening."

    def process_folder(self, folder):
        self.create_result_folder(folder)

        only_files = [f for f in listdir(folder) if isfile(join(folder, f))]
        only_images = [f for f in only_files if f[-3:].lower() in ['jpg', 'bmp', 'png', 'gif']]
        for file_obj in only_images:
            self.process_image(folder, file_obj)
        print 'Total processed: ' + repr(self.total_processed_files)
        print 'With conflict: ' + repr(self.total_conflict_files)
        print 'Failed: ' + repr(self.total_failed_files)


def main():
    parser = argparse.ArgumentParser(
        description='Script make from Retina images two iOS application ready '
                    'images for standard and Retina displays.\n'
                    'All images with with incorrect size will be placed in \'conflict\' folder for manual preparation.')
    parser.add_argument('source_folder', metavar='F', type=str, nargs='+',
                        help='Folder which contains images for preparation.')

    args = parser.parse_args()
    ImageProcessor().process_folder(args.source_folder[0])


if __name__ == "__main__":
    main()
