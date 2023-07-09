# CodeExplorer4CodeInterpreter

CodeExplorer4CodeInterpreter is a Python script that serves as a Code Explorer for the Code Interpreter plugin of ChatGPT. It provides comprehensive access to the entire project's code, facilitating interaction with the project's code files.

This Python script creates another Python script that contains all the code of the project from the specified path. To display the contents of a specific file, simply call the `display_file_content(file_path)` function, where `file_path` is the path to the file from the specified path. For example, `display_file_content('/src/main.rs')`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```
Python 3.7+
```

### Installation

1. Clone the repository:
```
git clone https://github.com/julienwetzel/CodeExplorer4CodeInterpreter.git
```

2. Navigate to the cloned repository:
```
cd CodeExplorer4CodeInterpreter
```

3. Run the script:
```
python ce4ci.py
```

## Usage

Once the generated Python file has been added to ChatGPT's code interpreter, add the following text to the end of the ChatGPT prompt: 

```
All the contents of the project files are in the attached python file.
Import the file with `/mnt/data/ce4ci_gen.py` and simply run the `display_file_content(file_path)`
function where `file_path` is the path of the file. For example, `display_file_content('/your/path/file.example')
```

**Note:** If you don't include `/mnt/data`, it won't find the file. In the example, `ce4ci_gen.py` is the name of the generated file that has been uploaded to ChatGPT's code interpreter plugin.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/LICENSE.md) file for details
