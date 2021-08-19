#!/usr/bin/python3

import hashlib
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Granite

import constants as cn

BLOCK_SIZE = 65536
file_hash = hashlib.sha256()

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        context = self.get_style_context()
        context.add_class ("rounded")

        title_label = Gtk.Label(label="Hasher")
        title_label_context = title_label.get_style_context()
        title_label_context.add_class("keycap")

        self.headerbar = Gtk.HeaderBar()
        headerbar_context = self.headerbar.get_style_context()
        headerbar_context.add_class("flat")
        self.headerbar.set_show_close_button(True)
        self.headerbar.set_custom_title(title_label)
        self.set_titlebar(self.headerbar)


        self.home_container = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0, homogeneous = True)

        self.welcome = Granite.WidgetsWelcome (title="Welcome to Hasher", subtitle="Hash your files")
        self.welcome.append ("folder-open", "Open a File", "Open a file to hash it out")
        self.welcome.connect("activated", self.on_welcome_activated)

        self.home_container.pack_start(self.welcome, False, False, 0)

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
                print("File selected: " + dialog.get_filename())

                with open(dialog.get_filename(), 'rb') as f: # Open the file to read it's bytes
                    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
                    while len(fb) > 0: # While there is still data being read from the file
                        file_hash.update(fb) # Update the hash
                        fb = f.read(BLOCK_SIZE) # Read

                print (file_hash.hexdigest())
                self.initial_file_selected()

            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")

            dialog.destroy()

    def initial_file_selected(self):
        self.stack = Gtk.Stack()
        self.stack.add_titled(Gtk.Label(label="Hashes Content"), "Hashes", "Hashes")
        self.stack.add_titled(Gtk.Label(label="Compare Content"), "Compare", "Compare")
        self.stack.add_titled(Gtk.Label(label="Verify Content"), "Verify", "Verify")

        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.has_focus = False
        self.stack_switcher.can_focus = False
        self.stack_switcher.can_default = False
        self.stack_switcher.receives_default = False
        self.stack_switcher.set_stack(self.stack)


        self.home_container.remove(self.welcome)
        self.headerbar.set_custom_title(self.stack_switcher)
        self.home_container.pack_start(self.stack, False, False, 1)
        self.home_container.show_all()
        self.headerbar.show_all()


