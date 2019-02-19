from setuptools import setup
from pathlib import Path
import os

home = str(Path.home())


requirements = [
    'beautifulsoup4==4.7.1',
    'click==7.0',
    'requests==2.21.0',
    'toml==0.10.0',
    'maya==0.6.1',
    'tzlocal==1.5.1'
]

setup(
    name='timetracker',
    version='0.2.1',
    description='A command-line utility to load hours in BairesDev Time tracker.',
    url='https://github.com/eyscode/timetracker/',
    author='Eysenck Gómez',
    author_email='eysenck.gomez@gmail.com',
    py_modules=['load_tt'],
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        load-tt=load_tt:load_tt
    ''',
    data_files=[(os.path.join(home, '.timetracker'), ['config.toml'])]
)
