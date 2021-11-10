import unittest
from tiedostopakkaus import huffman

class TestMain(unittest.TestCase):
	def setUp(self):
		pass

	def test_huffman(self):
		self.assertEqual(huffman("moi"), "palautus")
