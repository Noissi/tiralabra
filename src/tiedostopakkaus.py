import os
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    if not os.path.exists('pakatut'):
        os.makedirs('pakatut')
    
    pakkaa_vai_pura = int(input("Haluatko pakata vai purkaa tiedoston?\n1=pakkaa\n2=pura\n"))
    if pakkaa_vai_pura == 2:
        huff_vai_lempel = pakkaa_vai_pura = int(input("Purkualgoritmi?\n1=Huffman\n2=Lempel-Ziv\n"))
        polku_purettavaan = input("Anna polku purettavaan tiedostoon.\n")
        if huff_vai_lempel == 2:
            lempel = Lempelziv("pura")
            lempel.pura(polku_purettavaan)
        else:
            polku_purkusanakirjaan = input("Anna polku purkusanakirjaan.\n")
            huff = Huffman("pura")
            huff.pura(polku_purettavaan, polku_purkusanakirjaan)
    else:
        tiedosto = input("Anna polku pakattavaan tiedostoon.\n")
        huffman_vai_lempel = int(input("Aja huffman = 1, Aja lempel = 2\n"))
        pakkaus(tiedosto, huffman_vai_lempel)

def pakkaus(tiedosto, kumpi):
    if kumpi == 1:
        huffman = Huffman(tiedosto)
        huffman.aja()
    else:
        lempel_humpel = Lempelziv(tiedosto)
        lempel_humpel.aja()

main()
