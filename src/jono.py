class Jono:

	def __init__(self):
		self.jono = []

	# Tarkista onko jono tyhja
	def onTyhja(self):
		return self.jono == []

	def pituusYksi(self):
		return len(self.jono) == 1

	def lisaaJonoon(self, lisa):
		self.jono.append(lisa)

	def poistaJonosta(self):
		return self.jono.pop(0)
