import unittest
import os
from huffman import Huffman
from puu import Silmu
from jono import Jono

class TestHuffman(unittest.TestCase):
	def setUp(self):
		self.pakkaus1 = Huffman("testitiedostot/testi.txt")
		self.pakkaus2 = Huffman("testitiedostot/abc.txt")
		self.purku1 = Huffman("pakatut/abc.hfm")

	def test_huffman(self):
		pass
		#self.assertEqual(huffman("moi"), "palautus")
		
	def test_kirjainten_esiintyvyys(self):
		maarat = self.pakkaus1.kirjaintenEsiintyvyys()
		
		self.assertEqual(maarat["T"], 1)
		self.assertEqual(maarat["ä"], 2)
		self.assertEqual(maarat["m"], 1)
		self.assertEqual(maarat["t"], 4)
		self.assertEqual(maarat[" "], 3)
		
	def test_pienin_jonottaja_eka_tyhja(self):
		jono1 = Jono()
		jono2 = Jono()
		jono2.lisaaJonoon(Silmu("a", 8))
		silmu = self.pakkaus1.pieninJonottaja(jono1, jono2)
		
		self.assertEqual(silmu.maara, 8)
		self.assertEqual(silmu.kirjain, "a")
		
	def test_pienin_jonottaja_toka_tyhja(self):
		jono1 = Jono()
		jono2 = Jono()
		jono1.lisaaJonoon(Silmu("x", 4))
		silmu = self.pakkaus1.pieninJonottaja(jono1, jono2)
		
		self.assertEqual(silmu.maara, 4)
		self.assertEqual(silmu.kirjain, "x")
		
	def test_pienin_jonottaja_eka_pienin(self):
		jono1 = Jono()
		jono2 = Jono()
		jono1.lisaaJonoon(Silmu("x", 4))
		jono2.lisaaJonoon(Silmu("e", 5))
		silmu = self.pakkaus1.pieninJonottaja(jono1, jono2)
		
		self.assertEqual(silmu.maara, 4)
		self.assertEqual(silmu.kirjain, "x")
		
	def test_pienin_jonottaja_toka_pienin(self):
		jono1 = Jono()
		jono2 = Jono()
		jono1.lisaaJonoon(Silmu("x", 4))
		jono2.lisaaJonoon(Silmu("e", 2))
		silmu = self.pakkaus1.pieninJonottaja(jono1, jono2)
		
		self.assertEqual(silmu.maara, 2)
		self.assertEqual(silmu.kirjain, "e")
		
	def test_pienin_jonottaja_yhtasuuret(self):
		jono1 = Jono()
		jono2 = Jono()
		jono1.lisaaJonoon(Silmu("x", 2))
		jono2.lisaaJonoon(Silmu("e", 2))
		silmu = self.pakkaus1.pieninJonottaja(jono1, jono2)

		self.assertEqual(silmu.maara, 2)
		self.assertEqual(silmu.kirjain, "x")

	def test_kirjaimet_puuhun(self):
		esiintyvyys = [("c",1), ("\n", 3), ("b", 3), ("a", 5)]
		puu  = self.pakkaus2.kirjaimetPuuhun(esiintyvyys)

		self.assertEqual(puu.kirjain, None)
		self.assertEqual(puu.maara, 12)
		self.assertEqual(puu.vasen.kirjain, "a")
		self.assertEqual(puu.vasen.maara, 5)
		self.assertEqual(puu.oikea.kirjain, None)
		self.assertEqual(puu.oikea.vasen.kirjain, "b")
		self.assertEqual(puu.oikea.oikea.vasen.kirjain, "c")
		self.assertEqual(puu.oikea.oikea.oikea.kirjain, "\n")

	def test_lisaa_sanakirjaan(self):
		vasen = Silmu("\n", 3)
		oikea = Silmu("c", 1)
		silmu = Silmu(None, 4)
		silmu.lisaaLapset(vasen, oikea)
		oikea2 = Silmu("b", 3)
		silmu2 = Silmu(None, 7)
		silmu2.lisaaLapset(silmu, oikea2)
		oikea3 = Silmu("a", 5)
		silmu3 = Silmu(None, 12)
		silmu3.lisaaLapset(silmu2, oikea3)
		puu = silmu3
		self.pakkaus2.lisaaSanakirjaan(puu, "")
		print(self.pakkaus2.sanakirja)
		self.assertEqual(self.pakkaus2.sanakirja["a"], "1")
		self.assertEqual(self.pakkaus2.sanakirja["b"], "01")
		self.assertEqual(self.pakkaus2.sanakirja["c"], "001")
		self.assertEqual(self.pakkaus2.sanakirja["\n"], "000")

	def test_pakkaa(self):
		self.pakkaus2.sanakirja = {"a":"1", "b":"01", "c":"001", "\n":"000"}
		self.pakkaus2.pakkaa()

	def test_pura_tiedosto_on_olemassa(self):
		self.purku1.pura("pakatut/hfm_sanakirja.json")
		on_olemassa = os.path.exists("pakatut/abc.hfm_purettu")
		self.assertEqual(True, on_olemassa)

	def test_aja(self):
		tiedosto = self.pakkaus1.aja()
		self.assertEqual(tiedosto, "pakatut/testi.hfm")
