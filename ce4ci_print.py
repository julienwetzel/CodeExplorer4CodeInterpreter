import sys
import os
import importlib

def display_file_content(script_path, file_path):
    try:
        script_name = os.path.basename(script_path).split(".")[0]
        script_directory = os.path.dirname(script_path)
        sys.path.insert(0, script_directory)
        module = importlib.import_module(script_name)

        full_path = os.path.join(script_directory, file_path)
        file_content = module.display_file_content(full_path)
        print(file_content)
    except ImportError:
        print(f"Failed to import script: {script_name}")
    except AttributeError:
        print(f"Invalid module: {script_name}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_module_name(script_path):
    return os.path.basename(script_path).split(".")[0]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python helper.py [--list] <script_path> [<file_path>]")
    else:
        list_mode = False
        script_path = ""
        file_path = ""

        # Check if --list argument is present
        if "--list" in sys.argv:
            list_mode = True
            script_path = sys.argv[1]
        else:
            script_path = sys.argv[1]
            if len(sys.argv) >= 3:
                file_path = sys.argv[2]

        if list_mode:
            module_name = get_module_name(script_path)
            try:
                module = importlib.import_module(module_name)
                available_paths = module.get_available_file_paths()
                print("Available file paths:")
                for path in available_paths:
                    print(path)
            except ImportError:
                print(f"Failed to import script: {module_name}")
        else:
            display_file_content(script_path, file_path)
