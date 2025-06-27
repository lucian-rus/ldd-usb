import os
import json
import shutil

# these paths shall be relative to the parent dir
CONFIG_FILE_PATH = "../../config.json"
LDD_DIRECTORY_PATH = "../../ldd-usb"
TEMP_DIR_PATH = "../../tools/.temp"

SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


########################################################################################
#                               helper functions
########################################################################################
def get_parsed_json_data():
    """
    Reads and parses the JSON configuration file.

    Returns
    -------
    dict
        Parsed JSON data from the configuration file.
    """
    file = open(os.path.join(SCRIPT_DIR_PATH, CONFIG_FILE_PATH))
    json_data = json.load(file)

    file.close()
    return json_data


def create_directory(dir_path):
    """
    Creates a directory if it does not already exist.

    Parameters
    ----------
    dir_path : str
        Path of the directory to create.
    """
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        print("!!!      directory {dir} already exists".format(dir=dir_path))
    else:
        os.makedirs(dir_path)
        print("!!!      created directory {dir}".format(dir=dir_path))


def check_temp_dir_generation(compiler_flags, makefile_path):
    """
    Checks and ensures the temporary directory is generated as needed for the build process.

    Parameters
    ----------
    compiler_flags : list of str
        List of compiler flags to use.
    makefile_path : str
        Path to the Makefile to check or update.
    """
    if 0 != len(compiler_flags):
        temp_dir = os.path.join(SCRIPT_DIR_PATH, TEMP_DIR_PATH)
        create_directory(temp_dir)
        shutil.copy(makefile_path, temp_dir)


def update_compiler_flags(compiler_flags, raw_data):
    """
    Updates the compiler flags list based on the provided raw configuration data.

    Parameters
    ----------
    compiler_flags : list of str
        List of current compiler flags.
    raw_data : dict
        Raw configuration data from the JSON file.

    Returns
    -------
    list of str
        Updated list of compiler flags.
    """
    output_data = ""
    # dumb but works
    for line in raw_data:
        if "ccflags-y" in line:
            for flag in compiler_flags:
                line += " " + flag

        output_data += line + "\n"
    return output_data


########################################################################################
#                               parser functions
########################################################################################
def get_data_from_json(key):
    """
    Retrieves the value from the JSON File based on the given key.

    Returns
    -------
    generic data
        Value of the JSON key.
    """
    json_data = get_parsed_json_data()
    return json_data[key]


########################################################################################
#                               runner functions
########################################################################################
def create_pre_build_directories():
    """
    Creates all required directories before the build process, as specified in the configuration file.
    """
    print("> running directory creator")
    required_dir_list = get_data_from_json("pre_build_create_dirs")

    for directory in required_dir_list:
        dir_path = os.path.join(os.getcwd(), directory)
        create_directory(dir_path)


def update_default_makefile():
    """
    Updates the default Makefile with additional flags or alters the build process as needed.
    """
    print("> update default makefile")
    compiler_flags = get_data_from_json("compiler_flags")
    makefile_path = os.path.join(SCRIPT_DIR_PATH, LDD_DIRECTORY_PATH, "Makefile")

    check_temp_dir_generation(compiler_flags, makefile_path)

    # update the Makefile data
    file = open(makefile_path)
    raw_data = file.read().split("\n")
    raw_data.pop()
    file.close()

    output_data = update_compiler_flags(compiler_flags, raw_data)

    file = open(makefile_path, "w+")
    file.write(output_data)
    file.close()


def pre_build_runner():
    """
    Runs all pre-build steps, such as creating required directories.
    """
    create_pre_build_directories()
    update_default_makefile()


if __name__ == "__main__":
    print("------------------------------------------")
    print("         running pre-build script")
    print("------------------------------------------")
    pre_build_runner()
    print("> starting LDD build process")
