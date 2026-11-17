from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gio, Gtk

from gnocromicon import __version__
from gnocromicon.i18n import _
from gnocromicon.ui.preferences import PreferencesWindow


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application) -> None:
        super().__init__(application=application, title="Gnocromicón", default_width=900, default_height=640)
        self.set_titlebar(self._build_header())

        estado_vacio = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=12,
            halign=Gtk.Align.CENTER, valign=Gtk.Align.CENTER,
        )
        icono = Gtk.Image.new_from_icon_name("gnocromicon")
        icono.set_pixel_size(96)
        estado_vacio.append(icono)
        titulo = Gtk.Label(label=_("Libros de rol de mesa"))
        titulo.add_css_class("title-1")
        estado_vacio.append(titulo)
        detalle = Gtk.Label(label=_("La identificación de libros llegará en próximas versiones."))
        detalle.add_css_class("dim-label")
        estado_vacio.append(detalle)
        self.set_child(estado_vacio)

    def _build_header(self) -> Gtk.HeaderBar:
        header = Gtk.HeaderBar()
        menu = Gio.Menu()
        menu.append(_("Preferencias"), "app.preferences")
        menu.append(_("Acerca de Gnocromicón"), "app.about")
        boton = Gtk.MenuButton(icon_name="open-menu-symbolic", menu_model=menu)
        header.pack_end(boton)
        return header

    def open_preferences(self) -> None:
        PreferencesWindow(self.get_application()).present()

    def open_about(self) -> None:
        about = Gtk.AboutDialog(
            transient_for=self,
            modal=True,
            program_name="Gnocromicón",
            version=__version__,
            logo_icon_name="gnocromicon",
            comments=_("Identifica y cataloga libros de rol de mesa"),
            website="https://github.com/seguidodoblado/gnocromicon",
            website_label=_("github.com/seguidodoblado/gnocromicon"),
            authors=["José Antonio Seguido Doblado <jose.antonio.seguido@gmail.com>"],
            copyright="© 2026 José Antonio Seguido Doblado",
            license_type=Gtk.License.GPL_3_0,
            translator_credits=_("translator-credits"),
        )
        about.present()
