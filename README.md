<p align="center">
  <img src="https://github.com/JeysonFlores/hasher/blob/main/data/assets/icons/128x128/com.github.jeysonflores.hasher.svg" alt="Icon" />
</p>
<h1 align="center">Hasher</h1>
<h4 align="center">Hash, Compare and Verify your files</h4>

<p align="center">
  <a href="https://appcenter.elementary.io/com.github.jeysonflores.hasher"><img src="https://appcenter.elementary.io/badge.svg" alt="Get it on AppCenter" /></a>
</p>

<p align="center">
  <a href="https://github.com/fleury08/prettifier/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL3.0-blue.svg?style=for-the-badge">
  </a>
  <a href="https://github.com/fleury08/prettifier/releases">
    <img src="https://img.shields.io/badge/Release-v%201.0.2-blue.svg?style=for-the-badge">
  </a>
</p>

| ![Screenshot](https://github.com/JeysonFlores/hasher/blob/main/data/assets/screenshots/screenshot-1.png) | ![Screenshot](https://github.com/JeysonFlores/hasher/blob/main/data/assets/screenshots/screenshot-2.png) |
|------------------------------------------------------------------|------------------------------------------------------------------|
| ![Screenshot](https://github.com/JeysonFlores/hasher/blob/main/data/assets/screenshots/screenshot-3.png) | ![Screenshot](https://github.com/JeysonFlores/hasher/blob/main/data/assets/screenshots/screenshot-4.png) |


# Translations
In order to translate Hasher to a language you must add a folder with the language abbreviation (Example: **es**-Spanish, **pt**-Portuguese, **it**-Italian) 
on the po/ directory. Inside it you must create another folder called LC_MESSAGES. Inside that last folder, you must add two files: one called hasher.po(text file) and the compiled hasher.mo file (Your .PO editor should generate this file automatically).
Once you have done that, you must add those files to setup.py for installation. To do so, gotta add this to the install_data tuple:

`('bin/hasher/locale/LANG_ABBREVIATION/LC_MESSAGES', ['po/LANG_ABBREVIATION/LC_MESSAGES/hasher.mo'])`

`('bin/hasher/locale/LANG_ABBREVIATION/LC_MESSAGES', ['po/LANG_ABBREVIATION/LC_MESSAGES/hasher.po'])`

# Dependencies
  - `granite (>= 0.6.0)`
  - `libgtk-3-dev (>= 3.10)`
  - `python3 (>= 3.6)`
  - `python3-gi (3.36.0-1)`
  -  `gettext`

# Building
  ```
    git clone https://github.com/JeysonFlores/hasher.git
    cd hasher
    flatpak-builder build com.github.jeysonflores.hasher.yml --user --install --force-clean
  ```
  
 # Contributions
  ## Code 
   -  [Vishal Rao](https://github.com/vjr) - Accessibility enhancements
  ## Design
   -  [Vishal Rao](https://github.com/vjr) - Accessibility enhancements
  ## Translations
   - 🇪🇸 - 🇲🇽 Spanish Translation by [Jeyson Antonio Flores Deras](https://github.com/JeysonFlores)
# Extras
   - Thanks to [Mirko Brombin](https://github.com/mirkobrombin) for the [template](https://github.com/mirkobrombin/ElementaryPython).
