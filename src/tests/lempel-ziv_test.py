import unittest
import os
from lempelziv import Lempelziv

class TestLempelziv(unittest.TestCase):
    def setUp(self):
        self.pakkaus1 = Lempelziv("testitiedostot/testi.txt")
        self.pakkaus2 = Lempelziv("testitiedostot/abc.txt")

    def test_lempelziv(self):
        pass
		#self.assertEqual(huffman("moi"), "palautus")

    def test_pakkaa_testi(self):
        tulos = self.pakkaus1.pakkaa()
        indeksit = [84, 228, 109, 228, 32, 111, 110, 32, 116, 101, 115, 116, 105, 263, 101, 107, 266, 105]
        self.assertEqual(tulos, indeksit)

    def test_pakkaa_abc(self):
        tulos = self.pakkaus2.pakkaa()
        indeksit = [97, 98, 99, 10, 97, 260, 97, 10, 98, 98]
        self.assertEqual(tulos, indeksit)

    def test_pura_tiedosto_on_olemassa(self):
        self.pakkaus2.pura("pakatut/pakkaus.lzw")
        on_olemassa = os.path.exists("pakatut/pakkaus.lzw_purettu")
        self.assertEqual(True, on_olemassa)
    
    def test_aja(self):
        indeksit = self.pakkaus1.pakkaa()
        indeksit_malli = [84, 228, 109, 228, 32, 111, 110, 32, 116, 101, 115, 116, 105, 263, 101, 107, 266, 105]
        self.assertEqual(indeksit, indeksit_malli)
        
		
