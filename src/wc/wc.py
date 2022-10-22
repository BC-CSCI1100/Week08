import sys

def go(filename):
    charCount = 0
    wordCount = 0
    lineCount = 0
    inch = open(filename,"r")
    for line in inch:
        lineCount = lineCount + 1
        wordCount = wordCount + len(line.split())
        charCount = charCount + len(line)
    inch.close()
    print(f"%d  %d  %d" % (lineCount, wordCount, charCount))

go(sys.argv[1])
