from pathlib import Path

class Lempelziv:
    """ Luokka Lempel-Ziv -tiedostonpakkausalgoritmille.

        Määritteet:
            tiedosto: Pakattava tekstitiedosto
            sanakirja: Sanakirja pakkaamista varten.
    """

    def __init__(self, tiedosto):
        """ Luokan muodostaja. Luo uuden Lempel-Ziv -algoritmiolion.
		Parametrit:
		    tiedosto: Pakattava tekstitiedosto
		"""

        self.tiedosto = tiedosto
        self.sanakirja = {}

        self.nimi = Path(self.tiedosto).stem + ".lzw"
        self.polku = "pakatut/"

        
        self.sanakirja = {chr(i): i for i in range(256)}
        self.sanakirjan_koko = 259
        self.sanakirja["′"] = 256
        self.sanakirja["›"] = 257
        self.sanakirja["–"] = 258
        
        self.purkukirjan_koko = 259
        self.purkukirja = {i: chr(i) for i in range(256)}
        self.purkukirja["′"] = 256
        self.purkukirja["›"] = 257
        self.purkukirja["–"] = 258

    def aja(self):
        """ Ajaa Lempel-Ziv -pakkausalgoritmin.
		"""

        self.pakkaa()

        return  self.polku + self.nimi

    def pakkaa(self):
        """ Pakkaa tiedoston.
        """

        with open(self.polku + self.nimi, "wb") as binaaritiedosto, \
                open(self.tiedosto, "r") as tekstitiedosto:

            rivit = tekstitiedosto.readlines()

            binaariteksti = ""
            sana = ""
            indeksit = []
            for teksti in rivit:
                for merkki in teksti:
                    merkkijono = sana + merkki
                    if merkkijono in self.sanakirja:
                        sana = merkkijono
                    else:
                        binaariteksti += bin(self.sanakirja[sana])[2:].zfill(12)
                        indeksit.append(self.sanakirja[sana])
                        if self.sanakirjan_koko < 4096:
                            self.sanakirja[merkkijono] = len(self.sanakirja)
                            self.sanakirjan_koko += 1
                        sana = merkki
                        
            if sana == merkkijono or self.sanakirjan_koko == 4096:
                binaariteksti += bin(self.sanakirja[sana])[2:].zfill(12)
                indeksit.append(self.sanakirja[sana])
                

            if len(binaariteksti)%8 != 0:
                binaariteksti += "0000"
            tavupituus = len(binaariteksti)//8
            binaaritiedosto.write(int(binaariteksti, 2).to_bytes(tavupituus, 'big'))

        return indeksit

    def pura(self):
        """ Purkaa tiedoston.
        """

        with open(self.tiedosto, 'rb') as purettava:
            tavut = purettava.read()
        binaaristringi = ""

        for tavu in tavut:
            binaaristringi += "{0:b}".format(tavu).zfill(8)

        tulos = ""
        j = 0
        i = 12
        merkkijono1 = chr(int(binaaristringi[j:i], 2))
        tulos += merkkijono1
        j += 12
        i += 12

        while i <= len(binaaristringi):
            luku = int(binaaristringi[j:i], 2)
            if luku in self.purkukirja:
                merkkijono2 = self.purkukirja[luku]
            else:
                merkkijono2 = merkkijono1 + merkkijono1[0]
            tulos += merkkijono2

            if self.purkukirjan_koko < 4096:
                self.purkukirja[self.purkukirjan_koko] = merkkijono1 + merkkijono2[0]
                self.purkukirjan_koko += 1

            merkkijono1 = merkkijono2
            j += 12
            i += 12

        polku_split = self.tiedosto.split('/')
        tallennuspolku = '/'.join(polku_split[:-1]) + '/' + polku_split[-1] + "_purettu"
        with open(tallennuspolku, 'w') as tallennus:
            tallennus.write(tulos)

        return tallennuspolku