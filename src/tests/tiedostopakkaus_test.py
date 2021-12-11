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
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 12 tavua.\nPakatun tiedoston koko: 3 tavua.\nPakkauskoko pieneni 75%.\n")

	@patch('builtins.input', side_effect=['1', '1', "testitiedostot/tuksu.txt"])
	def test_main_huffman_pakkaus_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 1395 tavua.\nPakatun tiedoston koko: 658 tavua.\nPakkauskoko pieneni 53%.\n")

	'''
	@patch('builtins.input', side_effect=[2, 1, "pakatut/abc.hfm"])
	def test_main_huffman_purku(self, mock_inputs):
		tiedostopakkaus.main()
    '''
        
	@patch('builtins.input', side_effect=['1', '2', "testitiedostot/abc.txt"])
	def test_main_lempel_pakkaus_abc(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 12 tavua.\nPakatun tiedoston koko: 15 tavua.\nPakkauskoko pieneni -25%.\n")

	@patch('builtins.input', side_effect=['1', '2', "testitiedostot/tuksu.txt"])
	def test_main_lempel_pakkaus_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 1395 tavua.\nPakatun tiedoston koko: 434 tavua.\nPakkauskoko pieneni 69%.\n")

	@patch('builtins.input', side_effect=['2', '2', "pakatut/abc.lzw"])
	def test_main_lempel_purku_abc(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 15 tavua.\nPakatun tiedoston koko: 11 tavua.\nPakkauskoko pieneni -27%.\n")

	@patch('builtins.input', side_effect=['2', '2', "pakatut/tuksu.lzw"])
	def test_main_lempel_purku_tuksu(self, mock_inputs):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		tiedostopakkaus.main()
		sys.stdout = sys.__stdout__
		self.assertEqual(capturedOutput.getvalue(), "Pakattavan tiedoston koko: 434 tavua.\nPakatun tiedoston koko: 1394 tavua.\nPakkauskoko pieneni 221%.\n")

	'''
    # get_input palauttaa arvon '1'
	@patch('yourmodule.get_input', return_value='1')
	def test_pakkaus(self, input):
		self.assertEqual(answer(), 'you entered yes')
    '''
