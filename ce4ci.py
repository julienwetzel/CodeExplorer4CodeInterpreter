import os
import sys
import importlib
from pathlib import Path


# Function to read a file and return its content
def read_file(file_path):
    """
    Read a file and return its content.

    :param file_path: The path to the file.
    :return: The content of the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        print(f"{file_path} skipped because it is not a Unicode file")
        return None

# Main function that takes the project directory and output python file as arguments
def main(project_dir: Path, output_file: Path):
    """
    Main function that takes the project directory and output python file as arguments.

    :param project_dir: The directory of the project.
    :param output_file: The output python file.
    """
    # Check if gitignore_parser module is installed
    try:
        importlib.import_module('gitignore_parser')
    except ImportError:
        print("gitignore-parser module is missing. Please install it before running this script.")
        sys.exit(1)
    from gitignore_parser import parse_gitignore

    # Get the filename of the script
    script_filename = Path(__file__).name

    # Import gitignore_parser module after installation
    gitignore_path = project_dir / '.gitignore'
    gitignore_rules = []
    if gitignore_path.exists():
        gitignore_rules = parse_gitignore(gitignore_path)

    # Open the output python file in write mode
    with output_file.open('w') as py_file:
        # Write the file_contents dictionary declaration
        py_file.write("file_contents = {\n")
        
        # Process all files in the project directory
        for dirpath, dirnames, filenames in os.walk(project_dir):
            # Filter filenames based on gitignore rules, excluding the script file and output file
            filenames = [
                filename 
                for filename in filenames 
                if (
                    not gitignore_rules(Path(dirpath) / filename)
                    and filename != script_filename
                    and Path(dirpath) / filename != output_file
                )
            ]
            dirnames[:] = [dirname for dirname in dirnames if not gitignore_rules(Path(dirpath) / dirname)]
            
            for filename in filenames:
                file_path = Path(dirpath) / filename
                # Make file path relative to project directory and add leading /
                relative_path = '/' + str(file_path.relative_to(project_dir))
                file_content = read_file(file_path)
                # Write the file content to the dictionary
                py_file.write(f"    '{relative_path}': '''{file_content}''',\n")
        
        # Write the end of the file_contents dictionary declaration
        py_file.write("}\n\n")
        
        # Write the definition of the display_file_content function
        py_file.write("def display_file_content(file_path):\n")
        py_file.write("    print(file_contents[file_path])\n")

# Call the main function with command line arguments
if __name__ == "__main__":
    if len(sys.argv) == 3:
        project_dir = Path(sys.argv[1])
        output_file = Path(sys.argv[2])
        if not project_dir.exists():
            print(f"Project directory {project_dir} does not exist.")
            sys.exit(1)
        if output_file.exists():
            print(f"Output file {output_file} already exists. It will be overwritten.")
        main(project_dir, output_file)
    else:
        print("Usage: python ce4ci.py [project_dir] [output_file]")
        sys.exit(1)

