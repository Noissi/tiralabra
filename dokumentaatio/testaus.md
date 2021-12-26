# Testausdokumentti

Ohjelmaa testataan kattavilla yksikkö- ja integraatiotesteillä.

Testauksessa tullaan huomioimaan, että pakatun tiedoston koko on odotusten mukainen ja se purkautuu alkuperäiseksi.

### Testikattavuus

Sovelluksen haarautumakattavuus on 98%.

![](./kuvat/testikattavuus.png)

### Yksikkötestaus

Ohjelmaa on testattu kattavilla yksikkötesteillä, joissa on käytetty useita erilaisia ja kokoisia tekstitiedostoja. Testitiedostot kattavat ainakin yleisimmät poikkeustapaukset, jotka on otettu myös algoritmeissa huomioon.

Testeissä on tarkasteltu sekä lopputulosta (ohjelman tulostusta) että puurakennetta (Huffman) ja indeksejä (Lempel-Ziv).

### Järjestelmätestaus

Automaattisten testien lisäksi ohjelmaa on testattu manuaalisesti ongelmien havaitsemiseksi. Käyttöohje ja vaatimusmäärittely on otettu huomioon testauksessa. Ohjelmassa ei ole huomioitu käyttäjän virhesyötteitä (paitsi virheellinen tiedostonimi), vaan on keskitytty algoritmien toimintaan ja testaukseen.

Pakkauksen ja purkamisen onnistumista on tarkasteltu myös vertaamalla saatuja tuloksia yleisesti saatuihin arvoihin.

Pakkausalgoritmeja on testattu useilla esimerkkitekstitiedostoilla, jotka löytyvät kansiosta [testitiedostot](https://github.com/Noissi/tiralabra/blob/master/testitiedostot).
