import os
from pathlib import Path
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    if not os.path.exists('pakatut'):
        os.makedirs('pakatut')

    pakkaa_vai_pura = int(input("Haluatko pakata vai purkaa tiedoston?\n1 = pakkaa\n2 = pura\n"))
    huffman_vai_lempel = int(input("Valittava algoritmi:\n1 = Huffman\n2 = Lempel-Ziv\n"))
    tiedosto_loytyy = False
    if pakkaa_vai_pura == 1:
        while not tiedosto_loytyy:
            tiedosto = input("Anna polku pakattavaan tiedostoon.\n")
            tiedosto_loytyy = tiedosto_olemassa(tiedosto)
        pakkaus(tiedosto, huffman_vai_lempel)
    else:
        while not tiedosto_loytyy:
            tiedosto = input("Anna polku purettavaan tiedostoon.\n")
            tiedosto_loytyy = tiedosto_olemassa(tiedosto)
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
          " tavua.\nPakkauskoko on " + str(prosentti_osuus(koko1, koko2)) + "% alkuperäisestä tiedostosta.")

def purku(tiedosto, kumpi):
    if kumpi == 1:
        huffman = Huffman(tiedosto)
        purettu = huffman.pura()
    else:
        lempelziv = Lempelziv(tiedosto)
        purettu = lempelziv.pura()

    koko1 = tiedoston_koko(tiedosto)
    koko2 = tiedoston_koko(purettu)
    print("Purettavan tiedoston koko: " + str(koko1) + " tavua.\nPuretun tiedoston koko: " + str(koko2) +
          " tavua.\nTiedostokoko on " + str(prosentti_osuus(koko1, koko2)) + "% pakatusta tiedostosta.")

def tiedoston_koko(tiedosto):
    koko = Path(tiedosto).stat().st_size
    return koko

def prosentti_osuus(luku1, luku2):
    prosentti = luku2 * 100 / luku1
    return round(prosentti)

def tiedosto_olemassa(tiedosto):
    if not os.path.exists(tiedosto):
        print("Tiedostoa ei löytynyt.")
        return False
    return True

if __name__ == "__main__":
    main()
