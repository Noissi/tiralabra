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
        indeksit = [84, 228, 109, 228, 32, 111, 110, 32, 116, 101, 115, 116, 105, 263, 101, 107, 266, 105]
        self.assertEqual(tulos, indeksit)

    def test_pakkaa_abc(self):
        tulos = self.pakkaus2.pakkaa()
        indeksit = [97, 98, 99, 10, 97, 260, 97, 10, 98, 98]
        self.assertEqual(tulos, indeksit)

    def test_pakkaa_tuksu(self):
        tulos = self.pakkaus3.pakkaa()
        indeksit = [80, 97, 108, 97, 115, 105, 110, 32, 106, 117, 117, 114, 105, 32, 265, 100, 101, 115, 116, \
                    97, 32, 107, 111, 117, 108, 117, 273, 97, 110, 105, 46, 32, 256, 258, 260, 262, 264, 266, \
                    268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 259, 261, 263, 265, 267, 269, 117, \
                    271, 282, 298, 279, 281, 274, 302, 287, 257, 305, 291, 308, 294, 311, 296, 275, 277, 315, \
                    301, 285, 319, 289, 306, 292, 309, 295, 313, 328, 300, 317, 331, 304, 290, 307, 293, 310, \
                    312, 297, 339, 316, 283, 342, 320, 344, 335, 324, 348, 327, 299, 351, 318, 343, 334, 323, \
                    347, 326, 314, 340, 352, 303, 354, 364, 346, 337, 349, 360, 330, 371, 333, 322, 374, 325, \
                    338, 377, 341, 379, 321, 345, 336, 383, 376, 329, 386, 332, 388, 356, 366, 384, 393, 370, \
                    395, 355, 365, 375, 359, 400, 362, 372, 381, 390, 358, 368, 361, 353, 380, 389, 357, 367, \
                    350, 378, 402, 373, 411, 419, 385, 401, 363, 410, 418, 399, 369, 408, 416, 397, 405, 413, \
                    421, 428, 417, 398, 392, 432, 415, 396, 404, 391, 406, 443, 387, 403, 382, 412, 420, 394, \
                    439, 435, 447, 437, 455, 409, 440, 436, 454, 427, 461, 457, 453, 426, 433, 445, 452, 425, \
                    407, 444, 451, 424, 431, 414, 450, 423, 430, 442, 479, 422, 429, 441, 448, 484, 456, 446, \
                    468, 474, 286, 10, 490, 472, 478, 438, 466, 491, 473, 449, 485, 462, 458, 464, 470, 476, \
                    482, 488, 499, 434, 501, 498, 460, 513, 497, 483, 512, 471, 477, 519, 516, 521, 510, 459, \
                    465, 517, 522, 511, 524, 509, 487, 527, 508, 481, 534, 507, 475, 537, 463, 469, 285]
        self.assertEqual(tulos, indeksit)

    def test_pura_tiedosto_on_olemassa(self):
        self.purku1.pura()
        on_olemassa = os.path.exists("pakatut/abc.lzw_purettu")
        self.assertEqual(True, on_olemassa)

    def test_aja(self):
        tiedosto = self.pakkaus1.aja()
        self.assertEqual(tiedosto, "pakatut/testi.lzw")
