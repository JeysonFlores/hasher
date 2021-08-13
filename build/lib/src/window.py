#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk

import constants as cn


class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(
            self, 
            title=cn.App.application_name
        )

        context = self.get_style_context()
        context.add_class ("rounded")

        self.label = Gtk.Label(label="Welcome to Hasher")

        label_conext = self.label.get_style_context()
        label_conext.add_class("h1")

        self.add(self.label)

        self.resize(600, 400)
