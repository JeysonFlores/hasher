#!/usr/bin/python3

from distutils.core import setup

install_data = [
    ('share/applications', ['data/com.github.jeysonflores.hasher.desktop']),
    ('share/metainfo', ['data/com.github.jeysonflores.hasher.appdata.xml']),
    ('share/icons/hicolor/128x128/apps',['data/com.github.jeysonflores.hasher.svg']),
    ('bin/hasher',['src/constants.py']),
    ('bin/hasher',['src/main.py']),
    ('bin/hasher',['src/MainWindow.py']),
    ('bin/hasher',['src/__init__.py']),
    ('bin/hasher/locale/it_IT/LC_MESSAGES', ['src/locale/it_IT/LC_MESSAGES/hasher.mo']),
    ('bin/hasher/locale/it_IT/LC_MESSAGES', ['src/locale/it_IT/LC_MESSAGES/hasher.po'])
]

setup(  
    name='Hasher',
    version='1.0',
    author='Jeyson Flores',
    description='Hash your files',
    url='https://github.com/JeysonFlores/hasher',
    license='GNU GPL3',
    scripts=['com.github.jeysonflores.hasher'],
    packages=['src'],
    data_files=install_data
)
