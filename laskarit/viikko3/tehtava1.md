```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila

    Pelilauta "1" -- "40" Ruutu

    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Ruutu "1" -- "1" Aloitusruutu
    Ruutu "1" -- "1" Vankila
    Ruutu "1" -- "1" Sattuma_ja_yhteismaa
    Ruutu "1" -- "1" Asemat_ja_laitokset
    Ruutu "1" -- "1" Normaalit_kadut : nimi

    Normaalit_kadut "1" -- "4" Talo
    Normaalit_kadut "1" -- "1" Hotelli

    Pelinappula "1" -- "1" Pelaaja

    Sattuma_ja_yhteismaa "1" -- "0..*" Kortti : Toiminto
    
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "1" -- "0..*" Normaalit_kadut : omistaa
    
   


```