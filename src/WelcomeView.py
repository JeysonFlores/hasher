#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Handy, Granite

import constants as cn

class WelcomeView (Gtk.Grid):
    def __init__(self):

        Gtk.Window.__init__(self)

        self.halign, self.valign = Gtk.Align.CENTER, Gtk.Align.CENTER
        self.orientation = Gtk.Orientation.VERTICAL
        welcome_icon = Gtk.Image()
        welcome_icon.icon_name = "io.elementary.mail"
        welcome_icon.margin_bottom = 6
        welcome_icon.margin_end = 12
        welcome_icon.pixel_size = 64

        welcome_badge = Gtk.Image(icon_name="preferences-desktop-online-accounts", pixel_size=Gtk.IconSize.DIALOG)
        welcome_badge.halign = welcome_badge.valign = Gtk.Align.END

        welcome_overlay = Gtk.Overlay()
        welcome_overlay.halign = Gtk.Align.CENTER
        welcome_overlay.add (welcome_icon)
        welcome_overlay.add_overlay (welcome_badge)

        welcome_title = Gtk.Label(label="Connect an Account")
        welcome_title.wrap = True
        welcome_title.max_width_chars = 70
        welcome_title.get_style_context ().add_class (Granite.STYLE_CLASS_H1_LABEL)

        welcome_description = Gtk.Label (label="Mail uses email accounts configured in System Settings.")
        welcome_description.wrap = True
        welcome_description.max_width_chars = 70
        welcome_description.get_style_context ().add_class (Granite.STYLE_CLASS_H3_LABEL)

        welcome_button = Gtk.Button(label="Online Accounts…")
        welcome_button_style_context = welcome_button.get_style_context ()
        welcome_button.halign = Gtk.Align.CENTER
        welcome_button.margin_top = 24
        welcome_button_style_context.add_class (Granite.STYLE_CLASS_H3_LABEL)
        welcome_button_style_context.add_class (Gtk.STYLE_CLASS_SUGGESTED_ACTION)

        self.add (welcome_overlay)
        self.add (welcome_title)
        self.add (welcome_description)
        self.add (welcome_button)