import os
from pathlib import Path
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    if not os.path.exists('pakatut'):
        os.makedirs('pakatut')

    tiedosto = input("Anna polku tiedostoon.\n")
    pakkausvertailu(huffman, lempel)

def pakkausvertailu():
    for tiedosto in os.listdir("testitiedostot/"):
        koko = Path(tiedosto).stat().st_size

main()
