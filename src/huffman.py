from puu import Silmu
from jono import Jono

class Huffman:
	""" Luokka Huffman tiedostonpakkausalgoritmille.

    Määritteet:
    """

	def __init__(self, tiedosto):
		""" Luokan muodostaja. Luo uuden Huffman algoritmiolion..
		Args:
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
		self.pakkaa()

		print(self.sanakirja)
		#self.tulostaPuu(puu, ":")

	def pakkaa(self):
		""" Pakkaa tekstitiedoston pienempään tilaan. Luo uuden binääritiedoston.
		"""

		binaaritiedosto = open("pakatut/pakkaus", "wb")
		tiedosto = open(self.tiedosto, "r")
		rivit = tiedosto.readlines()
		binaaristringi = ""
		
		for teksti in rivit:
			for kirjain in teksti:
				binaaristringi += self.sanakirja[kirjain]
		binaaritiedosto.write(int(binaaristringi[::-1], 2).to_bytes(4, 'big'))
		binaaritiedosto.close()
		tiedosto.close()
		print(binaaristringi)

	def kirjaintenEsiintyvyys(self):
		""" Laskee kunkin kirjaimen esiintyvyyden annetussa tekstissä.
		    Palauttaa: 
		    	Sanakirja, jossa kirjainten määrä.
		"""

		tekstitiedosto = open(self.tiedosto, "r")
		rivit = tekstitiedosto.readlines()

		esiintyvyys = {}
		esiintyvyys["\n"] = 0

		for teksti in rivit:
			for kirjain in teksti:
				if kirjain in esiintyvyys:
					esiintyvyys[kirjain] += 1
				else:
					esiintyvyys[kirjain] = 1
			#esiintyvyys["\n"] += 1
		tekstitiedosto.close()
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

		return jono2.poistaJonosta()

	def kirjaimetPuuhun(self, esiintyvyys):
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
		self.sanakirja[puu.kirjain] = merkki
		if puu.vasen:
			self.lisaaSanakirjaan(puu.vasen, merkki + "0")
		if puu.oikea:
			self.lisaaSanakirjaan(puu.oikea, merkki + "1")

'''
	def tulostaPuu(self, puu, merkki):
		if puu.vasen:
			self.tulostaPuu(puu.vasen, merkki + "0")
		print(str(puu.kirjain) + " " + merkki)
		if puu.oikea:
			self.tulostaPuu(puu.oikea, merkki + "1")
'''	
