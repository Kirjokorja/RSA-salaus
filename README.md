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

## Sovelluksen käyttö

### Alkutoimet

1. Varmista, että koneellasi on asennettuna `Python`-versio `3.12`.
2. Varmista, että koneellasi on asennettuna vähintään `Poetry`-versio `2.0.0`.
3. Vedä RSA-salaus-projekti etärepositoriosta koneellesi.

### Asennus

1. Asenna riippuvuudet käskyllä:

```bash
poetry install
```

3. Käynnistä sovellus käskyllä:

```bash
poetry run invoke start
```

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
