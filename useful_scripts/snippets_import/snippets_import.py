#!/usr/bin/env python

__author__ = 'ihor.rusin'


from os import listdir, mkdir
from os.path import exists, join, isfile, expanduser
from shutil import copy2
import argparse


class SnippetsImport:
    def __init__(self):
        self.snippets_path = join(expanduser('~'), 'Library/Developer/Xcode/UserData/CodeSnippets')

    def do_import(self, source_folder):
        print 'Importing snippets to Xcode'
        only_files = [f for f in listdir(source_folder) if isfile(join(source_folder, f))]
        snippets = [f for f in only_files if f.endswith('codesnippet')]
        print 'Found %d snippets' % len(snippets)

        if not exists(self.snippets_path):
            try:
                mkdir(self.snippets_path)
            except Exception, msg:
                print 'Failed snippets destination folder creation: %s' % msg
                exit(-1)

        new_files = 0
        updated_files = 0

        for snippet in snippets:
            snippet_path = join(self.snippets_path, snippet)
            if exists(snippet_path):
                updated_files += 1
            else:
                new_files += 1
            try:
                copy2(join(source_folder, snippet), snippet_path)
            except Exception, msg:
                print 'Failed copying %s: %s' % (snippet, msg)

        print '%d snippets installed.' % new_files
        print '%d snippets updated.' % updated_files


def main():
    parser = argparse.ArgumentParser(description='Script imports all snippets from specified folder to Xcode.')
    parser.add_argument('--folder', '-f', type=str, default='.', help='Folder with snippets')
    args = parser.parse_args()
    options = vars(args)
    SnippetsImport().do_import(options['folder'])


if __name__ == '__main__':
    main()