import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        
    def test_rahan_otto_toimii_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.5)
        
    def test_saldo_ei_muutu_jos_rahaa_ei_riita(self):
        self.maksukortti = Maksukortti(100)
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(self.maksukortti.saldo_euroina(), 1.0)
        
    def test_palauttaa_true_jos_rahaa_riittaa(self):
        vastaus = self.maksukortti.ota_rahaa(250)
        self.assertTrue(vastaus)
        
    def test_palauttaa_false_jos_rahaa_ei_riita(self):
        self.maksukortti = Maksukortti(100)
        vastaus = self.maksukortti.ota_rahaa(400)
        self.assertFalse(vastaus)
    