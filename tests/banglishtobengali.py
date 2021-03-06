# coding=utf-8
from unittest import TestCase
from bnbphoneticparser import BanglishToBengali


class TestBanglishToBengali(TestCase):

    def test_banglish_to_bengali_parse(self):
        b2b = BanglishToBengali()
        self.assertEqual(b2b.parse("f"), "ফ")
        self.assertEqual(b2b.parse("muRi"), "মুড়ি")
        self.assertEqual(b2b.parse("AmAr"), "আমার")
        self.assertEqual(b2b.parse("AmAr poran"), "আমার পরান")
        self.assertEqual(b2b.parse("mn val nei"), "মন ভাল নেই")

