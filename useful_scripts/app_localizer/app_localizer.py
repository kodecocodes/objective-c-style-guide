#!/usr/bin/env python

# It is a combination of two scripts for working with Xcode localization files
# Authors of original script version: Viktor Maleichik and Ihor Rusin

__author__ = 'ihor.rusin'

import argparse
import csv
from os import mkdir
from os.path import join, exists


class LocalizationSplit:
    def __init__(self, options, files):
        self.localization_file = options['locfile']
        self.delimiter = options['delimiter']
        self.quotechar = options['quotechar']
        self.result_folder = options['folder']
        self.result_dictionary = {}

        if not exists(self.result_folder):
            mkdir(self.result_folder)

        fi = open(self.localization_file, "rb")
        reader = csv.reader(fi, dialect='excel', delimiter=self.delimiter, quotechar=self.quotechar)

        for row in reader:
            key = row[0]
            values = row[1:]
            self.result_dictionary[key] = values

        test_key, test_value = self.result_dictionary.popitem()
        column_count = len(test_value)
        print 'Found %d localizations' % column_count

        if column_count > len(files):
            print 'Number of localizations in \'' + self.localization_file + \
                  '\' is more than that in config file. Please check and fix it.'
            exit(-1)
        elif column_count < len(files):
            print 'Number of localization files in config file is more than that in \'' + \
                  self.localization_file + '\'. Please check and fix it.'
            exit(-1)

        for x in range(0, column_count):
            dict_to_write = self.dictionary_for_column(x)
            self.write_dictionary_to_file(dict_to_write, files[x])

    def dictionary_for_column(self, column_number):
        result = {}
        for key, value in self.result_dictionary.iteritems():
            result[key] = value[column_number]
        return result

    def write_dictionary_to_file(self, input_dictionary, file_name):
        print 'Writing %s' % file_name
        try:
            fo = open(join(self.result_folder, file_name), "wb")
            for key in sorted(input_dictionary.keys(), key=lambda x: x.lower()):
                value = input_dictionary[key]
                fo.write('"%s" = "%s";\n' % (key, value))
            fo.close()
        except IOError, msg:
            print 'Error: %s' % msg
            exit(-1)


class LocalizationMerge:
    def __init__(self, options, files):
        self.iter_count = 0
        self.merge_folder = options['folder']
        self.output_filename = options['output']
        self.unique_keys = {}

        only_files = files

        self.global_dict = {}
        for filename in only_files:
            filename = join(self.merge_folder, filename)
            file_dict = self.dictionary_for_file(filename)
            self.global_dict = self.merge_dict(self.global_dict, file_dict, filename)
            # DEBUG
            #for key in sorted(self.global_dict.keys(), key=lambda x: x.lower()):
            #    print key, self.global_dict[key]
            print '------------------------------------'

        fo = open(self.output_filename, 'wb')
        csv_writer = csv.writer(fo, dialect='excel', delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key in sorted(self.global_dict.keys(), key=lambda x: x.lower()):
            value = self.global_dict[key]
            #print key, value
            csv_writer.writerow([key] + value)
        fo.close()

        unique_keys = {key: value for key, value in self.unique_keys.iteritems() if len(value) <= self.iter_count}
        unique_keys_count = len(unique_keys.keys())
        if unique_keys_count > 0:
            print 'Found %d unique keys which presented not in all files:' % unique_keys_count
            for key, value in unique_keys.iteritems():
                print key + ' presented only in: ' + repr(value)
        print 'All strings were saved to ' + self.output_filename

    @staticmethod
    def dictionary_for_file(filename):
        print 'Loading ' + filename
        dictionary = {}
        with open(filename) as f:
            lines = f.read().splitlines(False)
        lines = (line for line in lines if line)
        line_count = 0
        for line in lines:
            splits = line.split("=", 1)
            for idx, split in enumerate(splits):
                split = split.strip(' \t;"')
                splits[idx] = split
            key = splits[0]
            value = splits[1]
            dictionary[key] = [value]
            line_count += 1
        print repr(line_count) + ' lines were processed.'
        return dictionary

    def merge_dict(self, dict1, dict2, filename):
        if len(dict1) == 0:
            for key in dict2.keys():
                self.unique_keys[key] = [filename]
            return dict2
        print 'Merging with previous loaded strings...'
        dict_result = dict1
        key_count = 0

        self.iter_count += 1

        for key, value in dict1.iteritems():
            if key in dict2:
                pass
            else:
                dict_result[key] += [' ']

        for key, value in dict2.iteritems():
            if key in dict_result:
                dict_result[key] += value
                self.unique_keys[key] += [filename]
            else:
                print 'Unique key: ' + key + ' added.'
                self.unique_keys[key] = [filename]
                dict_result[key] = [' '] * self.iter_count + value
            key_count += 1

        print repr(key_count) + ' keys were attached.'
        return dict_result


localization_config = 'localizations'


def print_localization_error():
    print 'You should create \'' + localization_config + '\' file and write',
    print 'down path of each localization(.strings) file of your project per line.'


def main():
    files = []
    try:
        with open(localization_config) as f:
            files = f.read().splitlines(False)
        files = [x for x in files if x]
        if len(files) == 0:
            print localization_config + ' file is empty'
            print_localization_error()
    except IOError, msg:
        print 'Error: %s' % msg
        print_localization_error()
        exit(-1)

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands', dest='mode')
    # A merge of command
    merge_parser = subparsers.add_parser('merge', help='merge localization files to .CSV')
    merge_parser.add_argument('--folder', '-p', type=str, default='.', help='project directory')
    merge_parser.add_argument('--output', '-o', type=str, default='localizations.csv', help='output filename')
    # A split command
    split_parser = subparsers.add_parser('split', help='split localization .CSV file')
    split_parser.add_argument('--locfile', '-l', type=str, default='localizations.csv',
                              help='.CSV contains localization')
    split_parser.add_argument('--delimiter', '-d', type=str, default=';', help='values delimiter')
    split_parser.add_argument('--quotechar', '-q', type=str, default='"', help='quote char')
    split_parser.add_argument('--folder', '-f', type=str, default='.', help='output folder')

    args = parser.parse_args()
    options = vars(args)
    if args.mode == 'merge':        
        LocalizationMerge(options, files)
    else:
        LocalizationSplit(options, files)


if __name__ == '__main__':
    main()