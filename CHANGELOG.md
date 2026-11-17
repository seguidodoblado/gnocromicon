# Changelog

Todos los cambios relevantes de este proyecto se documentarán
en este archivo.

## [Unreleased]

### Added

- Estructura inicial del proyecto: paquete `gnocromicon` (app, settings, theme, i18n, logsetup y ui) y tests básicos
- Ventana principal con menú de cabecera («Preferencias», «Acerca de Gnocromicón») y estado vacío a la espera de la identificación de libros
- Preferencias de idioma y tema: selector Sistema/Español/English y Sistema/Claro/Oscuro, persistidos en `~/.config/gnocromicon/settings.json` y aplicados reiniciando la app
- Traducción al inglés (i18n con `gettext`): catálogo `po/en.po`, scripts `i18n-extract.sh`/`i18n-compile.sh` y compilación automática al empaquetar
- Empaquetado `.deb` (`build-deb.sh`, `debian/`) con icono de la app y páginas de manual en inglés y español
- Integración continua (`ci.yml`: ruff, pytest y `.deb` con lintian) y despliegue (`cd.yml`: al subir una etiqueta `vX.Y.Z` ejecuta el CI sobre ese commit y deja la release en borrador con el mismo `.deb`)
- Documentos del repositorio en español e inglés (README, CONTRIBUTING, SECURITY, SUPPORT, PRIVACY y CODE_OF_CONDUCT)

### Fixed

- La tilde (tecla muerta) quedaba «flotando» en los campos de texto con IBus 1.5.29 y GTK4: la aplicación usa el método de entrada integrado de GTK (`GTK_IM_MODULE=simple`) cuando la sesión usa `ibus`
