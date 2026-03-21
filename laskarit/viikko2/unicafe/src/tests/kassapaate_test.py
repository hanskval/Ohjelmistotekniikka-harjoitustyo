import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassapaate_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_syo_edullisesti_kateisella_toimii_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_syo_maukkaasti_kateisella_toimii_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_edullisesti_kateisella_ei_riita_rahaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_kateisella_ei_riita_rahaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_toimii_oikein(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_toimii_oikein(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_syo_edullisesti_kortilla_ei_riita_rahaa(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_syo_maukkaasti_kortilla_ei_riita_rahaa(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_lataa_rahaa_kortille_toimii_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)

        self.assertEqual(kortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
        
    def test_lataa_rahaa_kortille_negatiivinen_summa_ei_muuta_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)

        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)