"""La "película" de la Mission: automatizar Su Película.

El pipeline la construye, la prueba y la despliega. Es una aplicación mínima
para que el pipeline tenga algo real que hacer:

- BUILD:  ``python pelicula.py`` monta la película (título, escenas y duración)
          y la guarda en ``dist/pelicula.txt``. Ese archivo es el resultado del
          build, y el pipeline lo sube como artifact.
- TEST:   ``python -m unittest -v`` ejecuta los tests de ``test_pelicula.py``.
- DEPLOY: los jobs de Preview y Production descargan ``dist/pelicula.txt``
          y simulan que lo publican.

Bonus challenge «Haz que un test falle»: cambia la duración de una escena a 0,
haz push y mira cómo el pipeline se detiene en el job Test.
"""

from pathlib import Path

TITULO = "El misterio del pipeline perdido"

# Cada escena: (nombre, minutos)
ESCENAS = [
    ("Un push a medianoche", 12),
    ("El build que no compilaba", 18),
    ("Los tests en rojo", 25),
    ("La Pull Request de la discordia", 20),
    ("Revision en Preview", 15),
    ("Merge a main", 10),
    ("Estreno en Produccion", 14),
]


def duracion_total(escenas):
    """Suma los minutos de todas las escenas."""
    return sum(minutos for _, minutos in escenas)


def construir_pelicula(titulo, escenas):
    """Devuelve el texto completo de la película."""
    lineas = [titulo.upper(), "=" * len(titulo), ""]
    for numero, (nombre, minutos) in enumerate(escenas, start=1):
        lineas.append(f"Escena {numero}: {nombre} ({minutos} min)")
    lineas.append("")
    lineas.append(f"Duracion total: {duracion_total(escenas)} min")
    return "\n".join(lineas) + "\n"


def main(carpeta_salida="dist"):
    """Construye la película y la guarda en <carpeta_salida>/pelicula.txt."""
    salida = Path(carpeta_salida)
    salida.mkdir(parents=True, exist_ok=True)
    archivo = salida / "pelicula.txt"
    archivo.write_text(construir_pelicula(TITULO, ESCENAS), encoding="utf-8")
    print(f"Pelicula construida en {archivo}")
    return archivo


if __name__ == "__main__":
    main()
