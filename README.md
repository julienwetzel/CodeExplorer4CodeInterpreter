[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-beige.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.fr.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.es.md)
[![cmn](https://img.shields.io/badge/lang-cmn-red.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.cmn.md)

# CodeExplorer4CodeInterpreter

CodeExplorer4CodeInterpreter is a Python-developed software designed to facilitate the sending of multiple documents to ChatGPT's Code Interpreter and allow easy interaction with it.

<div style="display:flex;">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/3f675698-96fd-45d3-96fb-b2033411ebd1" alt="Image 1" width="49%">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/9444f225-31ed-4b2a-b1ba-d61161a2087a" alt="Image 2" width="49%">
</div>

## Use Cases

- **Analysis of computer code projects**: CodeExplorer4CodeInterpreter can be used to send an entire computer code project to ChatGPT's Code Interpreter. This allows developers to ask questions about their code, obtain suggestions, explanations, or potential corrections, thereby facilitating the development process.
- **Analysis of journals and publications**: The software can also be used to send multiple journals and scientific publications to ChatGPT's Code Interpreter. Users can ask specific questions about articles, request summaries or additional analyses, or obtain in-depth explanations of complex concepts.
- **Assistance in writing and correction**: CodeExplorer4CodeInterpreter can be helpful to writers and students for sending documents such as essays, reports, or academic works to ChatGPT's Code Interpreter. They can ask for advice on structure, grammar, improving writing style, or even suggestions of relevant keywords.
- **Data Analysis**: The software can be used to send data sets to ChatGPT's Code Interpreter. Users can ask questions about the data, get visualizations, statistics, or recommendations on analysis methods to apply.
- **Help with information search**: The software can facilitate information search by sending documents containing specific information to ChatGPT's Code Interpreter. Users can ask questions on various topics and get detailed answers based on the content of the submitted documents.

## Features

- CodeExplorer4CodeInterpreter supports Python 3.7 and later versions, ensuring compatibility with most modern Python environments.
- Allows easy exploration of a project's code base.
- Generates a Python script that can be easily imported and used in the ChatGPT Code Interpreter plugin.

## Prerequisites

Before running CodeExplorer4CodeInterpreter, make sure you have the `gitignore_parser` module installed in your Python environment. You can install it using pip:

```bash
pip install gitignore-parser
```

## Getting Started

To get started with CodeExplorer4CodeInterpreter, you must have Python 3.7 or a higher version installed on your system.

Clone the repository using the following command:
```bash
git clone https://github.com/julienwetzel/CodeExplorer4CodeInterpreter.git
```

Access the cloned directory:
```bash
cd CodeExplorer4CodeInterpreter
```

To generate the Python script containing your project's code, run the following command:
```bash
python ce4ci.py [project_dir] [output_file]
```

where `[project_dir]` is your project directory and `[output_file]` is the name of the file to generate.

For example:
```bash
python ce4ci.py ./ ../../data/ce4ci_dict.py
```

After running the command, you will see a summary of the operation:
```bash
----------------------------------------------------
Total files processed: 5
Total directories processed: 0
Total file contents inserted: 3
Total files ignored due to .gitignore rules: 2
Total files skipped because they are not Unicode: 0
----------------------------------------------------
```
## Usage with the ChatGPT Code Interpreter plugin

Once the Python script is generated, you can use it with the Code Interpreter plugin of ChatGPT.

In the ChatGPT prompt, add the following text:

```bash
All the contents of the project files are in the attached python file.
Import the file with /mnt/data/ce4ci_dict.py and simply run the display_file_content(file_path)
function where file_path is the path of the file. For example, `display_file_content('/your/file.example')
To display the list of all project files, use the get_available_file_paths() function.
```

> Note: `ce4ci_dict.py` is the name of the generated file that has been uploaded to ChatGPT's Code Interpreter plugin. If `/mnt/data` is not included, the file will not be found.

## Exploring the generated Python dictionary

To explore the generated Python dictionary, you can use the `ce4ci_print.py` script.

To display the content of the Python dictionary, use the following command:
```bash
python ce4ci_print.py [--list] <script_path> [<file_path>]
```
For example:
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py '/LICENSE'
```
This will display the content of the LICENSE file.

To list the paths of all the files contained in the dictionary, use the following command:
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py --list
```
This will display all available file paths.

## License

This project is licensed under MIT - see the [LICENSE](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/LICENSE) file for more details.
