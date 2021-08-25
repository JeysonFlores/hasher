#!/usr/bin/python3

import hashlib
import gi
import HashView 
import locale, gettext, os

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, Gio


try:
    current_locale, encoding = locale.getdefaultlocale()
    current_locale = current_locale.split("_", 1)[0]
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


BLOCK_SIZE = 65536

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        context = self.get_style_context()
        context.add_class ("rounded")

        self.main_file = {"name": "", "route": "", "alg": "", "value": ""}
        self.secondary_file = {"name": "", "route": "", "alg": "", "value": ""}

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        self.stack = Gtk.Stack()


        # Hashes Content
        self.hashes_content = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20, homogeneous = False, valign = Gtk.Align.CENTER)
        hashes_content_context = self.hashes_content.get_style_context()
        hashes_content_context.add_class("main_content")

        self.hashes_select_file = Gtk.Button(label=_("Select File"),image=Gtk.Image(icon_name="document-open-symbolic", icon_size=Gtk.IconSize.BUTTON), always_show_image=True, can_focus=False)
        self.hashes_select_file.connect("clicked", self.main_file_selection)
        hashes_select_file_context = self.hashes_select_file.get_style_context()
        hashes_select_file_context.add_class("suggested-action")

        self.hashes_alg_combo = Gtk.ComboBoxText(can_focus=False)
        hashes_alg_combo_context = self.hashes_alg_combo.get_style_context()
        hashes_alg_combo_context.add_class("highlighted_text")

        algorithms = [
            "MD5",
            "SHA1",
            "SHA224",
            "SHA256",
            "SHA384",
            "SHA512",
        ]

        for algorithm in algorithms:
            self.hashes_alg_combo.append_text(algorithm)

        self.settings = Gio.Settings(schema_id="com.github.jeysonflores.hasher")

        self.hashes_alg_combo.set_active(self.settings.get_int("algorithm"))
        self.hashes_alg_combo.connect("changed", self.on_alg_changed)
        button_combo = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        button_combo_context = button_combo.get_style_context()
        button_combo_context.add_class("selection_data")
        button_combo.pack_start(self.hashes_select_file, True, True, 0)
        button_combo.pack_start(self.hashes_alg_combo, False, False, 1)
        self.hashes_content.pack_start(button_combo, False, False, 2)

        self.hashes_result = HashView.HashView()
        self.hashes_result.text_view.connect("icon-press", self.hashes_result_icon_selected)
        hashes_result_context = self.hashes_result.get_style_context()
        hashes_result_context.add_class("final_content")
        self.hashes_content.pack_start(self.hashes_result, False, True, 1)

        self.stack.add_titled(self.hashes_content, "Hashes", "Hashes")


        #Compare Content
        self.compare_content = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20, homogeneous = False, valign = Gtk.Align.CENTER)
        compare_content_context = self.compare_content.get_style_context()
        compare_content_context.add_class("main_content")

        self.compare_select_main_file = Gtk.Button(label=_("Select File"),image=Gtk.Image(icon_name="document-open-symbolic", icon_size=Gtk.IconSize.BUTTON), always_show_image=True, can_focus=False)
        self.compare_select_main_file.connect("clicked", self.main_file_selection)
        compare_select_main_file_context = self.compare_select_main_file.get_style_context()
        compare_select_main_file_context.add_class("highlighted_text")
        compare_select_main_file_context.add_class("flat_selection_data")
        self.compare_content.pack_start(self.compare_select_main_file, False, False, 0)

        self.compare_select_secondary_file = Gtk.Button(label=_("Select File to Compare"),image=Gtk.Image(icon_name="document-open-symbolic", icon_size=Gtk.IconSize.BUTTON), always_show_image=True, can_focus=False)
        self.compare_select_secondary_file.connect("clicked", self.secondary_file_selection)
        compare_select_secondary_file_context = self.compare_select_secondary_file.get_style_context()
        compare_select_secondary_file_context.add_class("highlighted_text")
        compare_select_secondary_file_context.add_class("flat_selection_data")
        self.compare_content.pack_start(self.compare_select_secondary_file, False, False, 1)

        self.compare_start = Gtk.Button(label=_("Compare!"), can_focus=False, sensitive=False)
        self.compare_start.connect("clicked", self.compare_files)
        compare_start_context = self.compare_start.get_style_context()
        compare_start_context.add_class("suggested-action")
        compare_start_context.add_class("small_content")
        self.compare_content.pack_start(self.compare_start, False, False, 2)

        self.compare_alert = Gtk.Image(icon_size=Gtk.IconSize.DND, visible=False) #True=emblem-default-symbolic - False=process-stop-symbolic
        compare_alert_context = self.compare_alert.get_style_context()
        compare_alert_context.add_class("icon_status")
        self.compare_content.pack_start(self.compare_alert, False, False, 3)

        self.stack.add_titled(self.compare_content, _("Compare"), _("Compare"))

        #Verify Content 
        self.verify_content = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0, homogeneous = False, valign = Gtk.Align.CENTER)
        verify_content_context = self.verify_content.get_style_context()
        verify_content_context.add_class("main_content")

        self.verify_select_main_file = Gtk.Button(label=_("Select File"),image=Gtk.Image(icon_name="document-open-symbolic", icon_size=Gtk.IconSize.BUTTON), always_show_image=True, can_focus=False)
        self.verify_select_main_file.connect("clicked", self.main_file_selection)
        verify_select_main_file_context = self.verify_select_main_file.get_style_context()
        verify_select_main_file_context.add_class("highlighted_text")
        verify_select_main_file_context.add_class("selection_data")
        self.verify_content.pack_start(self.verify_select_main_file, False, False, 0)

        verify_form = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        verify_form_label = Gtk.Label(label="Hash", halign=Gtk.Align.START)
        verify_form_label_context = verify_form_label.get_style_context()
        verify_form_label_context.add_class("h4")
        verify_form.pack_start(verify_form_label, True, True, 0)

        self.verify_form_entry = Gtk.Entry()
        self.verify_form_entry.connect("icon-press", self.verify_form_icon_selected)
        self.verify_form_entry.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "edit-paste-symbolic")
        verify_form.pack_start(self.verify_form_entry, True, True, 1)

        self.verify_content.pack_start(verify_form, False, False, 2)

        self.verify_start = Gtk.Button(label=_("Verify!"), can_focus=False, sensitive=False)
        self.verify_start.connect("clicked", self.verify_hashes)
        verify_start_context = self.verify_start.get_style_context()
        verify_start_context.add_class("suggested-action")
        verify_start_context.add_class("small_content")
        self.verify_content.pack_start(self.verify_start, False, False, 2)

        self.verify_alert = Gtk.Image(icon_size=Gtk.IconSize.DND, visible=False) #True=emblem-default-symbolic - False=process-stop-symbolic
        verify_alert_context = self.verify_alert.get_style_context()
        verify_alert_context.add_class("icon_status")
        self.verify_content.pack_start(self.verify_alert, False, False, 3)

        self.stack.add_titled(self.verify_content, _("Verify"), _("Verify"))


        #HeaderBar Content
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

    def on_alg_changed(self, algo):
        self.settings.set_int("algorithm", self.hashes_alg_combo.get_active())

    def main_file_selection(self, button):
        dialog = Gtk.FileChooserNative.new(_("Please choose a file"), self, Gtk.FileChooserAction.OPEN, _("Open"), _("Cancel"))
        response = dialog.run()

        if response == Gtk.ResponseType.ACCEPT:
                self.hashes_select_file.set_label(dialog.get_filename()[::-1].split("/", 1)[0][::-1])
                self.compare_select_main_file.set_label(dialog.get_filename()[::-1].split("/", 1)[0][::-1])
                self.verify_select_main_file.set_label(dialog.get_filename()[::-1].split("/", 1)[0][::-1])
                self.main_file["name"] = dialog.get_filename()[::-1].split("/", 1)[0][::-1]
                self.main_file["alg"] = self.hashes_alg_combo.get_active_text()
                self.main_file["route"] = dialog.get_filename()
                self.verify_start.set_sensitive(True)

                main_file_hash = self.get_hash(self.main_file["alg"], self.main_file["route"])

                self.main_file["value"] = main_file_hash
                self.hashes_result.alg_label.set_label(self.main_file["alg"] + " Hash")
                self.hashes_result.text_view.set_text(main_file_hash)

                if self.secondary_file["name"] != "":
                    self.compare_start.set_sensitive(True)

        dialog.destroy()                

    def hashes_result_icon_selected(self, entry, icon_position, event):
        if icon_position == Gtk.EntryIconPosition.SECONDARY:
            if self.hashes_result.text_view.get_text() != "":
                self.clipboard.set_text(self.hashes_result.text_view.get_text(), -1)

        elif icon_position == Gtk.EntryIconPosition.PRIMARY:
            if self.main_file["value"] != "":
                self.main_file["alg"] = self.hashes_alg_combo.get_active_text()

                main_file_hash = self.get_hash(self.main_file["alg"], self.main_file["route"])

                self.main_file["value"] = main_file_hash
                self.hashes_result.alg_label.set_label(self.main_file["alg"] + " Hash")
                self.hashes_result.text_view.set_text(main_file_hash)


    def get_hash(self, alg, filename):
        if alg == "MD5":
            file_hash = hashlib.md5()

        elif alg == "SHA1":
            file_hash = hashlib.sha1()

        elif alg == "SHA224":
            file_hash = hashlib.sha224()

        elif alg == "SHA256":
            file_hash = hashlib.sha256()

        elif alg == "SHA384":
            file_hash = hashlib.sha384()

        elif alg == "SHA512":
            file_hash = hashlib.sha512()

        with open(filename, 'rb') as f: 
                    fb = f.read(BLOCK_SIZE)
                    while len(fb) > 0:
                        file_hash.update(fb)
                        fb = f.read(BLOCK_SIZE)

        return file_hash.hexdigest()

    def secondary_file_selection(self, button):
        dialog = Gtk.FileChooserNative.new(_("Please choose a file"), self, Gtk.FileChooserAction.OPEN, _("Open"), _("Cancel"))
        response = dialog.run()

        if response == Gtk.ResponseType.ACCEPT:
            self.compare_select_secondary_file.set_label(dialog.get_filename()[::-1].split("/", 1)[0][::-1])
            self.secondary_file["name"] = dialog.get_filename()[::-1].split("/", 1)[0][::-1]
            self.secondary_file["route"] = dialog.get_filename()

            if self.main_file["name"] != "":
                self.compare_start.set_sensitive(True)

        dialog.destroy()      
        
    def compare_files(self, button):
        secondary_file_hash = self.get_hash(self.main_file["alg"], self.secondary_file["route"])

        self.secondary_file["value"] = secondary_file_hash

        if self.secondary_file["value"] == self.main_file["value"]:
            self.compare_alert.set_from_icon_name("emblem-default-symbolic", Gtk.IconSize.DND)
            self.compare_alert.set_visible(True)
        else:
            self.compare_alert.set_from_icon_name("process-stop-symbolic", Gtk.IconSize.DND)
            self.compare_alert.set_visible(True)

    def verify_form_icon_selected(self, entry, icon_position, event):
        entry.set_text(self.clipboard.wait_for_text())

    def verify_hashes(self, button):
        if self.verify_form_entry.get_text() != "":
            if self.main_file["value"] == self.verify_form_entry.get_text():
                self.verify_alert.set_from_icon_name("emblem-default-symbolic", Gtk.IconSize.DND)
                self.verify_alert.set_visible(True)
                return None

            algorithms = [
            "MD5",
            "SHA1",
            "SHA224",
            "SHA256",
            "SHA384",
            "SHA512",
            ]

            algorithms.remove(self.main_file["alg"])

            for alg in algorithms:
                hash = self.get_hash(alg, self.main_file["route"])
                if hash == self.verify_form_entry.get_text():
                    self.verify_alert.set_from_icon_name("emblem-default-symbolic", Gtk.IconSize.DND)
                    self.verify_alert.set_visible(True)
                    return None
            
            self.verify_alert.set_from_icon_name("process-stop-symbolic", Gtk.IconSize.DND)
            self.verify_alert.set_visible(True)
