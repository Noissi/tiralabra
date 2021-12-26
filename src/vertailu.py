import os
import matplotlib.pyplot as plt
from pathlib import Path
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    tiedostokansio1 = "testitiedostot/vertailu1/"
    tiedostokansio2 = "testitiedostot/vertailu2/"
    vertailu(tiedostokansio1, tiedostokansio2)
    
def vertailu(tiedostokansio1, tiedostokansio2):
    pakatut_koot_h = []
    pakatut_koot_l = []
    for tiedosto in sorted(os.listdir(tiedostokansio1)):
        koko_h = vertailuHuffman(tiedostokansio1 + tiedosto)
        koko_l = vertailuLempel(tiedostokansio1 + tiedosto)
        pakatut_koot_h.append(koko_h)
        pakatut_koot_l.append(koko_l)
    kuvaaja(pakatut_koot_h, pakatut_koot_l, "pakkauskuvaaja1.png", "Suomen laki")
    print(pakatut_koot_h)
    print(pakatut_koot_l)

    pakatut_koot_h2 = []
    pakatut_koot_l2 = []
    for tiedosto in sorted(os.listdir(tiedostokansio2)):
        koko_h = vertailuHuffman(tiedostokansio2 + tiedosto)
        koko_l = vertailuLempel(tiedostokansio2 + tiedosto)
        pakatut_koot_h2.append(koko_h)
        pakatut_koot_l2.append(koko_l)
    kuvaaja(pakatut_koot_h2, pakatut_koot_l2, "pakkauskuvaaja2.png", "a-kirjain")
    print(pakatut_koot_h2)
    print(pakatut_koot_l2)

def vertailuHuffman(tiedostopolku):
    koko = Path(tiedostopolku).stat().st_size
    huffman = Huffman(tiedostopolku)
    pakattu = huffman.aja()
    pakattu_koko = Path(pakattu).stat().st_size

    return prosenttiosuus(koko, pakattu_koko)

def vertailuLempel(tiedostopolku):
    koko = Path(tiedostopolku).stat().st_size
    lempelziv = Lempelziv(tiedostopolku)
    pakattu = lempelziv.aja()
    pakattu_koko = Path(pakattu).stat().st_size

    return prosenttiosuus(koko, pakattu_koko)

def kuvaaja(data1, data2, nimi, otsikko):
    plt.figure()
    plt.plot(range(1, len(data1) + 1), data1, marker='o')
    plt.plot(range(1, len(data2) + 1), data2, marker='o')
    
    plt.xlabel('Tiedoston rivien määrä')
    plt.ylabel('Pakatun tiedoston koko (% alkuperäisestä)')
    plt.xticks([1,2,3,4,5], ('10', '100', '500', '1000', '>4000'))
    plt.ylim((0, 260))
    
    plt.title("Pakkausvertailu (" + otsikko + ")")
    plt.legend(['Huffman', 'Lempel-Ziv']);
    plt.savefig("dokumentaatio/kuvat/" + nimi)

def prosenttiosuus(luku1, luku2):
    prosentti = luku2 * 100 / luku1
    return round(prosentti)

main()