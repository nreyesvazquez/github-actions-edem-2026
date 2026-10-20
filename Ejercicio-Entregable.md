## 🏆 Ejercicio Final: El Pipeline de Datos Seguro y Automatizado
Tu empresa necesita automatizar un proceso que recibe datos de ventas en formato JSON. Debes crear un workflow llamado 20.ejercicio_entregable.yaml que cumpla con los siguientes requisitos:

1. Activación: Se debe activar manualmente y permitir al usuario elegir si quiere ejecutar los "Tests de Seguridad" (sí/no).

2. Job 1 (CI & Seguridad):
   1. Debe correr en ubuntu-latest.
   2. Debe validar que el archivo ventas.json es un JSON válido.
   3. Condicional: Solo si el usuario marcó "sí" en el input inicial, debe ejecutar un script de Python que simule un escaneo de seguridad buscando claves API expuestas.

3. Job 2 (Procesamiento):
   1. Depende del Job 1.
   2. Debe usar una Matrix para simular el procesamiento en dos entornos: staging y production
   3. Debe generar un archivo de reporte .txt diferente para cada entorno.
   4. Debe subir los reportes como artefactos para que el jefe de departamento pueda descargarlos.

4. Job 3 (Notificación de Éxito):
   1. Se ejecuta solo si los anteriores terminaron bien.
   2. Debe usar un Secreto llamado DISCORD_WEBHOOK para simular el envío de una notificación (un simple echo de la URL enmascarada bastará).