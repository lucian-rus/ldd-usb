import os
import json
import shutil

CONFIG_FILE_PATH    = '../../config.json'
LDD_DIRECTORY_PATH  = '../../ldd-usb'

# function to get cleaner exception list
def get_cleaner_exception_list():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data = open(os.path.join(script_dir, CONFIG_FILE_PATH))
    json_data = json.load(raw_data)

    return json_data["output_cleaner_exceptions"]

# function to get mover exception list
def get_mover_exception_list():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data = open(os.path.join(script_dir, CONFIG_FILE_PATH))
    json_data = json.load(raw_data)

    return json_data["output_mover_exceptions"]

# function to get the output target directory
def get_output_mover_target_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data = open(os.path.join(script_dir, CONFIG_FILE_PATH))
    json_data = json.load(raw_data)

    return json_data["output_mover_target_dir"]

# function to get the target directory for the output process
def get_mover_output_target_dir():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data = open(os.path.join(script_dir, CONFIG_FILE_PATH))
    json_data = json.load(raw_data)

    return json_data["output_mover_target_dir"]

# function that cleans the directory in which the make command was ran
def run_post_build_cleaner(directory):
    cleaner_exception_list = get_cleaner_exception_list()
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name == 'Makefile':
                continue

            # dumb but works -> ensure that `mod.c` files are deleted as well if they are not in the exception list
            if (name.endswith('.c') or name.endswith('.h')) and 1 == name.count('.'):
                continue
            
            # create extension here
            if any(name.endswith('.' + ext) for ext in cleaner_exception_list):
                continue

            os.remove(os.path.join(root, name))

# function that moves the generated content to a target directory
def run_post_clean_mover(directory):
    mover_exception_list = get_mover_exception_list()
    output_directory_name = get_output_mover_target_dir()
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name == 'Makefile':
                continue

            # dumb but works -> ensure that `mod.c` files are deleted as well if they are not in the exception list
            if (name.endswith('.c') or name.endswith('.h')) and 1 == name.count('.'):
                continue
            
            # create extension here
            if any(name.endswith('.' + ext) for ext in mover_exception_list):
                continue
            
            print(os.path.join(os.getcwd(), output_directory_name, name))
            shutil.move(os.path.join(root, name), os.path.join(os.getcwd(), output_directory_name, name))

def post_build_runner(directory):
    print("> running post build cleaner")
    run_post_build_cleaner(directory)
    print("> running post build mover")
    run_post_clean_mover(directory)

if __name__ == "__main__":
    print("------------------------------------------")
    print("         running post-build script")
    print("------------------------------------------")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(script_dir, LDD_DIRECTORY_PATH)
    post_build_runner(dir_path)
    print("> done")