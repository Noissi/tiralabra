class Silmu:
    """ Puun silmuja kuvaava luokka
        Määritteet:
            vasen: Vasemman puoleinen alisilmu
            oikea: Oikean puoleinen alisilmu
            kirjain: Syötteenä annettu kirjain
            maara: Syötteenä annettu kirjaimen määrä tekstissä
    """

    def __init__(self, kirjain, maara):
        """ Luokan muodostaja. Luo uuden Silmun.
            Parametrit:
                kirjain: Silmuun talletettava kirjain
                maara: Kirjaimen määrä tekstissä
        """

        self.vasen = None
        self.oikea = None
        self.kirjain = kirjain
        self.maara = maara

    def lisaaLapset(self, vasen, oikea):
        """ Lisää silmulle lapsiksi parametreina annetut silmut.
            Parametrit:
                vasen: Silmu
                oikea: Silmu
        """

        self.vasen = vasen
        self.oikea = oikea
