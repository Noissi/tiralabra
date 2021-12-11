import os
from pathlib import Path
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    if not os.path.exists('pakatut'):
        os.makedirs('pakatut')
    if not os.path.exists('puretut'):
        os.makedirs('puretut')

    pakkaa_vai_pura = int(input("Haluatko pakata vai purkaa tiedoston?\n1 = pakkaa\n2 = pura\n"))
    huffman_vai_lempel = int(input("Valittava algoritmi:\n1 = Huffman\n2 = Lempel-Ziv\n"))
    if pakkaa_vai_pura == 1:
        tiedosto = input("Anna polku pakattavaan tiedostoon.\n")
        pakkaus(tiedosto, huffman_vai_lempel)
    else:
        tiedosto = input("Anna polku purettavaan tiedostoon.\n")
        purku(tiedosto, huffman_vai_lempel)

def pakkaus(tiedosto, kumpi):
    if kumpi == 1:
        huffman = Huffman(tiedosto)
        pakattu = huffman.aja()
    else:
        lempelziv = Lempelziv(tiedosto)
        pakattu = lempelziv.aja()

    koko1 = tiedoston_koko(tiedosto)
    koko2 = tiedoston_koko(pakattu)
    print("Pakattavan tiedoston koko: " + str(koko1) + " tavua.\nPakatun tiedoston koko: " + str(koko2) +
          " tavua.\nPakkauskoko pieneni " + str(pienentyma(koko1, koko2)) + "%.")

def purku(tiedosto, kumpi):
    if kumpi == 1:
        huffman = Huffman(tiedosto)
        polku_purkusanakirjaan = input("Anna polku purkusanakirjaan.\n")
        purettu = huffman.pura(polku_purkusanakirjaan)
    else:
        lempelziv = Lempelziv(tiedosto)
        purettu = lempelziv.pura()

    koko1 = tiedoston_koko(tiedosto)
    koko2 = tiedoston_koko(purettu)
    print("Pakattavan tiedoston koko: " + str(koko1) + " tavua.\nPakatun tiedoston koko: " + str(koko2) +
          " tavua.\nPakkauskoko pieneni " + str(pienentyma(koko1, koko2)*-1) + "%.")

def tiedoston_koko(tiedosto):
    koko = Path(tiedosto).stat().st_size
    return koko

def pienentyma(luku1, luku2):
    prosentti = (luku1-luku2) * 100 / luku1
    return round(prosentti)

if __name__ == "__main__":
    main()
