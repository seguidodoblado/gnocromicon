import logging

from gnocromicon import logsetup


def test_setup_writes_caught_exceptions_to_the_log_file(tmp_path, monkeypatch):
    monkeypatch.setattr(logsetup, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(logsetup, "LOG_PATH", tmp_path / "gnocromicon.log")
    root = logging.getLogger("gnocromicon")
    handlers_before = list(root.handlers)
    try:
        logsetup.setup()
        try:
            raise TimeoutError("sin respuesta del servicio")
        except TimeoutError:
            logging.getLogger("gnocromicon.ui.window").exception("Falló _identificar")
        for handler in root.handlers:
            handler.flush()

        text = (tmp_path / "gnocromicon.log").read_text(encoding="utf-8")
        assert "Falló _identificar" in text
        assert "TimeoutError: sin respuesta del servicio" in text
    finally:
        for handler in list(root.handlers):
            if handler not in handlers_before:
                root.removeHandler(handler)
                handler.close()
