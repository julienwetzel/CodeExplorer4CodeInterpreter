[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-beige.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.fr.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.es.md)
[![cmn](https://img.shields.io/badge/lang-cmn-red.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.cmn.md)

# CodeExplorer4CodeInterpreter

CodeExplorer4CodeInterpreter es un software desarrollado en Python diseñado para facilitar el envío de múltiples documentos al Intérprete de Código de ChatGPT y permitir una fácil interacción con él.

<div style="display:flex;">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/3f675698-96fd-45d3-96fb-b2033411ebd1" alt="Imagen 1" width="49%">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/9444f225-31ed-4b2a-b1ba-d61161a2087a" alt="Imagen 2" width="49%">
</div>

## Casos de Uso

- **Análisis de proyectos de código informático**: CodeExplorer4CodeInterpreter se puede utilizar para enviar un proyecto de código informático completo al Intérprete de Código de ChatGPT. Esto permite a los desarrolladores hacer preguntas sobre su código, obtener sugerencias, explicaciones o posibles correcciones, facilitando así el proceso de desarrollo.
- **Análisis de revistas y publicaciones**: El software también se puede utilizar para enviar múltiples revistas y publicaciones científicas al Intérprete de Código de ChatGPT. Los usuarios pueden hacer preguntas específicas sobre los artículos, solicitar resúmenes o análisis adicionales, u obtener explicaciones detalladas de conceptos complejos.
- **Asistencia en escritura y corrección**: CodeExplorer4CodeInterpreter puede ser útil para escritores y estudiantes para enviar documentos como ensayos, informes o trabajos académicos al Intérprete de Código de ChatGPT. Pueden pedir consejos sobre la estructura, la gramática, la mejora del estilo de escritura o incluso sugerencias de palabras clave relevantes.
- **Análisis de datos**: El software se puede utilizar para enviar conjuntos de datos al Intérprete de Código de ChatGPT. Los usuarios pueden hacer preguntas sobre los datos, obtener visualizaciones, estadísticas o recomendaciones sobre métodos de análisis para aplicar.
- **Ayuda con la búsqueda de información**: El software puede facilitar la búsqueda de información al enviar documentos que contienen información específica al Intérprete de Código de ChatGPT. Los usuarios pueden hacer preguntas sobre diversos temas y obtener respuestas detalladas basadas en el contenido de los documentos enviados.

## Características

- CodeExplorer4CodeInterpreter es compatible con Python 3.7 y versiones posteriores, asegurando la compatibilidad con la mayoría de los entornos Python modernos.
- Permite la fácil exploración de la base de código de un proyecto.
- Genera un script en Python que se puede importar y utilizar fácilmente en el plugin del Intérprete de Código de ChatGPT.

## Prerrequisitos

Antes de ejecutar CodeExplorer4CodeInterpreter, asegúrate de tener el módulo `gitignore_parser` instalado en tu entorno Python. Puedes instalarlo usando pip:

```bash
pip install gitignore-parser
```

## Primeros Pasos

Para empezar con CodeExplorer4CodeInterpreter, debes tener Python 3.7 o una versión superior instalada en tu sistema.

Clona el repositorio usando el siguiente comando:
```bash
git clone https://github.com/julienwetzel/CodeExplorer4CodeInterpreter.git
```

Accede al directorio clonado:
```bash
cd CodeExplorer4CodeInterpreter
```

Para generar el script en Python que contiene el código de tu proyecto, ejecuta el siguiente comando:
```bash
python ce4ci.py [directorio_del_proyecto] [archivo_de_salida]
```

donde `[directorio_del_proyecto]` es el directorio de tu proyecto y `[archivo_de_salida]` es el nombre del archivo a generar.

Por ejemplo:
```bash
python ce4ci.py ./ ../../data/ce4ci_dict.py
```

Después de ejecutar el comando, verás un resumen de la operación:
```bash
----------------------------------------------------
Total files processed: 5
Total directories processed: 0
Total file contents inserted: 3
Total files ignored due to .gitignore rules: 2
Total files skipped because they are not Unicode: 0
----------------------------------------------------
```
## Uso con el plugin del Intérprete de Código de ChatGPT

Una vez se genera el script en Python, puedes usarlo con el plugin del Intérprete de Código de ChatGPT.

En el prompt de ChatGPT, añade el siguiente texto:

```bash
Todos los contenidos de los archivos del proyecto están en el archivo Python adjunto.
Importa el archivo con /mnt/data/ce4ci_dict.py y simplemente ejecuta la función display_file_content(file_path)
donde file_path es la ruta del archivo. Por ejemplo, `display_file_content('/tu/file.example')
Para mostrar la lista de todos los archivos del proyecto, utiliza la función get_available_file_paths().
```

> Nota: `ce4ci_dict.py` es el nombre del archivo generado que se ha subido al plugin del Intérprete de Código de ChatGPT. Si no se incluye `/mnt/data`, no se encontrará el archivo.

## Explorando el diccionario Python generado

Para explorar el diccionario Python generado, puedes usar el script `ce4ci_print.py`.

Para mostrar el contenido del diccionario Python, utiliza el siguiente comando:
```bash
python ce4ci_print.py [--list] <ruta_del_script> [<ruta_del_archivo>]
```
Por ejemplo:
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py '/LICENSE'
```
Esto mostrará el contenido del archivo LICENSE.

Para listar las rutas de todos los archivos contenidos en el diccionario, utiliza el siguiente comando:
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py --list
```
Esto mostrará todas las rutas de archivos disponibles.

## Licencia

Este proyecto está licenciado bajo MIT - ve el archivo [LICENSE.md](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/LICENSE.md) para más detalles.
