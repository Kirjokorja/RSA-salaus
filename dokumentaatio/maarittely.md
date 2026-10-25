# Harjoitustyön määrittely

## Aihe

Toteutan ohjelman, joka salaa tekstiä RSA-salausalgoritmillä. Käyttäjä pystyy pyytämään ohjelmalta salausavaimet. Ohjelma tulostaa käyttäjälle julkisen ja yksityisen avainparin. Käyttäjä pystyy salaamaan ohjelmalla tekstipätkän antamalla sille julkisen avaimen ja salattavan viestin. Käyttäjä pystyy purkamaan salatun vietin ohjelmalla antamalla sille viestin salaamiseen käytetyn avainparin yksityisen avaimen ja salatun vietin.

Ohjelma luo salaisen ja julkisen avaimen luomalla satunnaiset alkuluvut p ja q käyttäen Eratostheneen seulaa ja Miller-Rabin-algoritmiä sekä laskemalla luvut e ja d käyttäen laajennettua Eukleideen algoritmiä. Ohjelma säilyttää julkisen ja salaisen avaimen parina, mistä se käyttää julkista avainta tunnistamaan oikean salaisen avaimen mahdollisesti muista luoduista avaimista. 

## Ohjelmointikielet

Rakennan ohjelmani Pythonilla. Pythonin lisäksi minulla on kokemusta Javasta, C#:sta sekä vähän C++:sta.

## Aika- ja tilavaativuus

**Salaamisen aikavaativuus:** O(kn^3), missä n on Miller-Rabinin testaaman luvun bittien määrä ja k testattujen lukujen määrä ennen kuin alkuluku löytyy\
**Salauksen purkamisen aikavaativuus:** O(n), missä n on salatun viestin pituus bitteinä\
**Tilavaativuus molemmissa tapauksissa:** O(n), missä n on salattavan tai purettavan viestin pituus bitteinä

## Käytettävät lähteet

Cormen, Thomas H., Leiserson, Charles E., Rivest, Ronald L. ja Stein, Clifford: *Introduction to Algorithms*, Third Edition, Cambridge, Massachusetts, London, England, 2009, The MIT Press, ISBN 978-0-262-03384-8.

Liu, David ja Badr, Mario: *Foundations of Computer Science, Course Notes for CSC110 and CSC111*, https://www.teach.cs.toronto.edu/~csc110y/fall/notes/.

Bugdani, Tanvi: RSA Algorithm: *Theory and Implementation in Python*, https://www.askpython.com/python/examples/rsa-algorithm-in-python.

Tarkoituksena on myös etsiä asiaan paneutuvia videoita YouTubesta ja katsoa mitä geeksforgeeks.org-sivustolta löytyy.

## Opinto-ohjelma

tietojenkäsittelytieteen kandidaatti (TKT)
