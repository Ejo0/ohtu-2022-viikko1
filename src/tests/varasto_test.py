import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(10, 3)
        self.negatiivinen_tilavuus = Varasto(-5)
        self.negatiivinen_saldo = Varasto(10, -5)
        self.ylitaytetty = Varasto(10, 15)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_tilavuus_ei_voi_olla_negatiivinen(self):
        self.assertAlmostEqual(self.negatiivinen_tilavuus.tilavuus, 0)

    def self_saldo_ei_voi_olla_negatiivinen(self):
        self.varasto2.ota_varastosta(8)
        self.assertAlmostEqual(self.varasto2.saldo, 0)
        self.assertAlmostEqual(self.negatiivinen_saldo.saldo, 0)

    def test_varaston_saldo_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.ylitaytetty.saldo, 10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivisen_lisays_ei_muuta_saldoa(self):
        self.varasto2.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto2.saldo, 3)

    def test_negatiivisen_otto_palauttaa_nollan_eika_muuta_saldoa(self):
        maara = self.varasto2.ota_varastosta(-2)
        self.assertAlmostEqual(maara, 0)
        self.assertAlmostEqual(self.varasto2.saldo, 3)

    def test_ylisuuri_nosto_nostaa_saldon_verran(self):
        maara = self.varasto2.ota_varastosta(7)
        self.assertAlmostEqual(maara, 3)
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_merkkijonotulosteen_tiedot_oikein(self):
        merkkijono = str(self.varasto2)
        oikea = "saldo = 3, vielä tilaa 77"
        self.assertEqual(merkkijono, oikea)
