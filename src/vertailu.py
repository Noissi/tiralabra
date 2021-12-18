import os
import matplotlib.pyplot as plt
from pathlib import Path
from huffman import Huffman
from lempelziv import Lempelziv

def main():
    pakatut_koot_h = vertailuHuffman()
    pakatut_koot_l = vertailuLempel()
    kuvaaja(pakatut_koot_h, pakatut_koot_l)

def vertailuHuffman():
    tiedostokansio = "testitiedostot/"
    pakatut_koot = []
    for tiedosto in os.listdir(tiedostokansio):
        koko = Path(tiedostokansio + tiedosto).stat().st_size
        huffman = Huffman(tiedostokansio + tiedosto)
        pakattu = huffman.aja()
        pakattu_koko = Path(pakattu).stat().st_size
        pakatut_koot.append(pienentyma(koko, pakattu_koko))

    return pakatut_koot

def vertailuLempel():
    tiedostokansio = "testitiedostot/"
    pakatut_koot = []
    for tiedosto in os.listdir(tiedostokansio):
        print(tiedosto)
        koko = Path(tiedostokansio + tiedosto).stat().st_size
        lempelziv = Lempelziv(tiedostokansio + tiedosto)
        pakattu = lempelziv.aja()
        pakattu_koko = Path(pakattu).stat().st_size
        pakatut_koot.append(pienentyma(koko, pakattu_koko))

    return pakatut_koot

def kuvaaja(data1, data2):
    plt.plot(range(1, len(data1) + 1), data1, marker='o')
    plt.plot(range(1, len(data2) + 1), data2, marker='o')
    
    plt.xlabel('Tiedosto')
    plt.ylabel('Pakatun tiedoston koko (% alkuperäisestä)')
    
    plt.title("Pakkausvertailu")
    plt.legend(['Huffman', 'Lempel-Ziv']);
    plt.savefig("pakkauskuvaaja.png")

def pienentyma(luku1, luku2):
    prosentti = luku2 * 100 / luku1
    return round(prosentti)

main()