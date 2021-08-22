#!/usr/bin/python3

import hashlib
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import HashView 

BLOCK_SIZE = 65536

hash_algorythms = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        context = self.get_style_context()
        context.add_class ("rounded")

        self.main_file = {"name": "", "alg": "", "value": ""}
        self.secondary_file = {"name": "", "alg": "", "value": ""}

        self.stack = Gtk.Stack()

        self.hashes_content = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20, homogeneous = False)
        hashes_content_context = self.hashes_content.get_style_context()
        hashes_content_context.add_class("main_content")

        self.hashes_select_file = Gtk.Button(label="Select File",image=Gtk.Image(icon_name="document-open-symbolic", icon_size=Gtk.IconSize.BUTTON), always_show_image=True, can_focus=False)
        self.hashes_select_file.connect("clicked", self.main_file_selection)
        hashes_select_file_context = self.hashes_select_file.get_style_context()
        hashes_select_file_context.add_class("suggested-action")
        #self.hashes_content.pack_start(self.hashes_select_file, False, False, 0)

        self.hashes_alg_combo = Gtk.ComboBoxText(can_focus=False)
        hashes_alg_combo_context = self.hashes_alg_combo.get_style_context()
        hashes_alg_combo_context.add_class("highlighted_text")

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
        #self.hashes_content.pack_start(self.hashes_alg_combo, False, True, 1)

        button_combo = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        button_combo_context = button_combo.get_style_context()
        button_combo_context.add_class("selection_data")
        button_combo.pack_start(self.hashes_select_file, True, True, 0)
        button_combo.pack_start(self.hashes_alg_combo, False, False, 1)

        self.hashes_content.pack_start(button_combo, False, False, 2)

        #self.hashes_start = Gtk.Button(label="Hash!")
        #hashes_start_context = self.hashes_start.get_style_context()
        #hashes_start_context.add_class("suggested-action")
        #hashes_start_context.add_class("small_content")
        #self.hashes_content.pack_start(self.hashes_start, False, True, 2)

        self.hashes_result = HashView.HashView()
        hashes_result_context = self.hashes_result.get_style_context()
        hashes_result_context.add_class("final_content")
        self.hashes_result.alg_label.set_label("Hash")
        self.hashes_content.pack_start(self.hashes_result, False, True, 1)

        self.stack.add_titled(self.hashes_content, "Hashes", "Hashes")
        self.stack.add_titled(Gtk.Label(label="Compare Content"), "Compare", "Compare")
        self.stack.add_titled(Gtk.Label(label="Verify Content"), "Verify", "Verify")

        

        self.compare_select_file = Gtk.Button(label="Select File")
        self.verify_select_file = Gtk.Button(label="Select File")




        self.stack_switcher = Gtk.StackSwitcher(receives_default=False)
        self.stack_switcher.set_stack(self.stack)

        self.headerbar = Gtk.HeaderBar(decoration_layout_set=True, decoration_layout="close:")
        headerbar_context = self.headerbar.get_style_context()
        headerbar_context.add_class("flat")
        self.headerbar.set_show_close_button(True)
        self.headerbar.set_custom_title(self.stack_switcher)
        self.set_titlebar(self.headerbar)
        
        self.add(self.stack)

        self.resize(600, 400)

    def main_file_selection(self, button):
        dialog = Gtk.FileChooserDialog(title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK,)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
                self.hashes_select_file.set_label(dialog.get_filename()[::-1].split("/", 1)[0][::-1])
                self.main_file["name"] = dialog.get_filename()[::-1].split("/", 1)[0][::-1]
                
                if self.hashes_alg_combo.get_active_text() == "MD5":
                    file_hash = hashlib.md5()
                    self.main_file["alg"] = "MD5"

                    with open(dialog.get_filename(), 'rb') as f: 
                        fb = f.read(BLOCK_SIZE)
                        while len(fb) > 0:
                            file_hash.update(fb)
                            fb = f.read(BLOCK_SIZE) 

                elif self.hashes_alg_combo.get_active_text() == "SHA1":
                    file_hash = hashlib.sha1()
                    self.main_file["alg"] = "SHA1"

                    with open(dialog.get_filename(), 'rb') as f: 
                        fb = f.read(BLOCK_SIZE)
                        while len(fb) > 0:
                            file_hash.update(fb)
                            fb = f.read(BLOCK_SIZE) 

                elif self.hashes_alg_combo.get_active_text() == "SHA224":
                    file_hash = hashlib.sha224()
                    self.main_file["alg"] = "SHA224"
                    with open(dialog.get_filename(), 'rb') as f: 
                        fb = f.read(BLOCK_SIZE)
                        while len(fb) > 0:
                            file_hash.update(fb)
                            fb = f.read(BLOCK_SIZE)

                elif self.hashes_alg_combo.get_active_text() == "SHA256":
                    file_hash = hashlib.sha256()
                    self.main_file["alg"] = "SHA256"

                    with open(dialog.get_filename(), 'rb') as f: 
                        fb = f.read(BLOCK_SIZE)
                        while len(fb) > 0:
                            file_hash.update(fb)
                            fb = f.read(BLOCK_SIZE) 

                elif self.hashes_alg_combo.get_active_text() == "SHA384":
                    file_hash = hashlib.sha384()
                    self.main_file["alg"] = "SHA384"

                    with open(dialog.get_filename(), 'rb') as f: 
                        fb = f.read(BLOCK_SIZE)
                        while len(fb) > 0:
                            file_hash.update(fb)
                            fb = f.read(BLOCK_SIZE)

                elif self.hashes_alg_combo.get_active_text() == "SHA512":
                    file_hash = hashlib.sha512()
                    self.main_file["alg"] = "SHA512"

                    with open(dialog.get_filename(), 'rb') as f: 
                        fb = f.read(BLOCK_SIZE)
                        while len(fb) > 0:
                            file_hash.update(fb)
                            fb = f.read(BLOCK_SIZE)

                self.main_file["value"] = file_hash.hexdigest()
                self.hashes_result.alg_label.set_label(self.hashes_alg_combo.get_active_text() + " Hash")
                self.hashes_result.text_view.set_text(file_hash.hexdigest())

        dialog.destroy()
        print(self.main_file)
                