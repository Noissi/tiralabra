# Toteutusdokumentti

### Ohjelman yleisrakenne

Tiedostossa huffman.py toteutetaan Huffmanin algoritmi Huffman-luokan avulla. Tiedostossa lempelziv.py toteutetaan Lempel-Ziv-Welch-algoritmi luokan Lempelziv avulla. Molemmissa luokissa varsinainen pakkaus tapahtuu pakkaa-metodissa. Algoritmien toteutus noudattaa melko pitkälti alkuperäisissä artikkeleissa (Lähteet) kuvattuja toteutuksia.
    
### Vertailu

### Puutteet ja parannusehdotukset

Pythonilla pakkausalgoritmien toteutusta vaikeuttaa se, ettei Pythonissa ole mitään helppoa tapaa tallentaa tiedostoihin yksittäisiä bittejä tai bittiryhmiä, joiden pituus ei ole jaollinen kahdeksalla, joten kaikki bitit pitää tallentaa tiedostoon tavuina. Tämän vuoksi koodissa pitää ensin yhdistää tallennettavat bitit pidemmäksi pätkäksi, joka sitten tallennetaan tiedostoon tavuina.

### Lähteet

Huffman, D. A. (1952). A method for the construction of minimum-redundancy codes. Proceedings of the IRE, 40(9), 1098-1101.

Ziv, J., & Lempel, A. (1977). A universal algorithm for sequential data compression. IEEE Transactions on information theory, 23(3), 337-343.
