import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"


def test_la_aplicacion_y_las_ventanas_se_importan_sin_errores():
    """Un nombre de clase no válido para GType solo falla al importar el módulo de GTK."""
    codigo = "import gnocromicon.app, gnocromicon.ui.window, gnocromicon.ui.preferences"
    resultado = subprocess.run(
        [sys.executable, "-c", codigo], env={"PYTHONPATH": str(SRC), "PATH": "/usr/bin:/bin"},
        capture_output=True, text=True,
    )
    assert resultado.returncode == 0, resultado.stderr
