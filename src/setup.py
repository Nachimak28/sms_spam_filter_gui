from distutils.core import setup
import py2exe

data_files = [('assets', ['assets/logo_spamFilter.png']),]
setup(
    data_files = data_files,
    console=['app.py']) 