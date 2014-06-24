#!/bin/sh

if command -v uncrustify > /dev/null; then
  uncrustify -q -c rw-uncrustify.cfg -f test-input.m | diff -u - test-expected.m
  if [[ $? -ne 0 ]]; then
    echo "ERROR: uncrustified output doesn't match the expected output."
    exit 1
  fi
else
  echo ERROR: cannot find uncrustify.
  exit 2
fi

echo "OK: rw-uncrustify.cfg did its job correctly."

