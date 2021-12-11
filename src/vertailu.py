import os
from pathlib import Path
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    pass

def pakkausvertailu():
    for tiedosto in os.listdir("testitiedostot/"):
        koko = Path(tiedosto).stat().st_size

main()
