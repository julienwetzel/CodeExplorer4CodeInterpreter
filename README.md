# CodeExplorer4CodeInterpreter

CodeExplorer4CodeInterpreter is a Python script for developers and researchers who want to explore and interact with a project's code base more efficiently. It is compatible with the Code Interpreter plugin of ChatGPT and provides a seamless way to access and interact with a project's code files.

This script scans a given project directory and generates a Python script containing all the project's code. This generated script acts as a code dictionary, providing easy access to all the project's code.

<div style="display:flex;">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/3f675698-96fd-45d3-96fb-b2033411ebd1" alt="Image 1" width="50%">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/9444f225-31ed-4b2a-b1ba-d61161a2087a" alt="Image 2" width="50%">
</div>

## Features

- CodeExplorer4CodeInterpreter supports Python 3.7 and above, ensuring compatibility with most modern Python environments.
- Allows easy exploration of a project's code base.
- Generates a Python script that can be easily imported and used in the ChatGPT Code Interpreter plugin.

### Prerequisites

Before running CodeExplorer4CodeInterpreter, ensure you have the `gitignore_parser` module installed in your Python environment. You can install it using pip:

```bash
pip install gitignore-parser
```

## Getting Started

To get started with CodeExplorer4CodeInterpreter, you need to have Python 3.7 or higher installed on your system.

Clone the repository using the following command:
```bash
git clone https://github.com/julienwetzel/CodeExplorer4CodeInterpreter.git
```

Navigate to the cloned repository:
```bash
cd CodeExplorer4CodeInterpreter
```

To generate the Python script containing your project's code, run the following command:
```bash
python ce4ci.py [project_dir] [output_file]
```

where `[project_dir]` is the directory of your project and `[output_file]` is the name of the file to be generated.

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
## Usage with ChatGPT Code Interpreter Plugin

After the Python script is generated, it can be used with the Code Interpreter plugin of ChatGPT.

In the ChatGPT prompt, add the following text:

```
All the contents of the project files are in the attached python file.
Import the file with /mnt/data/ce4ci_dict.py and simply run the display_file_content(file_path)
function where file_path is the path of the file. For example, `display_file_content('/your/file.example')
To display the list of all project files, use the get_available_file_paths() function.
```

Note: `ce4ci_dict.py` is the name of the generated file that has been uploaded to the Code Interpreter plugin of ChatGPT. If `/mnt/data` is not included, the file won't be found.

## Exploring the Generated Python Dictionary

To explore the generated Python dictionary, you can use the `ce4ci_print.py` script.

To display the content of the Python dictionary, use:
```bash
python ce4ci_print.py [--list] <script_path> [<file_path>]
```
For example:
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py '/LICENSE'
```
This will display the contents of the LICENSE file.

To list the paths of all files contained in the dictionary, use:
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py --list
```
This will display all the available file paths.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/LICENSE.md) file for details.

