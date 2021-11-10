from puu import Silmu

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

	def pakkaa(self):
		""" Pakkaa tekstitiedoston pienempään tilaan.
		    Palauttaa: 
		    	-
		"""

		esiintyvyys = kirjainten_esiintyvyys(self.tiedosto)
		esiintyvyys_jarj = sorted(esiintyvyys.items(), key=lambda x: x[1])
		puu = kirjaimet_puuhun(esiintyvyys_jarj)
		
		return "palautus"

	def kirjainten_esiintyvyys(self):
		""" Laskee kunkin kirjaimen esiintyvyyden annetussa tekstissä.
		    Palauttaa: 
		    	Sanakirja, jossa kirjainten määrä.
		"""
		
		teksti = self.tiedosto
		esiintyvyys = {}
		for kirjain in teksti:
			if kirjain in esiintyvyys:
				esiintyvyys[kirjain] += 1
			else:
				esiintyvyys[kirjain] = 1
		return esiintyvyys
		
	def kirjaimet_puuhun(self, kirjaimet):
		kirjaimet = kirjaimet.keys()
		maarat = kirjaimet.values()
		silmu_oikea = None
		silmu_vasen = None
		i = 0
		while i > len(kirjaimet):
			silmu = Silmu(kirjaimet[i])
			silmu.lapset(silmu_oikea, silmu_vasen)
			summa = maara1 + maara2
			i += 1
			if maara[i] < summa:
				silmu = kirjaimet_puuhun()
			
		
				
		
		
	
