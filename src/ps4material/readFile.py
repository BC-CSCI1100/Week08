# CSCI1100 Gateway to Computer Science
#
# Reading files with the read function.
#
# run: python3 readFile.py filename
#
# Also, reading individual lines:
#
#   line = inputFile.readline()       # Read one line
#
#   for line in inputFile:
#       ... line ...
import sys

def go():
    inputFile = open(sys.argv[1])

    string = inputFile.read()         # Reads the entire file
    print("We read:")
    print(string)
    inputFile.close()

go()
