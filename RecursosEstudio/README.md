# Recursos de estudio · GitHub Actions

Ejemplos comentados de todo el temario de la sesión **GitHub Actions** (Bloque Fundamentos: Git Actions, Docker y SQL). Cada workflow explica en comentarios qué hace cada línea, cómo probarlo y qué deberías ver en GitHub.

Objetivos de la sesión:

1. Conocer qué son las GitHub Actions.
2. Diferenciar los distintos componentes de las GitHub Actions.
3. Crear los primeros workflows.
4. Advertencias y recomendaciones.
5. Diseñar e implementar un pipeline de CI/CD básico para vuestro proyecto.

## Contenido de la carpeta

| Archivo | Qué enseña | Sección de la presentación |
|---------|------------|----------------------------|
| [`workflows/01_primer_workflow.yaml`](workflows/01_primer_workflow.yaml) | Lo mínimo: event, job, runner y step | Primer Workflow |
| [`workflows/02_steps_y_checkout.yaml`](workflows/02_steps_y_checkout.yaml) | Steps con `run` y con `uses`, `actions/checkout`, `name`, `working-directory` | second.yaml |
| [`workflows/03_jobs_paralelo_y_secuencia.yaml`](workflows/03_jobs_paralelo_y_secuencia.yaml) | Jobs en paralelo, `needs`, runners Linux y Windows, `if: always()`, `timeout-minutes` | Componentes: Jobs y Runner |
| [`workflows/04_eventos.yaml`](workflows/04_eventos.yaml) | `workflow_dispatch`, `push` y `pull_request` con filtros, `schedule` (cron) | Componentes: Event |
| [`workflows/05_inputs.yaml`](workflows/05_inputs.yaml) | Inputs de tipo `string`, `choice`, `number` y `boolean` | Inputs y third.yaml |
| [`workflows/06_contextos.yaml`](workflows/06_contextos.yaml) | Los contextos `github`, `runner`, `job`, `env`, `vars`, `secrets`, `inputs`, `steps`, `matrix`, `strategy` y `needs` | Contexts |
| [`workflows/07_env_y_secretos.yaml`](workflows/07_env_y_secretos.yaml) | `env` a tres niveles, `$GITHUB_ENV`, secretos, `::add-mask::`, `vars` | Gestión: configuración dinámica |
| [`workflows/08_matrix.yaml`](workflows/08_matrix.yaml) | Matrix de sistemas operativos y versiones de Python, `include`, `exclude`, `fail-fast` | Gestión: Matrix Strategy |
| [`workflows/09_outputs.yaml`](workflows/09_outputs.yaml) | Outputs de steps y de jobs, outputs de varias líneas | Outputs y outputs.yaml |
| [`workflows/10_artifacts.yaml`](workflows/10_artifacts.yaml) | Subir y descargar artifacts entre jobs | Artifacts |
| [`workflows/11_custom_actions.yaml`](workflows/11_custom_actions.yaml) | Usar las tres acciones propias de [`acciones/`](acciones/) | Custom Actions |
| [`workflows/12_workflow_reutilizable.yaml`](workflows/12_workflow_reutilizable.yaml) y [`12_llamar_reutilizable.yaml`](workflows/12_llamar_reutilizable.yaml) | **Extra**: un workflow que llama a otro (`workflow_call`) | Inputs (menciona `workflow_call`) |
| [`workflows/13_ci_cd_calculadora.yaml`](workflows/13_ci_cd_calculadora.yaml) | Pipeline CI/CD completo para la calculadora de `code/python` | Objetivo 05 |
| [`workflows/mision_pelicula/`](workflows/mision_pelicula/) | La **Mission: automatizar Su Película**, en sus cinco niveles | Mission I y II |
| [`acciones/saludo-composite/`](acciones/saludo-composite/) | Custom action de tipo **composite** | Custom Actions |
| [`acciones/contar-lineas-js/`](acciones/contar-lineas-js/) | Custom action de tipo **JavaScript** (Node.js) | Custom Actions |
| [`acciones/cartel-docker/`](acciones/cartel-docker/) | Custom action de tipo **Docker** | Custom Actions |
| [`su-pelicula/`](su-pelicula/) | La «película» que construye, prueba y despliega la Mission: `pelicula.py` y sus tests | Mission |
| [`datos/lista_peliculas.txt`](datos/lista_peliculas.txt) | Un archivo que leen los ejemplos 02 y 11 | — |
| [`.gitattributes`](.gitattributes) | Hace que los `.sh` se guarden con finales de línea de Linux | — |

## Índice

1. [Cómo probar los ejemplos](#1-cómo-probar-los-ejemplos)
2. [Qué es GitHub Actions: CI/CD](#2-qué-es-github-actions-cicd)
3. [Del cambio de código a producción](#3-del-cambio-de-código-a-producción)
4. [Componentes](#4-componentes)
5. [Anatomía de un workflow](#5-anatomía-de-un-workflow)
6. [Eventos](#6-eventos)
7. [Inputs](#7-inputs)
8. [Contextos y expresiones](#8-contextos-y-expresiones)
9. [Variables de entorno, variables y secretos](#9-variables-de-entorno-variables-y-secretos)
10. [Matrix](#10-matrix)
11. [Outputs, artifacts y caché](#11-outputs-artifacts-y-caché)
12. [Custom actions y workflows reutilizables](#12-custom-actions-y-workflows-reutilizables)
13. [Mission: automatizar Su Película](#13-mission-automatizar-su-película)
14. [Advertencias y recomendaciones](#14-advertencias-y-recomendaciones)
15. [Notas sobre la presentación y el repositorio](#15-notas-sobre-la-presentación-y-el-repositorio)
16. [Chuleta](#16-chuleta)
17. [Si algo falla](#17-si-algo-falla)
18. [Preguntas de repaso](#18-preguntas-de-repaso)

---

## 1. Cómo probar los ejemplos

GitHub **solo ejecuta los workflows que están en `.github/workflows/`**, en la raíz del repositorio, y no mira subcarpetas. Los de `RecursosEstudio/workflows/` están guardados para estudiar: para ejecutar uno, cópialo allí.

Desde la raíz del repositorio, en PowerShell:

```powershell
Copy-Item RecursosEstudio\workflows\01_primer_workflow.yaml .github\workflows\
git add .github/workflows/01_primer_workflow.yaml RecursosEstudio
git commit -m "Pruebo el ejemplo 01 de GitHub Actions"
git push
```

Después, en GitHub: pestaña **Actions** > el workflow en la lista de la izquierda > **Run workflow**.

- El botón **Run workflow** solo aparece si el workflow tiene `workflow_dispatch` **y** está en la rama por defecto (`main`).
- Los ejemplos 02, 08, 11, 12 y 13 leen archivos de `RecursosEstudio/` o de `code/python/`: la carpeta tiene que estar subida también.
- El 12 son **dos** archivos: cópialos los dos sin cambiarles el nombre.
- De la Mission, copia **un nivel cada vez**. Si copias varios, los que escuchan el mismo evento se ejecutan todos a la vez.
- El 04 tiene un `schedule` que lo lanza cada lunes. Si no lo quieres, borra ese bloque o borra el archivo de `.github/workflows/` cuando termines.
- Para dejar de ejecutar un ejemplo, bórralo de `.github/workflows/` (en `RecursosEstudio/` se queda guardado).

Todos se han revisado con [actionlint](https://github.com/rhysd/actionlint), que comprueba la sintaxis, las expresiones, las entradas de cada action y los scripts. Si instalas la extensión **GitHub Actions** de VS Code, también te marca los errores mientras escribes.

---

## 2. Qué es GitHub Actions: CI/CD

**GitHub Actions** es una plataforma de integración continua y entrega continua (CI/CD) que automatiza la compilación, las pruebas y el despliegue.

| Sigla | Significa | En la práctica |
|-------|-----------|----------------|
| **CI** | Integración continua | Cada vez que cambias algo en el código, se revisa automáticamente: se construye y se pasan los tests |
| **CD** | Entrega o despliegue continuo | Si todo está bien, el programa se publica o se entrega automáticamente |

---

## 3. Del cambio de código a producción

**Diseña tu propio pipeline.** Si vuestra aplicación tuviera miles de usuarios:

| Pregunta | Respuesta en el pipeline |
|----------|--------------------------|
| ¿Qué debería ocurrir cuando alguien modifica el código? | Que salte el pipeline solo, con cada Pull Request |
| ¿Qué deberíamos comprobar antes de aceptar el cambio? | Que se construye (**Build**) y que pasa los tests (**Test**) |
| ¿Cómo sabemos que la app sigue funcionando? | Por los tests automáticos |
| ¿Queremos probar el cambio antes de publicarlo? | Sí: en un entorno temporal (**Deploy Preview**) |
| ¿Cuándo debería llegar a producción? | Cuando la PR se aprueba y se fusiona en `main` (**Deploy Production**) |

**De la idea a GitHub Actions:** un workflow no es más que ese diagrama convertido en YAML.

| En el diagrama | En GitHub Actions |
|----------------|-------------------|
| La Pull Request | Event (trigger) |
| Build, Test, Preview, Production | Jobs |
| La máquina donde se ejecuta | Runner |
| Las tareas de cada fase | Steps |

Si una etapa falla, el pipeline se detiene y no continúa con la siguiente (`needs`). Lo tienes construido en la [Mission](#13-mission-automatizar-su-película).

---

## 4. Componentes

> Un **workflow** se activa cuando se produce un **evento**, y ejecuta una serie de **jobs** en un **runner**. Cada job tiene uno o varios **steps**, que ejecutan scripts o **actions**.

| Componente | Qué es | Dónde se escribe |
|------------|--------|------------------|
| **Workflow** | Un proceso automatizado. Un repositorio puede tener muchos, cada uno para una tarea | Un archivo `.yaml` en `.github/workflows/` |
| **Event** | Lo que ocurre en el repositorio y lanza el workflow (push, PR, a mano...) | `on:` |
| **Runner** | La máquina virtual que ejecuta un job: Ubuntu, Windows o macOS. La pone GitHub, o la tuya propia (*self-hosted*) | `runs-on:` |
| **Job** | Una serie de steps que se ejecutan en el mismo runner. Por defecto, en paralelo con los demás jobs | `jobs: <id>:` |
| **Step** | Un comando (`run`) o una action (`uses`). Se ejecutan en orden y comparten la máquina y sus archivos | `steps:` |
| **Action** | Una tarea ya programada y reutilizable (descargar el código, instalar Python...) | `uses: autor/action@versión` |

El **id de un job** es único en el workflow, empieza por una letra o `_` y solo lleva letras, números, `-` y `_`.

---

## 5. Anatomía de un workflow

```yaml
name: "Mi workflow"              # nombre en la pestaña Actions (opcional)

on:                              # EVENTO
  workflow_dispatch:

env:                             # variables para todos los jobs (opcional)
  APP: "calculadora"

jobs:
  build:                         # id del JOB
    name: Build                  # nombre visible (opcional)
    runs-on: ubuntu-latest       # RUNNER
    steps:                       # STEPS, en orden
      - uses: actions/checkout@v7         # una action
      - name: Saludar
        run: echo "Construyendo $APP"     # un comando

  test:
    needs: build                 # espera a que build termine bien
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testeando"
```

YAML usa la **indentación** (siempre espacios, nunca tabuladores) para decir qué va dentro de qué. Un `-` empieza un elemento de una lista.

---

## 6. Eventos

| Evento | Cuándo se lanza | Ejemplo |
|--------|-----------------|---------|
| `workflow_dispatch` | A mano, con **Run workflow** (admite inputs) | Todos los ejemplos |
| `push` | Al subir commits | [`04`](workflows/04_eventos.yaml), Mission 2, 3 y 5 |
| `pull_request` | Al abrir una PR, al subirle commits o al reabrirla | [`04`](workflows/04_eventos.yaml), [`13`](workflows/13_ci_cd_calculadora.yaml), Mission 4 y 5 |
| `schedule` | A una hora fija (cron, siempre en **UTC**) | [`04`](workflows/04_eventos.yaml) |
| `workflow_call` | Cuando otro workflow lo llama | [`12`](workflows/12_workflow_reutilizable.yaml) |

Filtros más usados:

```yaml
on:
  push:
    branches: [main, develop]         # solo estas ramas
    paths: ["code/python/**"]         # solo si cambian estos archivos
    # branches-ignore, paths-ignore, tags: ["v*"]
  pull_request:
    branches: [main]                  # rama DESTINO de la PR
    types: [opened, synchronize, reopened]
  schedule:
    - cron: "0 7 * * 1"               # minuto hora día mes día-semana: lunes a las 7:00 UTC
```

Para saber qué evento ha lanzado la ejecución: `${{ github.event_name }}`. Con eso, un `if:` puede ejecutar cada job o step solo con su evento.

---

## 7. Inputs

Solo existen con `workflow_dispatch`, con `workflow_call` y en las actions. Se leen con `${{ inputs.<id> }}`.

| Propiedad | Qué hace | ¿Obligatoria? |
|-----------|----------|---------------|
| `description` | Lo que ve el usuario en el formulario | Recomendada (en las actions, obligatoria) |
| `required` | Si se puede dejar vacío | No (por defecto `false`) |
| `default` | Valor por defecto | No |
| `type` | `string`, `boolean`, `choice` (con `options`), `number` o `environment` | No en `workflow_dispatch` (por defecto `string`); **sí** en `workflow_call` |

El id de cada input es único y solo lleva letras, números, `-` y `_`.

`inputs.gritar` respeta el tipo (un boolean es `true`/`false`); `github.event.inputs.gritar`, la forma antigua, lo convierte todo a texto. Por eso con la forma antigua hay que comparar `== 'true'`, entre comillas.

---

## 8. Contextos y expresiones

Un contexto es un objeto con información de la ejecución. Se lee con `${{ <contexto>.<propiedad> }}`, y GitHub lo sustituye por su valor **antes** de mandar el step al runner.

| Contexto | Qué tiene | Ejemplo |
|----------|-----------|---------|
| `github` | El evento, el repositorio, la rama, el commit, quién lo lanzó | `github.event_name`, `github.ref_name`, `github.sha`, `github.actor` |
| `env` | Las variables de `env:` del workflow, del job y del step | `env.GLOBAL_USER` |
| `vars` | Variables de configuración del repositorio | `vars.REGION` |
| `secrets` | Secretos | `secrets.DB_PASSWORD`, `secrets.GITHUB_TOKEN` |
| `inputs` | Los inputs | `inputs.thename` |
| `job` | El job actual | `job.status` |
| `jobs` | Los jobs de un workflow reutilizable | `jobs.tests.outputs.resultado` |
| `steps` | Los steps anteriores que tienen `id` | `steps.get-time.outputs.currenttime`, `steps.x.outcome` |
| `runner` | La máquina | `runner.os`, `runner.arch`, `runner.temp` |
| `strategy` | Datos de la matrix | `strategy.job-index`, `strategy.job-total` |
| `matrix` | La combinación actual | `matrix.os`, `matrix.python-version` |
| `needs` | Los jobs de los que depende este | `needs.build.result`, `needs.build.outputs.hora` |

Casi todo `github` y `runner` también está como variable de entorno en el runner: `$GITHUB_SHA`, `$GITHUB_ACTOR`, `$RUNNER_OS`...

Dentro de `${{ }}` se pueden usar operadores y funciones:

| Expresión | Para qué |
|-----------|----------|
| `==`, `!=`, `<`, `>`, `&&`, `\|\|`, `!` | Comparar y combinar. Los textos se comparan sin distinguir mayúsculas |
| `vars.REGION \|\| 'no definida'` | Valor por defecto si el primero está vacío |
| `success()`, `failure()`, `always()`, `cancelled()` | En un `if:`, según cómo hayan ido los steps o jobs anteriores |
| `contains(github.ref, 'release')`, `startsWith(...)`, `endsWith(...)` | Buscar dentro de un texto o de una lista |
| `format('{0}-{1}', a, b)` | Montar un texto |
| `toJSON(runner)` | Ver un contexto entero |
| `hashFiles('**/requirements.txt')` | Un resumen de archivos (se usa para las cachés) |

En un `if:` se pueden omitir los `${{ }}`: `if: github.event_name == 'push'`.

---

## 9. Variables de entorno, variables y secretos

| | `env` | `vars` | `secrets` |
|---|-------|--------|-----------|
| Para qué | Valores reutilizables del workflow | Configuración que no es secreta | Contraseñas, claves, tokens |
| Dónde se definen | En el YAML (`env:`) | Settings > Secrets and variables > Actions > **Variables** | Settings > Secrets and variables > Actions > **Secrets** |
| ¿Se ven en el log? | Sí | Sí | No: salen como `***` |
| Cómo se leen | `$NOMBRE` o `${{ env.NOMBRE }}` | `${{ vars.NOMBRE }}` | `${{ secrets.NOMBRE }}` |

`env` se puede poner a tres niveles: workflow, job y step. El más concreto gana. Para crear una variable durante la ejecución: `echo "NOMBRE=valor" >> "$GITHUB_ENV"` (sirve para los steps siguientes del mismo job).

Sobre los secretos:

- Nunca en el código ni en el YAML: siempre en Settings.
- Un secreto que no existe vale `''`: no da error, así que conviene comprobarlo (como en el ejemplo [`07`](workflows/07_env_y_secretos.yaml)).
- No se pueden usar directamente en un `if:`. Pásalo a `env:` y comprueba la variable.
- En las PR que vienen de un *fork*, los secretos no llegan (por seguridad).
- `secrets.GITHUB_TOKEN` lo crea GitHub en cada ejecución; sus permisos se limitan con `permissions:`.
- Para tapar en el log un valor que no es un secreto de GitHub: `echo "::add-mask::$valor"`.

---

## 10. Matrix

```yaml
strategy:
  fail-fast: false                                     # que terminen todos aunque uno falle
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ["3.12", "3.14"]                   # ¡entre comillas!
    exclude:
      - os: macos-latest
        python-version: "3.12"
    include:
      - os: ubuntu-latest
        python-version: "3.13"
runs-on: ${{ matrix.os }}
```

Un job por cada combinación, todos a la vez. Es lo que se usa para comprobar que el código funciona en varios sistemas o versiones. Las versiones van **entre comillas**: sin ellas, YAML lee `3.10` como el número `3.1`. Una matrix genera como máximo 256 jobs.

---

## 11. Outputs, artifacts y caché

| | Output | Artifact | Caché |
|---|--------|----------|-------|
| Qué guarda | Un texto corto | Archivos completos | Dependencias (lo que instala pip, npm...) |
| Para qué | Pasar un dato a otro step o job | Pasar archivos a otro job, o descargarlos | Que la siguiente ejecución vaya más rápida |
| Cómo | `echo "x=valor" >> "$GITHUB_OUTPUT"` | `actions/upload-artifact@v7` / `actions/download-artifact@v8` | `cache: pip` en `setup-python`, o `actions/cache` |
| Ejemplo | [`09`](workflows/09_outputs.yaml) | [`10`](workflows/10_artifacts.yaml) | [`13`](workflows/13_ci_cd_calculadora.yaml) |

Outputs, paso a paso:

```yaml
jobs:
  a:
    runs-on: ubuntu-latest
    outputs:                                            # 3. el job lo comparte
      hora: ${{ steps.get-time.outputs.currenttime }}
    steps:
      - id: get-time                                    # 1. el step necesita un id
        run: echo "currenttime=$(date)" >> "$GITHUB_OUTPUT"
      - run: echo "${{ steps.get-time.outputs.currenttime }}"   # 2. otro step lo lee
  b:
    needs: a
    runs-on: ubuntu-latest
    steps:
      - run: echo "${{ needs.a.outputs.hora }}"        # 4. otro job lo lee
```

En una acción JavaScript, lo mismo se hace con `core.setOutput('currenttime', valor)` (paquete `@actions/core`).

Los artifacts se ven y se descargan en la página de la ejecución (**Summary**, sección **Artifacts**). Se borran a los 90 días por defecto (`retention-days` lo cambia).

---

## 12. Custom actions y workflows reutilizables

Una acción propia vive en su carpeta con un archivo `action.yml`:

| Tipo | `runs.using` | Cómo funciona | Ventajas | Ejemplo |
|------|--------------|---------------|----------|---------|
| **Composite** | `composite` | Una lista de steps, como en un job | Lo más sencillo: es YAML | [`saludo-composite`](acciones/saludo-composite/action.yml) |
| **JavaScript** | `node24` | Un programa de Node.js (con `@actions/core`, o leyendo `INPUT_*` y escribiendo en `GITHUB_OUTPUT`) | Rápida; funciona en Linux, Windows y macOS | [`contar-lineas-js`](acciones/contar-lineas-js/index.js) |
| **Docker** | `docker` | Un contenedor construido con un Dockerfile | Entorno siempre igual, con lo que quieras instalado | [`cartel-docker`](acciones/cartel-docker/action.yml) |

Cómo se usan:

```yaml
- uses: actions/checkout@v7                          # para las acciones del propio repositorio
- uses: ./RecursosEstudio/acciones/saludo-composite  # acción del propio repositorio
  with:
    nombre: Oscar
- uses: usuario/repositorio@v1                       # acción publicada en otro repositorio
```

Un **workflow reutilizable** (`on: workflow_call`, ejemplo [`12`](workflows/12_workflow_reutilizable.yaml)) es parecido pero más grande: en vez de un step, aporta jobs enteros. Se llama desde un job con `uses: ./.github/workflows/archivo.yaml` y tiene que estar en `.github/workflows/`.

---

## 13. Mission: automatizar Su Película

El pipeline de la presentación, construido nivel a nivel sobre la app de [`su-pelicula/`](su-pelicula/):

| Nivel | Evento | Jobs | Archivo |
|-------|--------|------|---------|
| 1 · Manual | `workflow_dispatch` | Hola mundo | [`nivel1_manual.yaml`](workflows/mision_pelicula/nivel1_manual.yaml) |
| 2 · Push | `push` | Build | [`nivel2_push_build.yaml`](workflows/mision_pelicula/nivel2_push_build.yaml) |
| 3 · Push | `push` | Build → Test | [`nivel3_push_build_test.yaml`](workflows/mision_pelicula/nivel3_push_build_test.yaml) |
| 4 · Pull Request | `pull_request` | Build → Test → Preview | [`nivel4_pull_request_preview.yaml`](workflows/mision_pelicula/nivel4_pull_request_preview.yaml) |
| 5 · Merge a main | `pull_request` y `push` | Build → Test → Preview (en PR) o Production (en `main`) | [`nivel5_ci_cd.yaml`](workflows/mision_pelicula/nivel5_ci_cd.yaml) |

El archivo objetivo de la presentación es `.github/workflows/ci-cd.yml`: puedes copiar el nivel 5 con ese nombre.

La app: `python pelicula.py` construye la película en `dist/pelicula.txt`, y `python -m unittest -v` pasa sus 5 tests (desde la carpeta `su-pelicula`).

**Bonus challenges**, resueltos en el nivel 5:

| Reto | Cómo |
|------|------|
| Hacer que un test falle y ver qué ocurre | En `pelicula.py`, pon la duración de una escena a `0` y haz push: Test sale en rojo y ningún deploy se ejecuta |
| Generar un artifact | Build sube `dist/pelicula.txt` como artifact `su-pelicula`, y los deploy lo descargan |
| Utilizar un secret | Crea el secreto `DEPLOY_TOKEN`: Deploy Production lo usa (y en el log sale `***`) |
| Añadir aprobación antes de Production | Settings > Environments > `production` > **Required reviewers**: el job espera hasta que pulses **Approve and deploy** |

Los environments con aprobación funcionan en cualquier plan si el repositorio es público; en uno privado depende del plan de GitHub.

---

## 14. Advertencias y recomendaciones

**Seguridad**

- **No metas texto de usuarios dentro de un script.** GitHub sustituye `${{ }}` antes de ejecutar, así que un input o un título de PR con comillas se convierte en código. Con el nombre `Ana"; echo "COMANDO INYECTADO"; echo "`:

  ```yaml
  - run: echo "Hello there, ${{ inputs.thename }}!"     # ✘ ejecuta: echo "Hello there, Ana"; echo "COMANDO INYECTADO"; echo "!"
  - env:
      NOMBRE: ${{ inputs.thename }}
    run: echo "Hello there, $NOMBRE!"                   # ✔ imprime el nombre tal cual
  ```

  Pasa siempre por `env:` los inputs, los títulos y cuerpos de PR o issues, los nombres de rama y los mensajes de commit.
- **Secretos**: siempre en Settings, siempre por `env:`, nunca con `echo` de propósito ni en `toJSON(secrets)`.
- **Permisos mínimos**: `permissions: contents: read` arriba del workflow, y añade solo los que falten.
- **Actions de terceros**: usa las oficiales o las muy conocidas, y fija la versión (`@v7`). En proyectos serios se fija el commit exacto (`@<sha de 40 caracteres>`), porque una etiqueta se puede mover.
- **`pull_request_target`** se ejecuta con los secretos del repositorio aunque la PR venga de un fork: no hagas checkout del código de la PR en ese evento si no sabes lo que haces.

**Coste y tiempo**

- En repositorios **públicos**, los runners de GitHub son gratis. En **privados** hay minutos incluidos según el plan, y Windows y sobre todo macOS gastan más.
- `timeout-minutes` evita que un job colgado se quede las 6 horas que dura como máximo por defecto.
- `concurrency` con `cancel-in-progress: true` cancela la ejecución anterior si subes otro commit a la misma rama.
- Filtra con `paths:` para no lanzar el pipeline cuando cambia algo que no le afecta.
- `cache: pip` en `setup-python` ahorra reinstalar las dependencias cada vez.

**Comportamientos que sorprenden**

- `workflow_dispatch` solo muestra el botón si el workflow está en la rama por defecto.
- `schedule` va en UTC, se ejecuta en la rama por defecto, puede retrasarse cuando GitHub tiene mucha carga y, en repositorios públicos, se desactiva solo tras 60 días sin actividad.
- Cada job es una máquina nueva: lo que hace un job no existe en el siguiente.
- `actions/checkout` descarga por defecto solo el último commit (`fetch-depth: 1`). Para tener el historial: `fetch-depth: 0`.

---

## 15. Notas sobre la presentación y el repositorio

1. **`.githud`** (diapositiva «Mission: Automatizar vuestra película»): la carpeta es `.github/workflows/`. Con otro nombre, GitHub no encuentra el workflow.
2. **`cat ./github/workflows/list.txt`** (diapositivas de `second.yaml`): falta el punto, es `./.github/workflows/list.txt`. El `second.yaml` del repositorio está bien.
3. **Versiones de las actions.** La presentación usa `actions/checkout@v3` y `mi-peli.yaml` usa `@v4`. Las versiones actuales son `actions/checkout@v7`, `actions/setup-python@v7`, `actions/upload-artifact@v7` y `actions/download-artifact@v8`. Las antiguas usan versiones de Node.js retiradas, y las `v3` de artifacts ya no funcionan: GitHub hace fallar el step.
4. **`${{ inputs.thename }}` dentro de `run`** (`third.yaml`): funciona, pero permite inyectar comandos. Ver [Advertencias](#14-advertencias-y-recomendaciones).
5. **`login –pass ${{ secrets.DB_PASSWORD }}`** (diapositiva «Gestión»): el guion es un guion largo (`–`), que la terminal no entiende como opción: es `--pass`. Mejor aún, pasa el secreto por `env:` (ejemplo [`07`](workflows/07_env_y_secretos.yaml)).
6. **`core.setOutput("<output name>”, <value>)`** (diapositiva «Establecer un Output»): las comillas no casan. Es `core.setOutput('nombre', valor)`.
7. **«Un workflow puede ejecutar un número ilimitado\* de jobs»**: el asterisco importa. Una matrix genera como máximo 256 jobs, y cuántos jobs corren a la vez depende del plan.
8. **`8.python_pr.yaml`**: construye la imagen con `context: .`, así que `COPY . /app` copia todo el repositorio y `main.py` acaba en `/app/code/python/main.py`. La imagen se construye, pero su `CMD ["python", "main.py"]` fallaría al arrancarla. El ejemplo [`13`](workflows/13_ci_cd_calculadora.yaml) usa `context: code/python`.
9. **`code/python/DockerFile`**: Docker busca por defecto `Dockerfile` (con `f` minúscula); con otro nombre hay que indicarlo (`-f`, o `file:` en la action). Además usa `python:3.9-slim`, una versión de Python que ya no tiene soporte.
10. **`black`**: `code/python/test_main.py` no tiene el formato de black, así que `black --check` falla. En el ejemplo [`13`](workflows/13_ci_cd_calculadora.yaml) ese step lleva `continue-on-error: true`; con `black code/python` se arregla.

---

## 16. Chuleta

```yaml
on:
  workflow_dispatch:
    inputs:
      nombre: { description: "Tu nombre", required: true, type: string }
  push:          { branches: [main], paths: ["src/**"] }
  pull_request:  { branches: [main] }
  schedule:      [ { cron: "0 7 * * 1" } ]

permissions: { contents: read }
concurrency: { group: "${{ github.workflow }}-${{ github.ref }}", cancel-in-progress: true }
env: { APP: "demo" }

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    outputs: { version: "${{ steps.v.outputs.version }}" }
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with: { python-version: "3.13", cache: pip }
      - id: v
        run: echo "version=1.0.0" >> "$GITHUB_OUTPUT"
      - run: echo "VAR=valor" >> "$GITHUB_ENV"
      - uses: actions/upload-artifact@v7
        with: { name: build, path: dist/ }

  test:
    needs: build
    if: github.event_name != 'schedule'
    strategy: { matrix: { python: ["3.12", "3.13"] } }
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v8
        with: { name: build }
      - env: { TOKEN: "${{ secrets.MI_TOKEN }}" }
        run: echo "Versión ${{ needs.build.outputs.version }} con Python ${{ matrix.python }}"
```

| Workflow command | Qué hace |
|------------------|----------|
| `echo "x=valor" >> "$GITHUB_OUTPUT"` | Crea un output del step |
| `echo "X=valor" >> "$GITHUB_ENV"` | Crea una variable para los steps siguientes |
| `echo "texto" >> "$GITHUB_STEP_SUMMARY"` | Escribe en el resumen de la ejecución (admite Markdown) |
| `echo "::add-mask::$valor"` | Tapa un valor en el log |
| `echo "::warning::mensaje"` / `::error::` / `::notice::` | Anotación amarilla, roja o azul en la ejecución |

---

## 17. Si algo falla

| Lo que ves | Causa | Solución |
|------------|-------|----------|
| El workflow no aparece en la pestaña Actions | No está en `.github/workflows/` (o está en una subcarpeta), o la carpeta está mal escrita (`.githud`) | Muévelo a `.github/workflows/`, directamente |
| No sale el botón **Run workflow** | No tiene `workflow_dispatch`, o no está en la rama por defecto | Añade el evento y súbelo a `main` |
| `Invalid workflow file` · `You have an error in your yaml syntax` (en VS Code: `mapping values are not allowed in this context`) | Un `run:` en una sola línea con `: ` dentro, como `run: echo "Base de datos: $X"`: YAML lo lee como una clave | Escríbelo en bloque: `run: \|` y el comando en la línea de abajo (o entre comillas simples) |
| Un comando se corta donde hay un `#` | En una línea sin comillas, ` #` empieza un comentario de YAML: `run: echo "PR #5"` se queda en `echo "PR` | Escríbelo en bloque (`run: \|`) |
| `Invalid workflow file` · error de indentación | Tabuladores, o un nivel de espacios de más o de menos | Usa espacios; revisa que `steps` esté dentro del job |
| `No such file or directory` al leer un archivo del repositorio | Falta `actions/checkout` antes | Añade `- uses: actions/checkout@v7` como primer step |
| `Can't find 'action.yml', 'action.yaml' or 'Dockerfile' under ...` | Una acción local (`uses: ./...`) sin checkout antes, o la ruta está mal | Checkout primero; la ruta va desde la raíz del repositorio |
| `Container action is only supported on Linux` | Una acción Docker en un runner Windows o macOS | Usa `runs-on: ubuntu-latest` |
| `This request has been automatically failed because it uses a deprecated version of actions/upload-artifact: v3` | La v3 de artifacts está retirada | `upload-artifact@v7` y `download-artifact@v8` |
| `Unable to download artifact(s): Artifact not found for name: ...` | El job que descarga no espera al que sube, o el nombre no coincide | `needs:` al job que sube, y el mismo `name:` |
| `No files were found with the provided path: ...` al subir un artifact | La ruta de `path:` no existe. Ojo: `working-directory` no se aplica a los `with:` | Escribe la ruta desde la raíz del repositorio |
| El secreto llega vacío | No existe, está mal escrito, o la PR viene de un fork | Revisa Settings > Secrets; en forks no llegan |
| Un job sale como **skipped** | Su `if:` no se cumple, o falló un job de su `needs:` | Mira el job anterior; usa `if: always()` si debe ejecutarse siempre |
| La matrix pide Python `3.1` | `3.10` sin comillas | `python-version: ["3.10"]` |
| `exec /entrypoint.sh: no such file or directory` en la acción Docker | El `.sh` tiene finales de línea de Windows (CRLF) | El `.gitattributes` de esta carpeta lo evita; si no, guarda el archivo con LF |
| `Process completed with exit code 1` | Algún comando del step ha fallado (un test, flake8...) | Abre el step en el log: las líneas de encima dicen qué falló |

---

## 18. Preguntas de repaso

<details>
<summary>¿Qué cuatro piezas necesita como mínimo un workflow?</summary>

Un evento (`on:`), un job (`jobs:`), un runner (`runs-on:`) y al menos un step (`steps:`).
</details>

<details>
<summary>¿Qué diferencia hay entre un job y un step?</summary>

Un job es un grupo de steps que se ejecutan en el mismo runner, en orden. Los jobs se ejecutan en paralelo por defecto, cada uno en su máquina; los steps de un job comparten la máquina y sus archivos.
</details>

<details>
<summary>¿Para qué sirve actions/checkout?</summary>

Para descargar el código del repositorio en el runner. Sin él, la máquina está vacía: no se pueden leer archivos, ni ejecutar tests, ni usar acciones locales.
</details>

<details>
<summary>¿Cómo haces que el job test espere a build, y qué pasa si build falla?</summary>

Con `needs: build`. Si build falla, test no se ejecuta: sale como *skipped*.
</details>

<details>
<summary>¿Cómo pasas un dato de un step a otro? ¿Y de un job a otro?</summary>

De step a step: `echo "x=valor" >> "$GITHUB_OUTPUT"` en un step con `id`, y `${{ steps.<id>.outputs.x }}` en el siguiente. De job a job: además, declarándolo en `outputs:` del job y leyéndolo con `${{ needs.<job>.outputs.x }}`. Para archivos, artifacts.
</details>

<details>
<summary>¿Dónde guardas una contraseña y cómo la usas?</summary>

En Settings > Secrets and variables > Actions. Se lee con `${{ secrets.NOMBRE }}`, mejor pasándola por `env:`. En el log sale como `***`.
</details>

<details>
<summary>¿Qué hace una matrix?</summary>

Ejecuta el mismo job varias veces a la vez, una por cada combinación de valores (por ejemplo, sistema operativo y versión de Python).
</details>

<details>
<summary>¿Cuáles son los tres tipos de custom action?</summary>

Composite (varios steps en YAML), JavaScript (un programa de Node.js) y Docker (un contenedor). Las tres se describen en un `action.yml`.
</details>

<details>
<summary>En el pipeline final, ¿por qué Deploy Production no se ejecuta en una Pull Request?</summary>

Porque tiene `if: github.event_name == 'push' && github.ref == 'refs/heads/main'`: solo se ejecuta cuando el código llega a `main`. En una PR se ejecuta Deploy Preview.
</details>
