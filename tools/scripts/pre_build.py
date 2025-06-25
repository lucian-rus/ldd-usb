import os
import json
import shutil

# these paths shall be relative to the parent dir
CONFIG_FILE_PATH = "../../config.json"
LDD_DIRECTORY_PATH = "../../ldd-usb"
TEMP_DIR_PATH = "../../tools/.temp"

SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def get_parsed_json_data():
    file = open(os.path.join(SCRIPT_DIR_PATH, CONFIG_FILE_PATH))
    json_data = json.load(file)

    file.close()
    return json_data


def create_directory(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        print("!!!      directory {dir} already exists".format(dir=dir_path))
    else:
        os.makedirs(dir_path)
        print("!!!      created directory {dir}".format(dir=dir_path))


def get_pre_build_required_dirs():
    json_data = get_parsed_json_data()
    return json_data["pre_build_create_dirs"]


def get_compiler_flags():
    json_data = get_parsed_json_data()
    return json_data["compiler_flags"]


def get_liner_flags():
    json_data = get_parsed_json_data()
    return json_data["linker_flags"]


def create_pre_build_directories():
    print("> running directory creator")
    required_dir_list = get_pre_build_required_dirs()

    for directory in required_dir_list:
        dir_path = os.path.join(os.getcwd(), directory)
        create_directory(dir_path)


def update_default_makefile():
    print("> update default makefile")
    compiler_flags = get_compiler_flags()
    makefile_path = os.path.join(SCRIPT_DIR_PATH, LDD_DIRECTORY_PATH, "Makefile")

    if 0 != len(compiler_flags):
        temp_dir = os.path.join(SCRIPT_DIR_PATH, TEMP_DIR_PATH)
        create_directory(temp_dir)
        shutil.copy(makefile_path, temp_dir)

    # update the Makefile data
    file = open(makefile_path)
    raw_data = file.read().split("\n")
    output_data = ""
    file.close()

    # dumb but works
    raw_data.pop()
    for line in raw_data:
        if "ccflags-y" in line:
            for flag in compiler_flags:
                line += " " + flag

        output_data += line + "\n"

    file = open(makefile_path, "w+")
    file.write(output_data)
    file.close()


def pre_build_runner():
    create_pre_build_directories()
    update_default_makefile()


if __name__ == "__main__":
    print("------------------------------------------")
    print("         running pre-build script")
    print("------------------------------------------")
    pre_build_runner()
    print("> starting LDD build process")
