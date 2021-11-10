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
