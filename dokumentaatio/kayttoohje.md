# Käyttöohje

### Ohjelman asennus

Riippuvuuksien asentaminen
```
poetry install
```

### Ohjelman käyttö

1. Aja sovellus komennolla
```
poetry run invoke start
```

2. Tämän jälkeen sovellus kysyy, haluatko pakata vai purkaa tiedoston.
```
Haluatko pakata vai purkaa tiedoston?
1 = pakkaa
2 = pura
> 2
```

3. Valitse algoritmi.
```
Valittava algoritmi:
1 = Huffman
2 = Lempel-Ziv
> 1
```

4. Anna polku tiedostoon.
```
Anna polku purettavaan tiedostoon.
> polku/tiedosto.txt
```

Ohjelma kertoo puretun / pakatun tiedoston koon.
```
Purettavan tiedoston koko: 32249 tavua.
Puretun tiedoston koko: 57224 tavua.
Tiedostokoko on 177% pakatusta tiedostosta.
```
