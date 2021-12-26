import io
import sys
import unittest
import tiedostopakkaus
from unittest.mock import patch

class TestTiedostopakkaus(unittest.TestCase):

	@patch('builtins.input', side_effect=['1', '1', "testitiedostot/abc.txt"])
	def test_main_huffman_pakkaus_abc(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 12 tavua.\nPakatun tiedoston koko: 78 tavua.\nPakkauskoko on 650% alkuperäisestä tiedostosta.\n")

	@patch('builtins.input', side_effect=['1', '1', "testitiedostot/tuksu.txt"])
	def test_main_huffman_pakkaus_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 1402 tavua.\nPakatun tiedoston koko: 923 tavua.\nPakkauskoko on 66% alkuperäisestä tiedostosta.\n")

	@patch('builtins.input', side_effect=['1', '1', "testitiedostot/finnlex.txt"])
	def test_main_huffman_pakkaus_finnlex(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 422884 tavua.\nPakatun tiedoston koko: 232909 tavua.\nPakkauskoko on 55% alkuperäisestä tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '1', "pakatut/abc.hfm"])
	def test_main_huffman_purku_abc(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Purettavan tiedoston koko: 78 tavua.\nPuretun tiedoston koko: 12 tavua.\nTiedostokoko on 15% pakatusta tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '1', "pakatut/tuksu.hfm"])
	def test_main_huffman_purku_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Purettavan tiedoston koko: 923 tavua.\nPuretun tiedoston koko: 1402 tavua.\nTiedostokoko on 152% pakatusta tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '1', "pakatut/finnlex.hfm"])
	def test_main_huffman_purku_finnlex(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Purettavan tiedoston koko: 232909 tavua.\nPuretun tiedoston koko: 422884 tavua.\nTiedostokoko on 182% pakatusta tiedostosta.\n")

	@patch('builtins.input', side_effect=['1', '2', "testitiedostot/abc.txt"])
	def test_main_lempel_pakkaus_abc(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 12 tavua.\nPakatun tiedoston koko: 15 tavua.\nPakkauskoko on 125% alkuperäisestä tiedostosta.\n")

	@patch('builtins.input', side_effect=['1', '2', "testitiedostot/tuksu.txt"])
	def test_main_lempel_pakkaus_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 1402 tavua.\nPakatun tiedoston koko: 441 tavua.\nPakkauskoko on 31% alkuperäisestä tiedostosta.\n")

	@patch('builtins.input', side_effect=['1', '2', "testitiedostot/finnlex.txt"])
	def test_main_lempel_pakkaus_finnlex(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 422884 tavua.\nPakatun tiedoston koko: 184218 tavua.\nPakkauskoko on 44% alkuperäisestä tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '2', "pakatut/abc.lzw"])
	def test_main_lempel_purku_abc(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Purettavan tiedoston koko: 15 tavua.\nPuretun tiedoston koko: 11 tavua.\nTiedostokoko on 73% pakatusta tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '2', "pakatut/tuksu.lzw"])
	def test_main_lempel_purku_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Purettavan tiedoston koko: 441 tavua.\nPuretun tiedoston koko: 1402 tavua.\nTiedostokoko on 318% pakatusta tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '2', "pakatut/finnlex.lzw"])
	def test_main_lempel_purku_finnlex(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Purettavan tiedoston koko: 184218 tavua.\nPuretun tiedoston koko: 422873 tavua.\nTiedostokoko on 230% pakatusta tiedostosta.\n")

	@patch('builtins.input', side_effect=['2', '2', "pakatut/eitiedostoa.lzw", "pakatut/abc.lzw"])
	def test_main_lempel_purku_eitiedostoa(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Tiedostoa ei löytynyt.\nPurettavan tiedoston koko: 15 tavua.\nPuretun tiedoston koko: 11 tavua.\nTiedostokoko on 73% pakatusta tiedostosta.\n")
