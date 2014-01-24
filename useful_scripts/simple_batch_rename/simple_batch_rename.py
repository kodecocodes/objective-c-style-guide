#!/usr/bin/python

__author__ = 'Ihor Rusin'
__version__ = 'v0.1'


import argparse
from shutil import copyfile
from os import listdir
from os import mkdir
from os.path import isfile, join, exists, dirname


class FileProcessor:
    def __init__(self):
        self.processed_files = 0
        self.renamed_files = 0
        self.result_folder_name = 'renamed_files'

    @staticmethod
    def remove_words(file_name, words):
        for word in words:
            file_name = file_name.replace(word, '')
        return file_name

    def batch_rename(self, folder, words):
        path = join(dirname(folder), self.result_folder_name)
        if not exists(path):
            mkdir(path)
        only_files = [f for f in listdir(folder) if isfile(join(folder, f))]
        files_contains_words = [f for f in only_files if any(x in f for x in words)]
        for file_name in files_contains_words:
            copyfile(file_name, join(path, self.remove_words(file_name, words)))

        print files_contains_words


def main():
    parser = argparse.ArgumentParser(description='Script just remove some words in targeted path\n')
    parser.add_argument('--folder', '-f', type=str, default='.', help='Processing folder')
    parser.add_argument('words', metavar='WORDS', type=str, nargs='+', help='Removing words')

    args = parser.parse_args()
    options = vars(args)
    FileProcessor().batch_rename(options['folder'], options['words'])


if __name__ == "__main__":
    main()
