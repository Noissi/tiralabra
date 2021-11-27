from huffman import Huffman
from lempelziv import Lempelziv

def main():
    tiedosto = input("Anna polku tiedostoon.\n")
    huffman_vai_lempel = int(input("Aja huffman = 1, Aja lempel = 2\n"))
    jotain = pakkausvertailu(tiedosto, huffman_vai_lempel)
    print(jotain)

def pakkausvertailu(tiedosto, kumpi):
    if kumpi == 1:
        huffman = Huffman(tiedosto)
        huffman.aja()
    else:
        lempel_humpel = Lempelziv(tiedosto)
        lempel_humpel.aja()

main()
