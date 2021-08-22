#!/usr/bin/python3

import gi
import os
import locale
import gettext

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

try:
    current_locale, encoding = locale.getdefaultlocale()
    locale_path = os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ), 
        'locale'
    )
    translate = gettext.translation(
        "hasher", 
        locale_path, 
        [current_locale] 
    )
    _ = translate.gettext
except FileNotFoundError:
    _ = str

class App:
    application_shortname = "hasher"
    application_id = "com.github.jeysonflores.hasher"
    application_name = "Hasher"
    application_description = _('Hash your files')
    application_version ="1.0.1"
    app_years = "2021"
    main_url = "https://github.com/JeysonFlores/hasher"
    bug_url = "https://github.com/JeysonFlores/hasher/issues"
    help_url = "https://github.com/JeysonFlores/hasher/issues"
    translate_url = "https://github.com/JeysonFlores/hasher"
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0
