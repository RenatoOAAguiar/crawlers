import textract
from os import walk



f = []
for (dirpath, dirnames, filenames) in walk("pdf/"):
    text = textract.process("path/to/file.extension")
    print(text)