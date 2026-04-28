# Budjetointi sovellus

Sovelluksen avulla käyttäjä pysyy ajantasalla taloudellisesta tilanteestaan.

## Dokumentaatiot
- [Vaatimusmäärittely](dokumentaatiot/misc/vaatimusmaarittely.md)
- [Tyoaikakirjanoito](dokumentaatiot/misc/tyoaikakirjanpito.md)
- [Changelog](dokumentaatiot/misc/changelog.md)
- [Arkkitehtuuri](dokumentaatiot/misc/arkkitehtuuri.md)
- [Käyttoohje](dokumentaatiot/misc/kayttoohje.md)
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

# Testit

1. Pylint testin voi suorittaa komennolla:

    ```bash
    poetry run invoke lint
    ```
    ja testikattavuus raportin
    ```bash
    poetry run invoke coverage-report
    ```


# Laskarit
- [Viikko 1](laskarit/viikko1/viikko1.md)
- [Viikko 2](laskarit/viikko2)
- [Viikko 3](laskarit/viikko3)
