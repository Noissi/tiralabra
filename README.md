# Tiralabra

#### Tiedostonpakkaus

Tiralabra-kurssin algoritmityö.

### Dokumentaatio

* [Käyttöohje](https://github.com/Noissi/tiralabra/blob/master/dokumentaatio/kayttoohje.md)

* [Määrittelydokumentti](https://github.com/Noissi/tiralabra/blob/master/dokumentaatio/maarittely.md)

* [Toteutusdokumentti](https://github.com/Noissi/tiralabra/blob/master/dokumentaatio/toteutus.md)

* [Testausdokumentti](https://github.com/Noissi/tiralabra/blob/master/dokumentaatio/testaus.md)

### Viikkoraportit

* [Viikko 1](https://github.com/Noissi/tiralabra/blob/master/viikkoraportit/viikko1.md)

* [Viikko 2](https://github.com/Noissi/tiralabra/blob/master/viikkoraportit/viikko2.md)

* [Viikko 3](https://github.com/Noissi/tiralabra/blob/master/viikkoraportit/viikko3.md)

* [Viikko 4](https://github.com/Noissi/tiralabra/blob/master/viikkoraportit/viikko4.md)

* [Viikko 5](https://github.com/Noissi/tiralabra/blob/master/viikkoraportit/viikko5.md)

### Asennus

Lataa projektin viimeisin [release](https://github.com/Noissi/tiralabra/releases): _Assets_ -> _Source code_.

1. Riippuvuuksien asentaminen
```
poetry install
```

2. Sovelluksen ajaminen
```
poetry run invoke start
```
Anna polku pakattavaan tiedostoon, esimerkiksi:
```
polku/tiedosto.txt
```

Valitse pakkausalgoritmi 1: Huffman, 2: Lempel-Ziv, esimerkiksi:
```
1
```

### Testaus
Testien suorittaminen
```
poetry run invoke test
```
Testikattavuusraportti
```
poetry run invoke coverage-report
```

### Pylint
.pylintrc-tiedoston tarkistusten suorittaminen:
```
poetry run invoke lint
```

:chicken:
