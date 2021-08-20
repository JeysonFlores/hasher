#!/usr/bin/python3

import hashlib
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Granite

import constants as cn
import HashView 

BLOCK_SIZE = 65536
file_hash = hashlib.sha384()

hash_algorythms = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        context = self.get_style_context()
        context.add_class ("rounded")

        self.stack = Gtk.Stack()

        self.hashes_content = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0, homogeneous = False)
        hashes_content_context = self.hashes_content.get_style_context()
        hashes_content_context.add_class("uwu")

        self.hashes_select_file = Gtk.Button(label="Select File",image=Gtk.Image(icon_name="document-open-symbolic", icon_size=Gtk.IconSize.BUTTON), always_show_image=True) #leb
        hashes_select_file_context = self.hashes_select_file.get_style_context()
        hashes_select_file_context.add_class("suggested-action")
        self.hashes_content.pack_start(self.hashes_select_file, False, False, 0)

        self.hashes_alg_combo = Gtk.ComboBoxText()

        algorythms = [
            "MD5",
            "SHA1",
            "SHA224",
            "SHA256",
            "SHA384",
            "SHA512",
        ]

        for algorythm in algorythms:
            self.hashes_alg_combo.append_text(algorythm)

        self.hashes_alg_combo.set_active(0)
        self.hashes_content.pack_start(self.hashes_alg_combo, False, True, 1)

        self.hashes_start = Gtk.Button(label="Hash!")
        self.hashes_content.pack_start(self.hashes_start, False, True, 2)

        self.hashes_result = HashView.HashView() #leb
        self.hashes_result.alg_label.set_label("Hash")
        self.hashes_content.pack_start(self.hashes_result, False, True, 1)

        self.stack.add_titled(self.hashes_content, "Hashes", "Hashes")
        self.stack.add_titled(Gtk.Label(label="Compare Content"), "Compare", "Compare")
        self.stack.add_titled(Gtk.Label(label="Verify Content"), "Verify", "Verify")

        

        self.compare_select_file = Gtk.Button(label="Select File")
        self.verify_select_file = Gtk.Button(label="Select File")




        self.stack_switcher = Gtk.StackSwitcher(receives_default=False)
        self.stack_switcher.set_stack(self.stack)

        self.headerbar = Gtk.HeaderBar()
        headerbar_context = self.headerbar.get_style_context()
        headerbar_context.add_class("flat")
        self.headerbar.set_show_close_button(True)
        self.headerbar.set_custom_title(self.stack_switcher)
        self.set_titlebar(self.headerbar)
        
        self.add(self.stack)

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

                with open(dialog.get_filename(), 'rb') as f: 
                    fb = f.read(BLOCK_SIZE)
                    while len(fb) > 0:
                        file_hash.update(fb)
                        fb = f.read(BLOCK_SIZE) 

                print (file_hash.hexdigest())
                self.initial_file_selected()

            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")

            dialog.destroy()

