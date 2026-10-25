# Aineopintojen harjoitustyö: Algoritmit ja tekoäly

## Dokumentaatio

- [Määrittelyasiakirja](dokumentaatio/maarittely.md)
- [Testausasiakirja](dokumentaatio/testaus.md)
- [Toteutusasiakirja](dokumentaatio/toteutus.md)

## Viikkoraportit

- [Viikkoraportti 1](dokumentaatio/viikkoraportit/viikkoraportti1.md)
- [Viikkoraportti 2](dokumentaatio/viikkoraportit/viikkoraportti2.md)
- [Viikkoraportti 3](dokumentaatio/viikkoraportit/viikkoraportti3.md)
- [Viikkoraportti 4](dokumentaatio/viikkoraportit/viikkoraportti4.md)
- [Viikkoraportti 5](dokumentaatio/viikkoraportit/viikkoraportti5.md)
- [Viikkoraportti 6](dokumentaatio/viikkoraportit/viikkoraportti6.md)

## Sovelluksen käyttö

### Alkutoimet

1. Varmista, että koneellasi on asennettuna `Python`-versio `3.12`.
2. Varmista, että koneellasi on asennettuna vähintään `Poetry`-versio `2.0.0`.
3. Vedä RSA-salaus-projekti etärepositoriosta koneellesi.

### Asennus ja ajo

1. Asenna riippuvuudet käskyllä:

```bash
poetry install
```

3. Käynnistä sovellus käskyllä*:

```bash
poetry run invoke start
```

*`Windows`-käyttöjärjestelmällä ohjelma kannattaa ajaa suoraan komennolla `poetry run python3 src/index.py`, koska Invoke vaikuttaa takkuilevan Windowsin komentorivikäyttöliittymää käyttävien ohjelmien kanssa.

### Käyttö

Kun ajat ohjelman tulostaa se komentoriville ohjeet käytöstä. Voit pyytää ohjelmaa luomaan itsellesi salausavainparin syöttämällä ohjelmalle kirjaimen `a`, salaamaan tekstipätkän syöttämällä `s` ja purkamaan viestin salauksen syöttämällä `p`. Salatessa ohjelma pyytää julkisen avaimen kaksi osaa yksi kerrallaan ja lopuksi pyytää kirjoittamaan salattavan viesti. Salausta purettaessa ohjelma toimii samalla tavalla yksityisen avaimen osalta ja lopuksi pytää kirjoittamaan purettavan viestin. Purettavan viestin tulee olla kokonaislukumuodossa, jossa ohjelma sen tulosti salattaessa.

### Testaus

Voit ajaa testit käskyllä:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuuskertomuksen voi muodostaa käskyllä:

```bash
poetry run invoke coverage-report
```

### Koodin muotoileminen

Lähdekoodin voi muotoilla käskyllä:

```bash
poetry run invoke format-code
```

### Koodin laaduntarkastus

Koodin laadun voi tarkistaa käskyllä:

```bash
poetry run invoke lint
```
