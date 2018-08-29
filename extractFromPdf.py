import textract
from os import walk

for (dirpath, dirnames, filenames) in walk("pdf/"):
    for arquivo in filenames:
        text = textract.process(dirpath + arquivo)
        with open('contentBooks/' + arquivo.split(".pdf")[0] + '.txt', 'a', encoding="uft-8") as f:
            f.write(text.decode("utf-8"))