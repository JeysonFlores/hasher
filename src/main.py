#!/usr/bin/python3

import gi
import os, sys

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Gio, Granite, Gdk

import MainWindow as wn
import constants as cn

class Application(Gtk.Application):

    def do_activate(self):

        self.win = wn.MainWindow()
        self.win.connect("delete-event", self.delete_window)

        granite_settings = Granite.Settings.get_default()
        gtk_settings = Gtk.Settings.get_default ()

        #Since complex signals in Python are quite complicated, Dark Mode is determined at launch time(may change later)
        if granite_settings.get_prefers_color_scheme() == Granite.SettingsColorScheme.DARK:
            gtk_settings.set_property("gtk-application-prefer-dark-theme", True) 

        launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        if launch_dir == "/usr/bin":
            modules_path = "/usr/share/com.github.jeysonflores.hasher/hasher"
        else:
            modules_path = "/build/files/bin/hasher"

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path(modules_path + "/style.css")
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        #self.settings = Gio.Settings(schema_id="com.github.jeysonflores.hasher")
        #self.win.move(self.settings.get_int("pos-x"), self.settings.get_int("pos-y"))
        #self.win.resize(self.settings.get_int("window-width"), self.settings.get_int("window-height"))
        self.win.show_all()

        Gtk.main()

    def delete_window(self, window, event):
        #self.settings.set_int("pos-x", self.win.get_position().root_x)
        #self.settings.set_int("pos-y", self.win.get_position().root_y)

        #self.settings.set_int("window-width", self.win.get_size().width)
        #self.settings.set_int("window-height", self.win.get_size().height)
        
        Gtk.main_quit()

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
