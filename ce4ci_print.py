import sys
import os
import importlib.machinery

def display_file_content(script_path, file_path):
    try:
        script_directory = os.path.dirname(script_path)
        sys.path.insert(0, script_directory)

        module_name = os.path.basename(script_path).split(".")[0]
        module_loader = importlib.machinery.SourceFileLoader(module_name, script_path)
        module = module_loader.load_module()

        full_path = os.path.join(script_directory, file_path)
        file_content = module.display_file_content(full_path)

        if file_content:
            print(file_content.rstrip())
    except ImportError:
        print(f"Failed to import script: {script_path}")
    except AttributeError:
        print(f"Invalid module: {script_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_module_name(script_path):
    return os.path.basename(script_path).split(".")[0]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ce4ci_print.py [--list] <script_path> [<file_path>]")
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
                module_loader = importlib.machinery.SourceFileLoader(module_name, script_path)
                module = module_loader.load_module()
                available_paths = module.get_available_file_paths()
                print("Available file paths:")
                for path in available_paths:
                    print(path)
            except ImportError:
                print(f"Failed to import script: {script_path}")
        else:
            display_file_content(script_path, file_path)
