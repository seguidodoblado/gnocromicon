<p align="center">
  <img src="src/gnocromicon/assets/gnocromicon.svg" alt="Logotipo de Gnocromicón" width="128">
</p>

<h1 align="center">Gnocromicón</h1>

<p align="center">
  <a href="https://github.com/seguidodoblado/gnocromicon/releases"><img src="https://img.shields.io/github/v/release/seguidodoblado/gnocromicon" alt="release"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/actions/workflows/ci.yml"><img src="https://github.com/seguidodoblado/gnocromicon/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/actions/workflows/cd.yml"><img src="https://github.com/seguidodoblado/gnocromicon/actions/workflows/cd.yml/badge.svg" alt="CD"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/blob/main/COPYING"><img src="https://img.shields.io/github/license/seguidodoblado/gnocromicon" alt="license"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/commits/main/"><img src="https://img.shields.io/github/last-commit/seguidodoblado/gnocromicon" alt="last commit"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/commits/main/"><img src="https://img.shields.io/github/commit-activity/t/seguidodoblado/gnocromicon" alt="total commits"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/releases"><img src="https://img.shields.io/github/downloads/seguidodoblado/gnocromicon/total" alt="downloads"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/stargazers"><img src="https://img.shields.io/github/stars/seguidodoblado/gnocromicon?style=flat" alt="stars"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon/issues"><img src="https://img.shields.io/github/issues/seguidodoblado/gnocromicon" alt="issues"></a>
  <a href="https://github.com/seguidodoblado/gnocromicon"><img src="https://img.shields.io/github/languages/top/seguidodoblado/gnocromicon" alt="language"></a>
  <a href="https://codetime.dev"><img alt="CodeTime Badge" src="https://shields.jannchie.com/endpoint?style=flat&color=0284c7&url=https%3A%2F%2Fcodetime.dev%2Fv3%2Fusers%2Fshield%3Fuid%3D36830"></a>
  <a href="https://wakatime.com/badge/github/seguidodoblado/gnocromicon"><img src="https://wakatime.com/badge/github/seguidodoblado/gnocromicon.svg" alt="wakatime"></a>
</p>

## 🇪🇸 Español

<p align="center">
  Identifica y cataloga libros de rol de mesa.
</p>

Aplicación de escritorio (GTK 4 + PyGObject) heredera de [Comic Identify](https://github.com/seguidodoblado/comic-identify),
pensada para libros de rol de mesa. Está en sus primeros pasos: hoy ofrece la ventana principal, el idioma y el tema
configurables y el paquete `.deb`; la identificación de libros llegará en próximas versiones.

- **Interfaz en español e inglés** (gettext), e **idioma y tema (claro/oscuro) configurables** desde Preferencias,
  siguiendo el tema del sistema por defecto. El menú de la cabecera da acceso a Preferencias y a la ventana
  «Acerca de» estándar de GNOME.

## Instalación

Desde el `.deb` generado por `./build-deb.sh` (requiere `dpkg-dev`):

```sh
./build-deb.sh
sudo dpkg -i ../gnocromicon_*.deb
```

## Uso

```sh
gnocromicon
```

## Desarrollo

Requiere Python 3.11+, PyGObject y GTK 4 del sistema.

```sh
python3 -m venv --system-site-packages .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/ruff check .
.venv/bin/pytest -q
sh i18n-compile.sh   # genera los catálogos .mo antes de ejecutar la aplicación o los tests de i18n
python3 -m gnocromicon
```

## Privacidad

La aplicación funciona en tu equipo y no envía datos a ningún sitio. Consulta la [política de privacidad](PRIVACY.md).

## Licencia

GPL-3.0 o posterior. Consulta [`COPYING`](COPYING).

---

## 🇺🇸 English

<p align="center">
  Identify and catalog tabletop role-playing books.
</p>

Desktop application (GTK 4 + PyGObject), a sibling of [Comic Identify](https://github.com/seguidodoblado/comic-identify)
for tabletop role-playing books. It is in its first steps: today it offers the main window, configurable language
and theme, and the `.deb` package; book identification will arrive in upcoming versions.

- **Interface in Spanish and English** (gettext), and **configurable language and theme (light/dark)** from
  Preferences, following the system theme by default. The header menu gives access to Preferences and to the
  standard GNOME «About» window.

## Installation

From the `.deb` built by `./build-deb.sh` (requires `dpkg-dev`):

```sh
./build-deb.sh
sudo dpkg -i ../gnocromicon_*.deb
```

## Usage

```sh
gnocromicon
```

## Development

Requires Python 3.11+, PyGObject and the system GTK 4.

```sh
python3 -m venv --system-site-packages .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/ruff check .
.venv/bin/pytest -q
sh i18n-compile.sh   # builds the .mo catalogs before running the app or the i18n tests
python3 -m gnocromicon
```

## Privacy

The application runs on your computer and sends no data anywhere. See the [privacy policy](PRIVACY.md#-english).

## License

GPL-3.0 or later. See [`COPYING`](COPYING).
