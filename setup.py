#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='MerimeeMaintenance',
    version='0.1',
    description='Bot to maintain Merimee stuff on Wikimedia Commons.',
    long_description=open('README.md').read(),
    author='Jean-Frederic',
    author_email='JeanFred@github',
    url='https://commons.wikimedia.org/wiki/COM:MH',
    packages=[''],
    license='GPL',
    install_requires=['Pywikipediabot', 'MassUploadLibrary'],
    dependency_links=['http://pywikipedia.org/nightly/package/pywikipedia-rewrite/pywikipedia-rewrite-nightly.tgz#egg=Pywikipediabot',
                        'https://github.com/JeanFred/MassUploadLibrary/archive/master.tar.gz#egg=MassUploadLibrary'],
    )
