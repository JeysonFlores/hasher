#!/usr/bin/python3
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class HashView(Gtk.Box):

    def __init__(self):
        Gtk.Box.__init__(self, orientation = Gtk.Orientation.VERTICAL)

        self.alg_label = Gtk.Label(label="Hash", halign=Gtk.Align.START)
        alg_label_context = self.alg_label.get_style_context()
        alg_label_context.add_class("h4")
        self.pack_start(self.alg_label, True, True, 0)

        self.text_view = Gtk.Entry(editable=False, can_focus=False)
        self.text_view.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "edit-copy-symbolic")
        self.text_view.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "view-refresh-symbolic")
        self.pack_start(self.text_view, False, False, 0)

    
