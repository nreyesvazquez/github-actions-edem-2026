## 📖 Guía de Ejercicios: GitHub Actions
Este documento contiene 10 ejercicios diseñados para dominar la automatización con GitHub Actions.

1. Variables de Entorno Globales: Crea un workflow que defina una variable de entorno a nivel de workflow y la use en dos jobs distintos.

2. Manejo de Secretos: Simula un login. Usa un "Secreto" de GitHub para ocultar una contraseña y mostrarla de forma segura (enmascarada) en el log.

3. Matriz de Estrategia: Ejecuta un mismo job de "Test" simultáneamente en tres versiones diferentes de Python (3.11 y 3.12).

4. Artefactos de Construcción: Job 1 genera un archivo .txt con un mensaje. Job 2 debe descargar ese archivo y mostrar su contenido.

5. Filtros de Rama y Ruta: Crea un workflow que solo se active cuando haya un push en la rama develop Y que solo afecte a archivos dentro de una carpeta llamada docs/.

6. Validación de JSON: Crea un workflow que use una acción de la comunidad para validar que un archivo data.json en el repo tiene un formato correcto. Para este ejercicio debeis generar un archivo .json en la raíz del repositorio con las claves (curso, modulo y alumnos)

7. Salidas entre Jobs (Outputs): El Job A genera un número aleatorio y lo pasa como "output" al Job B.
   
8. Programación Temporal (Cron): Configura un workflow que se ejecute automáticamente todos los lunes a las 9:00 AM.

9.  Contenedores de Servicio: Configura un job que levante un servicio de base de datos Postgres a través de un container de servicio y verifique su conexión Deberas configurar estas variables de entorno: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.

10. Aprobación Manual y Despliegue: Un workflow con dos jobs: "Build" y "Deploy". "Deploy" solo debe ejecutarse si "Build" termina con éxito y solo si el evento es manual (workflow_dispatch).

