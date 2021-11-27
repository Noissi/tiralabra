class Jono:
    """ Jonorakennetta kuvaava luokka
        Määritteet:
            jono: Jonorakenne
    """

    def __init__(self):
        """ Luokan muodostaja. Luo uuden Jonon.
        """

        self.jono = []

    def onTyhja(self):
        """ Tarkistaa onko jono tyhja.
        """

        return self.jono == []

    def pituusYksi(self):
        """ Tarkistaa onko jonon pituus yksi.
        """

        return len(self.jono) == 1

    def lisaaJonoon(self, lisa):
        """ Lisää jonoon parametrin annetun termin.
            Parametrit:
                lisa: Jonoon lisattava termi.
        """

        self.jono.append(lisa)

    def poistaJonosta(self):
        """ Poistaa jonosta ensimmäisenä olevan termin.
        """

        return self.jono.pop(0)
