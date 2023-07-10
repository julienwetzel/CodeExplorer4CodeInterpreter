import importlib
import sys
import os

def display_file_content(script_path, file_path):
    try:
        script_name = os.path.basename(script_path).split(".")[0]
        sys.path.insert(0, os.path.dirname(script_path))
        module = importlib.import_module(script_name)
        file_content = module.display_file_content(file_path)
        print(file_content)
    except ImportError:
        print(f"Failed to import script: {script_name}")
    except AttributeError:
        print(f"Invalid module: {script_name}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ce4ci_print.py <generated_python_dict_path> <file_path_to_get_content>")
    else:
        script_path = sys.argv[1]
        file_path = sys.argv[2]
        display_file_content(script_path, file_path)
