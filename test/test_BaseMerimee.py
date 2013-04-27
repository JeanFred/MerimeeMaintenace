"""Test BaseMerimee.py."""

import unittest
import os.path
from BaseMerimee import BaseMerimee, handle_Merimee_csv_row, parse_Merimee_csv


class TestBaseMerimee(unittest.TestCase):

    """Base class for testing BaseMerimee related methods."""

    @classmethod
    def setUpClass(cls):
        cls.csv_file = os.path.join(os.path.dirname(__file__),
                                    'data', 'merimee-MH-10.csv')

        cls.merimee_row = {'ADRS': u'Dans le cimeti\xe8re',
                           'LOCA': u'Champagne-Ardenne ; Aube ; Aix-en-Othe',
                           'SCLE': u'15e si\xe8cle ; 16e si\xe8cle',
                           'COM': u'Aix-en-Othe',
                           'ETUD': u'Recensement immeubles MH',
                           'STAT': u'Propri\xe9t\xe9 de la commune',
                           'PPRO': u'Chapelle Saint-Avit (cad. AC 4) : inscription par arr\xeat\xe9 du 28 janvier 1975',
                           'DPT': u'10',
                           'INSEE': u'10003',
                           'AUTR': u'',
                           'AFFE': u'',
                           'REF': u'PA00078014',
                           'REG': u'Champagne-Ardenne',
                           'TICO': u'Chapelle Saint-Avit'}
        cls.merimee_row_enriched = cls.merimee_row.copy()
        cls.merimee_row_enriched['MH_TYPE'] = 'inscrit'

    def test_handle_Merimee_csv_row(self):
        """Test handle_Merimee_csv_row()."""
        result = handle_Merimee_csv_row(self.merimee_row)
        self.assertEqual(result, self.merimee_row_enriched)

    def test_parse_Merimee_csv(self):
        result = parse_Merimee_csv(self.csv_file)
        self.assertEqual(result['PA00078014'], self.merimee_row_enriched)
