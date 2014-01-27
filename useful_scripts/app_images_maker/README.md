# iOS Application Images Maker

This script can be useful if your project customer gives you only Retina images with incorrect filenames. Script generates standard images from you images set and automatically appends '@2x' file postfix to original images.

## Description and example

For example, let you have a folder contains Retina graphics for your project. 
Execute:
```
$ ./app_images_maker.py ~/projects/images
```
As result you will get images with standard size which place in 'result' folder with the same path as original images. Also all original images will be duplicated to the same 'result' folder with appended '@2x' postfix. If script will try to process an image with odd width or height then image will be placed in 'conflict' folder and also script will be append '@2x' postfix to file name.

## Using

You can use this script in two ways:

* First:
 
You can execute this script by typing in terminal:

```
$ ./python app_images_maker.py some_folder
```
* Second:
 
At first, you should set an execute rights for script

```
$ chmod +x app_images_maker.py
```
  and after type in console:
  
```
$ ./app_images_maker.py some_folder
```

## Installation

This script uses Pillow for image processing. So, before starting using script you should install Pillow library to your system. As example, on MacOS you should execute in console:
```
$ sudo pip install Pillow
```

If you don't have installed pip, you should install pip first:
```
$ sudo easy_install pip
```
