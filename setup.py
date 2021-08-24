#!/usr/bin/python3
import sys
from distutils.core import setup
from distutils.command.install import install as _install

def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'build-aux/post_install.py'])

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="- Running post-installation script")

install_data = [
    ('share/applications', ['data/com.github.jeysonflores.hasher.desktop']),
    ('share/metainfo', ['data/com.github.jeysonflores.hasher.appdata.xml']),
    ('share/icons/hicolor/128x128/apps',['data/assets/icons/128x128/com.github.jeysonflores.hasher.svg']),
    ('share/icons/hicolor/64x64/apps',['data/assets/icons/64x64/com.github.jeysonflores.hasher.svg']),
    ('share/icons/hicolor/48x48/apps',['data/assets/icons/48x48/com.github.jeysonflores.hasher.svg']),
    ('share/icons/hicolor/32x32/apps',['data/assets/icons/32x32/com.github.jeysonflores.hasher.svg']),
    ('share/icons/hicolor/24x24/apps',['data/assets/icons/24x24/com.github.jeysonflores.hasher.svg']),
    ('share/icons/hicolor/16x16/apps',['data/assets/icons/16x16/com.github.jeysonflores.hasher.svg']),
    ('share/glib-2.0/schemas', ["data/com.github.jeysonflores.hasher.gschema.xml"]),
    ('share/contractor', ["data/com.github.jeysonflores.hasher.contract"]),
    ('bin/hasher',['data/style.css']),
    ('bin/hasher',['src/constants.py']),
    ('bin/hasher',['src/main.py']),
    ('bin/hasher',['src/HashView.py']),
    ('bin/hasher',['src/MainWindow.py']),
    ('bin/hasher',['src/__init__.py'])
]

setup(  
    name='Hasher',
    version='1.0.1',
    author='Jeyson Flores',
    description='Hash your files',
    url='https://github.com/JeysonFlores/hasher',
    license='GNU GPL3',
    scripts=['com.github.jeysonflores.hasher'],
    packages=['src'],
    data_files=install_data,
    cmdclass={'install': install}
)
