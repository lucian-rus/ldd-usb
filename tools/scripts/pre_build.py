import os
import json

CONFIG_FILE_PATH    = '../../config.json'

# function to get the output target directory
def get_pre_build_required_dirs():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data = open(os.path.join(script_dir, CONFIG_FILE_PATH))
    json_data = json.load(raw_data)

    return json_data["pre_build_create_dirs"]

def create_pre_build_directories():
    required_dir_list = get_pre_build_required_dirs()

    for directory in required_dir_list:
        dir_path = os.path.join(os.getcwd(), directory)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            print("!!!      directory {dir} already exists".format(dir=dir_path))
        else:
            os.makedirs(dir_path)
            print("!!!      created directory {dir}".format(dir=dir_path))

def pre_build_runner():
    print("> running directory creator")
    create_pre_build_directories()

if __name__ == "__main__":
    print("------------------------------------------")
    print("         running pre-build script")
    print("------------------------------------------")
    pre_build_runner()
    print("> starting LDD build process")