class Silmu:
	""" Puun silmuja kuvaava luokka

    Attributes:
        vasen: vasemman puoleinen alisilmu
        oikea: oikean puoleinen alisilmu
        data:  syötteenä annettu kirjain
    """

	def __init__(self, kirjain, maara):
		""" Luokan muodostaja. Luo uuden Silmun.
        Args:
            kirjain: Silmuun talletettava kirjain.
        """

		self.vasen = None
		self.oikea = None
		self.kirjain = kirjain
		self.maara = maara

	def lisaaLapset(self, vasen, oikea):
		self.vasen = vasen
		self.oikea = oikea
