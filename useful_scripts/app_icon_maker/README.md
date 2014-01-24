# iOS Application Icons Maker

This script produces all icon sizes needed for iOS project from single image.

## Description and example

For example, let you have 1024x1024 application icon then you can make with this script all needed icons for iOS project.
Example:
```
$ ./app_icon_maker.py ExampleIcon.png
```
As result you will get next icons which will be placed in 'icons' folder with the same path as original icon:
```
iTunesArtwork.png
iTunesArtwork@2x.png
Icon-29.png
Icon-29@2x.png
Icon-40.png
Icon-40@2x.png
Icon-50.png
Icon-50@2x.png
Icon-60.png
Icon-60@2x.png
Icon-72.png
Icon-72@2x.png
Icon.png
Icon@2x.png
```

## Using

You can run this script in two ways:

* First way
 
You can execute this script typed in console:

```
$ ./python app_icon_maker.py ExampleIcon.png
```
* Second way
 
At first, you should set an execute rights for script

```
$ chmod +x app_icon_maker.py
```
  and after type in console:
  
```
$ ./app_icon_maker.py ExampleIcon.png
```

## Installation

This script uses Pillow library for working with images. So, before starting using script you should install Pillow library to your system. As example, on MacOS you should execute in console:
```
$ sudo pip install Pillow
```

If you don't have installed pip, you should install pip first:
```
$ sudo easy_install pip
```
