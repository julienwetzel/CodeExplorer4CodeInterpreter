import os
import sys
from pathlib import Path
from gitignore_parser import parse_gitignore

# Initialize counters
total_files = 0
total_dirs = 0
total_inserted = 0
total_ignored = 0
total_non_unicode = 0

def read_file(file_path):
    global total_non_unicode
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace("'''", "\\'\\'\\'")
        return content
    except UnicodeDecodeError:
        print(f"{file_path} skipped because it is not a Unicode file")
        total_non_unicode += 1
        return None


def process_directory(dirpath, gitignore_rules, script_dir, output_file, py_file):
    global total_files, total_dirs, total_inserted, total_ignored

    gitignore_path = dirpath / '.gitignore'
    if gitignore_path.exists():
        gitignore_rules = parse_gitignore(gitignore_path)

    for filename in os.listdir(dirpath):
        file_path = dirpath / filename
        if file_path.is_file():
            total_files += 1
            if not gitignore_rules(str(file_path)) and not (file_path.suffix == '.py' and file_path.name.startswith('ce4ci') and file_path.parent.resolve() == script_dir) and file_path != output_file:
                relative_path = '/' + str(file_path.relative_to(project_dir))
                file_content = read_file(file_path)
                if file_content is not None:
                    py_file.write(f"    '{relative_path}': '''{file_content}''',\n")
                    total_inserted += 1
            else:
                total_ignored += 1

    for filename in os.listdir(dirpath):
        file_path = dirpath / filename
        if file_path.is_dir() and not gitignore_rules(str(file_path)):
            total_dirs += 1
            process_directory(file_path, gitignore_rules, script_dir, output_file, py_file)


def main(project_dir: Path, output_file: Path):
    global total_files, total_dirs, total_inserted, total_ignored, total_non_unicode

    script_dir = Path(__file__).parent

    with output_file.open('w') as py_file:
        py_file.write("file_contents = {\n")

        gitignore_path = project_dir / '.gitignore'
        gitignore_rules = parse_gitignore(gitignore_path) if gitignore_path.exists() else lambda x: False

        process_directory(project_dir, gitignore_rules, script_dir, output_file, py_file)
        
        py_file.write("}\n\n")
        
        py_file.write("def display_file_content(file_path):\n")
        py_file.write("    print(file_contents[file_path])\n\n")
        py_file.write("def get_available_file_paths():\n")
        py_file.write("    return list(file_contents.keys())\n")

    # Print statistics
    print(f"----------------------------------------------------")
    print(f"Total files processed: {total_files}")
    print(f"Total directories processed: {total_dirs}")
    print(f"Total file contents inserted: {total_inserted}")
    print(f"Total files ignored due to .gitignore rules: {total_ignored}")
    print(f"Total files skipped because they are not Unicode: {total_non_unicode}")
    print(f"----------------------------------------------------")


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
