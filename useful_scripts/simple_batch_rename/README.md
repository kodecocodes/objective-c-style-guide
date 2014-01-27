# Simple batch file renamer

This script can be useful if your project customer provides you a lot of files with incorrect names.

## Description and example

For example, you have a folder contains Retina graphics for your project.  Each file has name like 'test_image_Retina.png'.
Execute:
```
$ ./simple_batch_rename.py Retina --folder ~/projects/images
```
As result you will get files with removed 'Retina' word from file name in 'renamed_files' subfolder in target directory. '--folder' key is not required. If '--folder' not presented script will run in it's working folder.

## Using

You can use this script in two ways:

* First:
 
You can execute this script by typing in terminal:

```
$ ./python simple_batch_rename.py Word1 Word2 Word3 --folder some_folder
```
* Second:
 
At first, you should set an execute rights for script

```
$ chmod +x simple_batch_rename.py
```
  and after type in console:
  
```
$ ./simple_batch_rename.py Word1 Word2 Word3 --folder some_folder
```

## Installation

Just download the script and execute it in console.
