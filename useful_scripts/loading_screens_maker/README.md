# iOS Application Loading Screens Maker

This script generates all required loading screens for iPhone and iPad applications from single image with 2048x2048 resolution.

## Description and example

For example, you have an image with required resolution
Execute:
```
$ ./loading_screen_maker.py image.png
```
As result you will get images with standard size which will be placed in 'loading_screens' folder under the same path as original images. 

## Using

You can use this script in two ways:

* First:
 
You can execute this script by typing in terminal:

```
$ ./python loading_screen_maker.py image.png
```
* Second:
 
At first, you should set an execute rights for script

```
$ chmod +x app_images_maker.py
```
  and after type in console:
  
```
$ ./loading_screen_maker.py image.png
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
