# Imagen de la acción Docker «Cartel de película».
# GitHub la construye en el runner cada vez que un workflow usa la acción.

# Alpine: una imagen Linux muy pequeña, así se construye rápido
FROM alpine:3.22

# Copiamos el script que hará el trabajo
COPY entrypoint.sh /entrypoint.sh

# Le damos permiso de ejecución aquí: si el archivo se sube desde Windows,
# Git no guarda ese permiso y el contenedor no podría ejecutarlo
RUN chmod +x /entrypoint.sh

# Lo que se ejecuta al arrancar el contenedor. Los args de action.yml
# llegan como argumentos: $1 es el título.
ENTRYPOINT ["/entrypoint.sh"]
