import os
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    if not os.path.exists('pakatut'):
        os.makedirs('pakatut')

    tiedosto = input("Anna polku tiedostoon.\n")
    huffman_vai_lempel = int(input("Aja huffman = 1, Aja lempel = 2\n"))
    pakkaus(tiedosto, huffman_vai_lempel)

def pakkaus(tiedosto, kumpi):
    if kumpi == 1:
        huffman = Huffman(tiedosto)
        huffman.aja()
    else:
        lempel_humpel = Lempelziv(tiedosto)
        lempel_humpel.aja()

def pakkausvertailu():
    pass

main()
