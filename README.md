Este repositorio, llamado **Github_Actions**, es un conjunto de ejemplos prácticos y ejercicios diseñados para enseñar y practicar el uso de **GitHub Actions**, una herramienta de automatización de flujos de trabajo (CI/CD) integrada en GitHub. Está estructurado como un tutorial progresivo, ideal para estudiantes que quieren aprender desde lo básico hasta conceptos avanzados de integración continua, despliegue y automatización de infraestructura.

### 1. **Propósito General del Repositorio**
- **Enseñar GitHub Actions**: GitHub Actions permite automatizar tareas como ejecutar pruebas, construir imágenes Docker, desplegar infraestructura y más, todo activado por eventos en el repositorio (como pushes o pull requests).
- **Estructura de Aprendizaje**: No es una aplicación real en producción, sino un "laboratorio" con ejemplos progresivos. Incluye una app simple en Python, configuración de infraestructura con Terraform y workflows que van de lo simple a lo complejo.
- **Archivos Clave**:
  - `README.md`: Descripción del repo.
  - `EXERCISES.md`: Lista de 9 ejercicios prácticos para practicar workflows.
  - `code/python/`: Una aplicación Python simple (calculadora) con tests y herramientas de calidad de código.
  - `code/terraform/`: Configuración básica de infraestructura en AWS usando Terraform.
  - `.github/workflows/`: 9 workflows de ejemplo, numerados del 1 al 9, que demuestran diferentes conceptos.

### 2. **Qué Hace Cada Parte del Repositorio**
Vamos por secciones:

#### **a. La Aplicación Python (`code/python/`)**
- **Propósito**: Una calculadora básica en Python para demostrar CI/CD. No es compleja, pero sirve para practicar pruebas y despliegues.
- **Archivos**:
  - `main.py`: Define funciones matemáticas (suma, resta, multiplicación, división) y una interfaz de consola para usar la calculadora. Es interactiva: pide números al usuario y muestra resultados.
  - `test_main.py`: Pruebas unitarias usando `unittest`. Verifica que las funciones matemáticas funcionen correctamente (ej.: suma de 2+3=5, división por cero da error).
  - `requirements.txt`: Lista de dependencias: `flake8` (linter para detectar errores de estilo), `black` (formateador de código), `coverage` (para medir cobertura de tests) y `bandit` (escáner de seguridad).
  - `DockerFile` (nota: debería ser `Dockerfile`): Instrucciones para construir una imagen Docker de la app. Usa Python 3.9, copia el código y ejecuta `main.py` al iniciar el contenedor.
- **Qué Hace en Conjunto**: Es un ejemplo de "app mínima" para CI/CD. Los workflows la usan para ejecutar tests, linting y builds.

#### **b. La Configuración de Terraform (`code/terraform/`)**
- **Propósito**: Demostrar automatización de infraestructura con Terraform en GitHub Actions.
- **Archivos**:
  - `providers.tf`: Especifica el proveedor de nube (AWS) y la región (eu-central-1).
  - `main.tf`: Configura un "backend" en S3 para almacenar el estado de Terraform (útil para equipos). Crea un bucket S3 de ejemplo llamado "pnieto-terraform-example-bucket" con tags.
- **Qué Hace**: Permite "infraestructura como código". Los workflows de Terraform inicializan, planean y aplican cambios en AWS (ej.: crear un bucket S3).

#### **c. Los Workflows de GitHub Actions (`.github/workflows/`)**
Estos son los "corazones" del repo: archivos YAML que definen automatizaciones. Hay 9, numerados para progresión:
- **1.single_step.yaml**: Workflow simple activado manualmente (`workflow_dispatch`). Tiene 2 jobs: uno imprime "Hello World" y otro "Bye World". Ideal para empezar: muestra jobs paralelos.
- **2.multiple_step.yaml**: Similar, pero con más pasos en un job.
- **3.multiple_job.yaml**: Jobs paralelos con dependencias.
- **4.multiple_job_lineal.yaml**: Jobs en secuencia.
- **5.event_commit.yaml**: Se activa en pushes; imprime mensajes.
- **6.event_pr.yaml**: Se activa en pull requests; valida cambios.
- **7.multiple_job_argument.yaml**: Pasa datos entre jobs.
- **8.python_pr.yaml**: CI completo para Python. En PRs/pushes: instala dependencias, ejecuta tests (`unittest`), linting (`flake8`), checks de seguridad (`bandit`) y valida el Dockerfile (`hadolint`). También construye una imagen Docker.
- **9.terraform.yaml**: CI para Terraform. En PRs: formatea código, inicializa, planea cambios en AWS y (opcionalmente) aplica. Usa secrets para credenciales AWS.

**Qué Hacen en Conjunto**: Demuestran evolución de workflows: desde "hola mundo" hasta pipelines reales de CI/CD que integran testing, linting, Docker y Terraform.

#### **d. El Documento de Ejercicios (`EXERCISES.md`)**
- **Propósito**: Guía práctica para que los alumnos creen sus propios workflows basados en los ejemplos.