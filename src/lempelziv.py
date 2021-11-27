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

        sanakirjan_koko = 256
        self.sanakirja = {chr(i): i for i in range(sanakirjan_koko)}

    def aja(self):
        """ Ajaa Lempel-Ziv -pakkausalgoritmin.
		"""

        indeksit = self.pakkaa()
        return indeksit

    def pakkaa(self):
        """ Pakkaa tiedoston.
        """

        binaaritiedosto = open("pakatut/pakkaus.lzw", "wb")
        tekstitiedosto = open(self.tiedosto, "r")
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
                    binaariteksti += bin(self.sanakirja[sana])[2:]
                    indeksit.append(self.sanakirja[sana])
                    self.sanakirja[merkkijono] = len(self.sanakirja)
                    sana = merkki

        tavupituus = len(binaariteksti)//8 + 1
        binaaritiedosto.write(int(binaariteksti[::-1], 2).to_bytes(tavupituus, 'big'))

        #if sana:
        #    tulos.append(self.sanakirja[sana])

        return indeksit

    def pura(self):
        """ Purkaa tiedoston.
        """

        pass
