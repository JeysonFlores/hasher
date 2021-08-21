#!/usr/bin/python3
import os, sys
from distutils.core import setup
from distutils.command.install import install as _install

def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'post_install.py'])

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")

install_data = [
    ('share/applications', ['data/com.github.jeysonflores.hasher.desktop']),
    ('share/metainfo', ['data/com.github.jeysonflores.hasher.appdata.xml']),
    ('share/icons/hicolor/128x128/apps',['data/com.github.jeysonflores.hasher.svg']),
    ('share/glib-2.0/schemas', ["data/com.github.jeysonflores.hasher.gschema.xml"]),
    ('bin/hasher',['data/style.css']),
    ('bin/hasher',['src/constants.py']),
    ('bin/hasher',['src/main.py']), #/usr/share/glib-2.0/schemas
    ('bin/hasher',['src/HashView.py']),
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
    data_files=install_data,
    cmdclass={'install': install}
)
