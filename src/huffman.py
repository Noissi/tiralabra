import json
from pathlib import Path
from puu import Silmu
from jono import Jono

class Huffman:
    """ Luokka Huffman tiedostonpakkausalgoritmille.

        Määritteet:
            tiedosto: Pakattava tekstitiedosto
            sanakirja: Sanakirja pakkaamista varten.
    """

    def __init__(self, tiedosto):
        """ Luokan muodostaja. Luo uuden Huffman algoritmiolion..
		Parametrit:
		    tiedosto: Pakattava tekstitiedosto
		"""

        self.tiedosto = tiedosto
        self.sanakirja = {}

    def aja(self):
        """ Ajaa Huffmanin pakkausalgoritmin.
		"""

        esiintyvyys = self.kirjaintenEsiintyvyys()
        esiintyvyys_jarj = sorted(esiintyvyys.items(), key=lambda x: x[1])
        puu = self.kirjaimetPuuhun(esiintyvyys_jarj)
        self.lisaaSanakirjaan(puu, "")
        pakattu = self.pakkaa()
        
        return pakattu

		#self.tulostaPuu(puu, ":")

    def pakkaa(self):
        """ Pakkaa tekstitiedoston pienempään tilaan. Luo uuden binääritiedoston.
		"""
        tiedosto_nimi = Path(self.tiedosto).stem
        with open("pakatut/" + tiedosto_nimi + ".hfm", "wb") as binaaritiedosto, \
                open(self.tiedosto, "r") as tekstitiedosto:

            rivit = tekstitiedosto.readlines()
            binaariteksti = ""
    
            for teksti in rivit:
                for kirjain in teksti:
                    binaariteksti += self.sanakirja[kirjain]
            
            if len(binaariteksti)%8 != 0:
                ekstranollat = 8-(len(binaariteksti)%8)
                binaariteksti += '0'*(8-(len(binaariteksti)%8))
            else:
                ekstranollat = 0
            tavupituus = len(binaariteksti)//8
            binaaritiedosto.write(int(binaariteksti, 2).to_bytes(tavupituus, 'big'))

        sanakirjatiedosto = open("pakatut/hfm_sanakirja.json", 'w')
        self.sanakirja["nollat"] = ekstranollat
        json.dump(self.sanakirja, sanakirjatiedosto)
        
        return "pakatut/" + tiedosto_nimi + ".hfm"

    def kirjaintenEsiintyvyys(self):
        """ Laskee kunkin kirjaimen esiintyvyyden annetussa tekstissä.
		    Palauttaa:
		    	Sanakirja, jossa kirjainten määrä.
		"""

        with open(self.tiedosto, "r") as tekstitiedosto:
            rivit = tekstitiedosto.readlines()
    
            esiintyvyys = {}
            esiintyvyys["\n"] = 0
    
            for teksti in rivit:
                for kirjain in teksti:
                    if kirjain in esiintyvyys:
                        esiintyvyys[kirjain] += 1
                    else:
                        esiintyvyys[kirjain] = 1
        return esiintyvyys

    def pieninJonottaja(self, jono1, jono2):
        """ Katsoo kummassa parametrina annetussa jonossa on etummaisena silmu
			pienemmällä arvolla (maara)
			Parametrit:
				jono1: Jono-olio
				jono2: Jono-olio
		    Palauttaa:
		    	Silmu-olion, jolla on pienin arvo (maara)
		"""

        if jono1.onTyhja():
            return jono2.poistaJonosta()
        elif jono2.onTyhja():
            return jono1.poistaJonosta()
        elif jono1.jono[0].maara <= jono2.jono[0].maara:
            return jono1.poistaJonosta()
        else:
            return jono2.poistaJonosta()

    def kirjaimetPuuhun(self, esiintyvyys):
        """ Luo kirjainten esiintyvyyksistä puurakenteen.
			Parametrit:
				esiintyvyys: Sanakirja, joka sisältää merkit avaimina ja niiden lukumäärän.
		    Palauttaa:
		    	Puu (eli ylimmän silmun).
		"""

        kirjaimet = [x[0] for x in esiintyvyys]
        maarat = [x[1] for x in esiintyvyys]

        jono1 = Jono()
        jono2 = Jono()

        for i in range(0, len(kirjaimet)):
            silmu = Silmu(kirjaimet[i], maarat[i])
            jono1.lisaaJonoon(silmu)

        while not (jono1.onTyhja() and jono2.pituusYksi()):
            vasen = self.pieninJonottaja(jono1, jono2)
            oikea = self.pieninJonottaja(jono1, jono2)

            esiintyvyys_summa = vasen.maara + oikea.maara

            ylasilmu = Silmu(None, esiintyvyys_summa)
            ylasilmu.lisaaLapset(vasen, oikea)

            jono2.lisaaJonoon(ylasilmu)

        return jono2.jono.pop(0)

    def lisaaSanakirjaan(self, puu, merkki):
        """ Luo sanakirjan, jossa jokaisella merkkillä on sen sijaintia puussa vastaava binaariluku.
			Parametrit:
				puu: Silmu, joka viittaa merkkien esiintyvyyttä kuvaavan puun alkuun
				merkki: binaariluku
		"""

        self.sanakirja[puu.kirjain] = merkki
        if puu.vasen:
            self.lisaaSanakirjaan(puu.vasen, merkki + "0")
        if puu.oikea:
            self.lisaaSanakirjaan(puu.oikea, merkki + "1")

    def tulostaPuu(self, puu, merkki):
        if puu.vasen:
            self.tulostaPuu(puu.vasen, merkki + "0")
        print(str(puu.kirjain) + " " + merkki)
        if puu.oikea:
            self.tulostaPuu(puu.oikea, merkki + "1")

    def pura(self, polku_purettavaan, polku_purkusanakirjaan):
        """ Purkaa tiedoston.
        """
        tavut = open(polku_purettavaan, 'rb').read()
        purkukirja = json.load(open(polku_purkusanakirjaan, 'r'))
        ekstranollat = int(purkukirja["nollat"])
        if "null" in purkukirja:
            purkukirja.pop("null")
        purkukirja.pop("nollat")
        purkukirja = {y:x for x,y in purkukirja.items()}
        binaaristringi = ""

        for tavu in tavut:
            binaaristringi += "{0:b}".format(tavu).zfill(8)
        if ekstranollat != 0:
            binaaristringi = binaaristringi[:(-1*ekstranollat)]
        i = 0
        tulos = ""
        bittijono = ""
        while i < len(binaaristringi):
            bittijono += binaaristringi[i]
            if bittijono in purkukirja:
                merkki = purkukirja[bittijono]
                tulos += merkki
                bittijono = ""
            i += 1

        polku_split = polku_purettavaan.split('/')
        tallennuspolku = '/'.join(polku_split[:-1]) + '/' + polku_split[-1] + "_purettu"
        tallennus = open(tallennuspolku, 'w')
        tallennus.write(tulos)
        print("Tiedosto purettu, huraa!\nPurettu tiedosto on " + tallennuspolku)
