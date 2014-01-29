# Snippets Importer

This scripts imports all snippets from working or specified directory to Xcode

## Description and example

For example, you have a folder contains snippets in ~/example/snippets
Execute:
```
$ ./snippets_import.py --folder ~/example/snippets
```
As result all snippets will be imported to Xcode. '--folder' key is not required. If '--folder' not presented script will run in it's working folder.

## Using

You can use this script in two ways:

* First:
 
You can execute this script by typing in terminal:

```
$ ./python snippets_import.py --folder ~/example/snippets
```
* Second:
 
At first, you should set an execute rights for script

```
$ chmod +x snippets_import.py
```
  and after type in console:
  
```
$ ./snippets_import.py --folder ~/example/snippets
```

## Installation

Just download the script and execute it in console.
