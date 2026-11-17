import gettext

from gnocromicon import i18n


def test_spanish_is_the_source_language_and_needs_no_catalog():
    assert i18n._("Preferencias") == "Preferencias"


def test_english_catalog_translates():
    translation = gettext.translation(i18n.DOMAIN, localedir=str(i18n.LOCALE_DIR), languages=["en"])
    assert translation.gettext("Preferencias") == "Preferences"
    assert translation.gettext("Idioma") == "Language"


def test_english_mo_file_exists():
    mo_path = i18n.LOCALE_DIR / "en" / "LC_MESSAGES" / f"{i18n.DOMAIN}.mo"
    assert mo_path.exists(), "Falta compilar po/en.po (ver po/README.md)"
