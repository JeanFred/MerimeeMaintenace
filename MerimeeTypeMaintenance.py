# -*- coding: utf-8 -*-

"""Maintenance for the 'type' parameter."""

import re
import pywikibot
import pywikibot.textlib as textlib
from pywikibot import Page, Category
from BaseMerimee import BaseMerimee

site = pywikibot.getSite('commons', 'commons')


class MerimeeTypeMaintenance:

    """Maintenance for the 'type' parameter."""

    def __init__(self):
        self.merimee = BaseMerimee()
        self.merimee.init_from_csv()
        self.template_name = u'Template:Mérimée'

    def get_merimee_id(self, page):
        """Return the Mérimée ID used on the given wikipage."""
        tpls = page.templatesWithParams()
        for (name, args) in tpls:
            if name.title() == self.template_name:
                merimee_id = args[0]
                return merimee_id

    def add_type_to_page(self, page_text, merimee_id):
        """Return the given wikipage text with the type added."""
        mh_item = self.merimee[merimee_id]
        mh_type = mh_item.get('MH_TYPE', None)
        if mh_type:
            template = u"{{Mérimée\|.*?}}"
            new_template = u'{{Mérimée|type=%s|1=%s}}' % (mh_type, merimee_id)
            new_page_text = re.sub(template, new_template, page_text, count=1)
            return new_page_text
        else:
            print "No type, cannot do anything"

    def process_page(self, page):
        """Process the given wikipage."""
        page_text = page.get()
        merimee_id = self.get_merimee_id(page)
        print u"Mérimée ID is %s" % merimee_id
        new_page_text = self.add_type_to_page(page_text, merimee_id)
        print "Replacing type... new text is:"
        print new_page_text

def main():
    """Main method."""
    maintenance = MerimeeTypeMaintenance()
    merimee_category = Category(site, title=u'Mérimée without type parameter')
    pages_generator = merimee_category.articles()
    for page in pages_generator:
    #page = pages_generator.next()
        maintenance.process_page(page)

if __name__ == "__main__":
    main()
