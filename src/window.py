#!/usr/bin/python3

from typing import Tuple
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Granite

import constants as cn


class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        context = self.get_style_context()
        context.add_class ("rounded")

        title_label = Gtk.Label(label="Hasher")
        title_label_context = title_label.get_style_context()
        title_label_context.add_class("keycap")

        self.headerbar = Gtk.HeaderBar()
        self.headerbar.set_show_close_button(True)
        self.headerbar.set_custom_title(title_label)
        self.set_titlebar(self.headerbar)

        self.home_container = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0, homogeneous = True)

        welcome = Granite.WidgetsWelcome (title="Welcome to Hasher", subtitle="Hash your files")
        welcome.append ("folder-open", "Open a File", "Open a file to hash it out")
        welcome.connect("activated", self.on_welcome_activated)

        self.home_container.pack_start(welcome, False, False, 0)

        self.add(self.home_container)

        self.resize(600, 400)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            dialog = Gtk.FileChooserDialog(
                title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
            )

            dialog.add_buttons(
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK,
            )

            response = dialog.run()

            if response == Gtk.ResponseType.OK:
                print("Open clicked")
                print("File selected: " + dialog.get_filename())
            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")

            dialog.destroy()

