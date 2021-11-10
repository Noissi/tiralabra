import unittest
from huffman import Huffman

class TestMain(unittest.TestCase):
	def setUp(self):
		pass

	def test_huffman(self):
		pass
		#self.assertEqual(huffman("moi"), "palautus")
		
	def test_kirjainten_esiintyvyys(self):
		pakkaus = Huffman("Tämä on testi teksti")
		maarat = pakkaus.kirjainten_esiintyvyys()
		self.assertEqual(maarat["T"], 1)
		self.assertEqual(maarat["ä"], 2)
		self.assertEqual(maarat["m"], 1)
		self.assertEqual(maarat["t"], 4)
		self.assertEqual(maarat[" "], 3)
