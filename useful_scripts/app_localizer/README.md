# iOS Application Localization Helper

This script can be useful in providing localization files to customer.

## Description and example

For example, you have a project with two localizations, e.g. EN and DE. At first, you should put app_localizer.py script to your project directoty. After that you should create 'localizations' plain text file in the same directory. Let you localization resources of your project stores in 'resources' folder then put next strings in 'localizations' file:
```
resources/en.lproj/Localizable.strings
resources/de.lproj/Localizable.strings
```
After that you should execute:
```
$ ./app_localizaer.py merge
```
As result you will get 'localizations.csv' file in script directory. After that you could convert it to .xls, as example and send it to your customer.
When customer finished translation of this file and sent it back to you, replace 'localization.csv' file by received file and run:
```
$ ./app_localizaer.py split
```
When script finishes work you will get translated project.

Script has many options for executing which you could get by running script with '--help' option.

## Using

You can use this script in two ways:

* First:
 
You can execute this script by typing in terminal:

```
$ ./python app_localizer.py {merge|split}
```
* Second:
 
At first, you should set an execute rights for script

```
$ chmod +x app_localizer.py
```
  and after type in console:
  
```
$ ./app_localizer.py {merge|split}
```

## Installation

Just download script, put it to your  project and run it.
