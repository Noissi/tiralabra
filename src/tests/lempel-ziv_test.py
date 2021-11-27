import unittest
from lempelziv import Lempelziv

class TestLempelziv(unittest.TestCase):
	def setUp(self):
		self.pakkaus1 = Lempelziv("testitiedostot/testi.txt")
		self.pakkaus2 = Lempelziv("testitiedostot/abc.txt")

	def test_lempelziv(self):
		pass
		#self.assertEqual(huffman("moi"), "palautus")
		
	def test_pakkaa(self):
		tulos = self.pakkaus2.pakkaa()
		print(tulos)
		print(self.pakkaus2.sanakirja)
		self.assertEqual(tulos, 1)
		
	def test_pura(self):
		pass
		
