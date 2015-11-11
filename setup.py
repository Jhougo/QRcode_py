<<<<<<< HEAD
from distutils.core import setup
import py2exe

setup(console=['QR.py'])
=======
from setuptools import setup

APP = ['QR.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
>>>>>>> origin/master
