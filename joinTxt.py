from os import walk
import re

for (dirpath, dirnames, filenames) in walk("newfiles/"):
    with open("medium1.txt", 'w', encoding="utf-8") as outfile:
        for arquivo in filenames:
            with open(dirpath + arquivo, 'r', encoding="utf-8") as readfile:
                texto = re.sub(r'[^]:[(.""?!"ºª#$%&()\'*+,-./:;<=>?@[\]^_`{|}~),{}/âÂôÔêÊãÃõÕçÇáÁéÉíÍóÓúÚa-zA-Z0-9"\n \._-]', '', readfile.read())
                outfile.write(texto + "\n \n")
                