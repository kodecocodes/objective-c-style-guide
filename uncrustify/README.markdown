# Uncrustification

**rw-uncrustify.cfg** is a configuration file for the [Uncrustify](http://uncrustify.sourceforge.net/)
source code beautifier. You can install it from source or from the epically-useful [Homebrew](http://brew.sh/).
You can also search the web for Xcode plugins if that's your thing.

The goal here is to automate the coding conventions of the style guide.

## Tests

Of course, there are tests!

A sample input file `test-input.m` is run through Uncrustify, and its output
is compared to the contents of `test-expected.m`. There should be a perfect
match.

To run the tests, just run the script `test-rw-uncrustify.sh`. You'll need
the command-line version of uncrustify.

## Conclusion

As with all things online, this is a work in progress. Pull requests and contributions are welcome.

