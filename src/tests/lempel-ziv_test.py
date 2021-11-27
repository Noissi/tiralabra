import unittest
from lempelziv import Lempelziv

class TestLempelziv(unittest.TestCase):
    def setUp(self):
        self.pakkaus1 = Lempelziv("/home/nomanoma/Documents/Kurssit/Tiralabra2021/tiralabra/testitiedostot/testi.txt")
        self.pakkaus2 = Lempelziv("/home/nomanoma/Documents/Kurssit/Tiralabra2021/tiralabra/testitiedostot/abc.txt")

    def test_lempelziv(self):
        pass
		#self.assertEqual(huffman("moi"), "palautus")

    def test_pakkaa_testi(self):
        tulos = self.pakkaus1.pakkaa()
        indeksit = [84, 228, 109, 228, 32, 111, 110, 32, 116, 101, 115, 116, 105, 263, 101, 107, 266, 105, 10]
        self.assertEqual(tulos, indeksit)

    def test_pakkaa_abc(self):
        tulos = self.pakkaus2.pakkaa()
        indeksit = [97, 98, 99, 10, 97, 260, 97, 10, 98, 98, 10]
        self.assertEqual(tulos, indeksit)

    def test_pura(self):
        pass
    
    def test_aja(self):
        indeksit = self.pakkaus1.pakkaa()
        indeksit_malli = [84, 228, 109, 228, 32, 111, 110, 32, 116, 101, 115, 116, 105, 263, 101, 107, 266, 105, 10]
        self.assertEqual(indeksit, indeksit_malli)
        
		
