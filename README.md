# Budjetointi sovellus

Sovelluksen avulla käyttäjä pysyy ajantasalla taloudellisesta tilanteestaan.

## Dokumentaatiot
- [Vaatimusmäärittely](dokumentaatiot/vaatimusmaarittely.md)
- [Tyoaikakirjanoito](dokumentaatiot/tyoaikakirjanpito.md)
- [Changelog](dokumentaatiot/changelog.md)
- [Arkkitehtuuri](dokumentaatiot/arkkitehtuuri.md)
# Asennus
1. Varmista että olet sovelluksen juurihakemistossa

2. Asenna riippuvuudet komennolla:

    ```bash
    poetry install
    ```

3.  Alusta tarvittavat tiedostot
    ```bash
    poetry run invoke build
    ```

4. Käynnistä sovellus komennolla:
    ```bash
    poetry run invoke start
    ```

# Laskarit
- [Viikko 1](laskarit/viikko1/viikko1.md)
- [Viikko 2](laskarit/viikko2)
- [Viikko 3](laskarit/viikko3)
