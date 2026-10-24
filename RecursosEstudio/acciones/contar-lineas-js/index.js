// =====================================================================
// index.js · el programa de la acción JavaScript «Contar líneas»
// ---------------------------------------------------------------------
// Cómo habla una acción con GitHub:
//   - Los INPUTS llegan como variables de entorno: el input «archivo» llega
//     como INPUT_ARCHIVO (INPUT_ + el nombre en mayúsculas).
//   - Los OUTPUTS se escriben en el archivo cuya ruta está en GITHUB_OUTPUT,
//     con el formato nombre=valor (lo mismo que hace echo ... >> $GITHUB_OUTPUT).
//   - Si el programa termina con un código distinto de 0, el step falla.
//
// Lo normal es usar el paquete oficial @actions/core, que hace esto por ti:
//     const core = require('@actions/core');
//     const archivo = core.getInput('archivo', { required: true });
//     core.setOutput('lineas', lineas);
//     core.setFailed('mensaje de error');
// Pero entonces hay que subir al repositorio también node_modules (o empaquetarlo
// con una herramienta como @vercel/ncc). Para un ejemplo de clase, sin
// dependencias se ve mejor qué pasa por debajo.
//
// Para probarla en tu ordenador (PowerShell, desde la raíz del repositorio):
//   $env:INPUT_ARCHIVO="RecursosEstudio/datos/lista_peliculas.txt"; $env:GITHUB_OUTPUT="salida.txt"
//   node RecursosEstudio/acciones/contar-lineas-js/index.js
// =====================================================================

const fs = require('fs');

// Equivale a core.getInput: lee INPUT_<NOMBRE> (los espacios pasan a _)
function getInput(nombre) {
  const variable = `INPUT_${nombre.replace(/ /g, '_').toUpperCase()}`;
  return (process.env[variable] || '').trim();
}

// Equivale a core.setOutput: añade nombre=valor al archivo de GITHUB_OUTPUT
function setOutput(nombre, valor) {
  fs.appendFileSync(process.env.GITHUB_OUTPUT, `${nombre}=${valor}\n`);
}

try {
  const archivo = getInput('archivo');
  if (!archivo) {
    throw new Error('Falta el input «archivo»');
  }

  // Las acciones JavaScript se ejecutan desde la raíz del repositorio (GITHUB_WORKSPACE)
  const contenido = fs.readFileSync(archivo, 'utf8');
  const lineas = contenido.split(/\r?\n/).filter((linea) => linea.trim() !== '').length;

  console.log(`${archivo} tiene ${lineas} líneas con texto`);
  setOutput('lineas', lineas);
} catch (error) {
  // ::error:: es un «workflow command»: GitHub lo enseña como una anotación roja
  console.log(`::error::${error.message}`);
  process.exitCode = 1; // equivale a core.setFailed
}
