# ignore this file
from distutils.core import setup
import py2exe

data_files = [('assets', ['assets/logo_spamFilter.png']),]
setup(
    data_files = data_files,
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    # windows = [{'script': "app.py"}],
    zipfile = None,
    console=['app.py']) 