from __future__ import annotations

import os
import sys

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gio, GLib, Gtk

from gnocromicon import i18n, logsetup, settings, theme
from gnocromicon.ui.window import MainWindow

APPLICATION_ID = "io.github.seguidodoblado.Gnocromicon"

# Con "python3 -m" argv[0] es la ruta de __main__.py y GTK derivaría de ahí el WM_CLASS;
# se fija para que coincida con StartupWMClass del .desktop y el panel muestre el icono.
GLib.set_prgname("gnocromicon")


class GnocromicónApplication(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id=APPLICATION_ID)
        self.system_theme: str | None = None

    def do_startup(self) -> None:
        Gtk.Application.do_startup(self)
        for nombre, accion in (("preferences", "open_preferences"), ("about", "open_about")):
            action = Gio.SimpleAction.new(nombre, None)
            action.connect("activate", lambda _a, _p, metodo=accion: getattr(self.props.active_window, metodo)())
            self.add_action(action)

    def do_activate(self) -> None:
        window = self.props.active_window
        if window is None:
            # El tema del sistema se captura antes de tocar gtk-theme-name, para
            # poder derivar la variante oscura sin perder el acento del usuario
            # (p. ej. Mint-Y-Orange) ni al volver a "Sistema" más adelante.
            self.system_theme = Gtk.Settings.get_default().get_property("gtk-theme-name")
            dark = settings.read_settings().get("dark_mode")
            if dark is not None:
                Gtk.Settings.get_default().set_property(
                    "gtk-theme-name", theme.theme_variant(self.system_theme, bool(dark))
                )
            window = MainWindow(self)
        window.present()


def main() -> int:
    language = settings.read_settings().get("language")
    if language:
        os.environ["LANGUAGE"] = language
    else:
        os.environ.pop("LANGUAGE", None)
    i18n.install()
    logsetup.setup()
    app = GnocromicónApplication()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
