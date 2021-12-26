import unittest
import os
from lempelziv import Lempelziv

class TestLempelziv(unittest.TestCase):
    def setUp(self):
        self.pakkaus1 = Lempelziv("testitiedostot/testi.txt")
        self.pakkaus2 = Lempelziv("testitiedostot/abc.txt")
        self.pakkaus3 = Lempelziv("testitiedostot/tuksu.txt")
        self.purku1 = Lempelziv("pakatut/abc.lzw")

    def test_lempelziv(self):
        pass
		#self.assertEqual(huffman("moi"), "palautus")

    def test_pakkaa_testi(self):
        tulos = self.pakkaus1.pakkaa()
        indeksit = [84, 228, 109, 228, 32, 111, 110, 32, 116, 101, 115, 116, 105, 266, 101, 107, 269, 105]
        self.assertEqual(tulos, indeksit)

    def test_pakkaa_abc(self):
        tulos = self.pakkaus2.pakkaa()
        indeksit = [97, 98, 99, 10, 97, 263, 97, 10, 98, 98]
        self.assertEqual(tulos, indeksit)

    def test_pakkaa_tuksu(self):
        tulos = self.pakkaus3.pakkaa()
        indeksit = [80, 97, 108, 97, 115, 105, 110, 32, 106, 117, 117, 114, 105, 32, 268, 100, 101, 115, 116, \
                    97, 32, 107, 111, 117, 108, 117, 276, 97, 110, 105, 46, 32, 259, 261, 263, 265, 267, 269, \
                    271, 273, 275, 277, 279, 281, 283, 285, 287, 289, 291, 262, 264, 266, 268, 270, 272, 117, \
                    274, 285, 301, 282, 284, 277, 305, 290, 260, 308, 294, 311, 297, 314, 299, 278, 280, 318, \
                    304, 288, 322, 292, 309, 295, 312, 298, 316, 331, 303, 320, 334, 307, 293, 310, 296, 313, \
                    315, 300, 342, 319, 286, 345, 323, 347, 338, 327, 351, 330, 302, 354, 321, 346, 337, 326, \
                    350, 329, 317, 343, 355, 306, 357, 367, 349, 340, 352, 363, 333, 374, 336, 325, 377, 328, \
                    341, 380, 344, 382, 324, 348, 339, 386, 379, 332, 389, 335, 391, 359, 369, 387, 396, 373, \
                    398, 358, 368, 378, 362, 403, 365, 375, 384, 393, 361, 371, 364, 356, 383, 392, 360, 370, \
                    353, 381, 405, 376, 414, 422, 388, 404, 366, 413, 421, 402, 372, 411, 419, 400, 408, 416, \
                    424, 431, 420, 401, 395, 435, 418, 399, 407, 394, 409, 446, 390, 406, 385, 415, 423, 397, \
                    442, 438, 450, 440, 458, 412, 443, 439, 457, 430, 464, 460, 456, 429, 436, 448, 455, 428, \
                    410, 447, 454, 427, 434, 417, 453, 426, 433, 445, 482, 425, 432, 444, 451, 487, 459, 449, \
                    471, 477, 289, 10, 493, 475, 481, 441, 469, 494, 476, 452, 488, 465, 461, 467, 473, 479, \
                    485, 491, 502, 437, 504, 501, 463, 516, 500, 486, 515, 474, 480, 522, 519, 524, 513, 462, \
                    468, 520, 525, 514, 527, 512, 490, 530, 511, 484, 537, 510, 478, 540, 466, 472, 288, 10, \
                    548, 10, 97, 549]
        self.assertEqual(tulos, indeksit)

    def test_pura_tiedosto_on_olemassa(self):
        self.purku1.pura()
        on_olemassa = os.path.exists("pakatut/abc.lzw_purettu")
        self.assertEqual(True, on_olemassa)

    def test_aja(self):
        tiedosto = self.pakkaus1.aja()
        self.assertEqual(tiedosto, "pakatut/testi.lzw")
