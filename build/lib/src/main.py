#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Gio, Granite

import MainWindow as wn
import constants as cn

import hashlib

class Application(Gtk.Application):

    def do_activate(self):

        self.win = wn.MainWindow()
        self.win.connect("delete-event", Gtk.main_quit)

        granite_settings = Granite.Settings.get_default()
        gtk_settings = Gtk.Settings.get_default ()

        #This snippet doesn't work
        if granite_settings.get_prefers_color_scheme == Granite.SettingsColorScheme.DARK:
            gtk_settings.set_property("gtk-application-prefer-dark-theme", True)  #

        self.win.show_all()

        Gtk.main()

    def pref_color_scheme(self):
        pass

app = Application()

app.application_id = cn.App.application_id
app.flags = Gio.ApplicationFlags.FLAGS_NONE
app.program_name = cn.App.application_name
app.build_version = cn.App.application_version
app.about_comments = cn.App.about_comments
app.app_years = cn.App.app_years
app.build_version = cn.App.application_version
app.app_icon = cn.App.application_id
app.main_url = cn.App.main_url
app.bug_url = cn.App.bug_url
app.help_url = cn.App.help_url
app.translate_url = cn.App.translate_url


def start():
    app.run("")
