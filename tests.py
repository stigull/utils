#! /usr/bin/env python
# -*- coding: utf8 -*-

import unittest

from utils.stringformatting import split_camel, slugify
from utils.dateformatting import get_day_of_week_in_icelandic
from utils.dateformatting import NEFNIFALL, THOLFALL, THAGUFALL, EIGNARFALL

class SplitCamelTestCase(unittest.TestCase):
    def test_not_camelcase(self):
        self.assertEqual(split_camel("rabison"), "rabison")
        self.assertEqual(split_camel("rabisontravis"), "rabisontravis")
        
    def test_camelcase(self):
        self.assertEqual(split_camel("RabisonTravis"), "rabison-travis")
        self.assertEqual(split_camel("Rabison"), "rabison")
        self.assertEqual(split_camel("RabisonTravisGabrai"), "rabison-travis-gabrai")
        
    def test_another_separator(self):
        self.assertEqual(split_camel("RabisonTravis", separator="+"), "rabison+travis")
        
        
class SlugifyTestCase(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify(u"[Jóhann Þorvaldur!]"), u"johann-thorvaldur")
        
class DayOfWeekTestCase(unittest.TestCase):
    def test_nf(self):
        expected_values = [u"mánudagur", u"þriðjudagur", u"miðvikudagur",
                    u"fimmtudagur", u"föstudagur", u"laugardagur", u"sunnudagur"]
                    
        for i, expected_value in enumerate(expected_values):
            self.assertEqual(get_day_of_week_in_icelandic(i,NEFNIFALL), expected_value)

    def test_thf(self):
        expected_values = [u"mánudag", u"þriðjudag", u"miðvikudag",
                            u"fimmtudag", u"föstudag", u"laugardag", u"sunnudag"]
        for i, expected_value in enumerate(expected_values):
            self.assertEqual(get_day_of_week_in_icelandic(i,THOLFALL), expected_value)
  
    def test_thgf(self):
        expected_values = [u"mánudegi", u"þriðjudegi", u"miðvikudegi",
                            u"fimmtudegi", u"föstudegi", u"laugardegi", u"sunnudegi"]
                            
        for i, expected_value in enumerate(expected_values):
            self.assertEqual(get_day_of_week_in_icelandic(i,THAGUFALL), expected_value)                                                      
        
    def test_ef(self):
        expected_values = [u"mánudags", u"þriðjudags", u"miðvikudags",
                            u"fimmtudags", u"föstudags", u"laugardags", u"sunnudags"]
        
        for i, expected_value in enumerate(expected_values):
            self.assertEqual(get_day_of_week_in_icelandic(i,EIGNARFALL), expected_value)                    

if __name__ == '__main__':
    unittest.main()
