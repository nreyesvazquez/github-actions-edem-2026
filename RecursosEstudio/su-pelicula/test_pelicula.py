"""Tests de la película. Los ejecuta el job Test del pipeline.

Desde la carpeta su-pelicula:  python -m unittest -v
Si un test falla, el comando termina con error, el job Test sale en rojo
y los jobs de despliegue (que tienen needs: test) no se ejecutan.
"""

import tempfile
import unittest
from pathlib import Path

from pelicula import ESCENAS, TITULO, construir_pelicula, duracion_total, main


class TestPelicula(unittest.TestCase):
    def test_tiene_titulo(self):
        self.assertTrue(TITULO.strip())

    def test_escenas_con_duracion_positiva(self):
        for nombre, minutos in ESCENAS:
            with self.subTest(escena=nombre):
                self.assertGreater(minutos, 0)

    def test_duracion_de_largometraje(self):
        # Un largometraje dura entre 60 y 180 minutos
        self.assertTrue(60 <= duracion_total(ESCENAS) <= 180)

    def test_construir_incluye_titulo_y_todas_las_escenas(self):
        texto = construir_pelicula(TITULO, ESCENAS)
        self.assertIn(TITULO.upper(), texto)
        self.assertEqual(texto.count("Escena "), len(ESCENAS))

    def test_main_escribe_el_archivo(self):
        with tempfile.TemporaryDirectory() as carpeta:
            archivo = main(carpeta)
            self.assertTrue(Path(archivo).exists())


if __name__ == "__main__":
    unittest.main()
