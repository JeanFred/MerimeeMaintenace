# -*- coding: utf-8 -*-

"""Dictionary wrapper of the Base Mérimée."""

import UserDict
import csv
import sys
import codecs
sys.path.append('../MassUploadLibrary')
from uploadlibrary import UnicodeCSV


class BaseMerimee(UserDict.UserDict):

    """Dictionary-like wrapper of the Base Mérimée."""

    def __init__(self, data={}, **kw):
        UserDict.UserDict.__init__(self)
        self.update(data)
        self.update(kw)

    def __add__(self, other):
        dict = BaseMerimee(self.data)
        dict.update(b)
        return dict

    def init_from_csv(self, csv_file='data/merimee-MH.csv'):
        """Initialise the base with the CSV file."""
        self.update(parse_Merimee_csv(csv_file))


def parse_Merimee_csv(csv_file):
    """Return the Mérimée database (as a dictionary) from the given CSV file."""
    file_handler = codecs.open(csv_file, 'r', 'latin-1')
    dataset = {}
    csvReader = UnicodeCSV.unicode_csv_dictreader(file_handler,
                                                  delimiter=';')
    try:
        for row in csvReader:
            merimee_id = row['REF']
            dataset[merimee_id] = handle_Merimee_csv_row(row)
    except csv.Error, e:
        sys.exit('file %s, line %d: %s' % (csv_file,
                                           csvReader.line_num, e))
    return dataset


def handle_Merimee_csv_row(csv_row):
    """Return a Mérimée dictionary enriched."""
    ppro = csv_row['PPRO']
    mh_type = None
    if 'classement' in ppro:
        mh_type = "classe"
    elif 'inscription' in ppro:
        mh_type = "inscrit"
    else:
        mh_type = None
    csv_row['MH_TYPE'] = mh_type
    return csv_row
