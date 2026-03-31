sequenceDiagram
    participant M as main-function
    participant LH as laitehallinto: HKLLaitehallinto
    participant K as lippu_luukku: Kioski
    participant MK as kallen_kortti: Matkakortti
    participant LL as rautatietori: Lataajalaite
    participant R6 as ratikka6: Lukijalaite
    participant B244 as bussi244: Lukijalaite
    
    Note over M, B244: Alustaa
    M->>LH: lisaa_lataaja(rautatietori)
    M->>LH: lisaa_lukija(ratikka6)
    M->>LH: lisaa_lukija(bussi244)

    M->>K: osta_matkakortti("Kalle")
    K-->>MK: Matkakortti("Kalle")
    K-->>M: kallen_kortti

    M->>LL: lataa_arvoa(kallen_kortti, 3)
    LL->>MK: kasvata_arvoa(3)
    
    Note over M, MK: Lipun osto (Ratikka, hinta 1.5)
    M->>R6: osta_lippu(kallen_kortti, 0)
    R6->>MK: vahenna_arvoa(1.5)
    R6-->>M: True

    M->>B244: osta_lippu(kallen_kortti, 2)
    Note right of B244: Arvo (1.5) < hinta (3.5)
    B244-->>M: False