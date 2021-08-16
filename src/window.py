#!/usr/bin/python3

import gi, WelcomeView

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Handy

import constants as cn


class Window(Handy.Window):

    def __init__(self):
        Handy.Window.__init__(
            self, 
            #title=cn.App.application_name
            title="Test"
        )

        context = self.get_style_context()
        context.add_class ("rounded")

        self.title_label = Gtk.Label(label="Welcome to Hasher")
        self.subtitle_label = Gtk.Label(label="Open a file to hash it out")

        title_label_context = self.title_label.get_style_context()
        title_label_context.add_class("h1")

        subtitle_label_context = self.subtitle_label.get_style_context()
        subtitle_label_context.add_class("h2")
        subtitle_label_context.add_class("dim-label")

        self.home_container = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0, homogeneous = True)
        self.home_container.pack_start(self.title_label, False, False, 0)
        self.home_container.pack_start(self.subtitle_label, False, False, padding = 0)

        #self.add(self.home_container)

        self.add(WelcomeView.WelcomeView())

        self.resize(600, 400)
