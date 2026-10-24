#!/bin/sh
# Script que se ejecuta DENTRO del contenedor de la acción «Cartel de película».
# $1 es el primer argumento: el título que llega desde args en action.yml.
#
# Este archivo tiene que tener finales de línea de Linux (LF). El .gitattributes
# de RecursosEstudio se encarga de que Git los guarde así aunque lo edites en Windows.
set -e

titulo="$1"
borde=$(printf '%s' "$titulo" | sed 's/./=/g')

echo "+==${borde}==+"
echo "|  ${titulo}  |"
echo "+==${borde}==+"

# Para comprobar que de verdad estamos en un contenedor Alpine, no en el runner Ubuntu
echo "Cartel dibujado dentro de: $(grep PRETTY_NAME /etc/os-release | cut -d '"' -f 2)"

# El output se escribe igual que en un step normal: GitHub monta el archivo
# de GITHUB_OUTPUT dentro del contenedor
echo "cartel=${titulo}, ya en cartelera" >> "$GITHUB_OUTPUT"
