import sys
from huffman import Huffman

def main():
	tiedosto = sys.argv[1]
	print(tiedosto)
	jotain = pakkausvertailu(tiedosto)
	print(jotain)

def pakkausvertailu(tiedosto):
	huffman = Huffman(tiedosto)
	huffman.aja()
	return huffman

main()
